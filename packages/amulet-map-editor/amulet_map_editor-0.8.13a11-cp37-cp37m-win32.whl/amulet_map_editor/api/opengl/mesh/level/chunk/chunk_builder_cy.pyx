# cython: language_level=3, boundscheck=False, wraparound=False

import numpy
cimport numpy

from libc.stdlib cimport malloc, calloc, free

cdef extern from "stdlib.h":
    void *memcpy(void *dest, void *src, size_t n) nogil

from cpython cimport array
import array

cdef float _brightness_step = 0.15
cdef dict _brightness_multiplier = {
    None: (1,) * 3,
    "up": (1,) * 3,
    "north": (1 - _brightness_step,) * 3,
    "south": (1 - _brightness_step,) * 3,
    "east": (1 - _brightness_step * 2,) * 3,
    "west": (1 - _brightness_step * 2,) * 3,
    "down": (1 - _brightness_step * 3,) * 3,
}

CULL_STR_INDEX = {
    None: 0,
    "up": 1,
    "down": 2,
    "north": 3,
    "east": 4,
    "south": 5,
    "west": 6,
}

cdef int CULL_MAP[7][3]
CULL_MAP[0][:] = (0, 0, 0)
CULL_MAP[1][:] = (0, 1, 0)
CULL_MAP[2][:] = (0, -1, 0)
CULL_MAP[3][:] = (0, 0, -1)
CULL_MAP[4][:] = (1, 0, 0)
CULL_MAP[5][:] = (0, 0, 1)
CULL_MAP[6][:] = (-1, 0, 0)

DEF ARRAY_VERT_COUNT = 10_008  # The number of vertices in the table
DEF ATTR_COUNT = 12  # The number of float attributes per vertex
DEF ARRAY_SIZE = ARRAY_VERT_COUNT * ATTR_COUNT


cdef struct VertArray:
    float* arr  # pointer to the array
    int size  # the number of floats in the array

cdef VertArray* VertArray_new(unsigned long size) nogil:
    # assert size and size % (ATTR_COUNT*3) == 0, "arr must have a multiple of 36 values"
    vert_array = <VertArray*>calloc(1, sizeof(VertArray))
    vert_array.arr = <float*>malloc(size * sizeof(float))
    vert_array.size = size
    return vert_array

cdef VertArray* VertArray_init(float* arr, unsigned long size) nogil:
    vert_array = VertArray_new(size)
    memcpy(vert_array.arr, arr, size * sizeof(float))
    return vert_array

cdef void VertArray_free(VertArray* vert_array) nogil:
    free(vert_array.arr)
    free(vert_array)

cdef VertArray* VertArray_from_py(array.array arr):
    assert arr.typecode == "f", "arr must be a float array"
    return VertArray_init(&arr.data.as_floats[0], len(arr))


cdef struct BlockModel:
    VertArray* faces[7]
    char is_transparent

cdef BlockModel* BlockModel_init(dict face_data, char is_transparent):
    block_model = <BlockModel*>calloc(1, sizeof(BlockModel))
    block_model.is_transparent = is_transparent
    cdef Py_ssize_t index
    for cull_id, index in CULL_STR_INDEX.items():
        if cull_id in face_data:
            arr = face_data[cull_id]
            if isinstance(arr, numpy.ndarray):
                arr = array.array("f", arr.ravel())
            if isinstance(arr, array.array) and arr.typecode == "f":
                block_model.faces[index] = VertArray_from_py(arr)
        else:
            block_model.faces[index] = NULL
    return block_model

cdef void BlockModel_free(BlockModel* block_model) nogil:
    cdef Py_ssize_t i
    for i in range(7):
        if block_model.faces[i]:
            VertArray_free(block_model.faces[i])
    free(block_model)


cdef class BlockModelManager:
    cdef BlockModel** blocks  # A pointer to an array of pointers to BlockModel structs
    cdef unsigned long block_size  # The size of the blocks array
    cdef unsigned long block_count  # The amount of the blocks array that is used

    def __cinit__(self):
        self.blocks = NULL
        self.block_size = 0
        self.block_count = 0

    def __init__(self):
        self.blocks = <BlockModel**>calloc(100, sizeof(BlockModel*))
        self.block_size = 100

    def __dealloc__(self):
        for i in range(self.block_count):
            BlockModel_free(self.blocks[i])
        free(self.blocks)

    cdef _extend(self):
        if self.block_count == self.block_size:
            blocks_temp = <BlockModel**>calloc(self.block_size + 100, sizeof(BlockModel*))
            memcpy(blocks_temp, self.blocks, self.block_size * sizeof(BlockModel*))
            free(self.blocks)
            self.blocks = blocks_temp
            self.block_size += 100

    cpdef add_block(self, dict face_data, int is_transparent):
        self._extend()
        self.blocks[self.block_count] = BlockModel_init(face_data, is_transparent)
        self.block_count += 1

    def __len__(self):
        return self.block_count


cdef struct VertArrayContainer:
    VertArray** arrays  # A pointer to an array of pointers to VertArrays
    int size  # The current size of the array
    int used  # The number of elements of the array that are used

cdef VertArrayContainer* VertArrayContainer_init() nogil:
    self = <VertArrayContainer*>calloc(1, sizeof(VertArrayContainer))
    self.arrays = <VertArray**>calloc(10, sizeof(VertArray*))
    self.size = 0
    self.used = 0
    return self

cdef void VertArrayContainer_free(VertArrayContainer* self) nogil:
    cdef int i
    for i in range(self.used):
        VertArray_free(self.arrays[i])
    free(self.arrays)
    free(self)

cdef void VertArrayContainer_append(VertArrayContainer* self, VertArray* vert_array) nogil:
    if self.used == self.size:
        _VertArrayContainer_extend(self)
    self.arrays[self.used] = vert_array
    self.used += 1

cdef void _VertArrayContainer_extend(VertArrayContainer* self) nogil:
    arr = <VertArray**>calloc(self.size + 5, sizeof(VertArray*))
    memcpy(arr, self.arrays, self.size * sizeof(VertArray*))
    free(self.arrays)
    self.arrays = arr
    self.size += 5


cdef struct VertArrayContainerTuple:
    VertArrayContainer* verts
    VertArrayContainer* verts_translucent

cdef VertArrayContainerTuple* VertArrayContainerTuple_init() nogil:
    self = <VertArrayContainerTuple*>calloc(1, sizeof(VertArrayContainerTuple))
    self.verts = VertArrayContainer_init()
    self.verts_translucent = VertArrayContainer_init()
    return self

cdef void VertArrayContainerTuple_free(VertArrayContainerTuple* self) nogil:
    VertArrayContainer_free(self.verts)
    VertArrayContainer_free(self.verts_translucent)
    free(self)

cdef VertArrayContainerTuple* create_lod0_sub_chunk(
    unsigned int[:, :, :] larger_blocks,
    BlockModelManager block_model_manager,
    long[:] sub_chunk_offset,
) nogil:
    cdef int x, y, z, x_, y_, z_, dx, dy, dz  # location variables

    # float counters
    cdef unsigned int vert_count, vert_end, vertex, vertex_attr

    cdef float shade
    cdef unsigned int block_id, cull_id
    cdef BlockModel* block_model
    cdef VertArray* vert_array

    cdef VertArray* vert_table = VertArray_new(ARRAY_SIZE)
    vert_table.size = 0
    cdef VertArray* trans_vert_table = VertArray_new(ARRAY_SIZE)
    trans_vert_table.size = 0

    cdef int size_x = larger_blocks.shape[0] - 2
    cdef int size_y = larger_blocks.shape[1] - 2
    cdef int size_z = larger_blocks.shape[2] - 2

    cdef VertArrayContainerTuple* verts = VertArrayContainerTuple_init()

    for x in range(size_x):
        for y in range(size_y):
            for z in range(size_z):
                x_ = x + 1
                y_ = y + 1
                z_ = z + 1
                block_id = larger_blocks[x_, y_, z_]
                block_model = block_model_manager.blocks[block_id]
                for cull_id in range(7):
                    if block_model.faces[cull_id]:
                        # iterate through each cull direction
                        if cull_id:
                            dx = x_ + CULL_MAP[cull_id][0]
                            dy = y_ + CULL_MAP[cull_id][1]
                            dz = z_ + CULL_MAP[cull_id][2]
                            # If the next block is opaque or both blocks are full transparent blocks, do nothing
                            if block_model_manager.blocks[larger_blocks[dx, dy, dz]].is_transparent == 0 or \
                               block_model_manager.blocks[larger_blocks[dx, dy, dz]].is_transparent == block_model_manager.blocks[larger_blocks[x_, y_, z_]].is_transparent == 1:
                                continue

                        vert_array = block_model.faces[cull_id]
                        vert_count = vert_array.size

                        if block_model.is_transparent == 1:
                            vert_end = trans_vert_table.size+vert_count
                            if vert_end > ARRAY_SIZE:
                                VertArrayContainer_append(verts.verts_translucent, trans_vert_table)
                                trans_vert_table = VertArray_new(ARRAY_SIZE)
                                trans_vert_table.size = 0
                                vert_end = vert_count
                            memcpy(&trans_vert_table.arr[trans_vert_table.size], vert_array.arr, vert_count * sizeof(float))
                            for vertex in range(trans_vert_table.size, vert_end, ATTR_COUNT):
                                trans_vert_table.arr[vertex + 0] += sub_chunk_offset[0] + x
                                trans_vert_table.arr[vertex + 1] += sub_chunk_offset[1] + y
                                trans_vert_table.arr[vertex + 2] += sub_chunk_offset[2] + z
                                shade = ((trans_vert_table.arr[vertex + 1] / 32) % 2)
                                if shade > 1:
                                    shade = - shade + 2
                                shade = 0.9 + 0.2 * shade
                                for vertex_attr in range(9, 12):
                                    trans_vert_table.arr[vertex + vertex_attr] *= shade
                            trans_vert_table.size += vert_count
                        else:
                            vert_end = vert_table.size+vert_count
                            if vert_end > ARRAY_SIZE:
                                VertArrayContainer_append(verts.verts, vert_table)
                                vert_table = VertArray_new(ARRAY_SIZE)
                                vert_table.size = 0
                                vert_end = vert_count
                            memcpy(&vert_table.arr[vert_table.size], vert_array.arr, vert_count * sizeof(float))
                            for vertex in range(vert_table.size, vert_end, ATTR_COUNT):
                                vert_table.arr[vertex + 0] += sub_chunk_offset[0] + x
                                vert_table.arr[vertex + 1] += sub_chunk_offset[1] + y
                                vert_table.arr[vertex + 2] += sub_chunk_offset[2] + z
                                shade = ((vert_table.arr[vertex + 1] / 32) % 2)
                                if shade > 1:
                                    shade = - shade + 2
                                shade = 0.9 + 0.2 * shade
                                for vertex_attr in range(9, 12):
                                    vert_table.arr[vertex + vertex_attr] *= shade
                            vert_table.size += vert_count

    if vert_table.size:
        VertArrayContainer_append(verts.verts, vert_table)
    else:
        VertArray_free(vert_table)
    if trans_vert_table.size:
        VertArrayContainer_append(verts.verts_translucent, trans_vert_table)
    else:
        VertArray_free(trans_vert_table)

    return verts


cdef tuple _create_lod0_chunk(
    BlockModelManager block_model_manager,
    list blocks,
    long[:] chunk_offset
):
    cdef int sub_chunk_count = len(blocks)
    cdef long[:] sub_chunk_offset
    cdef long sub_chunk_y
    cdef unsigned int[:, :, :] block_array
    cdef int i, j
    sub_chunk_verts = <VertArrayContainerTuple**>calloc(sub_chunk_count, sizeof(VertArrayContainerTuple*))
    for i in range(sub_chunk_count):
        block_array, sub_chunk_y = blocks[i]
        sub_chunk_offset = chunk_offset.copy()
        sub_chunk_offset[1] += sub_chunk_y

        sub_chunk_verts[i] = create_lod0_sub_chunk(
            block_array,
            block_model_manager,
            sub_chunk_offset,
        )

    cdef unsigned long vert_size = 0
    cdef unsigned long vert_size_translucent = 0
    cdef VertArrayContainerTuple* vert_array_container_tuple
    cdef VertArrayContainer* vert_array_container
    cdef VertArray* vert_array

    for i in range(sub_chunk_count):
        vert_array_container_tuple = sub_chunk_verts[i]
        vert_array_container = vert_array_container_tuple.verts
        for j in range(vert_array_container.used):
            vert_array = vert_array_container.arrays[j]
            vert_size += vert_array.size
        vert_array_container = vert_array_container_tuple.verts_translucent
        for j in range(vert_array_container.used):
            vert_array = vert_array_container.arrays[j]
            vert_size_translucent += vert_array.size

    chunk_verts = array.clone(array.array("f"), vert_size, zero=False)
    chunk_verts_translucent = array.clone(array.array("f"), vert_size_translucent, zero=False)

    vert_size = 0
    vert_size_translucent = 0

    for i in range(sub_chunk_count):
        vert_array_container_tuple = sub_chunk_verts[i]
        vert_array_container = vert_array_container_tuple.verts
        for j in range(vert_array_container.used):
            vert_array = vert_array_container.arrays[j]
            memcpy(&chunk_verts.data.as_floats[vert_size], vert_array.arr, vert_array.size * sizeof(float))
            vert_size += vert_array.size
        vert_array_container = vert_array_container_tuple.verts_translucent
        for j in range(vert_array_container.used):
            vert_array = vert_array_container.arrays[j]
            memcpy(&chunk_verts_translucent.data.as_floats[vert_size_translucent], vert_array.arr, vert_array.size * sizeof(float))
            vert_size_translucent += vert_array.size

    for i in range(sub_chunk_count):
        VertArrayContainerTuple_free(sub_chunk_verts[i])
    free(sub_chunk_verts)

    return [chunk_verts], [chunk_verts_translucent]


def _extend_blocks(resource_pack, block_palette):
    if not hasattr(resource_pack, "block_model_manager"):
        # TODO: set up a proper location for these
        resource_pack.block_model_manager = BlockModelManager()

    block_model_manager = resource_pack.block_model_manager

    done_count = len(block_model_manager)
    state_count = len(block_palette)

    for block_id in range(done_count, state_count):
        # more block states have been added

        model = resource_pack.get_block_model(
            block_palette[block_id]
        )
        vert_map = {}
        for py_cull_dir in model.faces.keys():
            if py_cull_dir in CULL_STR_INDEX:
                # the vertices in model space
                verts = model.verts[py_cull_dir].reshape((-1, 3))
                tverts = model.texture_coords[py_cull_dir].reshape((-1, 2))
                faces = model.faces[py_cull_dir]

                py_vert_table = numpy.zeros(
                    (faces.size, ATTR_COUNT), dtype=numpy.float32
                )
                py_vert_table[:, :3] = verts[faces]
                py_vert_table[:, 3:5] = tverts[faces]

                vert_index = 0
                for texture_index in model.texture_index[py_cull_dir]:
                    py_vert_table[vert_index : vert_index + 3, 5:9] = resource_pack.texture_bounds(model.textures[texture_index])
                    vert_index += 3

                py_vert_table[:, 9:12] = (
                    model.tint_verts[py_cull_dir].reshape((-1, 3))[faces]
                    * _brightness_multiplier[py_cull_dir]
                )
                vert_map[py_cull_dir] = py_vert_table
        block_model_manager.add_block(vert_map, model.is_transparent)


def create_lod0_chunk(
    resource_pack,
    chunk_offset: numpy.ndarray,
    blocks,
    block_palette,
    vert_len,  # should be 12
):
    _extend_blocks(resource_pack, block_palette)
    return _create_lod0_chunk(
        resource_pack.block_model_manager,
        blocks,
        chunk_offset
    )

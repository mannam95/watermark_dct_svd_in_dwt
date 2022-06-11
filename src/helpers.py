import numpy as np

def create_non_overlapping_blocks(data: np.ndarray, block_size: tuple):
    """
    This function divides the given 2D data into the given block size

    :param data: 2D array with input data.
    :param block_size: a tupel like 8*8
    :return: Returns the divided non-overlapping blocks.
    """ 
    height, width = data.shape
    block_height, block_width = block_size

    blocks_array = data.reshape(height // block_height,
                                block_height,
                                width // block_width,
                                block_width)
    blocks_array = blocks_array.swapaxes(1, 2)
    return blocks_array


def reshape_2d_data_with_padding(data: np.ndarray, block_size: tuple):
    """
    This function extends the given 2d data by adding extra zeros as padding.
    In such a way the given array will be exactly divisible by the given block_size.

    :param data: 2D array with input data.
    :param block_size: a tupel like 8*8
    :return: Returns the a new 2D array that is divisible by the given block_size
    """ 
    height, width = data.shape
    block_height, block_width = block_size

    x_padding_dims = height + ( block_height - (height % block_height))
    y_padding_dims = width + ( block_width - (width % block_width))

    new_data = np.empty(shape=(x_padding_dims, y_padding_dims))
    new_data.fill(0)

    new_data[0:height, 0:width] = data

    return new_data
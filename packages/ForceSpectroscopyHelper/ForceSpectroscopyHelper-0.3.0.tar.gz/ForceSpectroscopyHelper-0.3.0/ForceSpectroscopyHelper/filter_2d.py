from ForceSpectroscopyHelper.structures import *
from scipy.ndimage import gaussian_filter

def GaussianMap(data, sigma):
    return gaussian_filter(data, sigma)

def GaussianHannMap(data, kernel_size, sigma_x, sigma_y):
    filter = np.zeros(shape=(kernel_size, kernel_size))
    for x in range(0, kernel_size):
        for y in range(0, kernel_size):
            filter[x, y] = np.exp(-(x+1-kernel_size/2)**2/2/sigma_x/sigma_x-(y+1-kernel_size/2)**2/2/sigma_y/sigma_y) * np.sin(np.pi*(y+1)/kernel_size) * np.sin(np.pi*(y+1)/kernel_size)
    return convolve(data, filter)

def SmoothMap(data, N):
    I = data.shape[0]
    J = data.shape[1]
    data = np.array(data)
    ResultData = np.zeros((I, J))
    for j in range(0, J):
        for i in range(int((N - 1) / 2), int(I - (N - 1) / 2)):
            ResultData[i][j] = 0
            for m in range(int(i - (N - 1) / 2), int(i + (N - 1) / 2 + 1)):
                ResultData[i][j] += data[m][j]
            ResultData[i][j] = ResultData[i][j] / N

        for i in range(0, int((N - 1) / 2)):
            ResultData[i][j] = 0
            for m in range(0, int(i + (N - 1) / 2 + 1)):
                ResultData[i][j] += data[m][j]
            ResultData[i][j] = ResultData[i][j] / ((N - 1) / 2 + i + 1)

        for i in range(int(I - (N - 1) / 2), I):
            ResultData[i][j] = 0
            for m in range(int(i - (N - 1) / 2), I):
                ResultData[i][j] += data[m][j]
            ResultData[i][j] = ResultData[i][j] / ((N - 1) / 2 + I - i)
    return ResultData


def FFTMap(data, lowPass):
    I = data.shape[0]
    J = data.shape[1]
    data = np.array(data)
    window = np.flipud(np.hamming(I))
    ResultData = np.zeros((I, J))
    for j in range(0, J):
        fft = np.fft.rfft(data[:, j] * window)
        fft[lowPass:] = 0
        y = np.fft.irfft(fft) / window
        ResultData[:, j] = y
    return ResultData


def FFT2Map(data, lowPass):
    I = data.shape[0]
    J = data.shape[1]
    data = np.array(data)
    window = np.flipud(np.hamming(I) * np.hamming(J))
    fft = np.fft.rfft2(data * window)
    plt.imshow(fft)
    plt.colorbar()
    plt.show()

    fft[lowPass:] = 0
    im = np.fft.irfft2(fft) / window

    plt.imshow(im)
    plt.colorbar()
    plt.show()
    return im


# Assuming the image has channels as the last dimension.
# filter.shape -> (kernel_size, kernel_size, channels)
# image.shape -> (width, height, channels)
def convolve(image, filter, padding=(1, 1)):
    # For this to work neatly, filter and image should have the same number of channels
    # Alternatively, filter could have just 1 channel or 2 dimensions

    if (image.ndim == 2):
        image = np.expand_dims(image, axis=-1)  # Convert 2D grayscale images to 3D
    if (filter.ndim == 2):
        filter = np.repeat(np.expand_dims(filter, axis=-1), image.shape[-1], axis=-1)  # Same with filters
    if (filter.shape[-1] == 1):
        filter = np.repeat(filter, image.shape[-1], axis=-1)  # Give filter the same channel count as the image

    # print(filter.shape, image.shape)
    assert image.shape[-1] == filter.shape[-1]
    size_x, size_y = filter.shape[:2]
    width, height = image.shape[:2]

    output_array = np.zeros(((width - size_x + 2 * padding[0]) + 1,
                             (height - size_y + 2 * padding[1]) + 1,
                             image.shape[-1]))  # Convolution Output: [(W−K+2P)/S]+1

    padded_image = np.pad(image, [
        (padding[0], padding[0]),
        (padding[1], padding[1]),
        (0, 0)
    ])

    for x in range(
            padded_image.shape[0] - size_x + 1):  # -size_x + 1 is to keep the window within the bounds of the image
        for y in range(padded_image.shape[1] - size_y + 1):
            # Creates the window with the same size as the filter
            window = padded_image[x:x + size_x, y:y + size_y]

            # Sums over the product of the filter and the window
            output_values = np.sum(filter * window, axis=(0, 1))

            # Places the calculated value into the output_array
            output_array[x, y] = output_values

    return output_array
import matplotlib.pyplot as plt
from skimage.transform import rescale
import numpy as np

def load_population_matrix(path, scale):
    # Locations of Japans map corners:
    # Upper Left  ( 122.9320829,  45.5245833) (122d55'55.50"E, 45d31'28.50"N)
    # Lower Left  ( 122.9320829,  24.0412501) (122d55'55.50"E, 24d 2'28.50"N)
    # Upper Right ( 153.9904161,  45.5245833) (153d59'25.50"E, 45d31'28.50"N)
    # Lower Right ( 153.9904161,  24.0412501) (153d59'25.50"E, 24d 2'28.50"N)
    # Center      ( 138.4612495,  34.7829167) (138d27'40.50"E, 34d46'58.50"N)
    # https://stackoverflow.com/questions/63004971/find-latitude-longitude-coordinates-of-every-pixel-in-a-geotiff-image

    img = plt.imread(path)
    img = img[:,:,0]
    return rescale(img, scale, anti_aliasing=False)

if __name__ == "__main__":
    img = load_population_matrix('jpn_ppp_2020_1km_Aggregated.tif', 0.2)
    print(img.shape)
    plt.imshow(img, cmap='viridis')
    plt.show()
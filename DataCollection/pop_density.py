import matplotlib.pyplot as plt
from skimage.transform import rescale
import numpy as np

def load_population_matrix(path, scale):
    img = plt.imread(path)
    img = img[:,:,0]
    return rescale(img, scale, anti_aliasing=False)

if __name__ == "__main__":
    img = load_population_matrix('jpn_ppp_2020_1km_Aggregated.tif', 0.2)
    print(img.shape)
    plt.imshow(img, cmap='viridis')
    plt.show()
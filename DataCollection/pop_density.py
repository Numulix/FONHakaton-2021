import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from skimage.transform import rescale
from scipy.optimize import minimize

plt.rcParams["figure.figsize"] = (15, 15)
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

def get_optimal_distribution(available_res=10000, ret_size=10):
    cities = pd.read_csv('jp.csv')[['city', 'population']]
    goal = np.random.randint(10, 100, size=len(cities))
    n = len(cities)
    cities.head()

    def cost_fun(x):
        return np.mean((x-goal)**2)

    def constraint1(x):
        return available_res - np.sum(x)

    # initial guesses
    x0 = np.zeros(n)
    x0[0] = available_res

    # show initial objective
    # print('Initial Objective: ' + str(cost_fun(x0)))

    # optimize
    b = (0, available_res)
    bnds = [b for _ in range(n)] # np.tile(b, (1, len(cities)))

    con1 = {'type': 'ineq', 'fun': constraint1}
    cons = ([con1])
    solution = minimize(cost_fun, x0, bounds=bnds, constraints=cons)
    x = np.array(solution.x).astype(np.int64)

    ret = [x for x in zip(cities['city'].values, x)]
    ret.sort(key=lambda x: x[1], reverse=True)
    return ret[0:ret_size]

if __name__ == "__main__":
    img = load_population_matrix('jpn_ppp_2020_1km_Aggregated.tif', 0.2)
    print(img.shape)
    plt.imshow(img, cmap='viridis')
    plt.show()

    print(get_optimal_distribution())
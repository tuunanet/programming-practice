from multiprocessing import Pool, Process, Array
import numpy as np

if __name__ == '__main__':
    #1
    print("# 1. Create some random NumPy array data")
    m = 100
    n = 100
    X = np.random.randint(0, 1000, size=(m, n), dtype=int)
    print(f'--- Created random integer array X with shape={X.shape}, '
    'and elements bound between [0, 1000]')

    #2
    print("# 2. Create shared memory array")

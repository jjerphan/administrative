
import numpy as np

def load_data():
    f = open('data/gisette_train.data')
    X = np.fromfile(f, dtype=np.float64, sep=' ')
    f.close()
    X = X.reshape((13500, -1))

    f = open('data/gisette_train.labels')
    y = np.fromfile(f, dtype=np.float64, sep=' ')
    f.close()

    return  X, y
    
    
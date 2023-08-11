import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def load_files():
    print("Loading...")
    global __data_columns, __locations
    
    with open("./artifacts/columns.json") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]
    
    global __model
    with open("./artifacts/house_price_prediction_model.pickle", "rb") as f:
        __model = pickle.load(f)
    
    print("Loading completed")


if __name__ == '__main__':
    load_files()
    print(get_estimated_price("1st Phase JP Nagar", 1000, 2, 2))

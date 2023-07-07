import pickle
import numpy as np
import config
import json

class Diamondprice():
    def __init__(self):
        pass

    def get_data(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self, carat, cut, color, clarity, depth, table, x, y, z):
        self.get_data()

        cut = self.json_data["cut"][cut]
        color = self.json_data["color"][color]
        clarity = self.json_data["clarity"][clarity]  
       


        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0][0] = carat
        test_array[0][1] = cut
        test_array[0][2] = color
        test_array[0][3] = clarity
        test_array[0][4] = depth
        test_array[0][5] = table
        test_array[0][6] = x
        test_array[0][7] = y
        test_array[0][8] = z
        

        predicted_price = self.model.predict(test_array)[0]
        return predicted_price
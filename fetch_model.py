import joblib
import sklearn
loaded_data = joblib.load('grid_knn.pkl')

print(loaded_data)


def get_result(properties: []) -> bool:
    t = loaded_data.predict(properties)
    return t[0] == 1

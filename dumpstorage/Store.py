import pickle
import os

# Save
def save(obj, fileName):
    with open("dumpstorage/" + fileName + "obj", 'wb') as f:
        pickle.dump(obj, f)


def load(fileName):
    with open(os.path.join("dumpstorage", fileName), 'rb') as f:
        config_dictionary = pickle.load(f)
        return config_dictionary

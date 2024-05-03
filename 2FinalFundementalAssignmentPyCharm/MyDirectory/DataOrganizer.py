

import pickle

def save_data(data, filename):
    """Save data to a binary file using Pickle."""
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def load_data(filename):
    """Load data from a binary file using Pickle."""
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return None
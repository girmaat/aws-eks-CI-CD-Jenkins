import json
import os

def load_orders():
    data_path = os.path.join(os.path.dirname(__file__), "../data/seed.json")
    with open(data_path, "r") as f:
        orders = json.load(f)
    return orders

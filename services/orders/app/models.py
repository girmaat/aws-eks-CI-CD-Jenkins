from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    quantity: int

class Order(BaseModel):
    customer_name: str
    items: List[Item]
    total: float

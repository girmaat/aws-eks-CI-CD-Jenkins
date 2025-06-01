from fastapi import APIRouter, HTTPException
from .models import Order
from .seed_loader import load_orders

router = APIRouter()

# Load orders from seed data
orders_db = load_orders()

@router.get("/", summary="List all orders")
async def get_all_orders():
    return orders_db

@router.get("/{order_id}", summary="Get order by ID")
async def get_order_by_id(order_id: int):
    for order in orders_db:
        if order["id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@router.post("/", summary="Create a new order")
async def create_order(order: Order):
    new_order = order.dict()
    new_order["id"] = max(o["id"] for o in orders_db) + 1 if orders_db else 1
    orders_db.append(new_order)
    return {"message": "Order created", "order": new_order}

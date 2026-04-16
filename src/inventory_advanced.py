import numpy as np

def advanced_inventory(future_preds, lead_time=3, service_level=1.65, on_hand=50):

    # Step 1: Demand during lead time
    demand_lead_time = sum(future_preds[:lead_time])

    # Step 2: Standard deviation of demand
    std_dev = np.std(future_preds)

    # Step 3: Safety Stock
    safety_stock = service_level * std_dev * (lead_time ** 0.5)

    # Step 4: Reorder Point
    reorder_point = demand_lead_time + safety_stock

    # Step 5: Order Quantity
    order_qty = max(0, reorder_point - on_hand)

    print("\nADVANCED INVENTORY CALCULATION")
    print(f"Demand during Lead Time: {demand_lead_time}")
    print(f"Safety Stock: {safety_stock}")
    print(f"Reorder Point: {reorder_point}")
    print(f"Order Quantity: {order_qty}")

    return {
        "demand_lead_time": demand_lead_time,
        "safety_stock": safety_stock,
        "reorder_point": reorder_point,
        "order_qty": order_qty
    }
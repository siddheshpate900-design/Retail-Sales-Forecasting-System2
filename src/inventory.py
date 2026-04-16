import numpy as np

def inventory_calc(preds):

    avg_demand = np.mean(preds)

    # safety stock (extra buffer)
    safety_stock = avg_demand * 0.2

    # reorder point
    reorder_point = avg_demand + safety_stock

    print("\nInventory Calculation")
    print("Average Demand:", avg_demand)
    print("Safety Stock:", safety_stock)
    print("Reorder Point:", reorder_point)

    return {
        "avg_demand": avg_demand,
        "safety_stock": safety_stock,
        "reorder_point": reorder_point
    }
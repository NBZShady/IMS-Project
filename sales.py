import random

def daily_sales(available_items, inventory_records, current_day):

    """
    Handles daily sales, updates inventory records, and adjusts available items.

    Parameters:
    available_items (int): The number of items currently available.
    inventory_records (dict): Dictionary containing inventory records by day.
    current_day (int): The current day of the week.

    Returns:
    int: Updated number of available items after sales.
    """

    # Initialize sold_units to zero for days with no sales
    sold_units = 0

    # Generate sales data for the day, excluding restocking day (every 7th day)
    if current_day % 7 != 0:
        # Randomly determine units sold (up to 200)
        sold_units = random.randint(0, 200)
        available_items -= sold_units # Reduce available items by sold units

        # Ensure available items do not go below zero
        if available_items < 0:
            available_items = 0

    # Update the inventory record for the current day
    inventory_records[current_day] = (
        current_day,
        sold_units,
        inventory_records[current_day][2],  # Retain restocked units from previous records
        available_items,
    )
    return available_items # Return the updated number of available items
    



  
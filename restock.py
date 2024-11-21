def restock_inventory(available_items, inventory_records, current_day):

    """ 
    Handles restocking inventory on specific days and updates the inventory records. 

    Parameters: 
    available_items (int): The number of items currently available. 
    inventory_records (list of tuples): List of previous inventory records. 
    current_day (int): The current day of the week. 
  
    Returns: tuple: Updated inventory_records and available_items after restocking. 
    """


    
    restocked_units = 0

    # Special handling for Day 0 to fully restock
    if current_day == 0: available_items= 0 

    # Restock on every 7th day with a limit to not exceed 2000 total
    if current_day % 7 == 0:
        # Calculate restocked units needed to reach the maximum inventory (2000 units)
        restocked_units = 2000 - available_items
        available_items += restocked_units # Update available items after restocking

    # Update or append restocking record for the current day
    inventory_records.append((
        current_day,
        0,              # No sales are made on restocking day
        restocked_units,
        available_items
    ))

    return available_items # Return the updated inventory records and available items




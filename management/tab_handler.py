from menu import products

def calculate_tab(consumption):
    subtotal = 0.00

    for product in products:
        for item in consumption:
            if product["_id"] == item["_id"]:
                subtotal += product["price"] * item["amount"]

    return {'subtotal': f'{round(subtotal, 2)}'}

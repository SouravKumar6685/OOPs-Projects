from Admin import *
from Cart import *
from Customer import *
from Order import *
from PaymentGateway import *
from Product import *
from User import *

product_list = [
    Product("Iphone 16", 79999, "Electronics", 10, "High-performance mobile"),
    Product("Sony Headphone", 30000, "Electronics", 50, "Noise-cancelling headphones"),
    Product("Smart Watch", 2000, "Electronics", 25, "Latest smartwatch")

]

admin = Admin("Sourav6685", "sourav6685@gmail.com", "password1", "Pagalpur, Dholakpur, Imaginary")

customer = Customer("Sourav_singh", "sourav6685@gmail.com", "password1", "Badlapur, gokuldham, Imaginary")

if customer.login("Sourav_singh","password1"):

    for product in product_list:
        product.display_details()

    customer.cart.add_to_cart(product_list[0], 1)
    customer.cart.add_to_cart(product_list[1],2)


    customer.cart.calculate_total()
    customer.place_order()

    if customer.order_history:
        order = customer.order_history[0]
        admin.update_order_Status(order,"Shipped")
        Order.add_Status_update("Shipped","Your order has been Shipped.")

        admin.update_order_Status(order, "Delivered")
        Order.add_Status_update("Delivered", "Your order has been Delivered.")
    
    customer.view_order_history()

    customer.logout()
select products.product_name, order_details.quantity, orders.order_date, 
customers.contact_name
from products
join order_details on products.product_id = order_details.product_id
join orders on order_details.order_id = orders.order_id
join customers on orders.customer_id = customers.customer_id


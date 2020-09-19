from gbdxtools import Interface

# print(gbdx.ordering.order(order_id))
# print(order_id)

# print(gbdx.ordering.status(order_id))

from gbdxtools import Interface
gbdx = Interface()

order_id = gbdx.ordering.order("104001005C434C00")
print(order_id)

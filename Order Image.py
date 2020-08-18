from gbdxtools import Interface
gbdx = Interface()

order_id = gbdx.ordering.order("10400100143FC900")
print(order_id)
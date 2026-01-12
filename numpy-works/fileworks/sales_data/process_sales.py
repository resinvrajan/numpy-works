import numpy as np
data=np.loadtxt("fileworks\\sales_data\\sales.csv",delimiter=",",skiprows=1,dtype="str")
print(data)
units_sold=(data[:,3].astype("int"))
print(units_sold)
print("total =",np.sum(units_sold))
print("max unit=",np.max(units_sold))
print("min unit=",np.min(units_sold))
print("average =", np.average(units_sold))

# revenue finding units_sold x price
revenue=(data[:,3].astype("int"))*(data[:,4].astype("int"))
print("revenue=",revenue)
print("total revenue=",np.sum(revenue))
# unit_sold >8
print(data[data[:,3].astype("int")>8])
# category == Electronics
print(data[data[:,2]=="Electronics"])
# flat 100 for all products
discount=data[:,4].astype("int")-100
print(discount)
data[:,4]=data[:,4].astype("int")-100
print("discount",data)
# total revenue of north region
north_region_sales_report=data[data[:,-1]=="North"]
print(north_region_sales_report)
units_sold_of_north=north_region_sales_report[:,3].astype("int")
print(units_sold_of_north)
unit_price_of_north=north_region_sales_report[:,4].astype("int")
revenue_of_north=units_sold_of_north*unit_price_of_north
print(revenue_of_north)
print("total revenue of north=",np.sum(revenue_of_north))
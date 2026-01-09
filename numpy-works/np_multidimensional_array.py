import numpy as np
sales_report=np.array([
            [   [10,11],
                [12,13]
            ],
            [   [100,110],
                [120,130]
            ]
])
print(sales_report.ndim)
print(sales_report.shape)
print(sales_report[1,0,0])
print(sales_report[1,1,1])
sales_report[0,1,1]=10
print(sales_report)
print(sales_report[0,0,1])
sales_report[1,1,1]=150
print(sales_report)
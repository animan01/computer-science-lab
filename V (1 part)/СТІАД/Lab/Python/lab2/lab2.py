
# libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('../csv/nuclear.csv')
data.set_index("Index", inplace= True)
print(data.head())

# Data in Graph
data.plot()
plt.show()


# Data in box plot show.
data.boxplot()
plt.show()

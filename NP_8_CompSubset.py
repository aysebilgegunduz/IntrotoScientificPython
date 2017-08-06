import numpy as np
import matplotlib.pyplot as plt

#The dataformat is: year, month, day, daily average temperature, low, high, location.

data = np.genfromtxt('stockholm_td_adj.dat')

#If we are interested in the average temperature only in a particular month, say February,
                # then we can create a index mask and use it to select only the data for
# that month using:

print(np.unique(data[:,1]))   # the month column takes values from 1 to 12

mask_feb = data[:,1] == 2

# the temperature data is in column 3
months = np.arange(1,13)
monthly_mean = [np.mean(data[data[:,1] == month, 3]) for month in months]
fig, ax = plt.subplots()
ax.bar(months, monthly_mean)
ax.set_xlabel("Month")
ax.set_ylabel("Monthly avg. temp.")
plt.show(fig)

# week14_chap_visualization_06.py
import matplotlib.pyplot as plt
import numpy as np

# x (0 < x <20)

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505.0, 11865.3, 22105.3]


plt.bar(range(len(years)), gdp)
plt.title('GDP per capita')
plt.xlabel('year')
plt.ylabel('GDP ($)')


plt.xticks(range(len(years)), years)
plt.show()

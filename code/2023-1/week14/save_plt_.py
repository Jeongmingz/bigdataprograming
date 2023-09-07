# save_plt_.py
import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505.0, 11865.3, 22105.3]


# plt.plot(x, y) => liner graph
plt.plot(years, gdp, color='green', marker='x', linestyle='-') # solid, dotted, dashed
plt.title('GDP per capita')
plt.xlabel('year')
plt.ylabel('GDP ($)')


plt.savefig('gdp_dpi_1000.png', dpi=1000)  # dot per inch
plt.show()

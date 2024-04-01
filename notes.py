// Import data
import pandas as pd
sales = pd.read_csv('sales_data.csv', parse_dates = ['Date'])


// Understand the structure of the data
sales.head()
sales.shape
sales.info()

// Understand the statistical properties of the data
sales.describe()  // for quick statistical overview




import pandas as pd
app_data = pd.read_csv('googleplaystore.csv')
app_data.dropna()

"""
Cleans Installs column by getting rid of "+"s and "," and turns into str and then int
"""
app_data.Installs = [x.strip('+') for x in app_data.Installs]
app_data.Installs = app_data.Installs.str.replace(',', '')
app_data.Installs = app_data.Installs.astype(str).astype(int)

"""
Gets apps that have 1 billion+ downloads and print these apps with their categories
"""
top_downloads = app_data.loc[app_data.loc[:, 'Installs'] == 1000000000,:]
top_downloads[['App','Category']]

"""
Which app categories have the most downloads
"""
#sum all Installs from certains categories, and get max from that list
#category_data = app_data.groupby(['Genres']).sum()
category_data = app_data.groupby('Genres')['Installs'].sum()
category_data[category_data{Genres:'Communication'}]
category_data.loc[category_data.loc[:, 'Genres'] == 'Communication',:]

"""
Do apps with more reviews have more downloads?
"""
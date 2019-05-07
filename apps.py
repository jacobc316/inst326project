import pandas as pd
import matplotlib.pyplot as plt
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
print(top_downloads[['App','Category']])

"""
Gets app categories that have the most downloads
"""
#sum all Installs from certains categories, and get max from that list
category_data = app_data.groupby('Genres')['Installs'].sum().sort_values(ascending=False)
print("The most popular app categories by total downloads are:")
print(category_data.head())
#max_downloads = 0
#for genre, count in category_data.iteritems():
    #if count > max_downloads:
        #max_downloads = count
        #print("The most popular app cateogry by total downloads is '%s' with %i downloads" %(genre, max_downloads))
cat_data = category_data[:20].plot.bar()
cat_data.set_title('Top Categories by Installs')
cat_data.set_xlabel("Categories")
cat_data.set_ylabel("Installs (1.0 = 10 Billion)")
plt.show()


"""
Do apps with more reviews have more downloads?
"""
review_data_categories = app_data.groupby('Genres')['Reviews'].sum().sort_values(ascending=False)
print("The most popular app categories by total reviews are:")
print(review_data_categories.head())
rev_data = review_data_categories[:20].plot.bar()
rev_data.set_title('Top Categories by # Reviews')
rev_data.set_xlabel("Categories")
rev_data.set_ylabel("Reviews (1.0 = 1 Billion)")
plt.show()
# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True)
data.head()


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],  'Summer', (np.where(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both')))
better_event = data['Better_Event'].value_counts().index[0]
print(better_event)






# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries.drop(len(top_countries)-1, axis = 0, inplace  = True)
# print(top_countries.tail())

def top_ten(df, col_name):

    country_list = []
    top_df = df.nlargest(10, col_name)
    country_list = list(top_df['Country_Name'])
    return country_list

columns = top_countries.columns

top_10_summer = top_ten(top_countries, columns[1])
top_10_winter = top_ten(top_countries, columns[2])
top_10 = top_ten(top_countries, columns[3])
# print(top_10_summer)
# print(top_10_winter)
# print(top_10)
common = []
for country in top_10_summer:
    if country in top_10_summer and country in top_10_winter and country in top_10:
        common.append(country)

print(common)



    




# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
# print(summer_df)

fig, (ax1,ax2,ax3 ) = plt.subplots(nrows= 3, ncols = 1, figsize=(20,10))
ax1.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
ax1.set_xticklabels(summer_df['Country_Name'])
ax1.set_ylabel('Total Summer medals')
ax2.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
ax2.set_xticklabels(winter_df['Country_Name'])
ax3.set_ylabel('Total Winter medals')
ax3.bar(top_df['Country_Name'], top_df['Total_Medals'])
ax3.set_xticklabels(top_df['Country_Name'])
ax3.set_ylabel('Total medals')





# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = ''.join(summer_df[summer_df['Golden_Ratio'] == summer_max_ratio]['Country_Name'].values)
# print(summer_country_gold)
# print(summer_max_ratio)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = ''.join(winter_df[winter_df['Golden_Ratio'] == winter_max_ratio]['Country_Name'].values)

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = ''.join(top_df[top_df['Golden_Ratio'] == top_max_ratio]['Country_Name'].values)
# print(summer_df)


# --------------
#Code starts here
data_1 = data.drop(len(data)-1, axis = 0)
data_1['Total_Points'] = 3 * data_1['Gold_Total'] + 2 * data_1['Silver_Total'] + data_1['Bronze_Total'] 
most_points = max(data_1['Total_Points'])
best_country = ''.join(data_1[data_1['Total_Points'] == most_points]['Country_Name'])
print(most_points)
print(best_country)
print(data_1.head())


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total', 'Silver_Total','Bronze_Total']]
best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)
plt.show()



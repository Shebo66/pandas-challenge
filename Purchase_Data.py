#!/usr/bin/env python
# coding: utf-8

# In[1]:


 # Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load =  "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[2]:


purchase_data.head()


# In[3]:


#number of purchases
len(purchase_data)


# In[4]:


# data specific to people
players_df = purchase_data[['Gender','SN','Age']]
players_df = players_df.drop_duplicates()
players_df.head()


# In[5]:


#Total Number of Players
len(players_df)


# In[6]:


#get the number of unique items
unique_count = purchase_data['Item ID'].unique()
unique_count
len(unique_count)


# In[7]:


# get the vaerage price
average_price = purchase_data['Price'].mean()
average_price


# In[8]:


# Total revenue
sum_price = purchase_data['Price'].sum()
sum_price


# In[9]:


#create a data frame. Summary_df is a varibale name created 
summary_df = pd.DataFrame({'Number of Unique Items': len(unique_count),
                          'Average Price': average_price,
                           'Number of Purchases': len(purchase_data),
                           'Total Revenue': [sum_price]})
#the []in sum_price turned into a list
#Purchasing Analysis Total
summary_df


# In[10]:


# get unique values of male and female. We will use the players details. value_counts is a panda language
players_totalgender = players_df['Gender'].value_counts()
players_totalgender


# In[42]:


players_totalgenderpercentage = 100*players_totalgender/len(players_df)
players_totalgenderpercentage.round(2)


# In[43]:


#create a dataframe
gender_data = pd.DataFrame({'Total Count': players_totalgender,
                           'Percentage of Players':players_totalgenderpercentage})
gender_data.round(2)
#Gender Demographics


# In[13]:


gender_average = purchase_data.groupby(['Gender']).mean()
gender_average = gender_average['Price']
gender_average


# In[14]:


gender_sum = purchase_data.groupby(['Gender']).sum()
gender_sum = gender_sum['Price']
gender_sum 


# In[15]:


gender_count = purchase_data.groupby(['Gender']).count()
gender_count = gender_count['Price']
gender_count


# In[16]:


average_totalperson = gender_sum/gender_data['Total Count']
average_totalperson


# In[44]:


gender_df = pd.DataFrame({'Purchase Count':gender_count,
                         'Average Purchase Price': gender_average,
                         'Total Purchase Value':gender_sum,
                         'Average Total Purchase Per Person':average_totalperson})
gender_df.round(2)
#Purchasing Analysis Gender


# In[18]:


#Set up bins (categories of ages)
bins = [0,9.9,14.9,19.9,24.9,29.9,34.9,39.9,999]
labels = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']
players_df['Age Ranges'] = pd.cut(players_df['Age'],bins,labels = labels)
age_counts = players_df['Age Ranges'].value_counts()
age_counts


# In[19]:


age_percent = 100*age_counts/len(players_df)
age_percent


# In[20]:


bin_summary = pd.DataFrame({'Total Count': age_counts,
                           'Percentage of Players': age_percent})
#This below will arrange it by index (top to bottom etc)
bin_summary = bin_summary.sort_index()
bin_summary
#Age Demographics


# In[21]:


purchase_data['Age Ranges'] = pd.cut(purchase_data['Age'],bins,labels = labels)
purchase_dataaverage = purchase_data.groupby(['Age Ranges']).mean()['Price']
purchase_dataaverage


# In[22]:


purchase_datacount = purchase_data.groupby(['Age Ranges']).count()['Price']
purchase_datacount


# In[23]:


purchase_datasum = purchase_data.groupby(['Age Ranges']).sum()['Price']
purchase_datasum


# In[24]:


purchase_dataaverageperson = purchase_datasum/bin_summary['Total Count']
purchase_dataaverageperson


# In[45]:


purchase_analysisage = pd.DataFrame({'Purchase Count':purchase_datacount,
                                    'Average Purchase Price':purchase_dataaverage,
                                    'Total Purchase Value': purchase_datasum,
                                    'Total Average Purchase Per Person':purchase_dataaverageperson})
purchase_analysisage.round(2)


# In[26]:


# Purchase total value
SN_datasum = purchase_data.groupby(['SN']).sum()['Price']
SN_datasum


# In[27]:


SN_dataaverage = purchase_data.groupby(['SN']).mean()['Price']
SN_dataaverage


# In[28]:


SN_datacount = purchase_data.groupby(['SN']).count()['Price']
SN_datacount


# In[29]:


summary_SN = pd.DataFrame({'Purchase Count':SN_datacount,
                          'Average Purchase Price':SN_dataaverage,
                          'Total Purchase Value':SN_datasum})
summary_SN = summary_SN.sort_values(['Total Purchase Value'],ascending=False)
summary_SN.head()
#Top Spenders


# In[30]:


#retrieve columns Item ID, Item Name and Item Price by dropping the others
popular_items = purchase_data.drop(columns=['Purchase ID','SN','Age', 'Gender','Age Ranges'])
popular_items.head()                                 


# In[31]:


purchase_data


# In[32]:


#count number of rows that match each item name
#when we want to select colums we use []
# to list the columns Item ID, Item Name and Price. This Price is defined in popular items cell 30, not necessarily in the big purchase data
item_data = purchase_data[['Item ID', 'Item Name', 'Price']]
item_data.head()


# In[46]:


#item_namecount = popular_items.groupby(['Item Name', 'Item ID']).count()['Price']
#item_namecount
purchase_count = popular_items.groupby(["Item ID", "Item Name"]).count()["Price"]
average_item_price = popular_items.groupby(["Item ID", "Item Name"]).mean()["Price"]
total_purchase_value = popular_items.groupby(["Item ID", "Item Name"]).sum()["Price"]
popular_df = pd.DataFrame({
    "Purchase Count": purchase_count,
    "Item Price": average_item_price,
    "Total Purchase Value": total_purchase_value
})
popular_sorted_df = popular_df.sort_values("Purchase Count", ascending=False)
popular_sorted_df.head(5).round(2)
#Most popular items


# In[34]:


#item_idcount = popular_items.groupby(['Item ID']).count()['Price']
#item_idcount


# In[35]:


#item_namesum = popular_items.groupby(['Item Name']).sum()['Price']
#item_namesum 


# In[36]:


#item_idsum = popular_items.groupby(['Item ID']).sum()['Price']
#item_idsum 


# In[39]:


purchase_count = popular_items.groupby(["Item ID", "Item Name"]).count()["Price"]
average_item_price = popular_items.groupby(["Item ID", "Item Name"]).mean()["Price"]
total_purchase_value = popular_items.groupby(["Item ID", "Item Name"]).sum()["Price"]
popular_df = pd.DataFrame({
    "Purchase Count": purchase_count,
    "Item Price": average_item_price,
    "Total Purchase Value": total_purchase_value
})
popular_sorted_df = popular_df.sort_values("Total Purchase Value", ascending=False)
popular_sorted_df.head(5).round(2)
#Most profitable items


# In[ ]:





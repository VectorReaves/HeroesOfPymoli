#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[41]:


# We need to use numpy for this activity because of its focus on tabular data. 
import pandas as pd
import numpy as np

# Import the file using the address on Jupyter.
file = "Resources/purchase_data.csv"
purchaseData = pd.read_csv(file)
purchaseData_df = pd.DataFrame(purchaseData)
purchaseData_df.head()


# In[42]:


# We use this to count the total amount of purchase data.
playerAmount = purchaseData_df["SN"].count()
playerAmount


# ## Player Count

# * Display the total number of players
# 

# In[53]:


# Set vatiables to find unqiue players data. We use the drop function to remove duplicates.
playerDemographs = purchaseData.loc[:, ["Gender", "SN", "Age"]]
playerDemographs = playerDemographs.drop_duplicates()
playerNumbers = playerDemographs.count()[0]
pd.DataFrame({"Total Players": [playerNumbers]})


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[61]:


uniqueItem = len(purchaseData_df["Item ID"].unique())
uniqueItem

purchaseTotalAmount = purchaseData_df["Purchase ID"].count()
purchaseTotalAmount

revenueTotalAmount = purchaseData_df["Price"].sum()
revenueTotalAmount
avgPrice = purchaseData_df["Price"].mean()
avgPrice

avgPrice2 = revenueTotalAmount/purchaseTotalAmount
avgPrice2

# Display the summary data frame
transactionResults_df = pd.DataFrame([{"Number of Unique Items": uniqueItem, "Average Price": avgPrice,
                                      "Number of Purchases": purchaseTotalAmount, "Total Revenue": revenueTotalAmount}])
transactionResults_df["Average Price"] = transactionResults_df["Average Price"].map("${:,.2f}".format)
transactionResults_df["Total Revenue"] = transactionResults_df["Total Revenue"].map("${:,.2f}".format)
transactionResults_df

# reorganazing the column order for summary dataframe
transResultsFormer_df = transactionResults_df[["Number of Unique Items","Average Price","Number of Purchases", "Total Revenue" ]]
transResultsFormer_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[68]:



# The value counts method counts unique values in a column, then dataframe created to hold results
genderInfo_df = pd.DataFrame(purchaseData_df["Gender"].value_counts())
genderInfo_df

playerPercent = (purchaseData_df["Gender"].value_counts()/playerAmount)*100
playerPercent

# Calculations performed and added into Data Frame as a new column
genderInfo_df["Percentage of Players"] = playerPercent
genderInfo_df["Percentage of Players"] = genderInfo_df["Percentage of Players"].map("{:,.2f}%".format)
genderInfo_df

# Change the order of the columns 
genderInfo2_df = genderInfo_df[["Percentage of Players", "Gender"]]
genderInfo2_df

# Rename the column "Gender" to "Total Counts" using .rename(columns={})
fin_genderInfo_df = genderInfo2_df.rename(columns={"Gender":"Total Count"})
fin_genderInfo_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[76]:


# seperate gender groups
groupedGenderData_df = purchaseData_df.groupby(["Gender"])
groupedGenderData_df["Purchase ID"].count().head(10)

# now we want to format the string using the f string.
purchaseTotal1 = groupedGenderData_df["Price"].sum()
purchaseTotal1.head()
purchaseTotal2 = purchaseTotal1.map("${:,.2f}".format)
purchaseTotal2.head()
purchaseAverage = groupedGenderData_df["Price"].mean()
purchaseAverage.head()
purchaseAverage2 = purchaseAverage.map("${:,.2f}".format)
purchaseAverage2.head()
totalAmount = purchaseTotal1/groupedGenderData_df["Purchase ID"].count()
totalPurchaseID = totalAmount.map("${:,.2f}".format)
totalPurchaseID.head()
genderPurchaseInfo2_df = pd.DataFrame(groupedGenderData_df["Purchase ID"].count())
genderPurchaseInfo2_df["Average Purchase Price"] = purchaseAverage2  
genderPurchaseInfo2_df["Total Purchase Value"] = purchaseTotal2 
genderPurchaseInfo2_df["Normal Total"] = totalPurchaseID 
genderPurchaseInfo2_df

sumGenderData_df = genderPurchaseInfo2_df.rename(columns={"Purchase ID":"Purchase Count"})
sumGenderData_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[82]:


# In this segment, we need to create bins to mactch the vlaue data of transactions. Age bins in this case.
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
groupAgeData = purchaseData_df
groupAgeData["Age Summary"] = pd.cut(groupAgeData["Age"], age_bins, labels=group_names)
groupAgeData
groupAgeData = groupAgeData.groupby("Age Summary")
groupAgeData.count()
summaryAgedf = pd.DataFrame(groupAgeData.count())
summaryAgedf 
summaryAgedf["Purchase ID"] = (summaryAgedf["Purchase ID"]/playerAmount)*100
summaryAgedf 
summaryAgedf["Purchase ID"] = summaryAgedf["Purchase ID"].map("{:,.2f}%".format)
summaryAgedf

#  limit columns as well as rename columns using the rename function.
sumAge1df = summaryAgedf[["Purchase ID","SN"]]
sumAge1df
groupSumAgedf = sumAge1df.rename(columns={"Purchase ID":"Percentage of Players", "SN":"Total Count"})
groupSumAgedf


# ## Purchasing Analysis (Age)

# * Bin the purchaseData data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[86]:


# Here we want to get the average age and purchase content. Using mean and count functions to execute some of the results.
dataByAgedf = pd.DataFrame(grp_by_age_purchaseData_df["Purchase ID"].count())
dataByAgedf
valuebyAgeTotal = grp_by_age_purchaseData_df["Price"].sum()
valuebyAgeTotal
valuebyAgeTotalAmount = valuebyAgeTotal.map("${:,.2f}".format)
valuebyAgeTotalAmount


averagePricebyAge = grp_by_age_purchaseData_df["Price"].mean()
averagePricebyAge
dlr_averagePricebyAge = averagePricebyAge.map("${:,.2f}".format)
dlr_averagePricebyAge

normalized_totals_age = valuebyAgeTotal/grp_by_age_purchaseData_df["Purchase ID"].count()
dlr_normalized_totals_age = normalized_totals_age.map("${:,.2f}".format)
dlr_normalized_totals_age
dataByAgedf["Average Purchase Price"] = dlr_averagePricebyAge  
dataByAgedf["Total Purchase Value"] = valuebyAgeTotalAmount 
dataByAgedf["Normalized Totals"] = dlr_normalized_totals_age 
dataByAgedf
sumAgePurchaseDataVar = dataByAgedf.rename(columns={"Purchase ID":"Purchase Count"})
sumAgePurchaseDataVar


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[87]:


firstPurchaseInfo_df = pd.DataFrame(purchaseData)
firstPurchaseInfo_df.head()

groupHighestSpender_df = firstPurchaseInfo_df.groupby("SN")
groupHighestSpender_df.count()

purchaseID_df = pd.DataFrame(groupHighestSpender_df["Purchase ID"].count())
purchaseID_df

priceTotalValue = groupHighestSpender_df["Price"].sum()
priceTotalValue

averagePurchaseofSN = groupHighestSpender_df["Price"].mean()
averagePurchaseofSN
averageSNPurchase2 = averagePurchaseofSN.map("${:,.2f}".format)
averageSNPurchase2
purchaseID_df["Average Purchase Price"] = averageSNPurchase2
purchaseID_df["Total Purchase Value"] = priceTotalValue 
purchaseID_df

sumCountID = purchaseID_df.rename(columns={"Purchase ID":"Purchase Count"})
top5ID_df=sumCountID.sort_values("Total Purchase Value", ascending=False)
top5ID_df.head()
priceTotalValue2 = priceTotalValue.map("${:,.2f}".format)
top5ID_df["Total Purchase Value"] = priceTotalValue2
top5ID_df.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[97]:


# Here we need to group the data by item ID and item Name. We will also find the sum of the price for the analysis.

groupTopItems = orig_purchaseData_df.groupby(["Item ID", "Item Name"])
groupTopItems.count()

databyItems = pd.DataFrame(groupTopItems["Purchase ID"].count())
databyItems

totalvalueofItems = groupTopItems["Price"].sum()
totalvalueofItems
totalvalueofItems2 = totalvalueofItems.map("${:,.2f}".format)
totalvalueofItems2

purchaseVariableofItems = groupTopItems["Price"].mean()
purchaseVariableofItems
ItemsPurchased32 = purchaseVariableofItems.map("${:,.2f}".format)
ItemsPurchased32

databyItems["Item Price"] = ItemsPurchased32
databyItems["Total Purchase Value"] = totalvalueofItems2
databyItems

# Display the sum of the top five items using a head function.
sumofItemsPurchased = databyItems.rename(columns={"Purchase ID":"Purchase Count"})
top5Items=sumofItemsPurchased.sort_values("Purchase Count", ascending=False)
top5Items.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[106]:


# Here we need to total the top most profitable items by using the group variables and sum of each item.
# We use the {:} to set it to all of the data to read. At the end we find the best valued item adding all of the variables.
itemTotalValue3 = top5Items.sort_values("Total Purchase Value", ascending = False)
itemTotalValue3["Purchase Count"] = itemTotalValue3["Purchase Count"].map("{:}".format)
itemTotalValue3["Item Price"] = itemTotalValue3["Item Price"].map("${:}".format)
itemTotalValue3["Total Purchase Value"] = itemTotalValue3["Total Purchase Value"].map("${:}".format)
bestValueItem = itemTotalValue3.loc[:,["Purchase Count", "Item Price", "Total Purchase Value"]]

# In the end, jsut display the dataframe with a header.
bestValueItem.head(5)


# In[ ]:





# In[ ]:





# In[ ]:





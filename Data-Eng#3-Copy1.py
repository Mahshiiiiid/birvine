#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

# Read the test data using pandas
test_data = pd.read_csv('/Users/mahshid/Desktop/test_data.csv')

# Example assertions
assert test_data['Crash ID'].isnull().sum() == 0, "column1 contains null values"
assert test_data['Record Type'].dtype == 'int64', "column2 should be of integer data type"
assert test_data['Vehicle ID'].min() >= 0, "column3 should contain only positive values"

print("Number of unique Participant ID values:", test_data['Participant ID'].nunique())
print("Total number of rows:", len(test_data))





# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Examine the dataset's structure
print("Head of the dataset:")
print(test_data.head())

print("\nTail of the dataset:")
print(test_data.tail())

print("\nRandom sample of the dataset:")
print(test_data.sample(5))

# Step 2: Summary statistics
print("\nSummary statistics:")
print(test_data.describe())

# Step 3: Check for duplicates
print("\nNumber of duplicate rows:")
print(test_data.duplicated().sum())

# Step 4: Check for missing values
print("\nNumber of missing values:")
print(test_data.isnull().sum())

# Step 5: Visualize the data
# Histogram for a numeric column
plt.hist(test_data['Vehicle ID'], bins=30)
plt.title('Histogram of Vehicle ID')
plt.xlabel('Vehicle ID')
plt.ylabel('Frequency')
plt.show()

# Step 6: Investigate relationships between variables
print("\nCorrelation matrix:")
print(test_data.corr())

# Step 7: Check for inconsistencies
print("\nValue counts for 'Record Type' column:")
print(test_data['Record Type'].value_counts())



# In[9]:


import pandas as pd

# Read the test data using pandas
test_data = pd.read_csv('/Users/mahshid/Desktop/test_data.csv')

# Step 1: Handle missing values (fill missing values with the mean, for example)
test_data.fillna(test_data.mean(), inplace=True)

# Step 2: Convert data types (convert float columns to integers if needed)
test_data['Vehicle ID'] = test_data['Vehicle ID'].astype('int64')

# Step 3: Remove duplicates
test_data.drop_duplicates(inplace=True)

# Step 4: Rename columns (example: renaming 'Participant Vehicle Seq#' to 'Participant_Vehicle_Sequence')
test_data.rename(columns={'Participant Vehicle Seq#': 'Participant_Vehicle_Sequence'}, inplace=True)

# Step 5: Create new columns (example: create a 'Year' column from a 'Crash Date' column)
# test_data['Year'] = pd.to_datetime(test_data['Crash Date']).dt.year

# Display the cleaned dataset
print(test_data.head())


# In[15]:


# List of columns you want to display
columns_to_display = ['Crash ID', 'Record Type', 'Vehicle ID', 'Participant ID', 'Participant Display Seq#']

print(test_data[columns_to_display].head(200))


# In[18]:


# Load the data
data = pd.read_csv('/Users/mahshid/Desktop/test_data.csv')
assert data['Crash ID'].isnull().sum() == 0, "Crash ID column contains null values"
assert data['Record Type'].isnull().sum() == 0, "Record Type column contains null values"
assert data['Vehicle ID'].isnull().sum() == 0, "Vehicle ID column contains null values"
assert data['Participant ID'].isnull().sum() == 0, "Participant ID column contains null values"



# In[20]:


import pandas as pd

# Load the data
data = pd.read_csv('/Users/mahshid/Desktop/test_data.csv')

# Remove rows with missing values in the 'Vehicle ID' column
data = data.dropna(subset=['Vehicle ID'])

# Example assertions

# Check for null values in the 'Crash ID' column
assert data['Crash ID'].isnull().sum() == 0, "Crash ID column contains null values"

# Check for null values in the 'Record Type' column
assert data['Record Type'].isnull().sum() == 0, "Record Type column contains null values"

# Check for null values in the 'Vehicle ID' column
assert data['Vehicle ID'].isnull().sum() == 0, "Vehicle ID column contains {} null values".format(data['Vehicle ID'].isnull().sum())

# Check for null values in the 'Participant ID' column
assert data['Participant ID'].isnull().sum() == 0, "Participant ID column contains null values"

# Add more assertions based on your specific data conditions



# In[23]:


import pandas as pd

# Load the data
data = pd.read_csv('/Users/mahshid/Desktop/test_data.csv')

# Remove rows with missing values in the 'Participant ID' column
data = data.dropna(subset=['Participant ID'])

# Example assertions

# Check for null values in the 'Crash ID' column
assert data['Crash ID'].isnull().sum() == 0, "Crash ID column contains null values"

# Check for null values in the 'Record Type' column
assert data['Record Type'].isnull().sum() == 0, "Record Type column contains null values"

# Check for null values in the 'Vehicle ID' column
assert data['Vehicle ID'].isnull().sum() == 0, "Vehicle ID column contains {} null values".format(data['Vehicle ID'].isnull().sum())

# Check for null values in the 'Participant ID' column
assert data['Participant ID'].isnull().sum() == 0, "Participant ID column contains null values"

# Add more assertions based on your specific data conditions


# In[1]:


import pandas as pd

# Load the data
data = pd.read_csv('/Users/mahshid/Desktop/test_data.csv')

# Remove rows with invalid Crash Hour Codes
data = data[(data['Crash Hour'] >= 0) & (data['Crash Hour'] <= 23)]

# Check that all Crash Hour Codes are within the range of 0 to 23
assert data['Crash Hour'].between(0, 23).all(), "Not all Crash Hour Codes are within the range of 0 to 23"

# Check that the total number of crashes is greater than zero
assert len(data) > 0, "The total number of crashes is not greater than zero"






# In[8]:


import numpy as np

# Calculate the crash count for each month
month_counts = data['Crash Month'].value_counts()

# Calculate the mean and standard deviation of the crash count across months
mean_monthly_crashes = np.mean(month_counts)
std_monthly_crashes = np.std(month_counts)




coef_of_variation = std_monthly_crashes / mean_monthly_crashes

if coef_of_variation < 0.1:
    print("Crashes are evenly/uniformly distributed throughout the months of the year")
else:
    print("Crashes are not evenly/uniformly distributed throughout the months of the year")






# In[ ]:





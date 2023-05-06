#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


file_path = '/Users/mahshid/Downloads/bc_trip259172515_230215.csv'
data = pd.read_csv(file_path)


# In[4]:


data.head()


# In[5]:


filtered_data = data.drop(columns=['EVENT_NO_STOP', 'GPS_SATELLITES', 'GPS_HDOP'])


# In[6]:


filtered_data.head()


# In[7]:


# Read the CSV file again and get the list of column names
data = pd.read_csv(file_path, nrows=0)
column_names = data.columns.tolist()

# Remove the columns to be filtered out
columns_to_filter = ['EVENT_NO_STOP', 'GPS_SATELLITES', 'GPS_HDOP']
filtered_columns = [col for col in column_names if col not in columns_to_filter]


# In[8]:


filtered_data_usecols = pd.read_csv(file_path, usecols=filtered_columns)


# In[9]:


filtered_data_usecols.head()


# In[10]:


#Decoding
import pandas as pd
from datetime import datetime, timedelta

# Read the CSV file and filter the columns (use the correct file path)
file_path = '/Users/mahshid/Downloads/bc_trip259172515_230215.csv'
data = pd.read_csv(file_path)
filtered_data = data.drop(columns=['EVENT_NO_STOP', 'GPS_SATELLITES', 'GPS_HDOP'])

def decode_timestamp(row):
    opd_date = datetime.strptime(row['OPD_DATE'], '%d%b%Y:%H:%M:%S')  # Adjusted date format
    act_time = timedelta(seconds=row['ACT_TIME'])
    return opd_date + act_time






# In[11]:


filtered_data['TIMESTAMP'] = filtered_data.apply(decode_timestamp, axis=1)
filtered_data.head()



# In[12]:


print(filtered_data.columns)



# In[13]:


filtered_data = filtered_data.drop(columns=['OPD_DATE', 'ACT_TIME'])







# In[14]:


print(filtered_data.columns)


# In[15]:


filtered_data.head()


# In[16]:


filtered_data.head(10)


# In[17]:


# Step 1: Calculate the difference in METERS and TIMESTAMP
filtered_data['dMETERS'] = filtered_data['METERS'].diff()
filtered_data['dTIMESTAMP'] = filtered_data['TIMESTAMP'].diff().dt.total_seconds()

# Step 2: Create the SPEED column
filtered_data['SPEED'] = filtered_data.apply(lambda row: row['dMETERS'] / row['dTIMESTAMP'] if row['dTIMESTAMP'] > 0 else 0, axis=1)

# Step 3: Drop the unnecessary dMETERS and dTIMESTAMP columns
filtered_data = filtered_data.drop(columns=['dMETERS', 'dTIMESTAMP'])


# In[18]:


filtered_data.head(10)


# In[19]:


speed_stats = filtered_data['SPEED'].describe()
min_speed = speed_stats['min']
max_speed = speed_stats['max']
mean_speed = speed_stats['mean']

print(f"Minimum Speed: {min_speed} meters/second")
print(f"Maximum Speed: {max_speed} meters/second")
print(f"Average Speed: {mean_speed} meters/second")



# In[25]:


import pandas as pd
from datetime import datetime, timedelta

# Load the data
data = pd.read_csv('/Users/mahshid/Downloads/bc_veh4223_230215.csv')

# Define a function to decode the ACT_TIME column
def decode_act_time(act_time):
    reference_time = datetime(1970, 1, 1)
    decoded_time = reference_time + timedelta(seconds=act_time)
    return decoded_time

# Define a function to process a single trip
def process_trip(trip_data):
    # Step B: Filter the columns
    filtered_data = trip_data[['EVENT_NO_TRIP', 'VEHICLE_ID', 'METERS', 'GPS_LONGITUDE', 'GPS_LATITUDE', 'ACT_TIME']]
    
    # Step C: Decode the ACT_TIME column
    filtered_data['ACT_TIME'] = filtered_data['ACT_TIME'].apply(decode_act_time)
    
    # Step D: Calculate the distance between GPS points
    filtered_data['DISTANCE'] = filtered_data['METERS'].diff().fillna(0)
    
    # Step E: Calculate the time difference between GPS points
    filtered_data['TIME_DIFF'] = filtered_data['ACT_TIME'].diff().fillna(pd.Timedelta(seconds=0))
    
    return filtered_data

# Process the data
unique_trips = data['EVENT_NO_TRIP'].unique()
transformed_data = pd.DataFrame()

for trip in unique_trips:
    trip_data = data[data['EVENT_NO_TRIP'] == trip]
    transformed_trip_data = process_trip(trip_data)
    transformed_data = transformed_data.append(transformed_trip_data, ignore_index=True)

# Display the transformed data
pd.set_option('display.expand_frame_repr', False)
print(transformed_data)




    








# In[ ]:





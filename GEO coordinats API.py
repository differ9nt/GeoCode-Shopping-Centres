#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import time

API_KEY = 'add_your_key'


def get_coordinates(address):
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        'q': address,
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            location = data['results'][0]['geometry']
            return location['lat'], location['lng']  # latitude, longitude
    else:
        print(f"Error: {response.status_code} for address {address}")
    
    return None, None  


df = pd.read_csv('Shopping centres (population, competitors).csv')


coordinates = []
for address in df['Street']:
    lat, lon = get_coordinates(address)
    coordinates.append((lat, lon))
    time.sleep(1)  


df['latitude'] = [coord[0] for coord in coordinates]
df['longitude'] = [coord[1] for coord in coordinates]


df.to_csv('output_file.csv', index=False)

print("data saved")


# In[ ]:





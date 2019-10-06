# -*- coding: utf-8 -*-
"""
PROJECT: NYC Citibike Rides

Created on Mon Sep 23

@author: Michael ODonnell
"""

# import libraries
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.parser import parse
import matplotlib.pyplot as plt


# IMPORT DATA
citibike_rides_sep19 = pd.read_csv("201908-citibike-tripdata.csv")
citibike_rides_sep19 = citibike_rides_sep19[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_aug19 = pd.read_csv("201907-citibike-tripdata.csv")
citibike_rides_aug19 = citibike_rides_aug19[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_jul19 = pd.read_csv("201906-citibike-tripdata.csv")
citibike_rides_jul19 = citibike_rides_jul19[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_jun19 = pd.read_csv("201905-citibike-tripdata.csv")
citibike_rides_jun19 = citibike_rides_jun19[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_may19 = pd.read_csv("201904-citibike-tripdata.csv")
citibike_rides_may19 = citibike_rides_may19[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_apr19 = pd.read_csv("201903-citibike-tripdata.csv")
citibike_rides_apr19 = citibike_rides_apr19[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_mar19 = pd.read_csv("201902-citibike-tripdata.csv")
citibike_rides_mar19 = citibike_rides_mar19[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_feb19 = pd.read_csv("201901-citibike-tripdata.csv")
citibike_rides_feb19 = citibike_rides_feb19[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_jan19 = pd.read_csv("201812-citibike-tripdata.csv")
citibike_rides_jan19 = citibike_rides_jan19[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_dec18 = pd.read_csv("201811-citibike-tripdata.csv")
citibike_rides_dec18 = citibike_rides_dec18[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_nov18 = pd.read_csv("201810-citibike-tripdata.csv")
citibike_rides_nov18 = citibike_rides_nov18[['starttime','tripduration', 'start station name', 'end station name']]

citibike_rides_oct18 = pd.read_csv("201809-citibike-tripdata.csv")
citibike_rides_oct18 = citibike_rides_oct18[['starttime','tripduration', 'start station name', 'end station name']]

### concat all dataframes into one dataframe
frames = [citibike_rides_sep19, citibike_rides_aug19, citibike_rides_jul19,
          citibike_rides_jun19, citibike_rides_may19, citibike_rides_apr19,
          citibike_rides_mar19, citibike_rides_feb19, citibike_rides_jan19,
          citibike_rides_dec18, citibike_rides_nov18, citibike_rides_oct18]
citibike_rides = pd.concat(frames)


# fix data type of each column
citibike_rides["starttime"] = pd.to_datetime(citibike_rides["starttime"])
#citibike_rides["start station name"] = citibike_rides["start station name"].astype(str)
#citibike_rides["end station name"] = citibike_rides["end station name"].astype(str)
print(citibike_rides.dtypes)

# rename two columns
#citibike_rides = citibike_rides.rename(columns={"start station name": "start_station_name", "end station name": "end_station_name"})

# filter out rides > 45 minutes
citibike_rides = citibike_rides[(citibike_rides.tripduration <= 2700)]

# number of citibike stations
#print("number of citibike stations:", len(citibike_rides['start_station_name'].unique()))

# list of stations to calculate duration
stations = ["E 84 St & 1 Ave",
"W 41 St & 8 Ave",
"Broadway & W 60 St",
"E 17 St & Broadway",
"Fulton St & William St",
"N 6 St & Bedford Ave",
"E 7 St & Avenue A",
"W 87 St & Amsterdam Ave",
"9 Ave & W 28 St",
"W 4 St & 7 Ave S",
"Jay St & York St",
"Norfolk St & Broome St"]

# print mean duration of trips between stations
"""
for i in stations:
    for j in stations:
        print(i, "to", j, (citibike_rides[(citibike_rides.start_station_name == i) & (citibike_rides.end_station_name == j)]).tripduration.mean())
"""

# CITIBIKE FREQUENCY
print("number of total rides:", len(citibike_rides))
print("Duration of dataframe:", (citibike_rides['starttime'].max() - citibike_rides['starttime'].min()))
print("number of rides/day:", len(citibike_rides)/365)

### citibike rides by day of the week
print("citibike rides by day of the week (Sunday = 0)")
print(citibike_rides["starttime"].groupby(citibike_rides["starttime"].dt.month).count())

### most popular month for citibike
citibike_rides["starttime"].groupby(citibike_rides["starttime"].dt.month).count().plot(kind="barh",figsize = (7,4))
"""
# CITIBIKE RIDE DURATION
print("mean ride duration:", citibike_rides["tripduration"].mean())
print("median ride duration:", citibike_rides["tripduration"].median())

#citibike_rides[citibike_rides.tripduration <= 2700].plot(kind = "box")

#print("number of rides > 45min:", len(citibike_rides["tripduration"]>2700 == True))

### citibike rides by time of day
#print(citibike_rides["starttime"].groupby(citibike_rides["starttime"].dt.hour).count().plot(kind="bar",figsize = (8,5)))

print("Most common pickup docks:", citibike_rides["start station name"].value_counts())

day_df = citibike_rides["starttime"].groupby(citibike_rides["starttime"].dt.date).count()
"""

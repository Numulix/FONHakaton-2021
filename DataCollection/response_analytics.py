import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import minimize
import geopy.distance
from math import radians, cos, sin, asin, sqrt
import pickle
import json

N_CITIES = 17


def preprocess_distances(cities, available_res, path='distances.pkl'):
    # Between cities
    n = len(cities)
    k = len(available_res)
    dist = np.zeros((n,k))
    for i in range(n):
        for j in range(k):
            dist[i,j] = geopy.distance.distance(cities.iloc[i][['lat','lng']].values, 
                                                available_res.iloc[j][['lat','lng']].values).km
    with open(path, 'wb') as out:
        pickle.dump(dist, out, pickle.HIGHEST_PROTOCOL)
    
def load_distances(path='distances.pkl'):
    with open('distances.pkl', 'rb') as inp:
        return pickle.load(inp)
        

def get_earthquake_data():
    earthquakes = [
        {'epicenter':(44.117512, 20.189369), 'magnitude': 6},
        {'epicenter':(43.886935, 20.556935), 'magnitude': 7},
        {'epicenter':(43.654546, 20.838094), 'magnitude': 7}
    ]
    return earthquakes

def get_cities():
    return pd.read_csv('serbia_cities.csv')[['city', 'population', 'lat', 'lng']].iloc[0:N_CITIES]

def estimate_endangered(cities, earthquakes):
    for cities in cities:
        for eq in earthquakes:


def get_response_data():
    earthquakes = get_earthquake_data()
    cities_df = get_cities()
    endangered = estimate_endangered(cities, earthquakes)
    goal = endangered /10



    return {
        'earthquakes': earthquakes_json,
        'available_resources': resources_json,
        'endangered': endangered_json,
        'distribution': distribution_json
    }
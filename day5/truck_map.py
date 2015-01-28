#!/usr/bin/env python
''' Map food trucks by neighborhood in San Francisco.
'''

import json
import folium
import pandas as pd
import shapely.geometry as geom

def main():
    ''' Produce a map of neighborhood food trucks in San Francisco.
    '''
    # Load the neighborhoods GeoJSON data, and extract the neighborhood names
    # and shapes.
    nhoods = load_geo_json('sf_nhoods.json')
    features = extract_features(nhoods)

    # Load the food truck data, and extract (longitude, latitude) pairs.
    trucks = pd.read_csv('mobile_food.csv')
    loc = trucks[['Longitude', 'Latitude']].dropna()

    # Determine the neighborhood each food truck is in.
    trucks['Neighborhood'] = loc.apply(get_nhood, axis=1, features=features)

    counts = trucks['Neighborhood'].value_counts()
    counts = counts.reset_index()
    counts.columns = pd.Index(['Neighborhood', 'Trucks'])

    # Create a map.
    my_map = folium.Map(location=[37.77, -122.45], zoom_start=12)

    my_map.geo_json(geo_path = 'sf_nhoods.json',
                    key_on='feature.properties.name',
                    data = counts, columns = ['Neighborhood', 'Trucks'],
                    fill_color='BuGn')

    my_map.create_map('map.html')

def get_nhood(truck, features):
    ''' Identify the neighborhood of a given point.
    '''
    truck = geom.Point(*truck)
    for name, boundary in features:
        if truck.within(boundary):
            return name

    return None

def load_geo_json(path):
    ''' Load a GeoJSON file.
    '''
    with open(path) as file:
        geo_json = json.load(file)

    return geo_json

def extract_features(geo_json):
    ''' Extract names and geometries from a geo_json dict.
    '''
    features = []
    for feature in geo_json['features']:
        name = feature['properties']['name']
        geometry = geom.asShape(feature['geometry'])

        features.append((name, geometry))

    return features

if __name__ == '__main__':
    main()


'''
Script to download some interesting data from Github.com 

Thu Dec 18 17:13:16 PST 2014

There are about 25k repositories that match the query 'data science'.
We'll look at the most popular ones.
'''

import json
import requests


def query_github(params):
    '''
    Query Github using dict of params
    '''
    base = 'https://api.github.com/search/repositories'
    response = requests.get(base, params=params)
    return response.json()


if __name__ == '__main__':

    payload = {'q': 'data science', 'sort': 'stars'}
    ds = query_github(payload)

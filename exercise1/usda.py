'''
A simple client for USDA statistics
    http://quickstats.nass.usda.gov/api

Found the data set in the data.gov catalog:
    http://catalog.data.gov/dataset/quick-stats-agricultural-database-api

Fun fact: This actually queries a database with 31 million records
'''

import requests


# One could also remove these lines and manually set the key via:
# usda_key = <your key here>
with open('usda_key.txt') as f:
    usda_key = f.read().rstrip()


def get_param_values(param, key=usda_key):
    '''
    Returns the possible values for a single parameter 'param'

    >>> get_param_values('sector_desc')[:3]
    ['ANIMALS & PRODUCTS', 'CROPS', 'DEMOGRAPHICS']

    '''
    url = 'http://quickstats.nass.usda.gov/api/get_param_values'
    parameters = {'param': param, 'key': key}
    response = requests.get(url=url, params=parameters)
    return response.json()[param]


def query(parameters, key=usda_key):
    '''
    Returns the JSON response from the USDA agricultural database

    'parameters' is a dictionary of parameters that can be referenced here:
        http://quickstats.nass.usda.gov/api

    Example: Return all the records around cattle in Tehama County

    >>> cowparams = {'commodity_desc': 'CATTLE',
                     'state_name': 'CALIFORNIA',
                     'county_name': 'TEHAMA'}
    >>> tehamacow = query(cowparams)

    '''
    url = 'http://quickstats.nass.usda.gov/api/api_GET'
    parameters['key'] = key
    response = requests.get(url=url, params=parameters)
    try:
        return response.json()['data']
    except KeyError:
        return response.json()


if __name__ == '__main__':

    import operator
    # A few examples of usage

    # Possible values for 'commodity_desc'
    # commodity_desc = get_param_values('commodity_desc')
    # Expect:
    # ['AG LAND', 'AG SERVICES', 'AG SERVICES & RENT',
    # 'ALMONDS', ...

    # Value of rice crops in Yolo (Davis) county since 2005
    riceparams = {'sector_desc': 'CROPS',
                  'commodity_desc': 'RICE',
                  'state_name': 'CALIFORNIA',
                  'county_name': 'YOLO',
                  'year__GE': '2005',
                  'unit_desc': '$',
                  }

    # yolorice = query(riceparams)

    # Try using a dictionary comprehension to filter
    # yearvalue = {x['year']: x['Value'] for x in yolorice}
    # Expect:
    # {'2007': '26,697,000', '2012': '51,148,000'}

    # This was the sales, not the production
    tobacco = query({'commodity_desc': 'TOBACCO',
                     'sector_desc': 'CROPS',
                     'source_desc': 'CENSUS',
                     'domain_desc': 'TOTAL',
                     'agg_level_desc': 'STATE',
                     'year': '2012',
                     'freq_desc': 'ANNUAL',
                     'unit_desc': '$',
                     })

    # Rylan's query, which does production
    tprod = query({'sector_desc': 'CROPS',
                   'commodity_desc': 'TOBACCO',
                   'year': '2012',
                   'agg_level_desc': 'STATE',
                   'statisticcat_desc': 'PRODUCTION',
                   'short_desc': 'TOBACCO - PRODUCTION, MEASURED IN $'
                   })

    def cleanup(value):
        '''
        Massage data into proper form
        '''
        try:
            return int(value.replace(',', ''))

        # Some contain strings with '(D)'
        except ValueError:
            return 0

    t2 = [(cleanup(x['Value']), x['state_name']) for x in tobacco]
    t2.sort(key=operator.itemgetter(0), reverse=True)

    tprod2 = [(cleanup(x['Value']), x['state_name']) for x in tprod]
    tprod2.sort(key=operator.itemgetter(0), reverse=True)

    print(t2)

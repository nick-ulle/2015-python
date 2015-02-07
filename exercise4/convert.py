#!/usr/bin/env python3
''' Utility to convert the supermarket data to a SQLite database.

The directory structure should be
    
    convert.py
    tables/
        +-- supermarket_distances
        +-- supermarket_prices
        +-- supermarket_purchases

This script can then be executed using

    python3 convert.py

in the same directory.
'''

import os

import pandas as pd
import sqlalchemy as sa

def main():
    ''' Convert the supermarket data to a SQLite database.
    '''
    file_dir = 'tables'
    files = os.listdir(file_dir)

    engine = sa.create_engine('sqlite:///supermarket.sqlite')

    for f in files:
        print('Writing table {}...'.format(f), end='', flush=True)

        # Read the data in 500,000-row chunks.
        data_chunker = pd.read_table(os.path.join(file_dir, f), sep=' ',
                                     chunksize=5e5)
        data_chunks = iter(data_chunker)

        # Write the first chunk to the database; append the remaining chunks.
        # Use 1000-row commits.
        next(data_chunks).to_sql(f, engine, index=False, chunksize=1000)
        for chunk in data_chunks:
            chunk.to_sql(f, engine, if_exists='append', index=False,
                         chunksize=1000)
        
        print('done!')

if __name__ == '__main__':
    main()


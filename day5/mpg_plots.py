#!/usr/bin/env python
''' Plots for EPA fuel economy data.
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    ''' Run a demo of the functions in this module.
    '''
    vehicles = pd.read_csv('vehicles.csv')

    make_mpg_plot(vehicles)

def make_mpg_plot(vehicles):
    ''' Make a plot of MPG by Make and Year.
    '''
    # Take means by make and year.
    groups = vehicles.groupby(['year', 'make'])
    avg_mpg = groups.city_mpg.mean()

    # Convert the indexes to columns, then pivot.
    avg_mpg = avg_mpg.reset_index()
    mpg_matrix = avg_mpg.pivot('year', 'make', 'city_mpg')

    # Subset down to a few brands.
    brands = ['Honda', 'Toyota', 'Hyundai', 'BMW', 'Mercedes-Benz',
              'Ferrari', 'Lamborghini', 'Maserati', 'Fiat', 'Bentley',
              'Ford', 'Chevrolet', 'Dodge', 'Jeep']
    brand_matrix = mpg_matrix[brands]

    # Plot the data using seaborn and matplotlib.
    # The `subplots()` method returns a figure and an axes.
    fig, ax = plt.subplots(1, 1)
    sns.heatmap(brand_matrix, cmap='BuGn', ax=ax)
    ax.set_xlabel('Make')
    ax.set_ylabel('Year')
    ax.set_title('MPG by Make and Year')

    # Setting a tight layout ensures the entire plot fits in the plotting
    # window.
    fig.tight_layout()

    # Show the figure.
    fig.show()
    # Alternatively:
    # fig.savefig('mpg_plot.png')

# Only call `main()` when the script is executed directly (not when it's
# imported with `import mpg_plots`). This allows the script to be used as an
# application AND as a module in other scripts.
if __name__ == '__main__':
    main()


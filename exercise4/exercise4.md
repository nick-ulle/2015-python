
# Exercise 4 - Supermarket Data Analysis

In this exercise, you'll use Python to analyze data from the Italian
supermarket chain [Coop][].

The goals for this exercise are:

* Experience working with a large data set in Python
* Examine when SQL databases are appropriate
* Use `pandas` and `SQLAlchemy`

This exercise is deliberately challenging and open-ended so that you can
experiment with all of the tools you've learned.

## Data

Download the data [here][data].

The data records the supermarket purchases of 60,366 customers between January
2007 and December 2011. More details, and a description of the data, can be
found [here][desc]. This data was generously provided by the paper

> Pennacchioli, D., Coscia, M., Rinzivillo, S., Pedreschi, D. and Giannotti, F.
> (2013), "[Explaining the Product Range Effect in Purchase Data][paper]," Big
> Data 2013 Conference.

The data is distributed as three space-delimited text files, in a zip archive.
After extracting the files, you're encouraged to convert these files into a
SQLite database.

You can do this using the provided script, `convert.py`. The header of the
script includes instructions for use. It may take up to 30 minutes, and
requires 1 GB of disk space.

[Coop]: https://en.wikipedia.org/wiki/Coop_%28Italy%29
[data]: http://michelecoscia.com/wp-content/uploads/2013/02/supermarket_data.zip
[desc]: http://www.michelecoscia.com/?page_id=379
[paper]: http://www.michelecoscia.com/wp-content/uploads/2013/09/geocoop.pdf

## Tasks

Determine which customer spent the most, and which customer bought the most
items. How much did they spend, in USD? Note that the prices are given in
Euros (as a bonus, use `requests` to fetch the current exchange rate).

Compute the total spending for each customer, and make a histogram. Does a
gamma distribution fit well? If not, try to find a distribution that does.
Keep in mind that total spending is theoretically unbounded.

Analyze the network of customers and stores within short walking distance (say,
less than 2500 meters). Are there any isolated customers or stores? Do spending
habits differ for customers with few stores in walking distance? It may be
helpful to use `networkx` here.


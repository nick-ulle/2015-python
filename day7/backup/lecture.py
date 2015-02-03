
# # Data Storage
#
# What are some ways to store data?
#
# * CSV / delimited
# * JSON
# * XML
# * databases
#     - relational (SQL) database
#     - NoSQL database
# * HDF5
#
# Why are there so many formats?
#
# Each format has certain benefits and drawbacks. CSV, JSON, and XML are all
# human-readable! HDF5 files are not human-readable, but they can be loaded
# quickly and use minimal disk space.
#
# Databases differ from the other formats, because they support safe,
# simultaneous access by many users. Databases can be queried, as well, to
# extract specific subsets of the data.
#
# Relational databases store data as a collection of tables, which are very
# much like DataFrames (each column has a type). These are sometimes called SQL
# databases, because most relation databases can be queried using Structured
# Query Language (SQL). Examples:
#
# * SQLite
# * MariaDB (formerly MySQL)
# * MS SQL Server
# * Oracle
#
# NoSQL databases store data in other (possibly heterogeneous) formats, and
# abandon some of the safety checks in favor of pure speed. This is what Google
# and Facebook run on. Examples:
#
# * MongoDB
# * Cassandra
#
# Yes, you can access almost all of these from Python!
#
# ## Relational Databases
#
# Pandas makes it easy to access tables in a SQL database through the function
# `read_sql()`.

import pandas as pd

# Looking at the help file for this function, it has parameters for a SQL query
# string and a 'SQLAlchemy engine'.
#
# SQLAlchemy is a unified interface to SQL databases. For the moment, we're
# only going to use it to connect to the database. An *engine* is a wrapper
# around the database, that knows how to communicate with it.

import sqlalchemy as sa

engine = sa.create_engine('sqlite:///aa.db')

# The basics of SQL are not too complicated. If we want to select some rows
# from a database, we use a select statement:
#
#     SELECT <columns> FROM <table>
#
# How can we tell what tables are in the database?

engine.table_names()

# Let's select all columns in the 'aa' table.

aa = pd.read_sql('SELECT * FROM aa', engine)

# Can anyone tell what this dataset is?

aa.head()
aa.tail()

# Let's try a more complicated query using `WHERE`.

pd.read_sql('SELECT * FROM aa WHERE year >= 1950 AND year < 1960', engine)

# Who's the oldest person in the table?

pd.read_sql('SELECT * FROM aa ORDER BY age DESC LIMIT 10', engine)

# YOUR TURN:
# 
# * Who's the youngest person in the table?
# * How many Hepburns are in the table?
# * How many Californians have won?
# * Who has the most wins?

# The trick is to take advantage of SQL and Pandas together. Generally, you
# want to use SQL to reduce the data to a manageable size (i.e., so it fits in
# memory) and then use Pandas to investigate the fine details.


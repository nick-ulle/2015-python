
# # American Time Use Survey
#
# The Bureau of Labor Statistics collects economic and demographic information
# about Americans annually, using the 8-month long *Current Population Survey*
# (CPS). At the end of this survey, some respondents are selected for one more
# interview as part of the *American Time Use Survey* (ATUS).
#
# # Using SQLAlchemy
#
# One year (2013) of ATUS results makes for a small, but more realistic
# database.

import sqlalchemy as sa

engine = sa.create_engine('sqlite:///atus.db')

engine.table_names()

# SQLAlchemy shines when it has metadata about the database. Fortunately, it
# can extract metadata automatically.

meta = sa.MetaData(engine, reflect=True)

meta.tables

tables = meta.tables
type(tables)

# It mentions 'dict', so maybe we can treat it like a dict?

tables.keys()

who = tables['who']

who.columns
print(who.columns)

# ATUS includes several tables:
#
# * activity: activity, location, duration, etc...
# * eldercare: elders the respondent cared for
# * respondent: education, earnings, time alone, etc...
# * roster: age, gender, and relationships of each household member
# * summary: summary timings for activity data
# * who: who was present for each activity?
#
# Most of the data is encoded, so we'll focus on one task.
#
# How much did the average American sleep per day, in 2013?
#
# Important variables:
#
# * TULINENO - line number (1 is the respondent)
# * activity:
#     - TUCASEID - id number for case
#     - TRCODE - activity code (010101 is restful sleep)
#     - TUACTDUR24 - activity duration, in minutes
# * roster:
#     - TEAGE - respondent age
#     - TESEX - respondent sex

activity = tables['activity']
print(activity.columns)

# We can use Python instead of SQL code to build up a query, and it will
# automatically be translated to match the SQL dialect used by the database
# we're querying.

from sqlalchemy import select, literal_column, func

sleep_sums_q = select([
    activity.c.TRCODE, 
    func.sum(activity.c.TUACTDUR24).label('SLEEP')
]). \
    where(activity.c.TRCODE == 10101). \
    group_by(activity.c.TUCASEID)

print(sleep_sums_q)

# To query the database, we have to set up a connection.

conn = engine.connect()

# Now we can execute our query; the result is an iterator over rows.

result = conn.execute(sleep_sums_q)

for row in result:
    print('Code: {}, Duration: {} min'.format(*row))

# This can be converted to a DataFrame without much effort.

result = conn.execute(sleep_sums_q)

import pandas as pd

sleep_sums = pd.DataFrame.from_records(row for row in result)

# At this point, we could use Pandas to finish the analysis. Let's use
# SQLAlchemy instead, to see what else it can do.

sleep_avg_q = select([ 
    func.avg(literal_column('SLEEP')).label('AVG_SLEEP')
]).select_from(sleep_sums_q)

print(sleep_avg_q)

result = conn.execute(sleep_avg_q).fetchall()

result = result[0][0]
sleep_avg = result / 60


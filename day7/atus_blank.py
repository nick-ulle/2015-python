
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


# SQLAlchemy shines when it has metadata about the database. Fortunately, it
# can extract metadata automatically.


# It mentions 'dict', so maybe we can treat it like a dict?


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


# We can use Python instead of SQL code to build up a query, and it will
# automatically be translated to match the SQL dialect used by the database
# we're querying.


# To query the database, we have to set up a connection.


# Now we can execute our query; the result is an iterator over rows.


# This can be converted to a DataFrame without much effort.


# At this point, we could use Pandas to finish the analysis. Let's use
# SQLAlchemy instead, to see what else it can do.



ls
import pandas as pd
pd.read_sql?
import sqlalchemy as sa
engine = sa.create_engine('sql
engine = sa.create_engine('sqlite:///aa.db')
engine
engine.table_names()
query = 'SELECT * FROM aa'
aa = pd.read_sql(query, engine)
aa.head()
aa.tail()
query = 'SELECT * FROM aa WHERE person LIKE "%Brando"'
query
pd.read_sql(query, engine)
query = 'SELECT person FROM aa WHERE year >= 1920 AND year < 1930'
query
pd.read_sql(query, engine)
query
engine = sa.create_engine('sqlite:///aa.db')
query = 'SELECT * FROM aa ORDER BY age DESC LIMIT 5'
query
pd.read_sql(query, engine)
q = 'SELECT * FROM aa ORDER BY age ASC LIMIT 5'
query
q
pd.read_sql(q, engine)
q = 'SELECT * FROM aa WHERE person LIKE "%Hepburn"'
q
pd.read_sql(q, engine)
q = 'SELECT * FROM aa WHERE birthplace == "California"'
q
pd.read_sql(q, engine)
q = 'SELECT DISTINCT person f
q = 'SELECT DISTINCT person FROM aa WHERE birthplace == "California"'
q
pd.read_sql(q, engine)
pd.read_sql(q, engine).size
aa
aa.Person.value_counts()
q = 'SELECT COUNT(*) FROM aa GROUP BY person'
q
pd.read_sql(q, engine)
q
q = 'SELECT person, COUNT(*) as Count FROM aa GROUP BY person ORDER BY count DESC LIMIT 5'
q
q
pd.read_sql(q, engine)
%history -f log1.py

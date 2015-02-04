import sqlalchemy as sa
engine = sa.create_engine('sqlite:///atus.db')
engine.table_names()
meta = sa.MetaData(engine, reflect=True)
meta.tables
tables = meta.tables
type(tables)
tables.keys()
engine.table_names()
who = tables['who']
type(who)
who
who.columns
print(who.columns)
act = tables['activity']
print(act.columns)
from sqlalchemy import select, literal_column, func
sums_q = select([func.sum(act.c.TUACTDUR24).label('sleep')]).\
    group_by(act.c.TUCASEID)
print(sums_q)
sums_q = select([func.sum(act.c.TUACTDUR24).label('sleep')]).\
    where(act.c.TRCODE == 10101).\
    group_by(act.c.TUCASEID)
print(sums_q)
conn = engine.connect()
result = conn.execute(sums_q)
for row in result:
    print(row)
import pandas as pd
pd.DataFrame.from_records(row for row in result)
result = conn.execute(sums_q)
pd.DataFrame.from_records(row for row in result)
avg_q = select([func.avg(literal_column('Sleep').label('AVG_Sleep')]).\
               select_from(sums_q)



)
avg_q = select([func.avg(literal_column('Sleep')).label('AVG_Sleep')]).\
               select_from(sums_q)
print(avg_q)
result = conn.execute(avg_q)
result
result = result[0]
result = resultresult = conn.execute(avg_q).fetchall()
result
result = result[0][0]
result
result / 60
%history log2.py
%history -f log2.py

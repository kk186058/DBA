
SELECT
db.ownername AS Base, db.databasename AS Env
, db1.databasename AS Database1
, Coalesce(db2.databasename,'') AS Database2
, Coalesce(db3.databasename,'') AS Database3
, Coalesce(db4.databasename,'') AS Database4
, Coalesce(db5.databasename,'') AS Database5
, Coalesce(db6.databasename,'') AS Database6
, Coalesce(db7.databasename,'') AS Database7
, Coalesce(db8.databasename,'') AS Database8
, Coalesce(db9.databasename,'') AS Database9
, Coalesce(db10.databasename,'') AS Database10
, Coalesce(db11.databasename,'') AS Database11
, Coalesce(db12.databasename,'') AS Database12
, Coalesce(db13.databasename,'') AS Database13
, Coalesce(db14.databasename,'') AS Database14
, Coalesce(db15.databasename,'') AS Database15
, Coalesce(db16.databasename,'') AS Database16
, Coalesce(db17.databasename,'') AS Database17
, Coalesce(db18.databasename,'') AS Database18
, Coalesce(db19.databasename,'') AS Database19
, Coalesce(db20.databasename,'') AS Database20

FROM dbc.dbase db

INNER JOIN dbc.dbase db1 ON db.databasename = db1.ownername
INNER JOIN dbc.dbase db2 ON db1.databasename = db2.ownername
LEFT OUTER JOIN dbc.dbase db3 ON db2.databasename = db3.ownername
LEFT OUTER JOIN dbc.dbase db4 ON db3.databasename = db4.ownername
LEFT OUTER JOIN dbc.dbase db5 ON db4.databasename = db5.ownername
LEFT OUTER JOIN dbc.dbase db6 ON db5.databasename = db6.ownername
LEFT OUTER JOIN dbc.dbase db7 ON db6.databasename = db7.ownername
LEFT OUTER JOIN dbc.dbase db8 ON db7.databasename = db8.ownername
LEFT OUTER JOIN dbc.dbase db9 ON db8.databasename = db9.ownername
LEFT OUTER JOIN dbc.dbase db10 ON db9.databasename = db10.ownername
LEFT OUTER JOIN dbc.dbase db11 ON db10.databasename = db11.ownername
LEFT OUTER JOIN dbc.dbase db12 ON db11.databasename = db12.ownername
LEFT OUTER JOIN dbc.dbase db13 ON db12.databasename = db13.ownername
LEFT OUTER JOIN dbc.dbase db14 ON db13.databasename = db14.ownername
LEFT OUTER JOIN dbc.dbase db15 ON db14.databasename = db15.ownername
LEFT OUTER JOIN dbc.dbase db16 ON db15.databasename = db16.ownername
LEFT OUTER JOIN dbc.dbase db17 ON db16.databasename = db17.ownername
LEFT OUTER JOIN dbc.dbase db18 ON db17.databasename = db18.ownername
LEFT OUTER JOIN dbc.dbase db19 ON db18.databasename = db19.ownername
LEFT OUTER JOIN dbc.dbase db20 ON db19.databasename = db20.ownername


WHERE db.ownername = '${DATABASE}'

ORDER BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22
;

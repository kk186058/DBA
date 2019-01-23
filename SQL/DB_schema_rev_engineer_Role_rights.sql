SEL *
FROM dbc.allrolerights
WHERE databasename NOT LIKE ALL ( 'sys%')
AND databasename <> 'dbc'
;
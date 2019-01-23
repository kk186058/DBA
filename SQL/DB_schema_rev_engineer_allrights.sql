SEL *
FROM dbc.allrights
WHERE username <> databasename
AND username NOT IN ( 'dbc','public', 'viewpoint', 'SysAdmin','TDStats', 'SystemFe', 'TD_SYSXML'    ,'LockLogShredder','SYSLIB'  ,'tdwm'
)
AND databasename NOT LIKE ALL ( 'sys%')
AND databasename <> 'dbc'

;
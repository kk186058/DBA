SEL *
FROM dbc.allrights
WHERE username <> databasename

AND (databasename in ('${scope}') or databasename in ('${users}') or databasename in ('dbc', 'sys_calendar') )
and ( username in ('${scope}') or databasename in ('${users}'))
and databasename <> username

;
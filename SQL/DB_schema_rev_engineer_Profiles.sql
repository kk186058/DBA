SEL *
FROM dbc.profiles
where profilename in
(select profilename from dbc.dbase where databasename in ('${scope}') or databasename in ('${users}'))
;
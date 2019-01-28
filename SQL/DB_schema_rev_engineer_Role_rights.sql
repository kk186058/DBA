SEL *
FROM dbc.allrolerights
WHERE  (databasename in ('${scope}') or databasename in ('${users}') or databasename in ('dbc', 'sys_calendar') )
and rolename in (   SEL rolename
                    FROM dbc.rolemembers
                    where  ( grantee in ('${scope}') or grantee in ('${users}'))
                    )
;
SEL *
FROM dbc.roles
where rolename in (SEL rolename
                    FROM dbc.rolemembers
                    where  ( grantee in ('${scope}') or grantee in ('${users}')))
;
SEL *
FROM dbc.rolemembers
where  ( grantee in ('${scope}') or grantee in ('${users}'))
;
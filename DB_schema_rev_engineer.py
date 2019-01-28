import pandas as pd

# import numpy as np
import pyodbc
# from pandas.io.sql import read_sql
# import sys
import os
# import variables as var

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)

import sys
from time import strftime, localtime

import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)

scanstart = strftime("%Y-%m-%d %H:%M:%S", localtime())
filestart = strftime("%Y%m%d%H%M", localtime())

print("Running python script :" + sys.argv[0] + " on " + scanstart)

db_root = 'dbadmin'
usr_root = 'useradmin'

filename = 'schema' + filestart + '.xlsx'

try:
    os.remove(filename)
except OSError:
    pass


def fun_database_objects(filename, root = 'dbadmin', scope = 'all',users='all'):
    conn = pyodbc.connect('DRIVER={Teradata};DBCNAME=TDVMWARE;UID=dbc;PWD=dbc;QUIETMODE=YES;')

    with open('SQL/' + filename, 'r') as myfile:
        sql = myfile.read().replace('${DATABASE}', root).replace('${scope}', scope).replace('${users}', users)
        # print('sql; : ' + sql)

    Data = pd.read_sql(sql, conn)
    Data = Data.astype('str')

    # Data.columns = ['databasename']
    #
    # data_list = Data.databasename.unique()
    # data_list = [x.upper() for x in data_list]

    return Data

def fun_excel(in_df,in_sheet):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')

    num_objects = len(in_sheet)
    sheet_count = 0

    for d in in_df:

        # Convert the dataframe to an XlsxWriter Excel object.
        d.to_excel(writer, sheet_name=in_sheet[sheet_count], index=False)

        workbook  = writer.book
        worksheet = writer.sheets[in_sheet[sheet_count]]


        for i, col in enumerate(d.columns):
            # find length of column i
            column_len = d[col].astype(str).str.len().max()
            column_name_len = len(d.columns[i])
            if column_name_len > column_len:
                column_len = column_name_len
            # Setting the length if the column header is larger
            # than the max column value length
            column_len = max(column_len, len(col)) + 5
            # set the column length
            worksheet.set_column(i, i, column_len)

        sheet_count = sheet_count +1
    writer.save()
    writer.close()

df_lst = fun_database_objects('DB_schema_rev_engineer_list.sql', db_root)
df_hier = fun_database_objects('DB_schema_rev_engineer_hier.sql')
df_usr = fun_database_objects('DB_schema_rev_engineer_list.sql', usr_root)

db_in_scope = df_lst['DatabaseName'].values
db_in_scope = '\',\''.join(db_in_scope)

db_usr_in_scope = df_usr['DatabaseName'].values
db_usr_in_scope = '\',\''.join(db_usr_in_scope)

df_roles = fun_database_objects('DB_schema_rev_engineer_Roles.sql','na',db_in_scope, db_usr_in_scope)
df_profiles = fun_database_objects('DB_schema_rev_engineer_Profiles.sql','na',db_in_scope, db_usr_in_scope)

df_role_members = fun_database_objects('DB_schema_rev_engineer_Role_members.sql','na',db_in_scope, db_usr_in_scope)
df_role_access = fun_database_objects('DB_schema_rev_engineer_Role_rights.sql','na',db_in_scope, db_usr_in_scope)
df_db_access = fun_database_objects('DB_schema_rev_engineer_allrights.sql','na',db_in_scope)

lst_df = [df_lst, df_hier, df_usr, df_roles, df_profiles, df_role_members, df_role_access, df_db_access]
lst_tabs = ['DB_list', 'DB_hier', 'df_users', 'DB_Roles', 'DB_Profiles','DB_Role_mems', 'DB_Role_rights', 'DB_allrights']

fun_excel(lst_df,lst_tabs)


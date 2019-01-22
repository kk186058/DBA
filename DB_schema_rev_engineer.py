import pandas as pd

# import numpy as np
import pyodbc
# from pandas.io.sql import read_sql
# import sys
import os
# import variables as var

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)

filename = 'schema.xlsx'

try:
    os.remove(filename)
except OSError:
    pass


def fun_database_objects(filename):
    conn = pyodbc.connect('DRIVER={Teradata};DBCNAME=TDVMWARE;UID=dbc;PWD=dbc;QUIETMODE=YES;')

    with open(filename, 'r') as myfile:
        sql = myfile.read().replace('${DATABASE}', 'dbadmin')

    Data = pd.read_sql(sql, conn)
    Data = Data.astype('str')

    # Data.columns = ['databasename']
    #
    # data_list = Data.databasename.unique()
    # data_list = [x.upper() for x in data_list]

    return Data


df_lst = fun_database_objects('DB_schema_rev_engineer_list.txt')
df_hier = fun_database_objects('DB_schema_rev_engineer_hier.txt')


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(filename, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df_lst.to_excel(writer, sheet_name='DB_list', index=False)
df_hier.to_excel(writer, sheet_name='DB_hier', index=False)

workbook  = writer.book
worksheet = writer.sheets['DB_list']


worksheet.set_column(0, 0, 8)  # Width of column A set to 8.
worksheet.set_column(1, 15, 15)  # Width of column B set to 30.
for i, col in enumerate(df_lst.columns):
    # find length of column i
    column_len = df_lst[col].astype(str).str.len().max()
    column_name_len = len(df_lst.columns[i])
    if column_name_len > column_len:
        column_len = column_name_len
    # Setting the length if the column header is larger
    # than the max column value length
    column_len = max(column_len, len(col)) + 5
    # set the column length
    worksheet.set_column(i, i, column_len)


workbook  = writer.book
worksheet = writer.sheets['DB_hier']

worksheet.set_column(0, 0, 8)  # Width of column A set to 8.
worksheet.set_column(1, 15, 15)  # Width of column B set to 30.
for i, col in enumerate(df_hier.columns):
    # find length of column i
    column_len = df_hier[col].astype(str).str.len().max()
    column_name_len = len(df_hier.columns[i])
    if column_name_len > column_len:
        column_len = column_name_len
    # Setting the length if the column header is larger
    # than the max column value length
    column_len = max(column_len, len(col)) + 5
    # set the column length
    worksheet.set_column(i, i, column_len)

writer.save()

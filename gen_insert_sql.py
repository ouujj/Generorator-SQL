'''
        Create Insert SQL Command For VBA Coding
        Example : "INSERT INTO [TABEL]([field0],[field1]) &_
                  "VALUE('" & value0 &"','"& value1 & "' );"

'''

feild = int(input("Enter Number of field in Table : "))

sql_insert_statement0  = "INSERT INTO [TABEL]()&_"
sql_insert_index0 = 20

sql_insert_statement1  = "VALUE();"
sql_insert_index1 = 6

for i in range(feild):
    
    newinsert0 = "[field %d]"%i
    
    sql_insert_statement0  =  sql_insert_statement0[:sql_insert_index0] +  newinsert0 + sql_insert_statement0[sql_insert_index0:]
    sql_insert_index0 += len(newinsert0)

    newinsert1 = "'\" & value %d & \"',"%i
    sql_insert_statement1  =  sql_insert_statement1[:sql_insert_index1] +  newinsert1 + sql_insert_statement1[sql_insert_index1:]
    sql_insert_index1 += len(newinsert1)
    

    
   # sql_insert_statement1 += ""
sql_insert_statement1 = sql_insert_statement1[:-3] + sql_insert_statement1[-2:]
print(sql_insert_statement0 )
print(sql_insert_statement1 )

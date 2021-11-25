import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '11' 
database = 'TV' 
username = '' 
password = '' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


mySqlQuery =  (""" 
            SELECT * FROM dbo.Config_MessageQueueConfiguration;

              """)

cursor.execute(mySqlQuery)
result = cursor.fetchall()
print(result)
connection.close()
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="<<password>>",
  database="thazhal"
)


def bulk_insert(query_template, values, batchsize=1000):
  mycursor = mydb.cursor()
  N = len(values)
  for i in range(0, N, batchsize):
    mycursor.executemany(query_template, values[i: i+batchsize])
    mydb.commit()

  mycursor.close()



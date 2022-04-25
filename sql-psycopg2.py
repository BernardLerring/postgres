import psycopg2

# connect to psycopg2 database
connection = psycopg2.connect(database="chinook")

# build a cursor object
cursor = connection.cursor()

# cursor.execute('SELECT * FROM "Artist"')

# cursor.execute('SELECT "Name" FROM "Artist"')

# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [118])

cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Pearl Jam"])

# fetch the results(multiple)
results = cursor.fetchall()

# fetch the result(single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
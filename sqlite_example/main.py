import sqlite3

#create empty database
connection = sqlite3.connect("gta.db")

#create cursor object to use SQL commands - all comunications to database
cursor = connection.cursor()

#create table with these headers
cursor.execute("create table gta (release_year integer, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]   

#include data to table gta
cursor.executemany("insert into gta values (?,?,?)", release_list)

#print database rows
for row in cursor.execute("select * from gta"):
    print(row)

print("**********************************************************************************")

#print specific rows
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)

print("**********************************************************************************")

#create another table with these headers
cursor.execute("create table cities (gta_city text, real_city text)")
cursor.execute("insert into cities values (?,?)", ("Liberty City","New York"))
cursor.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})
cities_search = cursor.fetchall()
print(cities_search)

print("**********************************************************************************")
#manipulate database
for i in gta_search:
    one_adjusted = ["New York" if value=="Liberty City" else value for value in i]
    print(one_adjusted)

print("**********************************************************************************")

#manipulate database
for i in gta_search:
    adjusted = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
    print(adjusted)


#close connection to database
connection.close()
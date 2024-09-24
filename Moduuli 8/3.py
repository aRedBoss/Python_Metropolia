import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='omar',
    password='Amoury123',
    charset='utf8mb4',
    collation='utf8mb4_general_ci',
    autocommit=True
)

def airport_distance(airport1, airport2):
    cursor = yhteys.cursor()

    sql1 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{airport1}'"
    cursor.execute(sql1)
    result1 = cursor.fetchone()
    if result1 is None:
        cursor.close()
        return f"Airport {airport1} not found."


    sql2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{airport2}'"
    cursor.execute(sql2)
    result2 = cursor.fetchone()
    if result2 is None:
        cursor.close()
        return f"Airport {airport2} not found."

    cursor.close()

    airport1_coords = (result1[0], result1[1])  # (latitude, longitude)
    airport2_coords = (result2[0], result2[1])

    # Calculate the distance using geopy
    distance = geodesic(airport1_coords, airport2_coords).kilometers

    return f"The distance between {airport1} and {airport2} is {distance:.2f} kilometers."

    

print(airport_distance("EFAA", "EFAH"))
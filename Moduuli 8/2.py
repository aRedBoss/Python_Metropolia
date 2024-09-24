import mysql.connector

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

def airport_type(tyyppi):
    sql = f"select type, count(type) from airport where iso_country = '{tyyppi}' group by type;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    return result
print(airport_type(input("Give me country code: ")))
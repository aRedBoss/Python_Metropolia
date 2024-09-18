import mysql.connector

import mysql.connector

# Establish a connection to the MariaDB/MySQL database
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

def get_airport_name(code_ICAO):
    # Use f-string directly, but this is vulnerable to SQL injection
    sql = f"SELECT name FROM airport WHERE ident = '{code_ICAO}'"
    cursor = yhteys.cursor()

    cursor.execute(sql)  # Directly execute the query without passing parameters
    result = cursor.fetchall()

    cursor.close()  # Close cursor after operation

    return result

# Example call to the function
print(get_airport_name("00A"))
    

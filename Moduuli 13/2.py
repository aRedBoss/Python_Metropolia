from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'database': 'flight_game',
    'user': 'omar',
    'password': 'Amoury123',
    'charset': 'utf8mb4',
    'autocommit': True
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/kenttä/<icao>', methods=['GET'])
def get_airport(icao):
    try:

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT ident, name FROM airport WHERE ident = %s"
        cursor.execute(query, (icao,))
        result = cursor.fetchone()
        
        if result:

            response = {
                "ICAO": result['ident'],
                "Name": result['name']
            }
            return jsonify(response), 200
        else:

            response = {
                "error": "Airport not found",
                "ICAO": icao
            }
            return jsonify(response), 404

    except mysql.connector.Error as err:

        response = {
            "error": "Database error",
            "message": str(err)
        }
        return jsonify(response), 500
    finally:

        if 'connection' in locals():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)

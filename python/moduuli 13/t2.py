from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_airport_by_icao(icao):
    conn = sqlite3.connect("airports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "ICAO": icao,
            "Name": row[0],
            "Municipality": row[1]
        }
    else:
        return None

@app.route('/kenttä/<icao>', methods=['GET'])
def get_airport(icao):
    airport = get_airport_by_icao(icao.upper())
    if airport:
        return jsonify(airport)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)

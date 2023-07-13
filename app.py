from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql5464'
app.config['MYSQL_DB'] = 'photographers_DB'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add_photographer():
    return render_template('add.html')

@app.route('/api/photographers', methods=['GET'])
def get_photographers():
    query_params = request.args

    sql = "SELECT * FROM Photographers WHERE 1=1"
    conditions = []
    values = []

    for key, value in query_params.items():
        if key == 'birthday_from':
            conditions.append('birthday >= DATE(%s)')
            values.append(value)
        elif key == 'birthday_to':
            conditions.append('birthday <= DATE(%s)')
            values.append(value)
        elif key == 'name' and value:
            conditions.append('name = %s')
            values.append(value)
        elif key == 'surname' and value:
            conditions.append('surname = %s')
            values.append(value)
        elif key == 'cv_keyword' and value:
            conditions.append("cv LIKE %s")
            values.append(f"%{value}%")

    if conditions:
        sql += ' AND ' + ' AND '.join(conditions)

    cur = mysql.connection.cursor()
    cur.execute(sql, values)
    photographers = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()

    return jsonify(photographers)


@app.route('/api/photographers', methods=['POST'])
def create_photographer():
    photographer_data = request.get_json()
    name = photographer_data['name']
    surname = photographer_data['surname']
    birthday = photographer_data['birthday']
    cv = photographer_data['cv']

    # Check if deathday is provided
    if 'deathday' in photographer_data and photographer_data['deathday']:
        deathday = photographer_data['deathday']
    else:
        deathday = None

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO Photographers (name, surname, birthday, deathday, cv) VALUES (%s, %s, %s, %s, %s)",
        (name, surname, birthday, deathday, cv)
    )
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Photographer created successfully'})


@app.route('/api/photographers/<int:id>', methods=['PUT'])
def update_photographer(id):
    data = request.get_json()
    name = data['name']
    surname = data['surname']
    birthday = data['birthday']
    deathday = data['deathday'] if data['deathday'] != '' else None
    cv = data['cv']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE Photographers SET name = %s, surname = %s, birthday = %s, deathday = %s, cv = %s WHERE id = %s",
                (name, surname, birthday, deathday, cv, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Photographer updated'}), 200


@app.route('/api/photographers/<int:id>', methods=['GET'])
def get_photographer(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Photographers WHERE id = %s", (id,))
    photographer = cur.fetchone()
    if photographer is None:
        return jsonify({'message': 'Photographer not found'}), 404
    photographer = dict((cur.description[i][0], value) for i, value in enumerate(photographer))
    cur.close()
    return jsonify(photographer)


@app.route('/api/photographers/<int:id>', methods=['DELETE'])
def delete_photographer(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Photographers WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Photographer deleted successfully'})

if __name__ == '__main__':
    app.run()

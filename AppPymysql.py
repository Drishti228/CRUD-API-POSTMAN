from flask import Flask, request, jsonify
from ConnCRUDpymysql import create_intern, read_interns, read_intern, update_intern, delete_intern, close_connection

app = Flask(__name__)

# Routes for CRUD operations
@app.route('/interns', methods=['GET'])
def get_interns():
    interns = read_interns()
    return jsonify({'interns': interns})

@app.route('/interns/<int:intern_id>', methods=['GET'])
def get_intern(intern_id):
    intern = read_intern(intern_id)
    return jsonify({'intern': intern})

@app.route('/interns', methods=['POST'])
def create_intern_route():
    data = request.json
    create_intern(data['intern_name'], data['intern_doj'], data['intern_signum'])
    return jsonify({'message': 'Intern created successfully'})

@app.route('/interns/<int:intern_id>', methods=['PUT'])
def update_intern_route(intern_id):
    data = request.json
    update_intern(intern_id, data['intern_name'], data['intern_doj'], data['intern_signum'])
    return jsonify({'message': 'Intern updated successfully'})

@app.route('/interns/<int:intern_id>', methods=['DELETE'])
def delete_intern_route(intern_id):
    delete_intern(intern_id)
    return jsonify({'message': 'Intern deleted successfully'})

# Close database connection on application exit
@app.teardown_appcontext
def close_db_connection(exception=None):
    close_connection()

if __name__ == '__main__':
    app.run(debug=True)

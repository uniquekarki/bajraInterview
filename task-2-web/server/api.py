from hospital import *

@app.route('/api/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    # Check for blank requests
    if username is None or password is None:
        abort(400)
    
    # Check for existing users
    if User.query.filter_by(username = username).first():
        abort(400)
    
    user = User(username = username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201)

@app.route('/hospital', methods = ['GET'])
def get_appointment():
    return jsonify({'Hospital': Hospital.get_all_appointment()})

@app.route('/hospital/<int:id>', methods = ['GET'])
def get_appointment_by_id(id):
    return_value = Hospital.get_appointment(id)
    return jsonify(return_value)

@app.route('/hospital', methods = ['POST'])
def add_appointment():
    request_data = request.get_json()
    Hospital.add_appointment(request_data.get("patientName"), request_data.get("doctorName"), request_data.get("appointmentDate"))
    response = Response("Appointment Added", 201, mimetype = 'application/json')
    return response

@app.route('/hospital/<int:id>', methods = ['PUT'])
def update_appointment(id):
    request_data = request.get_json()
    Hospital.update_appointment(id,request_data.get("patientName"), request_data.get("doctorName"), request_data.get("appointmentDate"))
    response = Response("Appointment Updated", status=200, mimetype='application/json')
    return response

@app.route('/hospital/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    Hospital.delete_appointment(id)
    response = Response("Appointment Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=8000, debug=True)
from hospital import *

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
    Hospital.add_appointment(request_data['patientName'], request_data['doctorName'],request_data['appointmentDate'])
    response = Response("Appointment Added", 201, mimetype = 'application/json')
    return response

@app.route('/hospital/<int:id>', methods = ['PUT'])
def update_appointment(id):
    request_data = request.get_json()
    Hospital.update_appointment(id,request_data['patientName'], request_data['doctorName'], request_data['appointmentDate'])
    response = Response("Appointment Updated", status=200, mimetype='application/json')
    return response

@app.route('/hospital/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    Hospital.delete_appointment(id)
    response = Response("Appointment Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)
import Database as database
print("Patient class")



class Patient :
    global patient_count
    patient_count = 0 
    class Basis_Information :
        def __init__(self, first_name = None, last_name = None, phone_number = None, email = None, pass_word = None, age = None, gender = None):
            self.first_name = first_name
            self.last_name = last_name
            self.phone_number = phone_number
            self.email = email
            self.password = pass_word
            self.age = age
            self.gender = gender

    class Medical_Information :
        def __init__(self, blood_group = None, ailment = None, medical_history = None, doctor_id = None):
            self.blood_group = blood_group
            self.ailment = ailment
            self.medical_history = medical_history
            self.doctor_id = doctor_id
    
    class Hospital_Records :
        def __init__(self, appointments = None, lab_tests = None, prescriptions = None, billing = None):
            self.appointments = appointments
            self.lab_tests = lab_tests
            self.prescriptions = prescriptions
            self.billing = billing

    def __init__(patient):
        patient.basic_information = Patient.Basis_Information()
        patient.medical_information = Patient.Medical_Information()
        patient.hospital_records = Patient.Hospital_Records()
        patient.count = f"POO{patient_count+1}"

    def add_doctor_to_db (patient):
        database.Hospital["patient"][f"Patient_{patient.count}"] = {
            "First_name" : patient.basic_information.first_name,
            "Last_name" : patient.basic_information.last_name,
            "phone_number" : patient.basic_information.phone_number,
            "email_address" : patient.basic_information.email,
            "password" : patient.basic_information.password,
            "age" : patient.basic_information.age,
            "gender" : patient.basic_information.gender,
            "blood_group" : patient.medical_information.blood_group,
            "ailment" : patient.medical_information.ailment,
            "medical_history" : patient.medical_information.medical_history,
            "Doctor_assigned" : patient.medical_information.doctor_id,
            "appointments" : patient.hospital_records.appointments,
            "lab_tests" : patient.hospital_records.lab_tests,
            "prescriptions" : patient.hospital_records.prescriptions,
            "billing" : patient.hospital_records.billing
        }
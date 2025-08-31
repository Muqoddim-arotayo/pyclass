import Database as database
print("Doctor Class")


class Doctor :
    global doctor_count
    doctor_count = 0
    class Basis_Information :
        def __init__(self, first_name = None, last_name = None, phone_number = None, email = None, pass_word = None):
            self.first_name = first_name
            self.last_name = last_name
            self.phone_number = phone_number
            self.email = email
            self.password = pass_word

    class Professional_Details :
        def __init__(self, specialization = None, license_number = None, years_experience = None):
            self.specialization = specialization
            self.license_number = license_number
            self.years_experience = years_experience
    
    class Hospital_Role :
        def __init__(self, department = None, schedule = None, patients_assigned = None):
            self.department = department
            self.schedule = schedule
            self.patients_assigned = patients_assigned

    def __init__(doctor):
        doctor.basic_information = Doctor.Basis_Information() 
        doctor.professional_Details = Doctor.Professional_Details()
        doctor.hospital_Role = Doctor.Hospital_Role()
        doctor.count = f"DOO{doctor_count+1}"  

    def add_doctor_to_db (doctor):
        database.Hospital["doctors"][f"Doctor_{doctor.count}"] = {
            "First_name" : doctor.basic_information.first_name,
            "Last_name" : doctor.basic_information.last_name,
            "phone_number" : doctor.basic_information.phone_number,
            "email_address" : doctor.basic_information.email,
            "password" : doctor.basic_information.password,
            "specialization" : doctor.professional_Details.specialization,
            "license_number" : doctor.professional_Details.license_number,
            "years_experience" : doctor.professional_Details.years_experience,
            "department" : doctor.hospital_Role.department,
            "schedule" : doctor.hospital_Role.schedule,
            "patients_assigned" : doctor.hospital_Role.patients_assigned
        }
    

doc = Doctor(

)
        


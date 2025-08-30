from Doctor import Doctor
from Patient import Patient


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """ 

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')


    def save_patients_to_file(self, patients):
        try:
            with open('patients.txt', 'w') as file:
                for patient in patients:
                    # Write patient data to the file in a format that can be easily parsed later
                    file.write(f"{patient.get_first_name()},{patient.get_surname()},{patient.get_age()},{patient.get_mobile()},{patient.get_address()},{patient.get_symptoms()}\n")
            print("Patient data saved successfully.")
        except Exception as e:
            print("An error occurred while saving patient data:", e)
    def view_patient(self, patients):
            """
            print a list of patients
            Args:
                patients (list<Patients>): list of all the active patients
            """
            print("-----View Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            for index, item in enumerate(patients):
                print(f'{index+1:3}|{item}')
    def add_patients(self, patients):
        """
        Add a new patient to the system
        Args:
            patients (list): List of patients to be added
        """
        # Get patient details from user input
        fn = input("Enter patient's first name: ")
        ln = input("Enter patient's last name: ")
        age = input("Enter patient's age: ")
        mobile = input("Enter patient's mobile number: ")
        pc = input("Enter patient's postcode: ")
        sm = input("Enter patient's symptom: ")

        # Create a new Patient object
        new_patient = Patient(fn, ln, age, mobile, pc, sm)

        # Append the new patient to the list of patients
        patients.append(new_patient)

        # Save the updated list of patients to the file
        self.save_patients_to_file(patients)

        print("New patient has been added.")


    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if username == self.__username and password == self.__password:
            return True
        else:
            return False
        
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input('Enter doctors name:')
        surname = input("Enter doctor's surname: ")
        speciality = input("Enter doctor's speciality: ")

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = int(input('Enter the number you want to select: '))

        # register
        if op == 1:
            print("-----Register-----")
            # get the doctor details
            print('Enter the doctor\'s details: ')
            #ToDo4
            first_name = input('Enter doctor\'s first name: ')
            surname = input('Enter doctor\'s surname: ')
            speciality = input('Enter doctor\'s speciality: ') 



            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    return
                else:
                    new_doctor = Doctor(first_name,surname,speciality)
                    doctors.append(new_doctor)
                    print(f"{first_name}{surname}-({speciality}) has been registered.")
                    return
                    # break
                
                    

            # ToDo6;already done
            # add the doctor ...
            # ... to the list of doctors
            # print('Doctor registered.')

        # View
        elif op == 2:
            print("-----List of Doctors-----")
            #ToDo7
            self.view(doctors)

        # Update
        elif op == 3:
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                if(len(doctors)!=0):
                    try:
                        index = int(input('Enter the ID of the doctor: ')) - 1
                        doctor_index = self.find_index(index,doctors)
                        if doctor_index !=  False:
                            break
                        else:
                            print("Doctor not found")
                        # doctor_index is the ID mines one (-1)
                    except ValueError: # the entered id could not be changed into an int
                        print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: '))
            # make the user input lowercase

            if op == 1:
                new_first_name = input('Enter the new first name: ')
                doctors[index].set_first_name(new_first_name)
                print('First name updated successfully.')
            if op == 2:
                new_surname = input('Enter the new surname: ')
                doctors[index].set_surname(new_surname)
                print('New surname updated successfully.')
            if op == 3:
                new_speciality = input('Enter the new speciality: ')
                doctors[index].set_speciality(new_speciality)
                print('Speciality updated successfully.')
        # Delete
        elif op == 4:
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            if(len(doctors)!=0):
                doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
                if doctor_index >= 0 and doctor_index < len(doctors):
                    del doctors[doctor_index]
                    print("Doctor deleted.")
                else:
                    print('The id entered is incorrect')

        #if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')  



    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)
        
    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors) != False:
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                # link the patients to the doctor and vice versa
                #ToDo11
                print('The patient is now assign to the doctor.')
                if patients.save_records(patients):
                    print("Patient records successfully updated in patients.txt.")
                else:
                    print("Failed to update patient records.")

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        self.view(patients)

        # Check if there are patients to discharge
        if len(patients) != 0:
            patient_index = int(input('Please enter the patient ID: ')) - 1

            # Check if the index is within the range
            if 0 <= patient_index < len(patients):
                # Append the discharged patient to the discharge_patients list
                discharged_patient = patients.pop(patient_index)
                discharge_patients.append(discharged_patient)
                print(f"Patient with ID: {patient_index + 1} has been discharged")

                # Remove the discharged patient from the data file
                self.remove_patient_from_file(patient_index)

            else:
                print("Invalid patient ID. Please enter a valid ID.")
        else:
            print("No patients to discharge.")

    def remove_patient_from_file(self, patient_index):
        """
        Remove the discharged patient from the data file
        Args:
            patient_index (int): Index of the discharged patient
        """
        try:
            with open("patients.txt", "r") as file:
                lines = file.readlines()

            with open("patients.txt", "w") as file:
                for index, line in enumerate(lines):
                    # Skip the line corresponding to the discharged patient
                    if index != patient_index:
                        file.write(line)

            print("Patient removed from the data file.")

        except FileNotFoundError:
            print("Error: Patients data file not found.")

        except IndexError:
            print("Error: Invalid patient index.")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        # check
        for index in range(len(discharged_patients)):
            item = discharged_patients[index]
            print(f'{index+1:3}|{item}')


    def update_details(self):
            """
            Allows the user to update and change username, password and address
            """

            print('Choose the field to be updated:')
            print(' 1 Username')
            print(' 2 Password')
            print(' 3 Address')
            op = int(input('Input: '))

            if op == 1:
                username = input('Enter the new username: ')
                self.__username = username
                print("Sucessfully changed username")
            elif op == 2:
                password = input('Enter the new password: ')
                # validate the password
                if(password == input('Enter the new password again: ') and self.__password!=password):
                    self.__password = password
                    print("Sucessfully changed password")
                else:
                    print("Sorry something went wrong")
            elif op == 3:
                address = input('Enter the new address: ')
                self.__address= address
                print("Sucessfully changed address")
            else:
                print("Invaild input !")


    def get_management_report(self, doctors, patients):
        print("-----Management Reports-----")
        print('Choose the operation:')
        print(' 1 - Total number of doctors in the system')
        print(' 2 - Total number of patients per doctor')
        print(' 3 - Total number of patients based on the illness type.')
        op = input('Choose an option: ')
        try:
            if op == '1':
                print(f"The total number of doctors: {len(doctors)}")
            elif op == '2':
                for doctor in doctors:
                    totalPatients = doctor.get_total_patients()
                    print(f"{doctor.full_name()} has {totalPatients} patients")
            elif op == '3':
                unique_symptoms = set(tuple(patient.get_symptoms()) for patient in patients)
                for symptoms in unique_symptoms:
                    total = sum(1 for patient in patients if tuple(patient.get_symptoms()) == symptoms)
                    print(f'The total number of patients with {symptoms}: {total}')

            else:
                print("Invalid Option")
        except Exception as e:
            print(e)

        
    def relocate_doctor(self, patients, doctors):
        print("-----Relocate Doctor-----")
        print("-----List of Patients-----")
        self.view(patients)

        if len(patients) != 0:
            try:
                patient_index = int(input('Enter the ID of the patient to relocate the doctor from: ')) - 1
                if 0 <= patient_index < len(patients):
                    print("-----List of Doctors-----")
                    self.view(doctors)
                    new_doctor_index = int(input('Enter the ID of the new doctor: ')) - 1

                    if 0 <= new_doctor_index < len(doctors):
                        old_doctor_full_name = patients[patient_index].get_doctor()
                        patients[patient_index].link(doctors[new_doctor_index].full_name())
                        doctors[new_doctor_index].add_patient(patients[patient_index])
                        print(f"Successfully relocated {old_doctor_full_name} to {doctors[new_doctor_index].full_name()}.")
                        # Patient.write_patientsfile(patients)
                    else:
                        print('Invalid new doctor ID. Check your input.')
                else:
                    print('Invalid patient ID. Check your input.')
            except ValueError:
                print('Invalid input for patient or new doctor ID. Please enter a valid integer.')
        else:
            print('No patients available for relocation.')

    def find_index(self, index, doctors):
        if index in range(0, len(doctors)):
            return True
        else:
            return False

    def get_doctor_details(self):
        print('Enter the doctor\'s details:')
        first_name = input("Enter the first name:") 
        surname = input("Enter the surname:")
        speciality = input("Enter the speciality:")
        return first_name, surname, speciality

    def group_patients(self, patients):
        sameFamily = []
        for patient in patients:
            if patient.get_surname() == "Smith":
                sameFamily.append(str(patient))
        self.view(sameFamily)

    def read_patientsfile(read_data_files):
        patient_list = []
        try:
            with open(read_data_files, 'r') as d:
                for i in  d:
                    print(i.split(','))
                    patient_list.append(i)

        except FileNotFoundError:
            print(" No file found")

        finally:
            return patient_list
        
    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |   Symptoms')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name()) 
                self.view(patients)
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                print('The patient is now assign to the doctor.')

                # if Patient.write_patientsfile(patients):
                #     print("Patient records successfully updated in patients file")
                # else:
                #     print("Failed to update records in patient file")

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')
            
            
        except ValueError:
            print('Invalid ID')
            return

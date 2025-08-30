# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
def main():
    """
    the main function to be ran when the program runs
    """
    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234','Fever'), Patient('Mike','Jones', 37,'07555551234','L2 2AB','Head ache'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','COLD')]

    discharged_patients = []
    
    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')
    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- add patient') 
        print(' 5- Assign doctor to a patient')
        print(' 6- Update admin details')
        print(' 7- Get Management Report')
        print(' 8- View all the patients')
        print(' 9- View all the patients from the same family')
        print(' 10- Relocate Doctor of patients')
        print(' 11- Quit')
        # get the option
        op = input('Option: ')
        if op == '1':
            admin.doctor_management(doctors)
        elif op == '2':
            while True:
                op = input('Do you want to discharge any patient (Y/N): ').lower()
                if op == 'no' or op == 'n':
                    break
                elif op == 'yes' or op == 'y':
                    admin.discharge(patients,discharged_patients)
                else:
                    print('Please answer by yes or no.')
        elif op == '3':
            admin.view_discharge(discharged_patients)
        elif op =='4':
            admin.add_patients(patients)
            admin.save_patients_to_file(patients)  
        elif op == '5':
            admin.assign_doctor_to_patient(patients, doctors)
        elif op == '6':
            admin.update_details()
        elif op == '7':
            admin.get_management_report(doctors, patients)
        elif op == '8':
            admin.view_patient(patients)
        elif op == '9':
            admin.group_patients(patients)
        elif op == '10':
            admin.relocate_doctor(patients, doctors)
        elif op == '11':
            print('System terminated')
            quit()
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()

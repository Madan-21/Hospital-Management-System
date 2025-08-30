from Person import Person
class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptom, isFamily = False ):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        super().__init__(first_name,surname)
        self.__age = age
        self.__mobile = mobile
        self.__address = postcode
        self.__doctor = 'None'
        self.__symptoms = [symptom]
        self.isFamily = isFamily

    def get_doctor(self) :
        #ToDo3
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        # self.__symptoms = input("Enter your symptoms")
        print(self.__symptoms)
    
    def set_new_symptoms(self,symptom):
        self.__symptoms  = symptom

    def get_symptoms(self):
        symp=""
        for symptom in self.__symptoms:
            symp = symp + " "+ symptom
        return symp
    
    def get_age(self):
        return self.__age
    def get_mobile(self):
        return self.__mobile
    def get_address(self):
        return self.__address


    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__address:^10}|{self.get_symptoms():^15}'
    

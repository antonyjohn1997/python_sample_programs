class Car:
    def __init__(self,company,model,year):
       self.company=company
       self.model=model
       self.__year=year #private attribute

    def __calculate_age(self): # private method
        return 2024-self.__year

    def display_car_age(self):
        age=self.__calculate_age()
        print(f"the cars age is : {age} years") 
car=Car("toyota","corolla",2000)
car.display_car_age()           
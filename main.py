from enum import Enum

class InsuranceType(Enum):
    TRAFFIC = 1
    HEALTH = 2
    HOME = 3
class Methods(Enum):
    Linear = 0
    Polynomial = 1
    Logistic = 2
 
 #Insurance Types
insurance_types = [insurance.name and insurance.value for insurance in InsuranceType]
insurance_type_selection = int(input("Choose Insurance Types : " + str(insurance_types)+ " .:"))
insurance_type = InsuranceType(insurance_type_selection).name
#Methods
method_types = [method.name and method.value for method in Methods]
method_type_selection= int(input("Choose Method : " + str(method_types) + " : " ))
#Method Dependency Manager Class goes here

print(insurance_type)


#TODO : Read in SQL
data = []
#TODO : Prediction class

#TODO : Predict next value


#TODO : Print prediction

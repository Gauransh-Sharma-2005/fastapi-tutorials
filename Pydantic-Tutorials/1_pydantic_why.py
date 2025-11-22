# Problems:
      # --> Type Validation
      # --> Data Validation

# This function does not involve type validation
# def insert_patient_data(name, age):

#   print(name)
#   print(age)
#   print('Inserted into database')

# insert_patient_data('Nitish', 'thirty')


# So we use typehinting:
# typehinting does not produce error on datatype mismatch
# def insert_patient_data(name: str, age: int):

#   print(name)
#   print(age)
#   print('Inserted into database')

# insert_patient_data('Nitish', '30')


# So now we will strictly modify our function
# def insert_patient_data(name: str, age: int):

#   if type(name) == str and type(age) == int:  # this method is not scalable (type validation)
#     if age < 0: # this method is not scalable (data validation)
#       raise ValueError('Age cannot be negative')
#     print(name)
#     print(age)
#     print('Inserted into database')
#   else:
#     raise TypeError('Incorrect data type')

# insert_patient_data('Nitish', '30')


from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

  # Schema
  # By default every field is required
  name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 characters', examples=['Nitish', 'Ansh'])]  # str = Field(max_length=50)
  email: EmailStr # used to validate email format
  linkedin_url: AnyUrl
  age: int = Field(gt=0, lt=110)
  weight: Annotated[float,Field(gt=0, strict= True)]  # Field is used to add custom validation by applying a constraint. Field can also be used to add metadata with 'Annotated' module. Field can also be used to add default values. strict prevents type coercion(converting string to int).
  married: Annotated[bool, Field(default=None, description='Marital status')]
  allergies: Annotated[Optional[List[str]], Field(default= None,max_length=5)]  # this validates that it is a list as well as all the items are strings. Now this is a optional field. An optional field by default requires a None value in case the field is not described
  contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print('inserted into database')

def update_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print('updated')

patient_info = {'name': 'nitish', 'age': '30','email': 'abc@gmail.com', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'],'linkedin_url': 'http://linkedin.com/1322', 'contact_details': {'phone': '23451245'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

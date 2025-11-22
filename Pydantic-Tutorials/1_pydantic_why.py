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


from pydantic import BaseModel

class Patient(BaseModel):

  # Schema
  name: str
  age: int
  # weight: float

def insert_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print('inserted into database')

patient_info = {'name': 'nitish', 'age': '30'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

from pydantic import BaseModel

# In nested model we use pydantic object of one model in other model

# Advantages:
#    Better organzation of related data (eg, address, insurance)
#    Reusability: Use vitals in different models (eg., Patient, MedicalRecord)
#    Readability: Easier for developers and API consumers to understand 
#    Validation: Nested models are validated automatically. No extra work needed 

class Address(BaseModel):

  city: str
  state: str
  pin: str

class Patient(BaseModel):

  name: str
  gender: str
  age: int
  address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

# pydantic object of address model
address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

# pydantic object of patient model
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)
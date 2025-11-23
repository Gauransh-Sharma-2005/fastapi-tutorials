from pydantic import BaseModel

 # serialization is the process of converting a model instance into a less structured form, such as python dictionary or a JSON string which is useful for exporting, data storage, etc.
 # model_dump() --> converts the pydantic model object into a dictionary
 # model_dump_json() --> converts the pydantic model object into a JSON string
 # exclude_unset --> this will not include those fields during export which are not set when the instance is created.

class Address(BaseModel):

  city: str
  state: str
  pin: str

class Patient(BaseModel):

  name: str
  gender: str
  age: int
  address: Address
  marital_status: str = 'married'

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

# pydantic object of address model
address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

# pydantic object of patient model
patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include=['name', 'address'], exclude={'address': ['state']}, exclude_unset=True)  
# temp = patient1.model_dump_json()  

print(temp)
print(type(temp))
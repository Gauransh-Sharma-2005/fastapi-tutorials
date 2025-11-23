from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

# Field validator works in two modes - before mode and after mode
# after mode is the default mode where you will get the value of a field after type coercion
# in before mode you will get the value of the field before the type coercion

class Patient(BaseModel):

  name: str
  email: EmailStr
  age: int
  weight: float
  married: bool
  allergies: List[str]
  contact_details: Dict[str, str]

  @field_validator('email')
  @classmethod
  def email_validator(cls, value):

    valid_domains = ['hdfc.com', 'icici.com']
    # abc@gmail.com
    domain_name = value.split('@')[-1]

    if domain_name not in valid_domains:
      raise ValueError('Not a Valid Domain')
    
    return value
  
  @field_validator('name', mode='after')
  @classmethod
  def name_validator(cls, value):
    return value.upper()

  @field_validator('age', mode='after') 
  @classmethod
  def age_validator(cls, value):    # here if the mode is 'before', and value of age is string but encoded to be int, then it will show error
    if 0 < value < 100:
      return value
    else:
      raise ValueError('Age should be between 0 to 100')

def update_patient_data(patient: Patient):
  
  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print('updated')

patient_info = {'name': 'nitish', 'age': '30','email': 'abc@hdfc.com', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'],'linkedin_url': 'http://linkedin.com/1322', 'contact_details': {'phone': '23451245'}}

patient1 = Patient(**patient_info)  # validation --> type coercion done wherever required

update_patient_data(patient1)
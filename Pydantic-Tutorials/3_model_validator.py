from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

# Model validator is used when you want to validate mmultiple field at the same time.

class Patient(BaseModel):

  name: str
  email: EmailStr
  age: int
  weight: float
  married: bool
  allergies: List[str]
  contact_details: Dict[str, str]

  @model_validator(mode='after')
  def validate_emergency_contact(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
      raise ValueError('Patients older than 60 must have an emergency contact')
    return model


def update_patient_data(patient: Patient):
  
  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print('updated')

patient_info = {'name': 'nitish', 'age': '65','email': 'abc@hdfc.com', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'],'linkedin_url': 'http://linkedin.com/1322', 'contact_details': {'phone': '23451245', 'emergency': '2342164565'}}

patient1 = Patient(**patient_info)  # validation --> type coercion done wherever required

update_patient_data(patient1)
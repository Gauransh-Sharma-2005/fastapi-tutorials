from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

# a type of field in which value of the field is not provided by the user
# instead we use the rest of the fields to calculate the value of the computed field
# the name that you give to your function becomes the name of your field, in this case the function name is 'bmi' so the field is also named bmi.

class Patient(BaseModel):

  name: str
  email: EmailStr
  age: int
  weight: float # kg
  height: float # mtr
  married: bool
  allergies: List[str]
  contact_details: Dict[str, str]

  @computed_field
  @property
  def bmi(self) -> float:  # the ( -> float ) tells that the value of the bmi will be in float
    bmi = round(self.weight / (self.height**2),2)
    return bmi


def update_patient_data(patient: Patient):
  
  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print('BMI:', patient.bmi)
  print('updated')

patient_info = {'name': 'nitish', 'age': '65','email': 'abc@hdfc.com', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'],'linkedin_url': 'http://linkedin.com/1322', 'contact_details': {'phone': '23451245', 'emergency': '2342164565'}}

patient1 = Patient(**patient_info)  # validation --> type coercion done wherever required

update_patient_data(patient1)
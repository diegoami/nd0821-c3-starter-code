from pydantic import BaseModel, ValidationError, validator

from enum import Enum



# age,workclass,fnlgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,salary
# 39,State-gov,77516,Bachelors,13,Never-married,Adm-clerical,Not-in-family,White,Male,2174,0,40,United-States,<=50K

WORKCLASSES = [x.lower() for x in ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov', '?'
 'Self-emp-inc', 'Without-pay', 'Never-worked']]
EDUCATIONS = [x.lower() for x in ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college', 'Assoc-acdm'
 'Assoc-voc', '7th-8th', 'Doctorate', 'Prof-school', '5th-6th', '10th'
 '1st-4th', 'Preschool', '12th']]
MARITAL_STATUSES = [x.lower() for x in ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-spouse-absent'
 'Separated', 'Married-AF-spouse', 'Widowed']]
OCCUPATIONS = [x.lower() for x in ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Prof-specialty'
 'Other-service', 'Sales', 'Craft-repair', 'Transport-moving'
 'Farming-fishing', 'Machine-op-inspct', 'Tech-support', '?'
 'Protective-serv', 'Armed-Forces', 'Priv-house-serv']]
RELATIONSHIPS = [x.lower() for x in ['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried', 'Other-relative']]
RACES = [x.lower() for x in ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']]
SEXES = [x.lower() for x in ['Male', 'Female']]
NATIVE_COUNTRIES = [x.lower() for x in ['United-States', 'Cuba', 'Jamaica', 'India', '?', 'Mexico', 'South'
 'Puerto-Rico', 'Honduras', 'England', 'Canada', 'Germany', 'Iran'
 'Philippines', 'Italy', 'Poland', 'Columbia', 'Cambodia', 'Thailand', 'Ecuador'
 'Laos', 'Taiwan', 'Haiti', 'Portugal', 'Dominican-Republic', 'El-Salvador'
 'France', 'Guatemala', 'China', 'Japan', 'Yugoslavia', 'Peru'
 'Outlying-US(Guam-USVI-etc)', 'Scotland', 'Trinadad&Tobago', 'Greece'
 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary', 'Holand-Netherlands']]

class CensusEntry(BaseModel):
     age: int
     workclass: str
     fnlgt: int
     education: str
     education_num: str
     marital_status: str
     occupation: str
     relationship: str
     race: str
     sex: str
     capital_gain: int
     capital_loss: int
     hours_per_week: int
     native_country: str

     @validator('workclass')
     def validate_workclass(cls, workclass):
          if workclass.lower() not in WORKCLASSES:
               raise ValueError(f'workclass {workclass} not valid, must be in {WORKCLASSES}')

     @validator('education')
     def validate_education(cls, education):
          if education.lower() not in EDUCATIONS:
               raise ValueError(f'education {education} not valid, must be in {EDUCATIONS}')

     @validator('marital_status')
     def validate_marital_status(cls, marital_status):
          if marital_status.lower() not in MARITAL_STATUSES:
               raise ValueError(f'marital_status {marital_status} not valid, must be in {MARITAL_STATUSES}')

     @validator('occupation')
     def validate_occupation(cls, occupation):
          if occupation.lower() not in OCCUPATIONS:
               raise ValueError(f'occupation {occupation} not valid, must be in {OCCUPATIONS}')

     @validator('relationship')
     def validate_relationship(cls, relationship):
          if relationship.lower() not in RELATIONSHIPS:
               raise ValueError(f'relationship {relationship} not valid, must be in {RELATIONSHIPS}')

     @validator('race')
     def validate_race(cls, race):
          if race.lower() not in RACES:
               raise ValueError(f'race {race} not valid, must be in {RACES}')

     @validator('sex')
     def validate_sex(cls, sex):
          if sex.lower() not in SEXES:
               raise ValueError(f'sex {sex} not valid, must be in {SEXES}')

     @validator('native_country')
     def validate_native_country(cls, native_country):
          if native_country.lower() not in NATIVE_COUNTRIES:
               raise ValueError(f'native_country {native_country} not valid, must be in {NATIVE_COUNTRIES}')
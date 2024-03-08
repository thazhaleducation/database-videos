from mimesis import Person
from mimesis import Address
from mimesis import Generic
from mimesis.locales import Locale


person = Person(Locale.EN)
address = Address(Locale.EN)
generic = Generic(locale=Locale.EN)

from dataclasses import dataclass
branches=[
  "CSE",
  "MECH",
  "CIVIL",
  "EEE",
  "ECE",
  "IT"
]

@dataclass
class Student():
  id: int
  name: str
  country: str
  gender: str
  phone_number: str
  roll_no: str
  branch: str
  doj: str

DEFAULT_N = 1000000
def generate_students(N=DEFAULT_N):
  return [Student(x,
                  person.name(),
                  address.country(),
                  person.gender(),
                  person.phone_number(mask="###-###-####"),
                  f"{generic.datetime.year()}{branches[x % 5][:2]}{x}",
                  branches[x % 5],
                  generic.datetime.date(start=2023)) for x in range(1, N+1)]

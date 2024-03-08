from generate_students import generate_students
from db_utils import bulk_insert

N = 1000000
batchsize=1000
students = generate_students(N)
newline = "\n"
filename = "students.csv"
header = f"id,name,country,gender,phone_number{newline}"
with open(filename, "w") as f:
  f.write(header)
  [f.write(f"{st.id},{st.name},{st.country},{st.gender},{st.phone_number}{newline}") for st in students]

f.close()

from generate_students import generate_students
from db_utils import bulk_insert

N = 1000000
batchsize=1000
students = generate_students(N)

val = [(st.id, st.name, st.country,st.gender, st.phone_number) for st in students]

sql = "insert into students_without_pk (id, name, address, gender, mobile) values (%s, %s, %s, %s, %s)"

bulk_insert(query_template=sql, values=val)

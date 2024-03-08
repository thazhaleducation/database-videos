from generate_students import generate_students
from db_utils import bulk_insert


N = 1000000
batchsize=1000
students = generate_students(N)

val = [(st.name,st.country, st.gender, st.phone_number, st.roll_no , st.branch, st.doj) for st in students]

sql = "insert into students (name, address, gender, mobile, rollno, branch, doj) values (%s, %s, %s, %s, %s, %s, %s)"
bulk_insert(query_template=sql, values=val)

from datetime import datetime
filename = "students.csv"

def select(filter="id=1"):
  column_name,value = filter.split("=")
  with open(filename, "r") as students:
    header = students.readline()
    column_index = header.split(",").index(column_name)
    print(f"column={column_name} - value={value} - column_index={column_index}")
    res = []
    start_time = datetime.now()
    for st in students:
      curr_val = st.split(",")[column_index]
      # print(curr_val)
      if (curr_val.lower() == value.lower()):
        res.append(st)
    end_time = datetime.now()
  print("Time taken: %.2fs" % (time_taken(start_time, end_time)))
  students.close()
  return res

def time_taken(start_time, end_time):
  return (end_time - start_time).microseconds/1000000


# =========
# Querying|
# =========
# print(select(filter="id=1000"))
# print(select(filter="name=Will"))















from avltree.avltree import AvlTree, Key

def indexing():
  print("building index tree...")
  tree = AvlTree()
  with open(filename, "r") as students:
    header = students.readline()
    for st in students:
      key = Key(st.split(",")[0], st)
      tree.add(key)
  students.close()
  print("built index tree...")
  return tree



index_tree = indexing()  
command = ""
    

while command != "Exit":
  command = input("Enter the key to search or type Exit")
  if command != "Exit":
    start_time = datetime.now()
    result = index_tree.search(command)
    end_time = datetime.now()
    print("Time taken: %.2fs" % (time_taken(start_time, end_time)))
    print(result)
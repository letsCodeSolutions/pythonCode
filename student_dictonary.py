#Dictonary with one value for each key
#students ={"Bob":21,"John":31,"Ron":45,"Sam":36}

#Dictonary with list for each key
students = {
    "Bob":["ID001",21,"A"],
    "John":["ID002",31,"B"],
    "Ron":["ID003",45,"C"],
    "Sam":["ID004",36,"D"]
    }
print(students["Sam"])
print(students["Ron"][0])
print(students["John"][1:])

#Dictonary with Dictonary within
student_Dic = {
    "Bob":{"ID":"ID001","age":21,"grade":"A"},
    "John":{"ID":"ID002","age":31,"grade":"B"},
    "Ron":{"ID":"ID003","age":45,"grade":"C"},
    "Sam":{"ID":"ID004","age":36,"grade":"C"}
    }

print(student_Dic["Bob"])
print(student_Dic["John"]["age"])
print(student_Dic["Ron"]["ID"],student_Dic["Ron"]["grade"])
      

import pandas as pd

class MyClass:
      def __init__(self,my_stud):
         self.my_stud=my_stud

my_objects=[]
final_students=[]

while True:

    address={}
    student={}

    roll=int(input("Enter Student's Roll"))
    name=input("Enter Student's Name")
    age= int(input("Enter Student's age"))
    add1=input("Enter House No. and House Name")
    add2=input("Enter Street Name")
    add3=int(input("Enter Pincode"))
    add4=input("Enter City Name")
    add5=input("Enter State name")
    phone=input("Enter Phone No.")

    address["add1"]=add1
    address["add2"]=add2
    address["add3"]=add3
    address["add4"]=add4
    address["add5"]=add5

    student["roll"]=roll
    student["name"]=name
    student["age"]=age
    student["address"]=address
    student["phone"]=phone

    s=MyClass(student)
    my_objects.append(s)

    again=input("Do you want to enter more student details yes/no:").lower()
    if again=="yes":
        continue
    else:
        break

for i in my_objects:
    final_students.append(i.my_stud)

df=pd.json_normalize(final_students)

df.to_csv(r"C:\Users\risha\Downloads\my_students.csv", index=False, mode='a', header=False)

print("Data saved")
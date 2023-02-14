"""n=int(input())
i=1
c=n
while i<=n:
    print(" "*(c-1),"*"*(2*i-1) ," "*(c-1))
    i+=1
    c-=1
    
n=int(input())
i=n
c=1
while i>0:
    print(" "*(c-1),"*"*(2*i-1) ," "*(c-1))
    i-=1
    c+=1
    """
students = {
  "stud1" : {
    "name" : "name1",
    "surname" : "surname1",
    "id" : "id1"
  },
  "stud2" : {
    "name" : "name2",
    "surname" : "surname2",
    "id" : "id2"
  },
  "stud3" : {
    "name" : "name3",
    "surname" : "surname3",
    "id" : "id3"
  }
}
i=len(students)
iter="stud{}"
while i>0:
    print(students[iter.format(i)])
    i-=1


    


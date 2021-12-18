from typing import Mapping


class Employee:
    id=12
    salary=45000
    Holiday="Sunday"
    pass#-If we cannot write inside the data in any field like class and function, so pass cannot take error--

usama=Employee()
mudasir=Employee()
saad=Employee()
#-------Class Variables, All the objects share these variables--------
print(usama.id)
print(usama.Holiday)
print(mudasir.id)
print(mudasir.Holiday)
print(saad.id)
print(saad.Holiday)
#-------Object/Instance variables, and it  is the property of instance--------
#-------Every Instace have own variable-----------
usama.Name="Usama"
mudasir.leave=2
saad.passion="programming"
print(usama.Name)
print(mudasir.leave)
print(saad.passion)
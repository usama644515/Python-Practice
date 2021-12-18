# Public:
# Private:
# Protected:

class Employee:
    #------------Public:-------------
    company="Google"
    #------------Protected:-------------
    _company2="Youtube"
    #------------Private:-------------
    __company3="Instagram"

emp=Employee()
print(emp.company)
print(emp._company2)
print(emp._Employee__company3)#-----Because it is Private so we can access only that way-------
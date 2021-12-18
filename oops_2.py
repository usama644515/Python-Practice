
class Marks:
    def student_id(self,id):
        print(id)
    def GetMarks(self,isl,comp,maths):
        self.isl=isl
        self.comp=comp
        self.maths=maths
    def ShowMarks(self):
        print(f"The Marks in Islamiyat = {self.isl}")
        print(f"The Marks in Computer = {self.comp}")
        print(f"The Marks in Maths = {self.maths}")
    
    
if __name__ =='__main__':
    usama=Marks()
    usama.isl=int(input("Enter Your Islamiyat Marks\n"))
    usama.comp=int(input("Enter Your Computer Marks\n"))
    usama.maths=int(input("Enter Your Maths Marks\n"))
    usama.GetMarks(usama.isl,usama.comp,usama.maths)
    usama.ShowMarks()
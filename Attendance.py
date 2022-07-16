import json

class AttendanceManager:
    def __init__(self) -> None:
        self.Config = json.load( open("Modules//config.json",'r') )

        try:self.AttendanceSheet = open(self.Config["paths"]["attendancePath"],"r")
        except:self.AttendanceSheet = open(self.Config["paths"]["attendancePath"],"w")
        self.AttendanceSheet = open(self.Config["paths"]["attendancePath"],"r")

    def checkForStudent(self):
        #todo: face rec. and return the roll no of the student
        self.Present('201SE127')

    def Present(self,rollNumber:str):
        pass
'''
def CreateFile():
    StudentFile = open("Student.txt", "w")
    StudentFile.close()
CreateFile()
def WriteFile():
    StudentFile = open("Student.txt", "a")
    StudentFile.write()
    StudentFile.close()
WriteFile()
def ReadAsList():
    StudentFile = open("Student.txt", "r")
    lineas = StudentFile.readlines()
    print(lineas)
    StudentFile.close()
'''
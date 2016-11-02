class LineReader():
    def __init__(self,filename):
        self.fileobject = open(filename,'r')

    def __getitem__(self,index):
        line = self.fileobject.readline()
        if line == "":
            self.fileobject.close()
            return IndexError
        else:
            return line.split('::')[:2]

try:
    for name,age in LineReader("people.txt"):
        print("Age of {0} is : {1}".format(name,age))
except TypeError as error:
    #print("End of File")
    pass
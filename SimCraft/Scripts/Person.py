class ScriptedEntity:
    __ID = 0
    __x = 0
    __y = 0
    __z = 0
    def __init__(self, ID, x, y, z):
        self.__ID = ID
        self.__x = x
        self.__y = y
        self.__z = z
        
    def GetID(self):
        return self.__ID
    
    def GetPosition(self):
        return self.__x, self.__y, self.__z
    
    def SetPosition(self, x , y, z):
        self.__x = x
        self.__y = y
        self.__z = z

class Person(ScriptedEntity):
    __age = 0
    __sex = "unknown"
    def __init__(self, ID, age, sex, x, y, z):
        ScriptedEntity.__init__(self, ID, x, y, z)
        self.__age = age
        self.__sex = sex
        
    def GetID(self):
        return ScriptedEntity.GetID(self)
        
    def GetAge(self):
        return self.__age
    def SetAge(self, age):
        self.__age = age    
    
    def GetSex(self):
        return self.__sex
    def SetSex(self, sex):
        self.__sex = sex
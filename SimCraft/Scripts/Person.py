class ScriptedEntity():
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
	__foodReq = 1000
	__foodCollected = 0
	__goingToDo = "unknown"
	__goingToPos = [0,0,0]
	__TimeUntillSleep = 60 * 60 * 8 # sec * min * tim
	
	def __init__(self, ID, age, sex, x, y, z):
		ScriptedEntity.__init__(self, ID, x, y, z)
		self.__age = age
		self.__sex = sex
		
	def Update(self, deltaTime, id):
		incID = 0
		self.__TimeUntillSleep = self.__TimeUntillSleep - deltaTime
		
		if self.__goingToDo == "CollectFood":
			self.__foodCollected = self.__foodCollected + (1 * deltaTime)
		elif self.__goingToDo == "Sleep":
			i = 0
			
		if self.__foodCollected < self.__foodReq:
			self.__goingToDo = "CollectFood"
		else:
			self.__goingToDo = "Sleep"
			
		return incID
		
	def WalkTo(self, to):
		ScriptedEntity.SetPosition(self, to[0], to[1], to[2])
	
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
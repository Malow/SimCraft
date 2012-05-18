import Python
from Vector3 import Vector3
import math
import random


class ScriptedEntity():
    __ID = 0
    __Pos = Vector3(0,0,0)
	
    def __init__(self, ID, pos):
        self.__ID = ID
        self.__Pos = pos
        
    def GetID(self):
        return self.__ID
    
    def GetPosition(self):
        return self.__Pos
    
    def SetPosition(self, x, y, z):
        self.__Pos = Vector3(x, y, z)
		
class Wolf(ScriptedEntity):
	__age = 5
	__sex = "male"
	
	def __init__(self, ID, age, sex, pos):
		ScriptedEntity.__init__(self, ID, pos)
		if sex == "male":
			Python.CreateEntity("Media/WolfMale.obj", ID, pos.x, pos.y, pos.z)
		else:
			Python.CreateEntity("Media/WolfFemale.obj", ID, pos.x, pos.y, pos.z)
		self.__age = age
		self.__sex = sex
		
	def Update(self, deltaTime, entities, entId):
		self.__age += deltaTime / 31556926.0          # 1 year
		if self.__age < 5:
			Python.SetScale(self.GetID(), float(float(self.__age) / 10.0))
		else:
			Python.SetScale(self.GetID(), 1.0)
			
		if self.__age > 20:
			rand = random.random()               # between 0.0 and 1.0
			if(rand < deltaTime / (31556926.0 * 3.0)):      # I want the wolf to die within 3 years on avrage
				entities.remove(self)
				Python.DeleteEntity(self.GetID())
			
			
		
		return entId
			
	def GetAge(self):
		return self.__age
		
	def SetAge(self, age):
		self.__age = age
		
	def GetSex(self):
		return self.__sex
		
	def SetSex(self, sex):
		self.__sex = sex
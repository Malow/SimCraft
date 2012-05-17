from Vector3 import Vector3
import math
import Python

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
		
class FoodBush(ScriptedEntity):
	__food = 1000
	__foodGrowth = 10
	def __init__(self, ID, food, pos):
		ScriptedEntity.__init__(self, ID, pos)
		self.__food = food
		Python.CreateEntity("Media/FoodBush.obj", ID, pos.x, pos.y, pos.z)
		
	def Update(self, deltaTime, entities, entId):
		if self.__food < 1000:
			self.__food += self.__foodGrowth * deltaTime
		if self.__food > 1000:
			self.__food = 1000

	def RemoveFood(self, food):
		self.__food -= food
	def AddFood(self, food):
		self.__food += food
		
	def SetFood(self, food):
		self.__food = food
	def GetFood(self):
		return self.__food
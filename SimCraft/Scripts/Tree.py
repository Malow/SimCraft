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
		
class Tree(ScriptedEntity):
	__wood = 1000
	__woodGrowth = 10
	__age = 50
	def __init__(self, ID, age, wood, pos):
		ScriptedEntity.__init__(self, ID, pos)
		self.__age = age
		self.__wood = wood
		Python.CreateEntity("Media/Tree.obj", ID, pos.x, pos.y, pos.z)
		
	def Update(self, deltaTime, entities, entId):
		if self.__wood < 1000:
			self.__wood += self.__woodGrowth * deltaTime
		if self.__wood > 1000:
			self.__wood = 1000

	def RemoveWood(self, wood):
		self.__wood -= wood
	def AddWood(self, wood):
		self.__wood += wood
		
	def SetWood(self, wood):
		self.__wood = wood
	def GetWood(self):
		return self.__wood
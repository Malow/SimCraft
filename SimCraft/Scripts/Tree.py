from Vector3 import Vector3
import math
import Python
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
		
class Tree(ScriptedEntity):
	__MaxWood = 5000
	__wood = 1000
	__woodGrowth = __MaxWood / 1577846300.0       # 50 years to reach 5000 wood
	__age = 50
	def __init__(self, ID, age, wood, pos):
		ScriptedEntity.__init__(self, ID, pos)
		self.__age = age
		self.__wood = wood
		Python.CreateEntity("Media/Tree.obj", ID, pos.x, pos.y, pos.z)
		
	def Update(self, deltaTime, entities, entId):
		self.__age += deltaTime / 31556926.0          # 1 year
		
		if self.__age > 200:
			self.__wood -= self.__woodGrowth * deltaTime
			Python.SetScale(self.GetID(), float(float(self.__wood) / float(self.__MaxWood)))
			if self.__wood < 200:
				entities.remove(self)
				Python.DeleteEntity(self.GetID())
				
		elif self.__wood < 0:
			entities.remove(self)
			Python.DeleteEntity(self.GetID())
			
		else:
			if self.__wood < self.__MaxWood:
				Python.SetScale(self.GetID(), float(float(self.__wood) / float(self.__MaxWood)))
				self.__wood += self.__woodGrowth * deltaTime   
			elif self.__wood > self.__MaxWood:
				self.__wood = self.__MaxWood
				Python.SetScale(self.GetID(), float(float(self.__wood) / float(self.__MaxWood)))
			else:
				rand = random.random()               # between 0.0 and 1.0
				if(rand < deltaTime / (31556926.0 * 5.0)):      # I want 1 tree every 5 year or so, 31556926 secs
					rand2 = random.random()
					rand3 = random.random()
					rand2 -= 0.5
					rand3 -= 0.5
					newTree = Tree(entId, 1, 10, self.GetPosition() + Vector3(rand2, 0, rand3) * 40.0)
					entities.append(newTree)
					entId += 1
				
		return entId

	def RemoveWood(self, wood):
		self.__wood -= wood
	def AddWood(self, wood):
		self.__wood += wood
		
	def SetWood(self, wood):
		self.__wood = wood
	def GetWood(self):
		return self.__wood
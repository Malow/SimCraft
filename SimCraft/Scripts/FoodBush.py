from Vector3 import Vector3
import math
import Python
import random

class ScriptedEntity():
    __ID = 0
    __Pos = Vector3(0,0,0)
    __Iam = "Unknown"

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
	__MaxFood = 1000
	__food = 1000
	__foodGrowth = __MaxFood / (31556926.0 * 0.5)           # 0.5 year to reach 1000 food.
	def __init__(self, ID, food, pos):
		ScriptedEntity.__init__(self, ID, pos)
		self.__food = food
		Python.CreateEntity("Media/FoodBush.obj", ID, pos.x, pos.y, pos.z)

	def Update(self, deltaTime, entities, entId):
		if self.__food < 0:
			entities.remove(self)
			Python.DeleteEntity(self.GetID())

		else:
			if self.__food < self.__MaxFood:
				Python.SetScale(self.GetID(), float(float(self.__food) / float(self.__MaxFood)))
				self.__food += self.__foodGrowth * deltaTime
			elif self.__food > self.__MaxFood:
				self.__food = self.__MaxFood
				Python.SetScale(self.GetID(), float(float(self.__food) / float(self.__MaxFood)))
			else:
				rand = random.random()               # between 0.0 and 1.0
				if(rand < deltaTime / (31556926.0 * 2)):      # I want 1 bush every 2 years or so, 31556926 secs
					rand2 = random.random()
					rand3 = random.random()
					rand2 -= 0.5
					rand3 -= 0.5
					newBush = FoodBush(entId, 10, self.GetPosition() + Vector3(rand2, 0, rand3) * 20.0)
					entities.append(newBush)
					entId += 1

		return entId

	def RemoveFood(self, food):
		self.__food -= food
	def AddFood(self, food):
		self.__food += food

	def SetFood(self, food):
		self.__food = food
	def GetFood(self):
		return self.__food

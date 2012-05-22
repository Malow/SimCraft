import Python
from Vector3 import Vector3
from Person import Person
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
		#Python.SetPosition(self.GetID(), self.__Pos.x, self.__Pos.y, self.__Pos.z)

class Wolf(ScriptedEntity):
	__age = 5
	__sex = "male"

	__MovementSpeed = 0.1
	__VisionRange = 50.0
	__HuntingTarget = ScriptedEntity(0, Vector3(0, 0, 0))
	__MovingTarget = Vector3(100, 0, 100)
	__Home = Vector3(100, 0, 100)
	__IsFleeing = False

	__Energy = 2419200.0	# Survives about a month without food when sleeping / idleing
	__MaxEnergy = 2419200.0

	__Fatigue = 0.0
	__IsSleeping = False

	def __init__(self, ID, age, sex, pos):
		ScriptedEntity.__init__(self, ID, pos)
		if sex == "male":
			Python.CreateEntity("Media/WolfMale.obj", ID, pos.x, pos.y, pos.z)
		else:
			Python.CreateEntity("Media/WolfFemale.obj", ID, pos.x, pos.y, pos.z)
		self.__age = age
		self.__sex = sex
		self.__MovingTarget = self.GetPosition()
		self.__Home = self.GetPosition()

	def Update(self, deltaTime, entities, entId):
		self.__age += deltaTime / 31556926.0		  # 1 year
		self.__Energy -= deltaTime
		self.__Fatigue += deltaTime

		if self.__age < 5:
			Python.SetScale(self.GetID(), float(float(self.__age) / 10.0))
		else:
			Python.SetScale(self.GetID(), 1.0)

		if self.__age > 20:
			rand = random.random()			   # between 0.0 and 1.0
			if(rand < deltaTime / (31556926.0 * 3.0)):	  # I want the wolf to die within 3 years on avrage
				entities.remove(self)
				Python.DeleteEntity(self.GetID())

		if self.__Energy < 0.0:			   # Die due to lack of energy from killing stuff
			entities.remove(self)
			Python.DeleteEntity(self.GetID())


		if self.__IsSleeping == True:
			self.__Fatigue -= deltaTime * 3.0
			if self.__Fatigue < 0.0:
				self.__IsSleeping = False

		else:
			entId = self.MoveOrHunt(deltaTime, entities, entId)



		return entId


	def MoveOrHunt(self, deltaTime, entities, entId):
		self.__Energy -= deltaTime  # We're up and moving, use double energy.

		if self.__Fatigue > 43200:		# after 12 hours they need to go back to the den to sleep
			self.__IsFleeing = True
			self.__MovingTarget = self.__Home

		if (self.__IsFleeing == True) or not isinstance(self.__HuntingTarget, Person):
			self.AquireTarget(entities)
			movingVector = self.__MovingTarget - self.GetPosition()
			temp = movingVector
			if movingVector.Length() > 1.0:
				movingVector.Normalize()
				temp = self.GetPosition() + movingVector * (self.__MovementSpeed * deltaTime)
			else:
				temp = self.GetPosition() + movingVector
			self.SetPosition(temp.x, temp.y, temp.z)
			Python.SetPosition(self.GetID(), self.GetPosition().x, self.GetPosition().y, self.GetPosition().z)

			if (self.__MovingTarget - self.GetPosition()).Length() < 2.0:
				self.AquireMovementTarget()
				self.__IsFleeing = False
				if self.__Fatigue > 43200:
					self.__IsSleeping = True


		else:
			self.__Energy -= deltaTime * 2  # We're hunting, use quad energy and double fatigue.
			self.__Fatigue += deltaTime

			self.AquireTarget(entities)
			movingVector = self.__HuntingTarget.GetPosition() - self.GetPosition()
			temp = movingVector
			if movingVector.Length() > 1.0:
				movingVector.Normalize()
				temp = self.GetPosition() + movingVector * (self.__MovementSpeed * deltaTime * 4)   # quad movement speed when hunting human
			else:
				temp = self.GetPosition() + movingVector
			self.SetPosition(temp.x, temp.y, temp.z)
			Python.SetPosition(self.GetID(), self.GetPosition().x, self.GetPosition().y, self.GetPosition().z)
			if (self.__HuntingTarget.GetPosition() - self.GetPosition()).Length() < 2.0:
				entities.remove(self.__HuntingTarget)
				Python.DeleteEntity(self.__HuntingTarget.GetID())
				self.__Energy = self.__MaxEnergy
				self.__MovingTarget = self.__Home
				self.__IsFleeing = True

		return entId



	def AquireTarget(self, entities):
		closestDist = self.__VisionRange
		closestPerson = ScriptedEntity(0, Vector3(0, 0, 0))

		for ent in entities:
			if isinstance(ent, Person):
				distance = (ent.GetPosition() - self.GetPosition()).Length()
				if distance < closestDist:
					closestDist = distance
					closestPerson = ent

		self.__HuntingTarget = closestPerson

	def AquireMovementTarget(self):
		x = random.random()
		z = random.random()
		x *= 200
		z *= 200
		self.__MovingTarget = Vector3(x, 0, z)


	def GetAge(self):
		return self.__age

	def SetAge(self, age):
		self.__age = age

	def GetSex(self):
		return self.__sex

	def SetSex(self, sex):
		self.__sex = sex
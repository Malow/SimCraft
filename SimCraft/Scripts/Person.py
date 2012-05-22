import Python
from Vector3 import Vector3
import math
from FoodBush import FoodBush
import random
from Tree import Tree

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

class Person(ScriptedEntity):
    __age = 0
    __sex = "unknown"

    __walkSpeed = 0.1
    __goingToDo = "Nothing"
    __goingToPos = Vector3(0, 0, 0)
    __home = Vector3(0,0,0)

    __maxSleepTime = 60 * 60 * 8  #sec * min * tim
    __timeUntillSleep =  60 * 60 * 8 #sec * min * tim
    __AwakeSleepMultiplier = 1
    __SleepMultiplier = 3

    __foodMax = 27000
    __foodCollected = 10000
    __foodCollecingSpeed = 12
    __eatingSpeed = 6

    __woodReq = 50000
    __woodCollected = 0
    __woodCollectingSpeed = 5

    def __init__(self, ID, age, sex, pos):
    	ScriptedEntity.__init__(self, ID, pos)
        Python.Debug("Person: " + str(ID))
    	if sex == "male":
    		Python.CreateEntity("Media/HumanMale.obj", ID, pos.x, pos.y, pos.z)
    	else:
    		Python.CreateEntity("Media/HumanFemale.obj", ID, pos.x, pos.y, pos.z)
    	self.__age = age
    	self.__sex = sex
    	if self.__sex == "woman":
    		self.__foodCollecingSpeed *= 1.5
    	self.__home = Vector3(pos.x, pos.y , pos.z)
    	self.__foodCollected = random.randint(5000, 15000)
    	self.__goingToPos = self.__home

    def Update(self, deltaTime, entities, entId):
        if (1 - (self.__foodCollected / self.__foodMax)) > 1: #If a person doesn't get food he/she works slower etc (because they dont get energy)
            self.__woodCollectingSpeed = 3
            self.__foodCollecingSpeed = 9
            self.__SleepMultiplier = 2
            self.__AwakeSleepMultiplier = 2
            self.__eatingSpeed = 3
        else:
            self.__woodCollectingSpeed = 5
            self.__foodCollecingSpeed = 12
            self.__SleepMultiplier = 3
            self.__AwakeSleepMultiplier = 1
            self.__eatingSpeed = 6

        self.UpdateValues(deltaTime)

        if self.__goingToDo == "Sleep":
        	self.Sleeping(deltaTime)
        elif self.__goingToDo == "CollectFood":
        	self.CollectFood(deltaTime, entities, entId)
        elif self.__goingToDo == "GatherWood":
        	self.GatherWood(deltaTime, entities, entId)
        elif self.__goingToDo == "Nothing":
        	self.Nothing(deltaTime)
        #if entId == 4:
        #	tempPerson = Person(entId, 10, "male", Vector3(2, 0, 2))
        #	entities.append(tempPerson)
        #	pos = entities[entId].GetPosition()
        #	Python.CreateEntity("Media/Human.obj", tempPerson.GetID(), pos.x, pos.y, pos.z)
        #	entId += 1
        return entId

    def WalkTo(self, to, deltaTime):
        FromPosToTarget = to - self.GetPosition()
        temp = Vector3(FromPosToTarget.x, 0, FromPosToTarget.z)
        temp.Normalize()
        walkingVec = temp * (self.__walkSpeed * deltaTime)
        #Python.Debug("Short dist: " + str(walkingVec.Length()))
        #Python.Debug("Total dist: " + str(FromPosToTarget.Length()))
        if walkingVec.Length() < FromPosToTarget.Length():
        	newPos = self.GetPosition() + walkingVec
        else:
        	newPos = to

        ScriptedEntity.SetPosition(self, newPos.x, newPos.y, newPos.z)
        Python.SetPosition(self.GetID(), newPos.x, newPos.y, newPos.z)

    def UpdateValues(self, deltaTime):
        if self.__goingToDo == "CollectFood":
        	self.__timeUntillSleep -= deltaTime*self.__AwakeSleepMultiplier
        	self.__foodCollected -= (self.__eatingSpeed * deltaTime)
        elif self.__goingToDo == "Sleep":
        	self.__foodCollected -= ((self.__eatingSpeed / 2) * deltaTime)
        elif self.__goingToDo == "GatherWood":
            self.__timeUntillSleep -= deltaTime*self.__AwakeSleepMultiplier*2
            self.__foodCollected -= ((self.__eatingSpeed * 2) * deltaTime)
        elif self.__goingToDo == "Nothing":
        	self.__timeUntillSleep -= deltaTime*self.__AwakeSleepMultiplier
        	self.__foodCollected -= (self.__eatingSpeed * deltaTime)

    def Sleeping(self, deltaTime):
        self.__goingToPos = self.__home

        if self.GetPosition() == self.__goingToPos:
        	self.__timeUntillSleep += deltaTime * self.__SleepMultiplier
        	if self.__timeUntillSleep > self.__maxSleepTime:
        		self.__goingToDo = "Nothing"
        		if self.__foodCollected > 9000:
        			self.__foodCollected -= (10 * deltaTime)
        		else:
        			self.__foodCollected = 0
        else:
        	self.WalkTo(self.__goingToPos, deltaTime)

    def CollectFood(self, deltaTime, entities, entId):
        Python.Debug("CollectFood: " + str(self.__foodCollected))

        if self.__foodCollected > self.__foodMax:
        		self.__goingToDo = "Nothing"
        		return
        sleepValue = 1 - (math.pow(self.__timeUntillSleep / self.__maxSleepTime, 2))
        if sleepValue > 0.95:
        	self.__goingToDo = "Sleep"

        ######Calculate the closest foodBush
        distToClosest = 99999
        closest = self
        for entity in entities:
            if isinstance(entity, FoodBush):
                dist = (entity.GetPosition() - self.GetPosition()).Length()
                if dist < distToClosest:
                    if entity.GetFood() > (self.__foodCollecingSpeed * deltaTime):
                        distToClosest = dist
                        closest = entity
                    else:
                        #Python.Debug("Deleting: " + str(entity.GetID()))
                        Python.DeleteEntity(entity.GetID())
                        entities.remove(entity)

        self.__goingToPos = closest.GetPosition()
        ###### END
        if self.GetPosition() == self.__goingToPos:
        	if isinstance(closest, FoodBush):
        		closest.RemoveFood(self.__foodCollecingSpeed * deltaTime)
       			self.__foodCollected += (self.__foodCollecingSpeed * deltaTime)

        else:
        	self.WalkTo(self.__goingToPos, deltaTime)

    def GatherWood(self, deltaTime, entities, entId):
        Python.Debug("CollectFood: " + str(self.__woodCollected))
        if self.__woodCollected > self.__woodReq:
        	self.__goingToDo = "Nothing"
        	return
        #See if we need to panic sleep
        sleepValue = 1 - (math.pow(self.__timeUntillSleep / self.__maxSleepTime, 2))
        if sleepValue > 0.95:
        	self.__goingToDo = "Sleep"
        	return
        #See if we need to panic collect food
        if self.__foodCollected != 0:
        	gatherFoodValue = 1 - (self.__foodCollected / self.__foodMax)
        else:
        	gatherFoodValue = 1

        if gatherFoodValue > 0.95:
        	self.__goingToDo = "CollectFood"
        	return

        #Python.Debug("Sleep: " + str(sleepValue))
        #Python.Debug("Food: " + str(gatherFoodValue))
        ######Calculate the closest tree
        distToClosest = 99999
        closest = self
        for entity in entities:
            if isinstance(entity, Tree):
                dist = (entity.GetPosition() - self.GetPosition()).Length()
                if dist < distToClosest:
                    if entity.GetWood() > (self.__woodCollectingSpeed * deltaTime):
                        distToClosest = dist
                        closest = entity
                    else:
                        #Python.Debug("Deleting: " + str(entity.GetID()))
                        Python.DeleteEntity(entity.GetID())
                        entities.remove(entity)

        self.__goingToPos = closest.GetPosition()
        if self.__goingToPos == self.GetPosition():
        	return
        ###### END
        if self.GetPosition() == self.__goingToPos:
        	if isinstance(closest, Tree):
        		closest.RemoveWood(self.__woodCollectingSpeed * deltaTime)
       			self.__woodCollected += (self.__woodCollectingSpeed * deltaTime)
        else:
        	self.WalkTo(self.__goingToPos, deltaTime)

    def Nothing(self, deltaTime):
        Python.Debug("Nothing")
        random.seed(random.random())
        if self.GetPosition() == self.__goingToPos: #temp to see when its here
        	#Python.Debug("Im here")
        	self.__goingToPos += Vector3(random.randint(-5, 5), 0, random.randint(-5, 5))
        	if self.__goingToPos.x > self.__home.x + 10:
        		self.__goingToPos.x = self.__home.x
        	if self.__goingToPos.x < self.__home.x - 10:
        		self.__goingToPos.x = self.__home.x

        	if self.__goingToPos.z > self.__home.z + 10:
        		self.__goingToPos.z = self.__home.z
        	if self.__goingToPos.z < self.__home.z - 10:
        		self.__goingToPos.z = self.__home.z
        else:
        	self.WalkTo(self.__goingToPos, deltaTime)


        sleepValue = 1 - (math.pow(self.__timeUntillSleep / self.__maxSleepTime, 2))
        if self.__foodCollected != 0:
        	gatherFoodValue = 1 - (self.__foodCollected / self.__foodMax)
        else:
        	gatherFoodValue = 1

        Python.Debug("Sleep Value: " + str(sleepValue))
        Python.Debug("Gather Value: " + str(gatherFoodValue))

        if sleepValue > 0.8:
        	self.__goingToDo = "Sleep"
        elif gatherFoodValue > 0.8:
        	self.__goingToDo = "CollectFood"
        elif self.__woodCollected < self.__woodReq:
        	self.__goingToDo = "GatherWood"
        else:
        	self.__goingToDo = "Nothing"

	def GetAge(self):
		return self.__age

	def SetAge(self, age):
		self.__age = age

	def GetSex(self):
		return self.__sex

	def SetSex(self, sex):
		self.__sex = sex
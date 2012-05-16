import math

class Vector3():
	x = 0
	y = 0
	z = 0
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def __add__(self, other):
		return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
		
	def __sub__(self, other):
		return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
		
	def __mul__(self, other):
		return Vector3(self.x * other, self.y * other, self.z * other)
		
	def __div__(self, other):
		return Vector3(self.x / other, self.y / other, self.z / other)
		
	def __eq__(self, other):
		if self.x == other.x:
			if self.y == other.y:
				if self.z == other.z:
					return 1 == 1
		return 1 == 2
	
	def Length(self):
		return math.fabs(math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2)))
		
	def Normalize(self):
		length = self.Length()
		
		if length > 0:
			self.x /= length
			self.y /= length
			self.y /= length
			self.y /= length
			self.z /= length
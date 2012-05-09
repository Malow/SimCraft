import math

class Vector3():
	__x = 0
	__y = 0
	__z = 0
	def __init__(self, __x, __y, __z):
		self.__x = __x
		self.__y = __y
		self.__z = __z
	
	def __add__(self, other):
		return Vector3(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)
		
	def __sub__(self, other):
		return Vector3(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)
		
	def __mul__(self, other):
		return Vector3(self._ * other, self.__y * other, self.__z * other)
		
	def __eq__(self, other):
		if self.__x == other.__x:
			if self.__y == other.__y:
				if self.__z == other.__z:
					return 1 == 1
		return 1 == 2
	
	def Length(self):
		return math.sqrt(math.pow(self.__x, 2) + math.pow(self.__y, 2) + math.pow(self.__z, 2))
		
	def Normali__ze(self):
		length = self.Length()
		
		if length > 0:
			self.__x /= length
			self.__y /= length
			self.__z /= length
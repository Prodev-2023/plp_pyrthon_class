class Person:
	
	def __init__(self, name, age, gender):
		self.name = name;
		self.age = age;
		self.gender = gender;
		
	def introduce(self):
		print(f"Hi my name is {self.name}  and i am {self.age} years old and my gender is {self.gender}");
		
person1 = Person('paul',28,"male");

person1.introduce()
class Character(object):
	health = 100



class Spells(Character):
	def Fireball(self):
		print "Casts a fireball"



x = Character
y = Blacksmith


y.health = 130
print "Y health is " + str(y.health)
print "X health is " + str(x.health)
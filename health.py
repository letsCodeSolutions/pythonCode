import random
health = 50
difficulty = 1
portion_health = random.randrange(25,50)/2

health = int(health + portion_health)

print(portion_health)

print(health)

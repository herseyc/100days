################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
  #Enemies is not returned out of the function

increase_enemies()
#Since the increase in enemies is not returned enemies is still one.
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
  potion_strenght = 2
  print(potion_strenght)

drink_potion()

# Global Scope
player_health = 10

def drink_potion2():
  potion_strenght = 2
  print(player_health)

drink_potion2()

def game():
  def drink_potion2():
    potion_strenght = 2
    print(player_health)
  drink_potion2()

game()

# There is no Block Scope in Python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)


# Modifying Global Scope
enemies = 1

def increase_enemies2():
  global enemies
  # Modifying globals in a function is not the best thing to do better to return and modify outside the function
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies2()

# Global Constants
# Upper case variable
PI = 3.14159
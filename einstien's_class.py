# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


def f_to_c(f_temp):
  return (f_temp - 32) * 5/9
#Fahrenheit to Celsius  
f100_in_celsius = f_to_c(100)
print("Fahrenheit to Celsius:", round(f100_in_celsius,1), "degrees")


def c_to_f(c_temp):
  return (c_temp) * (9/5) + 32
#Celsius to Fahrenheit  
c0_in_fahrenheit = c_to_f(0)
print("Celsius to Farhenheit:", round(c0_in_fahrenheit,1), "degrees")


def get_force(mass,acceleration):
  force = mass * acceleration
  return force
#Force of Train:
train_force = get_force(train_mass,train_acceleration)
print("Train Force:", train_force)
print("The GE train supplies",  str(train_force) ,  "Newtons of force")

#Energy of Bomb
c =  3*10**8
def get_energy(mass,c):
  get_energy = mass * c**2
  return get_energy

bomb_energy = get_energy(bomb_mass,c)
print("A 1kg bomb supplies",  bomb_energy, " Joules.")

#Work done by Train
def get_work(mass,acceleration,distance):
   force = get_force(mass,acceleration)
   return force * distance

train_work = get_work(train_mass, train_acceleration,train_distance)
print( "The GE train does", str(train_work), "Joules of work over", str(train_distance), "meters.")


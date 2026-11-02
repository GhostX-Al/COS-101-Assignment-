# COS 101 ASSIGNMENT
# Five Physics Formulas
# Name: Your Name

# 1. Speed = Distance / Time
def speed(distance, time):
    return distance / time


# 2. Force = Mass * Acceleration
def force(mass, acceleration):
    return mass * acceleration


# 3. Density = Mass / Volume
def density(mass, volume):
    return mass / volume


# 4. Work Done = Force * Distance
def work_done(force, distance):
    return force * distance


# 5. Weight = Mass * Gravity
def weight(mass, gravity=9.8):
    return mass * gravity


# Display results
print("PHYSICS FORMULAS")

print("Speed:", speed(100, 20), "m/s")
print("Force:", force(10, 5), "N")
print("Density:", density(50, 10), "kg/m³")
print("Work Done:", work_done(20, 5), "J")
print("Weight:", weight(10), "N")
# Get inputs from the user
m = int(input("Enter DOF of a single body (m): "))
N = int(input("Enter number of bodies (N): "))
j1 = int(input("Enter number of joints with 1 DOF: "))
j2 = int(input("Enter number of joints with 2 DOF: "))
j3 = int(input("Enter number of joints with 3 DOF: "))

# Apply Gruebler's formula
DOF = m * (N - 1) - ((m - 1) * j1 + (m - 2) * j2 + (m - 3) * j3)

# Print the result
print("Degrees of Freedom (DOF) of the mechanism is:", DOF)

Ku = 1.06
Pu = 2.5

print(f"Controlador P 	--> Kp = {0.50*Ku}")
print(f"Controlador PI 	--> Kp = {0.45*Ku} Ti = {Pu/1.2}")
print(f"Controlador PID --> Kp = {0.60*Ku} Ti = {Pu/2.0} Td = {Pu/8}")
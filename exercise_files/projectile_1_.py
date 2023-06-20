from math import pi, tan, cos

g = 9.81
# g= acceleration due to gravity: 9.81 (m/s squared)
vo = 44
# v0= the initial velocity (m/s)
x = 0.5
# x= the horizontal distance travelled
yo = 1
# y0 = height of the barrel (m)
theta = 80 * pi/180
# theta = degrees to radians

y = yo + x*tan(theta) - (g*x**2)/(2*((vo * cos(theta))**2))

print('Height of projectile:', y, 'm')
# prints the value of y

print('The height of projectile to two decimal places is:', end="")
print(round(y, 2))
# prints value of y to two decimal places using round ('', 2)
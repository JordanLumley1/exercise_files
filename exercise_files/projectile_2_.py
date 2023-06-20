from math import pi, tan, cos

g = 9.81

vo = input('What is the initial velocity? (m/s):')
vo = float(vo)
# float() converts string into floating point number allowing decimals.

x = input('What is the horizontal distance travelled? (m):')
x = float(x)

yo = input('what is the height of the barrel? (m):')
yo = float(yo)

e = input('What is the elevation? (deg):')
e = float(e)

theta = e * pi/180


y = yo + x*tan(theta) - (g*x**2)/(2*((vo * cos(theta))**2))

print('Height of projectile:', y, 'm')

print('The height of projectile to two decimal places is:', end="")
print(str(round(y, 2)) + 'm')
# prints value of y to two decimal places using round ('', 2)

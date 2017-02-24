# projectile motion "simulation"
import sys
import math

def degrees_to_radians( degrees ):
	#radians = degrees
	#radians *= math.pi
	#radians /= 180
	#return radians
	return degrees * math.pi / 180

def radians_to_degrees( radians ):
	return radians * 180 / math.pi


i = 0

time_step = 0.1 # seconds
velocity = 0 # feet/second
angle_degrees = 0 # degrees

g = 32.0 # ft/sec^2 -- The acceleration of gravity at or near the Earth's surface

i = 0
for arg in sys.argv:
	print "argv[" , i , "] = " + sys.argv[i] ; 
	i += 1

print ""

for i in range( 1, len(sys.argv)-1 ):
	if sys.argv[i] == "-ts": 
		i += 1;
		time_step = float(sys.argv[i])
	elif sys.argv[i] == "-angle": 
		i += 1;
		angle_degrees = float(sys.argv[i])
	elif sys.argv[i] == "-velocity": 
		i += 1;
		velocity = float(sys.argv[i])

print "time_step = ", time_step, " seconds" 
print "angle_degrees = ", angle_degrees, " degrees"
print "type(angle_degrees) = ", type(angle_degrees)
print "velocity = ", velocity, " feet/second"

angle_radians = degrees_to_radians( angle_degrees )
print "angle_radians = ", angle_radians, " radians"

vy0 = velocity * math.sin( angle_radians )
vx0 = velocity * math.cos( angle_radians )

print "vx0 = ", vx0, " feet/second"
print "vy0 = ", vy0, " feet/second"

vy = vy0
vx = vx0
y = 0.0
x = 0.0
t = 0.0

i_count = 0
i_max_count = 1000

print "N","\t","t","\t","x","\t","y","\t","vx","\t","vy"

while True:  
	i_count += 1


	# v_y(t) = v_y_0 - gt
	vy = vy0 - g * t;

	y = (vy0 * t) - (0.5 * g * t * t);

	x = vx * t;
	
	print i_count,"\t",t,"\t",x,"\t",y,"\t",vx,"\t",vy

	if y < 0:
		break
	#elif i_count > i_max_count:
	#	break

	t += time_step




from modulephytong import *
from time import sleep



#----------------------------------------------------------------------------------------------------------------------
def semaforo(x,y,radio):
	for i in range(10):
		if x==234:
			create_text(100,250,´Luz Verde Avanza´,16,´SW´,´green´,tags=´texto´)
	    		create_filled_circle(x,y,radio,´green´)
	   		sleep(10)
	  	for i in range(0,10):
	     		create_filled_circle(x,y,radio,´black´)
	     		sleep(0.5)
	     		create_filled_circle(x,y,radio,´green´,tags=´borra´)
	     		sleep(0.5)
	 		erase(´texto´)
	 		erase(´borra´)
	 		create_circle(x,y,radio,´green´)

		if x==500:
	  		create_text(300,250,´Luz Amarilla Preventivo´,16,´SW´,´yellow´,tags=´texto´)
	   	 	create_filled_circle(x,y,radio,´yellow´,tags=´borra2´)
	    		sleep(6)
	    		erase(´texto2´)
	    		erase(´borra2´)
	    		create_circle(x,y,radio,´yellow´)

	if x==766:
	    create_text(500,250,´Luz Roja Alto Total´,16,´SW´,´red´,tags=´texto´)
	    create_filled_circle(x,y,radio,´yellow´,tags=´borra3´)
	    sleep(10)
	    erase(´texto3´)
	    erase(´borra3´)
	    create_circle(x,y,radio,´red´)
	x+=266
	if x>766:
	   x=234
#----------------------------------------------------------------------------------------------------------------------
create_rectangle(90,350,910,650,´white´)
create_rectangle(20,0,40,500,´white´)
create_rectangle(20,500,90,520,´white´)
create_rectangle(80,50,900,150,´white´)

color=[´green´,´yellow´,´red´]
x=234
y=500
radio=130

for i in range(3):
    create_circle(x,y,radio,color[i])
    x+=266

for i in range(40):
    sleep(0.2)
    move(´mueve´,1,20)
    move(´recta´,1,20)

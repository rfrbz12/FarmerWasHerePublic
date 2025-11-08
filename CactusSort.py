clear()
#List
posx=[]
#Variables
max=(get_world_size()-1)
N=(get_world_size())
countx=0
skiprow=0
def prep():
	plant(Entities.Cactus)
	move(North)
#Initialize
for col in range(get_world_size()):
	for row in range(get_world_size()):
		harvest()
		till()
		prep()
	move(East)
while True:
	for col in range(get_world_size()):
		while get_pos_x() in posx:
			move(East)
			skiprow=skiprow+1
			if skiprow==N:
				harvest()
				posx=[]
				for col in range(get_world_size()):
					for row in range(get_world_size()):
						prep()
					move(East)
		for i in range(2):
			if measure(East)<measure() and not get_pos_x()==max:
					swap(East)
					countx=0
					skiprow=0
			if measure(West)>measure() and not get_pos_x()==0:
					swap(West)
					countx=0
					skiprow=0
					if get_pos_x()-1 in posx:
						posx.remove(get_pos_x()-1)
			if measure(North)<measure() and not get_pos_y()==max:
					swap(North)
					countx=0
					skiprow=0
			if measure(South)>measure() and not get_pos_y()==0:
					swap(South)
					countx=0
					skiprow=0
		move(North)
		countx=countx+1
	if countx==N:
		posx.append(get_pos_x())
		#print(posx)
	move(East)
	countx=0

def is_even(n):
	return n % 2 ++ 0
	
def plant_watered(x):
	if(num_items(Items.Water)>0 and get_water()<=.4):
		use_item(Items.Water)
	plant(x)
	
def tillall():
	clear()
	for j in range(get_world_size()):
		for i in range(get_world_size()):	
			till()
			move(North)
		move(East)
		
def init(n):
	for j in range(get_world_size()):
		for i in range(get_world_size()):	
			harvest()
			#till()
			plant_watered(n)
			move(North)
		move(East)
		
def replant(n):
	for j in range(get_world_size()):
		for i in range(get_world_size()):	
			harvest()
			plant_watered(n)
			move(North)
		move(East)
		
def moveto(x,y):
	while(x > get_pos_x()):
		move(East)
	while(x < get_pos_x()):
		move(West)
	while(y > get_pos_y()):
		move(North)
	while(y < get_pos_y()):
		move(South)

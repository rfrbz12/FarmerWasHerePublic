import Functions

# -----------------------------------
# DETERMINISTIC SEED GENERATOR (ROLL-OVER ENABLED)
# -----------------------------------
# Creates a fixed seed pattern for the grid using coordinate math.
# Plants cactus values 1–9 in a pseudo-normal distribution.
# The drone rolls over edges to minimize travel.
# -----------------------------------

N = get_world_size()
seed = []


# -----------------------------------
# FUNCTION: seed_value(x, y)
# -----------------------------------
# Purpose:
#   Generate a deterministic pseudo-random value (1–9)
#   based on (x, y) coordinates.
#   Middle values (4–6) appear more often for a "normal" spread.
# -----------------------------------
def seed_value(x, y):
	s1 = (x * 73 + y * 151 + 97) % 5
	s2 = (y * 89 + x * 167 + 53) % 5

	a = s1 + 1   # 1–5
	b = s2 + 1   # 1–5
	val = a + b - 1   # 1–9 range, mid-biased

	if val < 1:
		val = 1
	if val > 9:
		val = 9

	return val


# -----------------------------------
# FUNCTION: build_seed()
# -----------------------------------
# Purpose:
#   Build a full N×N seed[] grid deterministically.
#   Each entry corresponds to seed[y*N + x].
# -----------------------------------
def build_seed():
	global seed
	seed = []
	for y in range(N):
		for x in range(N):
			seed.append(seed_value(x, y))


# -----------------------------------
# FUNCTION: plant_seed()
# -----------------------------------
# Purpose:
#   Plant the generated seed pattern onto the real grid.
#   The drone rolls over automatically at grid edges.
# -----------------------------------
def plant_seed():
	for y in range(N):
		for x in range(N):
			index = y * N + x
			if index >= len(seed):
				break

			# Move to coordinate
			Functions.moveto(x, y)

			# Target cactus value
			target = seed[index]
			current = measure()

			# Replant until match
			for attempt in range(50):
				if current == target:
					break
				harvest()
				plant(Entities.Cactus)
				current = measure()

		# Roll over horizontally after finishing a row
		move(East)

	# After last tile, roll automatically wraps to start (0,0)
	move(East)


# -----------------------------------
# MAIN PROGRAM
# -----------------------------------

# 1. Clear and till world
#clear()
#Functions.tillall()

# 2. Build deterministic seed pattern
build_seed()

# 3. Apply pattern to field with rollover movement
plant_seed()

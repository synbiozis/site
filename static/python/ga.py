from random import randrange, choice

class population:

	# Initialisation
	def __init__(self, size=50, mut=15, toursize=5):
		self.pop = [self.generate() for i in range(size)]
		self.mut = mut
		self.toursize = toursize
		self.sol = "1111000000000000000000111100000000000000000000000000000000001111"

	# Evolve population
	def evolve(self):

		newPop = population(len(self))

		for i in range(len(self)):
			parents = (self.tourn(), self.tourn())
			newIndi = self.crossover(*parents)
			newPop[i] = self.mutate(newIndi)

		self.pop = newPop.pop
		# Shorter : self.pop = [self.mutate(self.crossover(self.tourn(), self.tourn())) for _ in range(len(self))]

	# Population methods
	def tourn(self):
		new = population(self.toursize)
		for i in range(self.toursize):
			 new[i] = choice(self)
		return new.getFittest()

	def crossover(self, j, k):
		return [choice([j[i], k[i]]) for i in range(len(j))]

	def mutate(self, val):
		return [choice(['0', '1']) if randrange(1000) <= self.mut else val[i] for i in range(len(val))]

	def generate(self, size=64):
		return [choice(['0', '1']) for i in range(size)]

	def getMaxFit(self):
		return len(self[0])

	# Fitness calc
	def getFittest(self):
		fit = self[0]
		val = self.getFitness(fit)
		for i in range(len(self)):
			if self.getFitness(self[i]) > val:
				fit = self[i]
				val = self.getFitness(self[i])

		return fit
		# Shorter : return sorted([(self.getFitness(indi), indi) for indi in self])[-1][1]


	def getFitness(self, val):
		fitness = 0
		for i in range(len(val)):
			if str(val[i]) == self.sol[i]:
				fitness += 1

		return fitness
        # Shorter : return len([1 for (index, value) in enumerate(val) if str(value) == self.sol[index]])

	# Specials methods
	def __getitem__(self, i):
		return self.pop[i]

	def __setitem__(self, i, val):
		self.pop[i] = val

	def __len__(self):
		return len(self.pop)


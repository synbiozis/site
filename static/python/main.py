#!usr/bin/python
#coding: UTF-8

from time import time

from pop import population

pop = population()

print 'population start with a fittest of', pop.getFitness(pop.getFittest())

gen = 1
vals = []

fitness = 0
popMax = pop.getMaxFit()

while fitness < popMax:
	start = time()
	fittest = pop.getFittest()
	fitness = pop.getFitness(fittest)
	print 'Generation', gen, ': fittest =', fitness
	pop.evolve()
	gen += 1
	vals.append(time() - start)

print "\nFind solution in", sum(vals), "s."
print "Average time for a generation :", sum(vals) / len(vals), "s."
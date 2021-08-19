import math
import os
import random
from collections import defaultdict

def euc_2d(c1,c2):
   return  math.sqrt((c1[0] - c2[0])**2.0 + (c1[1] - c2[1])**2.0).__round__()

def cost(perm, cities):
   distance = 0
   index = 0
   for element in perm:
      c1 =  perm[index]
      c2 = perm[0] if (index == len(perm) -1) else perm[index+1]
      index+=1
      distance += euc_2d(cities.index(c1), cities.index(c2))
   return distance

def random_permutation(cities):
   perm =[]
   for elements in cities:
      perm.append(cities.__getitem__(cities.index(elements)))
   for elem in perm:
      index  = perm.index(elem)
      r = random.randrange(len(perm) - index) + index
      aux = perm[r]
      perm[r] =  perm[index]
      perm[index] = aux

   return perm

def stochastic_two_opt_2(perm):
   c1 = random.randrange(len(perm.keys()))
   c2 =  random.randrange(len(perm.keys()))
   exclude = []
   first_element =  len(perm.keys())-1 if c1 ==0 else c1 -1
   second_element = 0 if c1 == len(perm.keys()) -1 else c1+1
   exclude.append(first_element)
   exclude.append(second_element)
   c2 =  random.randrange(len(perm.keys()))
   while c2 in exclude:
      if c2 < c1:
         aux = c1
         c1 =c2
         c2 = c1
      for a in range(c1, c2):
         aux = perm[c1]
         perm[c1] = perm[c2]
         perm[c2] = aux

      return perm

def local_search(best, cities, max_no_improv, neighborhood):
   count = 0
   while(count <= max_no_improv):
      candidate = {"vector": None, "cost": None, "best": None}
      candidate["vector"] = []
      for elements in neighborhood:
         candidate["vector"] =  stochastic_two_opt_2(candidate)
      candidate["cost"] = cost(candidate.get("vector"), cities)
      if candidate.get("cost") < best.get("cost"):
         count = 0
         best =  candidate
      else:
         count+=1
   return best

def search(cities, neighborhoods, max_no_improv, max_no_improv_ls):
   best = {"vector": random_permutation(cities), "cost": None}
   best['cost'] = cost(best.get("vector"), cities)
   iter, count, p1, p2 = 0, 0, 0, 0
   while(count <= max_no_improv):

      while(p1 < neighborhoods):
         candidate = {"vector": None}
         candidate["vector"] = best.get("vector")
         while(p2 < neighborhoods):
            candidate["vector"] = stochastic_two_opt_2(candidate)
            p2+=1
         candidate["cost"] = cost(candidate.get("vector"), cities)
         candidate = local_search(candidate, cities, max_no_improv_ls, len(neighborhoods))
         pr = f'interation : {iter+1}, neigh = {len(neighborhoods)}, best={best.get("cost")}'
         print(pr)
         iter+=1
         if(candidate.get("cost") < best.get("cost")):
            best = candidate
            count = 0
            print("New best, restarting neighborhood search")
         else:
            count += 1
         p1+=1
   return best

berlin52 = [[565,575],[25,185],[345,750],[945,685],[845,655],
   [880,660],[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
   [1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
   [415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
   [835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
   [410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
   [685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
   [95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
   [830,610],[605,625],[595,360],[1340,725],[1740,245]]

max_no_improv = 50
max_no_improv_ls = 70
neighborhoods = random.randrange(1,20)
best = search(berlin52, neighborhoods, max_no_improv, max_no_improv_ls)
print(best)





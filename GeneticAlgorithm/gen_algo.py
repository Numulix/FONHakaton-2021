from Earthquake import Earthquake
import random
from Population import Population

poplutaion =[]
eartuquakes=[]
distribution=[]
proffesionals=1000
pepole_need_for_place=[]
list_of_bests=[]
max_iter=100
richter=10

def mutate(distrb,rate):
    prof=proffesionals
    if random.random() < rate:
        for i in range(len(distrb)):
            distrb[i] = random.randint(distrb[i]+(distrb[i]/2),prof)
            prof-=distrb[i]
    return distrb

def generate_popultaion(num_pop):
    for i in range(num_pop):
        density_of_population=random.uniform(1,100)
        poplutaion.append(Population(density_of_population))

def genterate_earthquakes(num_earthquakes):
    for i in range(num_earthquakes):
        longitude=random.uniform(1,100)
        latitude=random.uniform(1,100)
        magnitude=random.randint(0,10)
        area=random.uniform(1,50)
        eartuquakes.append(Earthquake(longitude,latitude,magnitude,area))

def generate_data():
    generate_popultaion(5)
    genterate_earthquakes(5)


def number_of_people_needed_for_place():
    global pepole_need_for_place
    for i in range(len(eartuquakes)):
        pepole_need_for_place.append(round((poplutaion[i].density_of_population*eartuquakes[i].area)/(richter-eartuquakes[i].magnitude+1)))

def fitness_function(distrb):
    loss=0
    for i in range(len(distrb)):
        loss+=(pepole_need_for_place[i]-distrb[i])**2
    return loss

def selection_tournament(population, size):
      competition_list = []
      while len(competition_list) < size:
          competition_list.append(random.choice(population))
      best_chromosome = None
      best_function_value = None
      for selected in competition_list:
          selected_value = fitness_function(selected)
          if best_chromosome is None or selected_value < best_function_value:
              best_function_value = selected_value
              best_chromosome = selected
      return best_chromosome


    #
def crossover(h1, h2):
    return heuristic_crossover(h1,h2)

def heuristic_crossover(h1,h2):
    l = [[], []]
    prof=proffesionals
    for i in range(len(l)):
      r=random.uniform(0.0, 1.0)
      for j in range(len(h1)):
          val=round(r*(h1[i]-h2[i])+h1[i])
          new_mutated_cordinate=random.randint(val,prof)
          prof-=new_mutated_cordinate
          l[i].append(new_mutated_cordinate)
    return l


def make_population(num_of_places):
    prof=proffesionals
    example_of_distrbution=[]
    for i in range(num_of_places):
        print(prof,pepole_need_for_place[i])
        p=random.randint(0,min(prof,pepole_need_for_place[i]))
        print(p)
        example_of_distrbution.append(p)
        prof-=p
    return example_of_distrbution

def make_examples_of_population():
    for i in range(10):
        distribution.append(make_population(len(eartuquakes)))

def genetic_algorithm():
    best = None
    best_f = None
    t=0
    global distribution
    generate_data()
    number_of_people_needed_for_place()
    make_examples_of_population()
    while t < max_iter or best_f!=0:
        n_distribution = distribution[:]
        added=0
        while added < 100:
            h1 = selection_tournament(distribution, 3)
            h2 = selection_tournament(distribution, 3)
            if fitness_function(h2) < fitness_function(h1):
                tmp=h1
                h1=h2
                h2=tmp
            h3, h4 = crossover(h1, h2)
            mutate(h3, 0.5)
            mutate(h4,0.5)
            n_distribution.append(h3)
            n_distribution.append(h4)
            added+=1
        distribution = sorted(n_distribution, key=lambda x: fitness_function(x))[:added]
        f = fitness_function(distribution[0])
        added+=1
        print(distribution[0])
        if best is None or best_f > f:
            best = distribution[0]
            best_f = f
        t+=1

def genetic_algorithm_driver():
   genetic_algorithm()

genetic_algorithm_driver()


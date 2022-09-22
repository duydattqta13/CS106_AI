from ortools.linear_solver import pywraplp
from ortools.algorithms import pywrapknapsack_solver
import seaborn as sns
import matplotlib.pyplot as plt
import time
import data
def main():
	inp = data.input_data()
	
	check_point = 0

	for name in range(check_point, len(inp)):
    		
		#Declare time
		start = time.time()
		elapsed = 0
		print('File name: ' + inp[name])
		print('Package number: ' + str(name))
		with open(inp[name] + ".kp") as level_file:
			rows = level_file.read().split('\n')
		
		number_items = (int)(rows[1])
		capacities = [(int)(rows[2])]
		values = []
		weights = [[]]
		for i in range(4, number_items + 5 - 1):
			x = rows[i].split(" ")[0]
			y = rows[i].split(" ")[1]
			values.append((int)(x))
			weights[0].append((int)(y))
			

		solver = pywrapknapsack_solver.KnapsackSolver(
			pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')


		#time limit = seconds ------ 3 minutes = 180 seconds
		solver.set_time_limit(180)

		solver.Init(values, weights, capacities)
		computed_value = solver.Solve()

		packed_items = []
		packed_weights = []
		total_weight = 0
		for i in range(len(values)):
			if solver.BestSolutionContains(i):
				packed_items.append(i)	
				packed_weights.append(weights[0][i])
				total_weight += weights[0][i]

		elapsed = time.time() - start

		with open("output/Google-OR-Tools/" + "test " + str(name) + ".txt", 'w+') as solver_file:
			solver_file.write('File name: {}.kp\n'.format(inp[name]))
			solver_file.write('Execution time: {} sec\n'.format(elapsed))
			solver_file.write('Capacity = {} \n'.format(str(capacities[0])))
			solver_file.write('Total weight = {} \n'.format(str(total_weight)))
			solver_file.write('Total value = {} \n'.format(computed_value))
			solver_file.write('Number of items: {} \n'.format(str(len(packed_items))))
			solver_file.write('Packed items: {} \n'.format(packed_items))
			solver_file.write('Packed weights: {}'.format(len(packed_items)))

		print('Execution time: ' + str(elapsed))
		print()

if __name__ == '__main__':
	main()
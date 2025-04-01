import cma
import opensim as osim
import sys
import math
import numpy as np

KNOTS = 3
solution_file = 'sol.txt'

def simfunc(params, viz=False):
		
	model_filename = 'gait9dof18musc_Thelen_BigSpheres_20160914.osim'

	model = osim.Model(model_filename)
	init_state = [0, 2.0, 1.02, 0, 0, 0, 0, 0, 0, 0]
	stepsize = 0.005;
	nbr_timesteps = 200;

	state = model.initSystem()
	muscleController = osim.PrescribedController();
	muscleSet = model.getMuscles();
	nbr_muscles = muscleSet.getSize();

	#if viz:
	#	model.setUseVisualizer(True)

	state = model.initSystem()
	editableCoordSet = model.updCoordinateSet();

	for i in range(0,editableCoordSet.getSize()-1):
		editableCoordSet.get(i).setValue(state, init_state[i])

	manager = osim.Manager(model)
	manager.initialize(state)

	f = 0;

	total_time = stepsize * nbr_timesteps;

	for i in range(0,nbr_timesteps+1):
		t = (i+1) * stepsize
		state = manager.integrate(t)
		phase = min(math.floor((t*KNOTS)/total_time),KNOTS-1)

		for j in range(0,nbr_muscles):
			muscleSet.get(j).setActivation(state, params[phase*nbr_muscles+j]);

		model.realizeDynamics(state);
		com = model.calcMassCenterPosition(state);
		
		# TODO: change one thing in the line below to encourage the character to stay upright.
		f = f + com.get(0);

		# TODO: if you wanted the character to have its right toe as high as possible,
		# what cost function term could you add after the line below:
		toes_r = model.getBodySet().get("toes_r").getTransformInGround(state).p()
	
	if viz:
		statesDegrees = manager.getStateStorage();
		statesDegrees.printToFile("optSimulation.sto", "w");

	f = -1 * f;
	print(f)
	return f


def parallel_func():
	import multiprocessing as mp
	# TODO: you could try changing maxiter and popsize
	es = cma.CMAEvolutionStrategy(KNOTS*18 * [0], 0.3, {'maxiter':8, 'popsize':8})
	pool = mp.Pool(es.popsize)
	while not es.stop():
		X = es.ask()
		f_values = pool.map_async(simfunc, X).get()
		es.tell(X, f_values)
	simfunc(es.result[0], True)
	np.savetxt(solution_file, es.result[0])


def replay_solution():
	sol = np.loadtxt(solution_file)
	simfunc(sol, True)

if __name__ == '__main__':	
	parallel_func()
	#replay_solution()




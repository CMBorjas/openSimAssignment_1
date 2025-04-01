import opensim as osim
import sys
import math



model_filename = 'gait9dof18musc_Thelen_BigSpheres_20160914.osim'

model = osim.Model(model_filename)
model.setUseVisualizer(True)

state = model.initSystem()

editableCoordSet = model.updCoordinateSet();
deg_to_rad = math.radians 

init_state = [
	0.0, 		#pelvis_tilt 
	0.0, 		#pelvis_tx
	0.6,		#pelvis_ty 
	deg_to_rad(119), 		#hip_flexion_r
	deg_to_rad(-119), 		#knee_angle_r
	0.0, 		#ankle_angle_r
	deg_to_rad(119), 		#hip_flexion_l
	deg_to_rad(-119), 		#knee_angle_l
	0.0,		#ankle_angle_l
	0.0		# lumbar_extension
	]

for i in range(editableCoordSet.getSize()):
	coord = editableCoordSet.get(i)
	print(f"{i}: {coord.getName()} (default={coord.getDefaultValue()})")


for i in range(0,editableCoordSet.getSize()):
	editableCoordSet.get(i).setValue(state, init_state[i])

manager = osim.Manager(model)
finalTime = 5
manager.initialize(state)
manager.integrate(finalTime)


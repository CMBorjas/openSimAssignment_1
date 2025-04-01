import opensim as osim
import math

# Load model
model = osim.Model("gait9dof18musc_Thelen_BigSpheres_20160914.osim")
model.setUseVisualizer(True)

# Clear built-in controllers to allow pure dynamics
model.updControllerSet().clearAndDestroy()
model.finalizeConnections()

# Initialize system
state = model.initSystem()

# Set crouched pose (in radians)
deg = math.radians
crouch_pose = {
    'pelvis_tx': 0.0,
    'pelvis_ty': 0.4,           # lower pelvis to ensure feet touch floor
    'pelvis_tilt': -0.29,
    'hip_flexion_r': deg(119),
    'knee_angle_r': deg(-119),
    'ankle_angle_r': deg(30.0),
    'hip_flexion_l': deg(119),
    'knee_angle_l': deg(-119),
    'ankle_angle_l': deg(30)
}

coord_set = model.updCoordinateSet()
for i in range(coord_set.getSize()):
    coord = coord_set.get(i)
    name = coord.getName()
    if name in crouch_pose:
        coord.setValue(state, crouch_pose[name])
        coord.setSpeedValue(state, 0.0)

# Realize full model state
model.realizeAcceleration(state)

# Run forward simulation
manager = osim.Manager(model)
manager.initialize(state)
final_time = 5.0
state = manager.integrate(final_time)

# Save result
manager.getStateStorage().printToFile("crouched_fall.sto", "w")

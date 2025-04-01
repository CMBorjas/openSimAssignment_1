import opensim as osim
import math

# Load model
model = osim.Model('gait9dof18musc_Thelen_BigSpheres_20160914.osim')
model.setUseVisualizer(True)

# Disable all controllers that may interfere
model.updControllerSet().clearAndDestroy()
model.finalizeConnections()

# Initialize system
state = model.initSystem()

deg_to_rad = math.radians
init_state = {
    'pelvis_tilt': 0.0,
    'pelvis_tx': 0.0,
    'pelvis_ty': 0.4,                  # lowered pelvis to avoid floating
    'hip_flexion_r': deg_to_rad(200),
    'knee_angle_r': deg_to_rad(-200),
    'ankle_angle_r': 0.0,
    'hip_flexion_l': deg_to_rad(200),
    'knee_angle_l': deg_to_rad(-200),
    'ankle_angle_l': 0.0
}
# Apply the pose
coord_set = model.updCoordinateSet()
for i in range(coord_set.getSize()):
    coord = coord_set.get(i)
    name = coord.getName()
    if name in init_state:
        coord.setValue(state, init_state[name])
        coord.setSpeedValue(state, 0)

# Re-realize the model's state
model.realizeVelocity(state)
model.realizeAcceleration(state)

# Run the forward simulation for 5 seconds
final_time = 5.0
manager = osim.Manager(model)
manager.initialize(state)
state = manager.integrate(final_time)

# Save the result to analyze or visualize
manager.getStateStorage().printResult("crouched_sim", ".", -1, ".sto", "states")

manager.getStateStorage().print("crouched_sim_output.sto")



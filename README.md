# Assignment 1

## 1. Install OpenSim and Python Scripting

Follow the instructions provided in the [OpenSim Python Scripting Guide](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/pages/53085346/Scripting+in+Python).

> **Note:** Setting up Python scripting might be challenging. If you assist a fellow student in the class with setting up Python scripting on their computer, write their name on your assignment to earn 5% bonus points.

---

## 2. Run a Forward Simulation

1. Refer to the `ForwardSimulationExample` folder attached with this assignment.
2. Modify the pose of the character so that:
    - It is in a crouched position (knees bent).
    - Its feet are touching the floor (not floating in the air).
3. Run a 5-second forward simulation. You should observe the character falling to the floor.

### Submission:
- Submit your modified code.
- Include a short write-up explaining your approach and observations.

---

## 3. Run a Simple Optimization for the Character to Maintain Balance

1. Use the provided `BalanceOptimization.py` file.
2. Install the required library by running:  
    ```bash
    pip install cma
    ```
3. Look for lines marked with `TODO` in the file and make the necessary changes to ensure the character stays balanced (does not fall).

### Questions to Address:
- How does the simulation change if you reduce the number of iterations (`maxiter`) from 8 to 1?
- What cost function term could you add to make the right toe reach as high as possible?

### Replay:
- Use the `replay_solution` function to visualize the optimized solution.

### Submission:
- Submit your modified code.
- Include a short write-up addressing the questions and explaining your approach.

---
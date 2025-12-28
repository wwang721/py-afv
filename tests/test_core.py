import numpy as np


def test_MATLAB(data_dir, simulator):
    # Compare forces computed by our code with those from MATLAB implementation
    
    pts = np.loadtxt(data_dir / "init_pts.csv", delimiter=',')
    simulator.update_positions(pts)

    # Build the diagram
    diag = simulator.build()

    # Get forces
    forces = diag["forces"]

    # This is only for the points in 'init_pts.csv' file
    forces_matlab = np.loadtxt(data_dir / "init_forces.csv", delimiter=',')
    F_comp = np.abs(forces - forces_matlab)

    assert np.max(F_comp) < 1e-8

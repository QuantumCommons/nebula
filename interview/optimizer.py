import numpy as np
from scipy.optimize import minimize


def run_optimization(objective_fn):
    initial_theta = np.random.uniform(low=0, high=2 * np.pi, size=2)

    result = minimize(objective_fn, initial_theta, method="COBYLA")

    return result

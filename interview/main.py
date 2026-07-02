from hamiltonian import build_hamiltonian
from ansatz import build_ansatz
from backend import estimate_energy
from optimizer import run_optimization


def objective(theta):
    hamiltonian = build_hamiltonian()
    circuit = build_ansatz(theta)
    energy = estimate_energy(circuit, hamiltonian)

    print(f"Estimated ground energy: {energy}")

    return energy


if __name__ == "__main__":
    result = run_optimization(objective)

    print("\n=== Optimization Result ===")
    print(f"Optimal parameters: {result.x}")
    print(f"Estimated ground energy: {result.fun}")

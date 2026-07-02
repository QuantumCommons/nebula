from qiskit.quantum_info import Statevector


def estimate_energy(circuit, hamiltonian):
    state = Statevector.from_instruction(circuit)

    energy = 0.0

    for pauli, coeff in zip(hamiltonian.paulis, hamiltonian.coeffs):
        expectation = state.expectation_value(pauli).real
        energy += coeff.real * expectation

    return energy

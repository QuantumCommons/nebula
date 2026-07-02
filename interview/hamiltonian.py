from qiskit.quantum_info import SparsePauliOp


def build_hamiltonian():
    paulis = [
        ("ZI", -1.05),
        ("IZ", -1.05),
        ("ZZ", 0.39),
        ("XX", 0.18),
    ]

    return SparsePauliOp.from_list(paulis)

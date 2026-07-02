from qiskit import QuantumCircuit


def build_ansatz(theta):
    qc = QuantumCircuit(2)

    qc.ry(theta[0], 0)
    qc.ry(theta[1], 1)

    qc.cx(0, 1)

    return qc

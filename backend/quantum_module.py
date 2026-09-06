from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Pauli


def analyze_quantum_state():

    # Create 1-qubit quantum circuit
    qc = QuantumCircuit(1)

    # Put qubit into superposition
    qc.h(0)

    # Get quantum state
    state = Statevector.from_instruction(qc)

    # Pauli operators
    pauli_x = Pauli("X")
    pauli_y = Pauli("Y")
    pauli_z = Pauli("Z")

    # Calculate measurements
    x_value = float(
        state.expectation_value(pauli_x).real
    )

    y_value = float(
        state.expectation_value(pauli_y).real
    )

    z_value = float(
        state.expectation_value(pauli_z).real
    )

    return {
        "pauli_x": x_value,
        "pauli_y": y_value,
        "pauli_z": z_value
    }
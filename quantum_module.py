from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Pauli


# Create a 1-qubit quantum circuit
qc = QuantumCircuit(1)

# Put the qubit into superposition
qc.h(0)

print("=== Q-SENTINEL QUANTUM MODULE ===")
print()
print("Quantum Circuit:")
print(qc)

# Get quantum state
state = Statevector.from_instruction(qc)

print("Quantum State:")
print(state)

# Pauli X, Y and Z operators
pauli_x = Pauli("X")
pauli_y = Pauli("Y")
pauli_z = Pauli("Z")

# Calculate expectation values
x_value = state.expectation_value(pauli_x)
y_value = state.expectation_value(pauli_y)
z_value = state.expectation_value(pauli_z)

print()
print("Pauli Measurements:")
print("X =", x_value)
print("Y =", y_value)
print("Z =", z_value)

print()
print("Quantum Analysis Completed!")
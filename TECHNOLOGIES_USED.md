
# CRYPTONOVA – Technologies and Tools Used

## 1. Programming Language

### Python 3.14
Used as the primary programming language for developing the CRYPTONOVA prototype and integrating the different modules.

---

## 2. Development Environment

### Visual Studio Code (VS Code)
Used as the primary development environment for writing, editing, executing, and testing the Python source code.

---

## 3. Quantum Computing Framework

### Qiskit
Used for quantum circuit simulation and quantum-state analysis.

### QuantumCircuit
Used to create and define the quantum circuit.

### Statevector
Used to simulate and analyze the quantum state produced by the circuit.

### Pauli Operators
Pauli X, Y, and Z operators are used for quantum-state measurement and analysis.

---

## 4. Cryptography

### Cryptography Python Library
Used for implementing secure digital signatures.

### Ed25519
Used for digital signature generation and signature verification.

---

## 5. Web Dashboard

### Streamlit
Used to develop the interactive CRYPTONOVA web dashboard and display the results of digital signature verification, quantum analysis, threat scores, and security classification.

---

## 6. Security and Audit

### SHA-256
Used to generate a cryptographic audit hash for tamper-evident recording of the security analysis result.

### hashlib
Python's built-in hashing module used to generate the SHA-256 hash.

---

## 7. Data Handling

### JSON
Used to structure and process audit information before generating the SHA-256 audit hash.

### datetime
Used to record timestamps for audit records.

---

## 8. Source Code Management

### GitHub
Used to store, manage, document, and share the CRYPTONOVA source code and project files.

---

## 9. Web Browser

A web browser is used to access and interact with the Streamlit-based CRYPTONOVA dashboard.

---

# Package Installation

The following external Python packages are required:

```bash
pip install qiskit cryptography streamlit

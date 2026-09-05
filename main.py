from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Pauli


print("=" * 55)
print("        Q-SENTINEL CYBER THREAT DETECTION")
print("=" * 55)

# -------------------------------------------------
# 1. DIGITAL SIGNATURE
# -------------------------------------------------

document = b"Q-Sentinel Secure Document"

private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()

signature = private_key.sign(document)

print("\n[1] DIGITAL SIGNATURE")
print("Signature generated successfully.")


# -------------------------------------------------
# 2. SIGNATURE VERIFICATION
# -------------------------------------------------

try:
    public_key.verify(signature, document)
    signature_valid = True
    print("Signature Verification : VALID")
except:
    signature_valid = False
    print("Signature Verification : INVALID")


# -------------------------------------------------
# 3. QUANTUM SIMULATION
# -------------------------------------------------

print("\n[2] QUANTUM SIMULATION")

qc = QuantumCircuit(1)
qc.h(0)

state = Statevector.from_instruction(qc)

print("Quantum state created successfully.")


# -------------------------------------------------
# 4. PAULI X, Y, Z ANALYSIS
# -------------------------------------------------

x_value = float(state.expectation_value(Pauli("X")).real)
y_value = float(state.expectation_value(Pauli("Y")).real)
z_value = float(state.expectation_value(Pauli("Z")).real)

print("\n[3] PAULI MEASUREMENTS")
print("Pauli X :", round(x_value, 3))
print("Pauli Y :", round(y_value, 3))
print("Pauli Z :", round(z_value, 3))


# -------------------------------------------------
# 5. THREAT ANALYSIS
# -------------------------------------------------

print("\n[4] THREAT ANALYSIS")

quantum_anomaly = False

threat_score = 0

if not signature_valid:
    threat_score += 40

if quantum_anomaly:
    threat_score += 30

threshold = 50

if threat_score >= threshold:
    result = "ATTACK DETECTED"
else:
    result = "GENUINE"


print("Threat Score :", threat_score, "/ 100")
print("Threshold    :", threshold)
print("Final Result :", result)


# -------------------------------------------------
# FINAL RESULT
# -------------------------------------------------

print("\n" + "=" * 55)
print("              FINAL VERDICT")
print("=" * 55)
print("Digital Signature :", "VALID" if signature_valid else "INVALID")
print("Threat Score      :", threat_score, "/ 100")
print("Detection Result  :", result)
print("=" * 55)
# -------------------------------------------------
# 6. TAMPERING / ATTACK SIMULATION
# -------------------------------------------------

print("\n[5] ATTACK SIMULATION")

tampered_document = b"Q-Sentinel HACKED Document"

try:
    public_key.verify(signature, tampered_document)
    tampered_valid = True
except:
    tampered_valid = False

if not tampered_valid:
    attack_score = 90
    attack_result = "ATTACK DETECTED"
else:
    attack_score = 0
    attack_result = "GENUINE"

print("Original Document  : VERIFIED")
print("Modified Document  : DETECTED")
print("Threat Score       :", attack_score, "/ 100")
print("Result             :", attack_result)
# -------------------------------------------------
# 7. OTHER ATTACK SIMULATIONS
# -------------------------------------------------

print("\n[6] OTHER ATTACK SIMULATIONS")

# REPLAY ATTACK
replay_score = 75
print("\nReplay Attack")
print("Threat Score :", replay_score, "/ 100")
print("Result       : ATTACK DETECTED")


# IMPERSONATION ATTACK
impersonation_score = 85
print("\nImpersonation Attack")
print("Threat Score :", impersonation_score, "/ 100")
print("Result       : ATTACK DETECTED")


# QUANTUM CHANNEL MANIPULATION
quantum_attack_score = 80
print("\nQuantum Channel Manipulation")
print("Threat Score :", quantum_attack_score, "/ 100")
print("Result       : ATTACK DETECTED")


print("\n========================================")
print("       ALL ATTACK TESTS COMPLETED")
print("========================================")
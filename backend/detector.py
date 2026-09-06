# Q-SENTINEL Threat Detector


def calculate_threat_score(signature_valid, quantum_anomaly, attack_type):
    
    score = 0

    # Digital signature verification
    if not signature_valid:
        score += 40

    # Quantum measurement anomaly
    if quantum_anomaly:
        score += 30

    # Attack-specific score
    if attack_type == "Forgery":
        score += 20

    elif attack_type == "Replay":
        score += 15

    elif attack_type == "Impersonation":
        score += 25

    # Limit score to 100
    score = min(score, 100)

    return score


def classify_threat(score):
    
    threshold = 50

    if score >= threshold:
        return "ATTACK DETECTED"
    else:
        return "GENUINE"


# Test cases
tests = [
    ("Genuine", True, False),
    ("Forgery", False, True),
    ("Replay", False, True),
    ("Impersonation", False, True)
]


print("====================================")
print("       Q-SENTINEL THREAT DETECTOR")
print("====================================")

for attack_type, signature_valid, quantum_anomaly in tests:

    score = calculate_threat_score(
        signature_valid,
        quantum_anomaly,
        attack_type
    )

    result = classify_threat(score)

    print()
    print("Scenario:", attack_type)
    print("Threat Score:", score, "/ 100")
    print("Result:", result)

print()
print("Threat Detection Completed!")
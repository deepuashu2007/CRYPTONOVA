from fastapi import FastAPI
from pydantic import BaseModel
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey
)
from cryptography.hazmat.primitives import serialization
import base64

from backend.quantum_module import analyze_quantum_state
from backend.audit import create_audit_hash



app = FastAPI(
    title="CRYPTONOVA API",
    description="Quantum-Inspired Cyber Threat Detection for Digital Signature Security",
    version="1.0.0"
)


# -----------------------------
# REQUEST MODELS
# -----------------------------

class DocumentRequest(BaseModel):
    document: str


class VerifyRequest(BaseModel):
    document: str
    signature: str
    public_key: str


class AnalyzeRequest(BaseModel):
    scenario: str


# -----------------------------
# DIGITAL SIGNATURE
# -----------------------------

@app.post("/sign")
def create_signature(request: DocumentRequest):

    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    document = request.document.encode()

    signature = private_key.sign(document)

    encoded_signature = base64.b64encode(signature).decode()

    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )

    encoded_public_key = base64.b64encode(
        public_key_bytes
    ).decode()

    return {
        "project": "CRYPTONOVA",
        "document": request.document,
        "signature": encoded_signature,
        "public_key": encoded_public_key,
        "status": "Digital signature created successfully"
    }


# -----------------------------
# SIGNATURE VERIFICATION
# -----------------------------

@app.post("/verify")
def verify_signature(request: VerifyRequest):

    try:
        signature = base64.b64decode(request.signature)

        public_key_bytes = base64.b64decode(
            request.public_key
        )

        public_key = Ed25519PublicKey.from_public_bytes(
            public_key_bytes
        )

        public_key.verify(
            signature,
            request.document.encode()
        )

        return {
            "project": "CRYPTONOVA",
            "signature_valid": True,
            "result": "GENUINE"
        }

    except Exception:

        return {
            "project": "CRYPTONOVA",
            "signature_valid": False,
            "result": "ATTACK / TAMPERED"
        }


# -----------------------------
# THREAT ANALYSIS
# -----------------------------
@app.post("/analyze")
def analyze_threat(request: AnalyzeRequest):

    quantum_result = analyze_quantum_state()

    scores = {
        "Genuine": 0,
        "Forgery / Tampering": 90,
        "Replay Attack": 75,
        "Impersonation": 85,
        "Quantum Channel Manipulation": 80
    }

    threat_score = scores.get(request.scenario, 0)

    threshold = 50

    if threat_score >= threshold:
        result = "ATTACK DETECTED"
    else:
        result = "GENUINE / SAFE"

    audit_data, audit_hash = create_audit_hash(
        request.scenario,
        threat_score,
        result
    )

    return {
        "project": "CRYPTONOVA",
        "scenario": request.scenario,
        "threat_score": threat_score,
        "threshold": threshold,
        "result": result,
        "quantum_analysis": quantum_result,
        "audit_record": audit_data,
        "audit_hash": audit_hash
    }
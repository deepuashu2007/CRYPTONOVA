import hashlib
import json
from datetime import datetime


def create_audit_hash(scenario, threat_score, result):

    audit_data = {
        "project": "CRYPTONOVA",
        "scenario": scenario,
        "threat_score": threat_score,
        "result": result,
        "timestamp": datetime.now().isoformat()
    }

    audit_string = json.dumps(
        audit_data,
        sort_keys=True
    )

    audit_hash = hashlib.sha256(
        audit_string.encode()
    ).hexdigest()

    return audit_data, audit_hash
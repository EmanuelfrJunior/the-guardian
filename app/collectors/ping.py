from ping3 import ping
from datetime import datetime


def ping_host(host: str):
    tempo = ping(host, timeout =2)
    

    return {
    
            "host": host,
            "latency_ms": round(tempo * 1000, 2) if tempo else None,
            "status": "online" if tempo else "offline",
            "timestamp": datetime.utcnow().isoformat()

    }

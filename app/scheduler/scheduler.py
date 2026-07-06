import time
from app.collectors.ping import ping_host

HOSTS = [
        "1.1.1.1",
        "8.8.8.8",
        "google.com"
        ]

def run_scheduler(interval):
    print("=== THE GUARDIAN ===")

    while True:
        for host in HOSTS:
            result = ping_host(host)

            status = "->ONLINE<-" if result["status"] == "online" else "->OFFLINE<_"

            print(f"{status} {result['host']} - {result['latency_ms']} ms")

        print("-" * 40)
        time.sleep(interval)

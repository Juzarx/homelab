import requests
import socket
from datetime import datetime

HTTP_SERVICES = {
    "Homepage": ("http://localhost", "homepage.home"),
    "Pi-hole": ("http://localhost/admin", "pihole.home"),
    "Prometheus": ("http://localhost/-/healthy", "prometheus.home"),
    "Grafana": ("http://localhost/api/health", "grafana.home"),
    "Nextcloud": ("http://localhost/status.php", "nextcloud.home"),
    "Grimmory": ("http://localhost", "grimmory.home"),
    "Navidrome": ("http://localhost", "navidrome.home"),
}

TCP_SERVICES = {
    "Minecraft": ("GamesVMTailscaleIP", 25565),
}

def check_http(name, url, host_header=None):
    try:
        headers = {"Host": host_header} if host_header else {}
        response = requests.get(url, headers=headers, timeout=5)
        status = "UP" if response.status_code == 200 else f"DOWN ({response.status_code})"
    except requests.exceptions.RequestException as e:
        status = f"DOWN ({type(e).__name__})"
    return status

def check_tcp(name, host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            return "UP"
    except OSError as e:
        return f"DOWN ({type(e).__name__})"

def main():
    print(f"Health check - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
    for name, (url, host) in HTTP_SERVICES.items():
        status = check_http(name, url, host)
        print(f"{name:15} {status}")
    for name, (host, port) in TCP_SERVICES.items():
        status = check_tcp(name, host, port)
        print(f"{name:15} {status}")

if __name__ == "__main__":
    main()
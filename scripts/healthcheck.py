import requests
import socket
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

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

def send_discord_alert(down_services):
    message = "** Homelab Alert **\nThe following services are DOWN:\n"
    for name, status in down_services:
        message += f"- {name}: {status}"
    try:
        requests.post(DISCORD_WEBHOOK_URL, json ={"content": message}, timeout=5)
    except requests.exceptions.RequestException:
        print("Failde to send Discord Alert")

def send_telegram_alert(down_services):
    message = "Homelab Alert\nThe following services are DOWN\n"
    for name, status in down_services:
        message += f"-{name}: {status}\n"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID,"text": message}, timeout=5)
    except requests.exceptions.RequestException:
        print("Failed to send telegram alert")
    


def main():
    print(f"Health check - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)

    down_services = []

    for name, (url, host) in HTTP_SERVICES.items():
        status = check_http(name,url, host)
        print(f"{name:15} {status}")
        if not status.startswith("UP"):
            down_services.append((name, status))

    for name, (url, host) in TCP_SERVICES.items():
        status = check_http(name,url, host)
        print(f"{name:15} {status}")
        if not status.startswith("UP"):
            down_services.append((name, status))

    if down_services:
        send_discord_alert(down_services)
        send_telegram_alert(down_services)



if __name__ == "__main__":
    main()
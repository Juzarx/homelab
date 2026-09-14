from flask import Flask, jsonify, render_template
import subprocess
import re
from health_check import check_http, check_tcp, HTTP_SERVICES, TCP_SERVICES

app = Flask(__name__)

VM_HOSTS = {
    "infra": "localhost",
    "media": "julio@MediaVMIP",
    "games": "julio@GamesVMIP",
}

@app.route("/")
def home ():
    return render_template("index.html")

@app.route("/api/minecraft/status")
def minecraft_status():
    result = subprocess.run(
        ["ssh", "julio@192.168.1.68", "docker", "inspect", "-f", "{{.State.Running}}", "mc"],
        capture_output=True, text=True
    )
    is_running = result.stdout.strip()== "true"
    return jsonify({"running": is_running})

@app.route("/api/minecraft/start", methods=["POST"])
def minecraft_start():
    result = subprocess.run(
        ["ssh", "julio@192.168.1.68", "docker", "start", "mc"],
        capture_output=True, text=True 
    )
    success = result.returncode == 0
    return jsonify({
        "success": success,
        "output": result.stdout,
        "error": result.stderr
    })

@app.route("/api/minecraft/stop", methods=["POST"])
def minecraft_stop():
    save_result = subprocess.run(
        ["ssh", "julio@192.168.1.68", "docker", "exec", "mc", "rcon-cli", "save-all"],
        capture_output=True, text=True 
    )
    stop_result = subprocess.run(
        ["ssh", "julio@192.168.1.68", "docker", "stop","mc"],
        capture_output=True, text=True
    )
    success = save_result.returncode == 0 and stop_result.returncode == 0
    return jsonify({
        "success": success,
        "save_output": save_result.stdout,
        "stop_output": stop_result.stdout
    })

@app.route("/api/minecraft/list", methods=["GET"])
def minecraft_list():
    list_result = subprocess.run(
        ["ssh", "julio@192.168.1.68", "docker", "exec", "mc", "rcon-cli", "list"],
        capture_output=True, text=True
    )
    success = list_result.returncode == 0

    raw_output = list_result.stdout
    clean_output = re.sub(r'\x1b\[[0-9;]*m', '', raw_output).strip()

    players = []
    match = re.search(r'online:\s*(.*)', clean_output)
    if match and match.group(1).strip():
        players = [name.strip() for name in match.group(1).split(",")]

    return jsonify({
        "success": success,
        "player_count": len(players),
        "players": players
    })

@app.route("/api/services/status")
def services_status():
    statuses = {}
    for name, (url, host) in HTTP_SERVICES.items():
        statuses[name] = check_http(name, url, host)
    for name, (host, port) in TCP_SERVICES.items():
        statuses[name] = check_tcp(name, host, port)
    return jsonify(statuses)

@app.route("/api/restart/<vm>/<container>", methods=["POST"])
def restart_container(vm, container):
    if vm not in VM_HOSTS:
        return jsonify({"success": False, "error": "Unknown VM"}), 400

    host = VM_HOSTS[vm]
    if host == "localhost":
        command = ["docker", "restart", container]
    else:
        command = ["ssh", host, "docker", "restart", container]

    result = subprocess.run(command, capture_output=True, text=True)
    success = result.returncode == 0
    return jsonify({"success": success, "output": result.stdout, "error": result.stderr})


if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5000)


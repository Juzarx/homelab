from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home ():
    return "Homelab control panel is running"

@app.route("/api/minecraft/status")
def minecraft_status():
    result = subprocess.run(
        ["ssh", "user@gamesVMIP", "docker", "inspect", "-f", "{{.State.Running}}", "mc"],
        capture_output=True, text=True
    )
    is_running = result.stdout.strip()== "true"
    return jsonify({"running": is_running})

@app.route("/api/minecraft/start", methods=["POST"])
def minecraft_start():
    result = subprocess.run(
        ["ssh", "user@gamesVMIP", "docker", "start", "mc"],
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
        ["ssh", "user@gamesVMIP", "docker", "exec", "mc", "rcon-cli", "save-all"],
        capture_output=True, text=True 
    )
    stop_result = subprocess.run(
        ["ssh", "user@gamesVMIP", "docker", "stop","mc"],
        capture_output=True, text=True
    )
    success = save_result.returncode == 0 and stop_result.returncode == 0
    return jsonify({
        "success": success,
        "save_output": save_result.stdout,
        "stop_output": stop_result.stdout
    }) 


if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5000)


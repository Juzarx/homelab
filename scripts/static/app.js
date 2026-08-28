async function checkStatus() {
    const response = await fetch("/api/minecraft/status");
    const data = await response.json();
    const statusEl = document.getElementById("mc-status");
    statusEl.textContent = data.running ? "Online" : "Offline";
}

async function startServer() {
    const statusEl = document.getElementById("mc-status");
    statusEl.textContent = "Starting...";
    await fetch("/api/minecraft/start", { method: "POST" });
    setTimeout(checkStatus, 3000);
}

async function stopServer() {
    const statusEl = document.getElementById("mc-status");
    statusEl.textContent = "Stopping...";
    await fetch("/api/minecraft/stop", { method: "POST" });
    setTimeout(checkStatus, 3000);
}

async function checkPlayers() {
    const response = await fetch("api/minecraft/list");
    const data = await response.json();
    const listEl = document.getElementById("player-list");
    listEl.innerHTML = "";

    if (data.success && data.players.length > 0) {
        data.players.forEach(player => {
            listEl.innerHTML += `<li>${player}</li>`;
        });
    } else if (data.success){
        listEl.innerHTML = "<li>No players online</li>";
    } else {
        listEl.innerHTML = "<li>Could not fetch player list</li>";
    }
}

document.getElementById("start-btn").addEventListener("click", startServer);
document.getElementById("stop-btn").addEventListener("click", stopServer);

checkStatus();
checkPlayers();
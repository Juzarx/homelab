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

const SERVICES = [
    { vm: "infra", container: "traefik", label: "Traefik", healthName: null },
    { vm: "infra", container: "pihole", label: "Pi-hole", healthName: "Pi-hole" },
    { vm: "infra", container: "homepage", label: "Homepage", healthName: "Homepage" },
    { vm: "media", container: "nextcloud", label: "Nextcloud", healthName: "Nextcloud" },
    { vm: "media", container: "grimmory", label: "Grimmory", healthName: "Grimmory" },
    { vm: "media", container: "navidrome", label: "Navidrome", healthName: "Navidrome" },
    { vm: "games", container: "minecraft", label: "Minecraft", healthName: "Minecraft" },
];

async function buildRestartTable() {
    const response = await fetch("/api/services/status");
    const statuses = await response.json();

    const tbody = document.getElementById("restart-table");
    tbody.innerHTML = "";

    SERVICES.forEach(service => {
        const status = service.healthName ? statuses[service.healthName] : "N/A";
        const statusColor = status && status.startsWith("UP") ? "green" : "red";

        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${service.label}</td>
            <td style="color: ${statusColor}">${status}</td>
            <td><button data-vm="${service.vm}" data-container="${service.container}">Restart</button></td>
        `;
        tbody.appendChild(row);
    });

    document.querySelectorAll("#restart-table button").forEach(btn => {
        btn.addEventListener("click", async () => {
            const vm = btn.dataset.vm;
            const container = btn.dataset.container;
            btn.textContent = "Restarting...";
            btn.disabled = true;
            await fetch(`/api/restart/${vm}/${container}`, { method: "POST" });
            btn.textContent = "Restart";
            btn.disabled = false;
            buildRestartTable();
        });
    });
}

buildRestartTable();

document.getElementById("start-btn").addEventListener("click", startServer);
document.getElementById("stop-btn").addEventListener("click", stopServer);

checkStatus();
checkPlayers();
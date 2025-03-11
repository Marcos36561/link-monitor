function atualizarStatus() {
    fetch("/status")
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById("cards-container");
            container.innerHTML = "";

            for (const [nome, info] of Object.entries(data)) {
                const card = document.createElement("div");
                card.className = "card";
                card.innerHTML = `
                    <h3>${nome}</h3>
                    <p>${info.ip}</p>
                    <div class="status ${info.status === "ONLINE" ? "online" : "offline"}">
                        ${info.status}
                    </div>
                `;
                card.style.backgroundColor = info.status === "ONLINE" ? "#28a745" : "#dc3545";
                container.appendChild(card);
            }
        })
        .catch(error => console.error("Erro ao buscar status:", error));
}

setInterval(atualizarStatus, 5000);
atualizarStatus();
from flask import Flask, render_template, jsonify
import subprocess
import time
import threading
import csv
import platform

app = Flask(__name__)

# Classe Link
class Link:
    def __init__(self, nome, ip):
        self.nome = nome
        self.ip = ip
        self.status = "Verificando..."

    def verificar_status(self):
        try:
            if platform.system().lower() == "windows":
                output = subprocess.run(["ping", "-n", "1", "-w", "1000", self.ip], capture_output=True, text=True)
            else:
                output = subprocess.run(["ping", "-c", "1", "-W", "1", self.ip], capture_output=True, text=True)

            if "1 received" in output.stdout or "bytes=32" in output.stdout:
                self.status = "ONLINE"
            else:
                self.status = "OFFLINE"
        except Exception as e:
            print(f"Erro ao enviar PING para {self.ip}: {e}")
            self.status = "ERRO"

# Função para carregar links a partir do arquivo CSV
def carregar_links():
    condominios = []
    with open("links.csv", mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            link = link(linha["nome"], linha["ip"])
            links.append(condominio)
    return links

# Carrega os links do arquivo CSV
links = carregar_links()

# Função para monitorar os condomínios em segundo plano
def monitorar_links():
    while True:
        for link in links:
            link.verificar_status()
        time.sleep(5)  # Dispara um PING a cada 5 segundos

# Rota principal para exibir o status dos links
@app.route("/")
def index():
    return render_template("index.html")

# Rota para retornar os status dos condomínios em formato JSON
@app.route("/status")
def status():
    status_links = {
        link.nome: {"ip": link.ip, "status": link.status} for link in links
    }
    return jsonify(status_links)

# Iniciar o monitoramento em uma thread separada
if __name__ == "__main__":
    # Inicia a thread de monitoramento
    monitor_thread = threading.Thread(target=monitorar_links)
    monitor_thread.daemon = True  # Thread encerra quando o programa principal encerrar
    monitor_thread.start()

    # Inicia o servidor Flask
    if __name__ == '__main__':
        app.run(debug=False)

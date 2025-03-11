# Monitoramento_de_Link
O Link Monitor é um sistema simples de monitoramento de links desenvolvido em Python utilizando o framework Flask. Ele realiza pings periodicamente (a cada 5 segundos) nos IPs cadastrados e exibe o status de conectividade na interface do usuário em tempo real. Os IPs são organizados por Condomínio, onde cada entrada possui um nome e um IP correspondente.

Funcionalidades:

Monitoramento automático dos IPs cadastrados
Organização dos IPs por Condomínio (Nome + IP)
Atualização em tempo real do status dos links
Interface web intuitiva

Tecnologias Utilizadas:

Python
Flask
Ping (ICMP)
HTML, CSS e JavaScript


Como Usar

1. Clone este repositório:
   
   git clone https://github.com/Marcos36561/Monitoramento_de_Link

3. Acesse a pasta do projeto:
   
   cd link-monitor

4. Instale as dependências:
   pip install -r requirements.txt

5. Edite o arquivo condominios.csv e adicione os condomínios e seus respectivos IPs no seguinte formato:
   
   Nome,IP
   Condomínio A,192.168.1.1
   Condomínio B,8.8.8.8
   Condomínio C,1.1.1.1

6. Execute o sistema:
   
   python app.py

8. Acesse no navegador:
   http://localhost:5000


Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.


Licença
Este projeto está sob a licença MIT.

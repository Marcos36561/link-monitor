# link-monitor
O Link Monitor é um sistema simples de monitoramento de links desenvolvido em Python utilizando o framework Flask. Ele realiza pings periodicamente (a cada 5 segundos) nos IPs cadastrados e exibe o status de conectividade na interface do usuário em tempo real. Os IPs são organizados por Link, onde cada entrada possui um nome e um IP correspondente.

Funcionalidades:

Monitoramento automático dos IPs cadastrados
Organização dos IPs por Link (Nome + IP)
Atualização em tempo real do status dos links
Interface web intuitiva

Tecnologias Utilizadas:

Python
Flask
Ping (ICMP)
HTML, CSS e JavaScript


Como Usar

1. Clone este repositório:

   ```sh
   git clone https://github.com/Marcos36561/link-monitor
   ```
   
3. Acesse a pasta do projeto:

   ```sh
   cd link-monitor
   ```

4. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

6. Edite o arquivo condominios.csv e adicione os condomínios e seus respectivos IPs no seguinte formato:

   ```sh
   nome,ip
   Link A,192.168.1.1
   Link B,8.8.8.8
   Link C,1.1.1.1
   ```

7. Execute o sistema:

   ```sh
   python app.py
   ```

8. Acesse no navegador:

   ```sh
   http://localhost:5000
   ```

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.


Este projeto está sob a licença MIT.

File Transfer System
Este projeto implementa um sistema de transferência de arquivos em uma arquitetura cliente-servidor usando Python, RPyC para comunicação remota e Tkinter para a interface gráfica no cliente. O servidor oferece uma série de funcionalidades para gerenciar arquivos, enquanto o cliente permite interagir com o servidor de maneira intuitiva.

Funcionalidades
Servidor
Upload de Arquivos: Permite o envio de arquivos para o servidor para compartilhamento.
Listagem de Arquivos: Fornece uma lista de arquivos disponíveis no servidor.
Download de Arquivos: Permite que os clientes baixem arquivos disponíveis no servidor.
Registro de Interesse: Clientes podem registrar interesse em arquivos que ainda não estão disponíveis. O servidor notifica os clientes registrados assim que o arquivo de interesse for adicionado.
Cancelamento de Registro de Interesse: Permite aos clientes cancelar o registro de interesse em um arquivo específico.
Criação de Arquivos .txt: Cria arquivos de texto diretamente no servidor com o conteúdo especificado.
Cliente
Envio de Arquivos: O cliente pode enviar arquivos para o servidor.
Listagem de Arquivos: Permite visualizar todos os arquivos disponíveis no servidor.
Download de Arquivos: Baixa arquivos do servidor para o sistema de arquivos local.
Notificação de Evento: Recebe notificações assíncronas do servidor sobre a disponibilidade de arquivos de interesse.
Requisitos
Python 3.x
RPyC: Para comunicação remota entre cliente e servidor.
Tkinter: Para a interface gráfica do cliente.
Como Usar
Servidor
Instale as dependências:

bash
Copiar código
pip install rpyc
Execute o servidor:

bash
Copiar código
python servidor.py
O servidor será iniciado na porta 18812 e estará pronto para aceitar conexões de clientes.

Cliente
Instale as dependências:

bash
Copiar código
pip install rpyc
Execute o cliente:

bash
Copiar código
python cliente.py
A interface gráfica será aberta, permitindo que você envie, liste e baixe arquivos.

Estrutura do Projeto
plaintext
Copiar código
.
├── servidor.py         # Código do servidor
└── cliente.py          # Código do cliente com interface gráfica
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
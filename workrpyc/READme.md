# Sistema de transferencia de arquivos
Este projeto implementa um sistema de transferência de arquivos em uma arquitetura cliente-servidor usando Python, RPyC para comunicação remota e Tkinter para a interface gráfica no cliente. O servidor oferece uma série de funcionalidades para gerenciar arquivos, enquanto o cliente permite interagir com o servidor de maneira intuitiva.

## Funcionalidades

### Servidor
- Upload de Arquivos: Permite o envio de arquivos para o servidor para compartilhamento.- Listagem de Arquivos: Fornece uma lista de arquivos disponíveis no servidor.
- Download de Arquivos: Permite que os clientes baixem arquivos disponíveis no servidor.
- Criação de Arquivos .txt: Cria arquivos de texto diretamente no servidor com o conteúdo especificado.

### Cliente
- Envio de Arquivos: O cliente pode enviar arquivos para o servidor.
- Listagem de Arquivos: Permite visualizar todos os arquivos disponíveis no servidor.
- Download de Arquivos: Baixa arquivos do servidor para o sistema de arquivos local.

## Requisitos
- Python 3.x
- RPyC: Para comunicação remota entre cliente e servidor.
- Tkinter: Para a interface gráfica do cliente.

## Como Usar

### Clonar o Repositório
    1. Clone o repositório:
        git clone https://github.com/willybnt/sistemasdistribuidos.git
    2. Navegue até o diretório do projeto:
        cd "seu-repositorio"

### Servidor
    1. Instale as dependências:
        pip install rpyc
    2. Execute o servidor:
        python servidor.py

O servidor será iniciado na porta 18812 e estará pronto para aceitar conexões de clientes.

### Cliente
    1. Instale as dependências:
        pip install rpyc
    2. Execute o cliente:
        python cliente.py

A interface gráfica será aberta, permitindo que você envie, liste e baixe arquivos.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
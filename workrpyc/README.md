# Aplicação de transferência de arquivos em uma arquitetura cliente-servidor

Este projeto implementa um sistema de transferência de arquivos em uma arquitetura cliente/servidor utilizando RPyC (Remote Python Calls) para comunicação entre componentes.

## Pré-requisitos

- Python 3.x instalado
- RPyC (Remote Python Call)
- Editor de código

## Instalação 

1. Clone este repositório para o seu ambiente local:
    "git clone https://github.com/seu-usuario/seu-repositorio.git"
2. Navegue até o diretorio do projeto:
    "cd seu-repositorio"
3. Instale as dependências:
    pip install rpyc

## Executando o servidor

1. Navegue até o diretório do projeto no terminal.
2. Execute o seguinte comando  para iniciar o servidor:
    python servidor.py

## Executando o cliente

1. Abra outro terminal ou outra janela de terminal.
2. navegue até o diretório do projeto.
3. Execute o seguinte comando para iniciar o cliente:
    python cliente.py

## Testando a funcionalidade de enviar arquivo

1. Com o servidor em execução, execute o cliente.
2. O cliente enviará um arquivo chamado exemplo.txt para o servidor.
3. Verifique no terminal do servidor se o arquivo foi recebido e salvo no diretório onde o servidor está sendo executado.

## Testando a funcionalidade de listar arquivos

1. Após enviar um arquivo para o servidor, o cliente pode solicitar a lista de arquivos disponíveis.

2. No terminal do cliente, será exibida uma lista com os nomes dos arquivos que estão disponíveis no servidor.

## Testando a Funcionalidade de Baixar Arquivo

1. O cliente pode baixar um arquivo existente no servidor.
2. O arquivo baixado será salvo no diretório do cliente com o prefixo baixado_.
3. Verifique se o arquivo foi salvo corretamente no diretório do cliente.

## Testando a Funcionalidade de Registro de Interesse

1. Com o servidor em execução, o cliente pode registrar interesse em um arquivo inexistente, como arquivo_inexistente.txt.

2. Crie manualmente o arquivo arquivo_inexistente.txt no diretório do servidor:
    echo "Conteúdo do arquivo" > arquivo_inexistente.txt

3. Observe que o cliente será notificado assim que o arquivo estiver disponível no servidor.

## Testando a Funcionalidade de Cancelar Registro de Interesse

1. O cliente pode cancelar o registro de interesse em um arquivo.
2. Após o cancelamento, mesmo que o arquivo se torne disponível, o cliente não receberá notificações.
3. Verifique se o registro foi cancelado corretamente ao observar que nenhuma notificação é recebida após a criação do arquivo.

## Estrutura do Projeto

- servidor.py: Código do servidor que gerencia os arquivos e as notificações.
- cliente.py: Código do cliente que realiza upload, download e registra interesses.
- README.md: Documentação do projeto.
- example.txt: Arquivo de exemplo usado para testes de upload e download.
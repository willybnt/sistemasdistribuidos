import rpyc
from rpyc.utils.server import ThreadedServer
import os

# Classe ServidorArquivo que herda de rpyc.Service
class ServidorArquivo(rpyc.Service):
    def __init__(self):
        # Dicionário para armazenar arquivos enviados ao servidor
        self.arquivos = {}
        # Lista para armazenar interesses dos clientes em arquivos específicos
        self.interesses = []

    # Método exposto para permitir que os clientes enviem arquivos ao servidor
    def exposed_enviar_arquivo(self, nome_arquivo, dados_arquivo):
        # Salva o arquivo recebido no servidor
        with open(nome_arquivo, 'wb') as f:
            f.write(dados_arquivo)
        # Adiciona o nome do arquivo ao dicionário de arquivos
        self.arquivos[nome_arquivo] = nome_arquivo
        # Verifica se há algum cliente interessado no arquivo recebido
        self.verificar_interesses(nome_arquivo)

    # Método exposto para listar os arquivos armazenados no servidor
    def exposed_listar_arquivos(self):
        # Retorna uma lista dos nomes dos arquivos armazenados
        return list(self.arquivos.keys())

    # Método exposto para permitir que os clientes baixem arquivos do servidor
    def exposed_baixar_arquivo(self, nome_arquivo):
        # Verifica se o arquivo solicitado está armazenado no servidor
        if nome_arquivo in self.arquivos:
            # Abre o arquivo em modo de leitura binária e retorna seu conteúdo
            with open(nome_arquivo, 'rb') as f:
                return f.read()
        else:
            # Retorna None se o arquivo não for encontrado
            return None

    # Método exposto para registrar o interesse de um cliente em um arquivo específico
    def exposed_registrar_interesse(self, nome_arquivo, cliente, validade):
        # Adiciona uma tupla com o nome do arquivo, cliente e validade à lista de interesses
        self.interesses.append((nome_arquivo, cliente, validade))

    # Método exposto para cancelar o interesse de um cliente em um arquivo específico
    def exposed_cancelar_interesse(self, nome_arquivo, cliente):
        # Remove o interesse correspondente da lista de interesses
        self.interesses = [(f, c, v) for f, c, v in self.interesses if not (f == nome_arquivo and c == cliente)]

    # Método exposto para criar um arquivo .txt no servidor com o conteúdo fornecido
    def exposed_criar_arquivo_txt(self, nome_arquivo, conteudo):
        # Cria e escreve o conteúdo no arquivo .txt
        with open(nome_arquivo, 'w') as f:
            f.write(conteudo)
        # Adiciona o nome do arquivo ao dicionário de arquivos
        self.arquivos[nome_arquivo] = nome_arquivo

    # Método para verificar se há clientes interessados no arquivo recém-enviado
    def verificar_interesses(self, nome_arquivo):
        # Itera sobre a lista de interesses
        for interesse in self.interesses:
            # Verifica se o interesse é pelo arquivo recém-enviado
            if interesse[0] == nome_arquivo:
                # Obtém o cliente interessado
                cliente = interesse[1]
                # Notifica o cliente que o arquivo de interesse está disponível
                cliente.notificar_evento(nome_arquivo)
                # Remove o interesse da lista após a notificação
                self.interesses.remove(interesse)

# Ponto de entrada do programa
if __name__ == "__main__":
    # Cria uma instância do servidor threaded, passando a classe ServidorArquivo e a porta de conexão
    servidor = ThreadedServer(ServidorArquivo(), port=18812)
    # Inicia o servidor
    servidor.start()

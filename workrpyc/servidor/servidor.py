import rpyc
from rpyc.utils.server import ThreadedServer
import os

class ServidorArquivo(rpyc.Service):
    def __init__(self):
        self.arquivos = {}
        self.interesses = []

    def exposed_enviar_arquivo(self, nome_arquivo, dados_arquivo):
        with open(nome_arquivo, 'wb') as f:
            f.write(dados_arquivo)
        self.arquivos[nome_arquivo] = nome_arquivo
        self.verificar_interesses(nome_arquivo)

    def exposed_listar_arquivos(self):
        return list(self.arquivos.keys())

    def exposed_baixar_arquivo(self, nome_arquivo):
        if nome_arquivo in self.arquivos:
            with open(nome_arquivo, 'rb') as f:
                return f.read()
        else:
            return None

    def exposed_registrar_interesse(self, nome_arquivo, cliente, validade):
        self.interesses.append((nome_arquivo, cliente, validade))

    def exposed_cancelar_interesse(self, nome_arquivo, cliente):
        self.interesses = [(f, c, v) for f, c, v in self.interesses if not (f == nome_arquivo and c == cliente)]

    def exposed_criar_arquivo_txt(self, nome_arquivo, conteudo):
        """Cria um arquivo .txt no servidor."""
        with open(nome_arquivo, 'w') as f:
            f.write(conteudo)
        self.arquivos[nome_arquivo] = nome_arquivo

    def verificar_interesses(self, nome_arquivo):
        for interesse in self.interesses:
            if interesse[0] == nome_arquivo:
                cliente = interesse[1]
                cliente.notificar_evento(nome_arquivo)
                self.interesses.remove(interesse)

if __name__ == "__main__":
    servidor = ThreadedServer(ServidorArquivo(), port=18812)
    servidor.start()

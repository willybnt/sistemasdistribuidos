import rpyc

class ClienteArquivo:
    def __init__(self, host='localhost', port=18812):
        self.conn = rpyc.connect(host, port)

    def enviar_arquivo(self, nome_arquivo):
        with open('C:/Users/willy/OneDrive/Documentos/faculdade/sistemasdistribuidos/workrpyc/servidor/exemplo.txt', 'rb') as f:
            dados = f.read()
        self.conn.root.enviar_arquivo(nome_arquivo, dados)

    def listar_arquivos(self):
        return self.conn.root.listar_arquivos()

    def baixar_arquivo(self, nome_arquivo):
        dados = self.conn.root.baixar_arquivo(nome_arquivo)
        if dados:
            with open(f'baixado_{nome_arquivo}', 'wb') as f:
                f.write(dados)
        else:
            print("Arquivo não encontrado no servidor.")

    def registrar_interesse(self, nome_arquivo, validade=60):
        self.conn.root.registrar_interesse(nome_arquivo, self, validade)

    def cancelar_interesse(self, nome_arquivo):
        self.conn.root.cancelar_interesse(nome_arquivo, self)

    def notificar_evento(self, nome_arquivo):
        print(f"Notificação: {nome_arquivo} está agora disponível no servidor!")

if __name__ == "__main__":
    cliente = ClienteArquivo()
    cliente.enviar_arquivo('exemplo.txt')
    print(cliente.listar_arquivos())
    cliente.baixar_arquivo('exemplo.txt')
    cliente.registrar_interesse('arquivo_inexistente.txt')
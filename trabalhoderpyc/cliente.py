import rpyc
import tkinter as tk
from tkinter import filedialog, messagebox

class ClienteArquivo:
    def __init__(self, host='localhost', port=18812):
        self.conn = rpyc.connect(host, port)

    def enviar_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, 'rb') as f:
            dados = f.read()
        nome_arquivo = caminho_arquivo.split('/')[-1]
        self.conn.root.enviar_arquivo(nome_arquivo, dados)

    def listar_arquivos(self):
        return self.conn.root.listar_arquivos()

    def baixar_arquivo(self, nome_arquivo, destino):
        dados = self.conn.root.baixar_arquivo(nome_arquivo)
        if dados:
            with open(destino, 'wb') as f:
                f.write(dados)
            messagebox.showinfo("Sucesso", f"Arquivo {nome_arquivo} baixado com sucesso!")
        else:
            messagebox.showerror("Erro", "Arquivo não encontrado no servidor.")

    def criar_interface(self):
        root = tk.Tk()
        root.title("Cliente de Arquivos")

        def selecionar_arquivo():
            caminho_arquivo = filedialog.askopenfilename()
            if caminho_arquivo:
                self.enviar_arquivo(caminho_arquivo)
                messagebox.showinfo("Sucesso", "Arquivo enviado com sucesso!")

        def listar_arquivos():
            arquivos = self.listar_arquivos()
            messagebox.showinfo("Arquivos no servidor", "\n".join(arquivos))

        def baixar_arquivo():
            nome_arquivo = entrada_nome_arquivo.get()
            destino = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=nome_arquivo)
            if nome_arquivo and destino:
                self.baixar_arquivo(nome_arquivo, destino)

        botao_enviar = tk.Button(root, text="Enviar Arquivo", command=selecionar_arquivo)
        botao_enviar.pack(pady=10)

        botao_listar = tk.Button(root, text="Listar Arquivos", command=listar_arquivos)
        botao_listar.pack(pady=10)

        tk.Label(root, text="Nome do arquivo para baixar:").pack(pady=5)
        entrada_nome_arquivo = tk.Entry(root)
        entrada_nome_arquivo.pack(pady=5)

        botao_baixar = tk.Button(root, text="Baixar Arquivo", command=baixar_arquivo)
        botao_baixar.pack(pady=10)

        root.mainloop()

if __name__ == "__main__":
    cliente = ClienteArquivo()
    cliente.criar_interface()

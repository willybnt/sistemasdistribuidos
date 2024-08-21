import rpyc
import tkinter as tk
from tkinter import filedialog, messagebox

# Classe ClienteArquivo responsável por conectar-se ao servidor e manipular arquivos
class ClienteArquivo:
    def __init__(self, host='localhost', port=18812):
        # Conecta ao servidor RPyC utilizando o host e porta especificados
        self.conn = rpyc.connect(host, port)

    # Método para enviar um arquivo ao servidor
    def enviar_arquivo(self, caminho_arquivo):
        # Abre o arquivo no caminho especificado em modo de leitura binária
        with open(caminho_arquivo, 'rb') as f:
            dados = f.read()  # Lê o conteúdo do arquivo
        # Extrai o nome do arquivo a partir do caminho completo
        nome_arquivo = caminho_arquivo.split('/')[-1]
        # Chama o método remoto no servidor para enviar o arquivo
        self.conn.root.enviar_arquivo(nome_arquivo, dados)

    # Método para listar os arquivos disponíveis no servidor
    def listar_arquivos(self):
        # Retorna a lista de arquivos do servidor utilizando um método remoto
        return self.conn.root.listar_arquivos()

    # Método para baixar um arquivo do servidor
    def baixar_arquivo(self, nome_arquivo, destino):
        # Chama o método remoto no servidor para baixar o arquivo pelo nome
        dados = self.conn.root.baixar_arquivo(nome_arquivo)
        if dados:  # Verifica se o servidor retornou dados (se o arquivo foi encontrado)
            # Abre um arquivo no caminho de destino especificado em modo de escrita binária
            with open(destino, 'wb') as f:
                f.write(dados)  # Escreve os dados no arquivo
            # Exibe uma mensagem de sucesso após o download do arquivo
            messagebox.showinfo("Sucesso", f"Arquivo {nome_arquivo} baixado com sucesso!")
        else:
            # Exibe uma mensagem de erro se o arquivo não foi encontrado no servidor
            messagebox.showerror("Erro", "Arquivo não encontrado no servidor.")

    # Método para criar a interface gráfica do cliente
    def criar_interface(self):
        # Cria a janela principal do Tkinter
        root = tk.Tk()
        root.title("Cliente de Arquivos")  # Define o título da janela
        root.configure(bg="#FFC0CB")  # Define a cor de fundo da janela

        # Função para selecionar e enviar um arquivo
        def selecionar_arquivo():
            # Abre um diálogo para seleção de arquivo
            caminho_arquivo = filedialog.askopenfilename()
            if caminho_arquivo:  # Verifica se um arquivo foi selecionado
                self.enviar_arquivo(caminho_arquivo)  # Envia o arquivo selecionado
                # Exibe uma mensagem de sucesso após o envio
                messagebox.showinfo("Sucesso", "Arquivo enviado com sucesso!")

        # Função para listar os arquivos disponíveis no servidor
        def listar_arquivos():
            arquivos = self.listar_arquivos()  # Obtém a lista de arquivos do servidor
            # Exibe a lista de arquivos em uma mensagem
            messagebox.showinfo("Arquivos no servidor", "\n".join(arquivos))

        # Função para baixar um arquivo do servidor
        def baixar_arquivo():
            nome_arquivo = entrada_nome_arquivo.get()  # Obtém o nome do arquivo a partir do campo de entrada
            # Abre um diálogo para selecionar o destino de salvamento do arquivo
            destino = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=nome_arquivo)
            if nome_arquivo and destino:  # Verifica se o nome do arquivo e destino foram especificados
                self.baixar_arquivo(nome_arquivo, destino)  # Baixa o arquivo

        # Cria o botão para enviar arquivo com configuração de cor e estilo
        botao_enviar = tk.Button(root, text="Enviar Arquivo", command=selecionar_arquivo, bg="white", fg="black", relief="flat")
        botao_enviar.pack(pady=10)  # Adiciona o botão à janela com um espaço vertical

        # Cria o botão para listar arquivos com configuração de cor e estilo
        botao_listar = tk.Button(root, text="Listar Arquivos", command=listar_arquivos, bg="white", fg="black", relief="flat")
        botao_listar.pack(pady=10)  # Adiciona o botão à janela com um espaço vertical

        # Cria um rótulo e um campo de entrada para o nome do arquivo a ser baixado
        tk.Label(root, text="Nome do arquivo para baixar:", bg="#FFC0CB", fg="white").pack(pady=5)
        entrada_nome_arquivo = tk.Entry(root, bg="white", fg="black")
        entrada_nome_arquivo.pack(pady=5)  # Adiciona o campo de entrada à janela com um espaço vertical

        # Cria o botão para baixar arquivo com configuração de cor e estilo
        botao_baixar = tk.Button(root, text="Baixar Arquivo", command=baixar_arquivo, bg="white", fg="black", relief="flat")
        botao_baixar.pack(pady=10)  # Adiciona o botão à janela com um espaço vertical

        root.mainloop()  # Inicia o loop principal da interface gráfica

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    cliente = ClienteArquivo()  # Cria uma instância do cliente
    cliente.criar_interface()  # Cria a interface gráfica do cliente

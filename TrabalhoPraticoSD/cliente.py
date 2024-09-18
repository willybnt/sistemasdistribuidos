import rpyc
import time
import threading

def cliente(numero):
    conn = rpyc.connect('localhost', 18861)
    servicos = [("cabelo", 3), ("barba", 4), ("bigode", 5)]

    for i in range(20):
        for servico, duracao in servicos:
            print(f"Cliente {numero}: Tentando cortar {servico}...")
            conn.root.cortar(servico, duracao, numero)
            time.sleep(1)

    conn.close()

if __name__ == "__main__":
    clientes = [threading.Thread(target=cliente, args=(i,)) for i in range(1, 6)]

    for t in clientes:
        t.start()

    for t in clientes:
        t.join()

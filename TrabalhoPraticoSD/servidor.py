import rpyc
import time
import threading

class BarbeiroService(rpyc.Service):
    lock = threading.Lock()

    def exposed_cortar(self, servico, duracao, cliente_id):
        with self.lock:
            print(f"Cliente {cliente_id} está solicitando {servico}...")
            print(f"Servindo {servico} para cliente {cliente_id}...")
            time.sleep(duracao)
            print(f"Serviço de {servico} concluído para cliente {cliente_id}.")

if __name__ == "__main__":
    from rpyc import ThreadedServer
    print("Servidor iniciado!")
    ThreadedServer(BarbeiroService(), port=18861).start()

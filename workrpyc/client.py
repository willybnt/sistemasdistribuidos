import rpyc

class FileClient:
    def __init__(self, host='localhost', port=18812):
        self.conn = rpyc.connect(host, port)

    def upload_file(self, file_name):
        with open('C:/Users/willy/OneDrive/Documentos/faculdade/sistemasdistribuidos/workrpyc/example.txt', 'rb') as f:

            data = f.read()
        self.conn.root.upload_file(file_name, data)

    def list_files(self):
        return self.conn.root.list_files()

    def download_file(self, file_name):
        data = self.conn.root.download_file(file_name)
        if data:
            with open(f'downloaded_{file_name}', 'wb') as f:
                f.write(data)
        else:
            print("File not found on server.")

    def register_interest(self, file_name, validity=60):
        self.conn.root.register_interest(file_name, self, validity)

    def cancel_interest(self, file_name):
        self.conn.root.cancel_interest(file_name, self)

    def notify_event(self, file_name):
        print(f"Notification: {file_name} is now available on the server!")

if __name__ == "__main__":
    client = FileClient()
    client.upload_file('example.txt')
    print(client.list_files())
    client.download_file('example.txt')
    client.register_interest('missing_file.txt')
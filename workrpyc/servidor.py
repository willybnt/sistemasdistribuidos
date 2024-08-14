import rpyc
from rpyc.utils.server import ThreadedServer
import os

class FileServer(rpyc.Service):
    def __init__(self):
        self.files = {}
        self.interests = []

    def exposed_upload_file(self, file_name, file_data):
        with open(file_name, 'wb') as f:
            f.write(file_data)
        self.files[file_name] = file_name
        self.check_interests(file_name)

    def exposed_list_files(self):
        return list(self.files.keys())

    def exposed_download_file(self, file_name):
        if file_name in self.files:
            with open(file_name, 'rb') as f:
                return f.read()
        else:
            return None

    def exposed_register_interest(self, file_name, client, validity):
        self.interests.append((file_name, client, validity))

    def exposed_cancel_interest(self, file_name, client):
        self.interests = [(f, c, v) for f, c, v in self.interests if not (f == file_name and c == client)]

    def check_interests(self, file_name):
        for interest in self.interests:
            if interest[0] == file_name:
                client = interest[1]
                client.notify_event(file_name)
                self.interests.remove(interest)

if __name__ == "__main__":
    server = ThreadedServer(FileServer(), port=18812)
    server.start()

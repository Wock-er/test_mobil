import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


# def client_connect():
#     host = socket.gethostname()  # получение хостнейма локальной машины
#
#     port = 1917
#     client_socket = socket.socket()
#     client_socket.connect((host, port))
#
#     msg = input(' -> ')
#     return client_socket

# def output_massage(client_socket):
#     msg = '->'
#     while msg.lower().strip() != 'bye':
#         client_socket.send(msg.encode())
#         data = client_socket.recv(1024).decode()
#         print(data)
#         msg = input('->')
#     client_socket.close()


class Buttons(BoxLayout):
    def btn_clk(self):
        self.lbl.text = "You have been pressed"


class Mobile(App):
    def build(self):
        return Buttons()


if __name__ == '__main__':
    app = Mobile()

    app.run()

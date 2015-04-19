__author__ = 'ymode'
import socket


class IRC:

    def __init__(self, network, port, nick, channel):
        self.network = network
        self.port = port
        self.nick = nick
        self.channel = channel

    def connect(self):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((self.network, self.port))
        print connection.recv(4096)
        connection.send('NICK ' + self.nick + '\r\n')
        connection.send('USER ' + self.nick + ' ' + self.nick + ' ' + self.nick + ' :ircpie \r\n')
        connection.send('JOIN ' + self.channel + '\r\n')
        while True:
            data = connection.recv(4096)
            if data.find('PING') != -1:
                connection.send('PONG' + data.split()[1] + '\r\n')
            print data

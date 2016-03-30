from threading import Thread,activeCount
import socket
import os

class IpScan:
    def __init__(self,host):
        self.host = host
        self.report = []

    def scan(self,port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            indicator = s.connect_ex((self.host,port))
            if indicator == 0:
                print(port)
                self.report.append(port)
        except:
            pass

    def ipScan(self):
        i = 0
        while i < 65535:
            if activeCount() <= 200:
                Thread(target=self.scan,args=(i,)).start()
                i = i + 1

        while True:
            if activeCount() == 1:
                break


if __name__ == '__main__':
    a = IpScan('202.118.19.26')
    a.ipScan()
    print(a.report,a.host)
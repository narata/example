import socket
host = '202.118.19.26'
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
    print("建立socket错误:%s"%e )

port = 22

try:
    a = s.connect((host,port))
except socket.error as e:
    print("host 端口错误%s"% e)

print(a)
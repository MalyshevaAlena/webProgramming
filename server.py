import socket
import sys


def pars_accept(conn, addr):
    data = b""
    while not b"\n\r" in data:
        text = conn.recv(1024)
        if not text:
            break
        else:
            data += text
        if not data:
            return

    data = data.decode("utf-8")
    if len(data.split(" ")) < 3:
    	return
    data = data.split("\n\r")[0]
    type, address, query = data.split(" ", 2)

    index_file = open('C:\\Users\\Алена\Desktop\web1\git\webProgramming\index.html')
    about_file = open('C:\\Users\\Алена\Desktop\web1\git\webProgramming\\about\\aboutme.html')

    if type == "GET" and (address == "/index.html" or address == "/"):
        send(conn, index_file.read())
    elif type == "GET" and address == "/about/aboutme.html":
        send(conn, about_file.read())        

    index_file.close()
    about_file.close()

def send(conn, data=""):
    conn.send(b"HTTP/1.1 " + "200 OK".encode("utf-8") + b"\r\n")
    conn.send(b"Server: simplehttp\r\n")
    conn.send(b"Connection: close\r\n")
    conn.send(b"Content-Type: " + "text/html; charset=utf-8".encode("utf-8") + b"\r\n")
    conn.send(b"Content-Length: " + bytes(len(data)) + b"\r\n")
    conn.send(b"\r\n")
    conn.send(data.encode("utf-8"))

def main():
    sock = socket.socket()
    sock.bind(('', 8000))
    sock.listen(1)

    try:
        while True:
            conn, addr = sock.accept()
            try:
            	pars_accept(conn, addr)
            finally:
            	conn.close()
    finally:
        sock.close()

if __name__ == "__main__":
    main()
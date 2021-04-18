import socket

target_host = "127.0.0.1"
target_post = 9997

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(b"AAABBBCCC", (target_host, target_post))

# receive some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()

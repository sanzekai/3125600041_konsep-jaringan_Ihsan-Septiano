#!/usr/bin/env python3
"""UDP demo receiver: binds only to localhost; classroom exercise."""
import socket

HOST, PORT = '127.0.0.1', 9999
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    sock.settimeout(30)
    print(f'[UDP receiver] Listening on {HOST}:{PORT} (30 s timeout)')
    try:
        data, addr = sock.recvfrom(4096)
    except socket.timeout:
        print('Timeout: no datagram received. Try running udp_sender.py.')
    else:
        print(f'From {addr[0]}:{addr[1]} | length={len(data)} bytes | data={data!r}')

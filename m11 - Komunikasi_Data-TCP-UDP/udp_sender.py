#!/usr/bin/env python3
"""UDP demo sender: sends one datagram to localhost only."""
import socket

DESTINATION = ('127.0.0.1', 9999)
PAYLOAD = b'halo-udp'
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    n = sock.sendto(PAYLOAD, DESTINATION)
    print(f'[UDP sender] Sent {n} payload bytes to {DESTINATION[0]}:{DESTINATION[1]}')
    print(f'Expected UDP length for this example: 8 + {n} = {8 + n} bytes')

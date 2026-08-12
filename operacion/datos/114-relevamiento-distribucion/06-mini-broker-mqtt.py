"""Broker MQTT 3.1.1 minimo (CONNECT/PUBLISH-QoS1/PUBACK/PINGREQ/DISCONNECT).

Solo para verificar el camino `live` del canal MQTT sin instalar Mosquitto.
No es un broker: no rutea a suscriptores, solo acepta e imprime lo publicado.
"""
import json
import socket
import struct
import sys
import threading

PUBLISHED = []


def _read_remaining_length(sock):
    mult, value = 1, 0
    while True:
        b = sock.recv(1)
        if not b:
            return None
        byte = b[0]
        value += (byte & 127) * mult
        if not (byte & 128):
            return value
        mult *= 128


def handle(conn, addr, out_path):
    try:
        while True:
            head = conn.recv(1)
            if not head:
                break
            ptype = head[0] >> 4
            flags = head[0] & 0x0F
            rlen = _read_remaining_length(conn)
            if rlen is None:
                break
            body = b""
            while len(body) < rlen:
                chunk = conn.recv(rlen - len(body))
                if not chunk:
                    break
                body += chunk

            if ptype == 1:  # CONNECT
                conn.sendall(bytes([0x20, 0x02, 0x00, 0x00]))  # CONNACK ok
            elif ptype == 3:  # PUBLISH
                qos = (flags >> 1) & 0x03
                tlen = struct.unpack(">H", body[:2])[0]
                topic = body[2:2 + tlen].decode("utf-8")
                rest = body[2 + tlen:]
                pid = None
                if qos > 0:
                    pid = struct.unpack(">H", rest[:2])[0]
                    rest = rest[2:]
                PUBLISHED.append({"topic": topic, "qos": qos, "payload": rest.decode("utf-8")})
                with open(out_path, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(PUBLISHED[-1]) + "\n")
                if qos == 1:
                    conn.sendall(bytes([0x40, 0x02]) + struct.pack(">H", pid))  # PUBACK
            elif ptype == 12:  # PINGREQ
                conn.sendall(bytes([0xD0, 0x00]))
            elif ptype == 14:  # DISCONNECT
                break
    except OSError:
        pass
    finally:
        conn.close()


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 1883
    out_path = sys.argv[2] if len(sys.argv) > 2 else "/tmp/mini_broker_published.jsonl"
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(8)
    print(f"mini-broker escuchando en 127.0.0.1:{port}, log -> {out_path}", flush=True)
    while True:
        conn, addr = srv.accept()
        threading.Thread(target=handle, args=(conn, addr, out_path), daemon=True).start()


if __name__ == "__main__":
    main()

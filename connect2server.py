import socket
import struct
import json
import Move as mv

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def receive_current_state(sock):
    
    len_bytes = struct.unpack('>i', recvall(sock, 4))[0]
    current_state_server_bytes = sock.recv(len_bytes)
    json_current_state_server = json.loads(current_state_server_bytes)

    return json_current_state_server

def convert_move_to_json_for_server(move):

    from_ = move.get()["from"]
    to_ = move.get()["to"]
    turn = move.get()["turn"]

    move = {"from": from_, "to": to_, "turn": turn}
    json_move = json.dumps(move)
    return json_move


def connect_to_server(player_name, color):

    #first connection with the server 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        if color == 'white':
            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 5800)
        elif color == 'black':
            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 5801)
        else:
            raise Exception("Se giochi o sei bianco oppure sei nero")
        
        sock.connect(server_address)
        #send player's name to the server
        sock.send(struct.pack('>i', len(player_name)))
        sock.send(player_name.encode())

        while(True):

            state = receive_current_state(sock)
            print("Current state")
            print(state)

            move = mv.Move("e3", "d3", color)

            move_for_server = convert_move_to_json_for_server(move)#convert_move_for_server(move, color)
            sock.send(struct.pack('>i', len(move_for_server)))
            sock.send(move_for_server.encode())

            state = receive_current_state(sock)
            print("Current state")
            print(state)


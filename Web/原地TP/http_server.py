import socket
import datetime
import traceback
import sys
from json import loads as from_json, dumps as jsonify

def log(msg, level: str = 'info', where: str = None) -> None:
    '''Print message'''
    levelmsg = level if level else "null"
    mainmsg = f'[{str(datetime.datetime.now())}][{where if where else (lambda f: f.f_locals["c_logger_where"] if "c_logger_where" in f.f_locals else f.f_code.co_name)(sys._getframe().f_back)}/{levelmsg}] {str(msg if msg is not None else "(null)")}'
    colorlevel = levelmsg.lower()
    if colorlevel.endswith('info'):
        print("\033[1;37;40m%s\033[0m" % mainmsg)
    elif colorlevel.endswith('warn'):
        print("\033[1;33;40m%s\033[0m" % mainmsg)
    elif colorlevel.endswith('error'):
        print("\033[1;31;40m%s\033[0m" % mainmsg)
    else:
        print(mainmsg)

config_adapter_addr, config_adapter_port = "0.0.0.0",10004

def parse_http_request(rawData:bytes):
    lines = rawData.split(b"\r\n")
    if len(lines) < 3:
        return False,None
    sp = 0
    for x in range(1,len(lines)):
        if lines[x] == b"":
            sp = x
            break
    head = lines[0].decode("utf-8").split(" ")
    if len(head) == 3:
        return True,(head[0].lower(),head[1],lines[1:sp],lines[sp:])
    else:
        return False,None

def handle_socket_conn(adapter:socket.socket):
    connection, remote = adapter.accept()
    log(f"accepted connection from {remote}","info")
    with connection:
        content = connection.recv(8192)
        success,result = parse_http_request(content)
        if success:
            log("packet was parsed through http protocol","info")
            response_data = handle_request(result)
            connection.sendall(response_data.encode("utf-8"))
        else:
            log("invaild http request! dropped",'warn')
        log("Connection closed",'info')

def handle_request(result):
    method,path,header,body = result
    CONST_HTTP_RESPONSE_TEMPALTE = \
"""\
HTTP/1.1 302 Redirect\r\n\
Server: AkarinAdapter alpha/1.0\r\n\
Location: /\r\n\
Flag: ZFun{the_server_is_written_by_ltkk_in_5_minutes_and_there_is_no_bug}\r\n\
\r\n\
"""
    return CONST_HTTP_RESPONSE_TEMPALTE

def serve_forever():
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP) as adapter:
        adapter.bind((config_adapter_addr, config_adapter_port))
        adapter.listen(1024)
        log(f"message adapter initialized, listen at {config_adapter_addr}:{config_adapter_port}","info")
        while True:
            try:
                handle_socket_conn(adapter)
            except KeyboardInterrupt:
                log("Bye~",'error')
                break
            except Exception:
                log(f"Unhandled Exception occured!","error")
                traceback.print_exc()
    log("message_loop exited",'info')

serve_forever()
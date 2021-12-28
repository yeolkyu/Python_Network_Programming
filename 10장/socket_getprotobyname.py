# 프로토콜 번호 확인 프로그램

import socket

def get_constants(prefix):
    #socket의 {속성값: 속성문자상수}의 딕셔너리 쌍을 반환한다.
    #prefix = 속성문자상수의 시작 문자열
    return {
        getattr(socket, n):n
        for n in dir(socket)
        if n.startswith(prefix)
    }
     
protocols =get_constants('IPPROTO_') #{속성값: 속성문자상수}

for name in ['icmp','udp','tcp']:
    proto_num =socket.getprotobyname(name) #프로토콜 번호
    const_name =protocols[proto_num]
    print('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(
        name, proto_num, const_name,
        getattr(socket ,const_name)))
#인수를 지정한 소켓 정보 찾기 프로그램

import socket

def get_constants (prefix ):
    """소켓 모듈의 상수를 이름과 맵핑시키는 딕셔너리를 만든다
    """
    return {
        getattr (socket ,n ):n
        for n in dir (socket )
        if n .startswith (prefix )
    }

families =get_constants ('AF_')
types =get_constants ('SOCK_')
protocols =get_constants ('IPPROTO_')

responses =socket .getaddrinfo (
    host ='www.dongyang.ac.kr',
    port ='http',
    family =socket .AF_INET ,
    type =socket .SOCK_STREAM ,
    proto =socket .IPPROTO_TCP ,
    flags =socket .AI_CANONNAME ,
)

for response in responses :
    # Unpack the response tuple
    family ,socktype ,proto ,canonname ,sockaddr =response

    print ('Family        :',families [family ])
    print ('Type          :',types [socktype ])
    print ('Protocol      :',protocols [proto ])
    print ('Canonical name:',canonname )
    print ('Socket address:',sockaddr )
    print ()
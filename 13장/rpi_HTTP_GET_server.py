#라즈베리파이에 연결된 LED를 제어하는 HTTP GET 서버 프로그램

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse
import RPi.GPIO as GP

#다중 query를 &를 기준으로 분리하고 딕셔너리로 반환
def query_parse(query):
        a = query.split("&")
        temp = []
        for item in a:
            temp.append(item.split("="))
        for i in range(len(temp)):
            if len(temp[i]) == 1:
                temp[i].append('')
        
        return dict(temp)

def setGPIO(pin, mode): #라즈베리파이 GPIO 설정
        GP.setmode(GP.BCM)
        GP.setwarnings(False)
        GP.setup(pin, mode)
    
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = parse.urlparse(self.path) #URL 분해
        msg = parsed_path.query #query 분리
        if msg == '': #query가 없으면 종료
            return
        parsed_query = query_parse(msg) #다중 query를 딕서너리로 분해
        
        #query에 따라 LED 제어
        if parsed_query["led"] == "on":
            resp="LED is ON"
            GP.output(18, 1) #LED를 ON
        elif parsed_query["led"] == "off":
            resp="LED is OFF"
            GP.output(18, 0)#LED를 OFF
        else:
            resp="Fault" #요청 오류

        #헤더 전송
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        
        #응답 메시지 전송
        self.wfile.write(resp.encode()) 


setGPIO(18, GP.OUT) #GPIO 18을 출력으로 설정
httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()

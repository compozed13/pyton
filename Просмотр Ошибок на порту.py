import telnetlib
import time
3
port = input('Введите порт - ')
stroka = f'show error ports {port}\n'.encode() 
telnet = telnetlib.Telnet('192.168.136.43')
telnet.read_until(b'UserName:')
telnet.write(b'dff\n')
telnet.read_until(b'PassWord:')
telnet.write(b'\n')
telnet.write(stroka)
time.sleep(2)
all_result = telnet.read_until(b'Excessive', timeout=5)
asd = all_result.decode('utf-8')
asd = asd.split(' ')
a = [i for i in asd if i != '']
print(*a[19:22])
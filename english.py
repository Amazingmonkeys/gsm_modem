import serial


def send_message(com, tel_num, content):
    s = serial.Serial(com, 115200)
    s.write(b'AT+CMGF=1\r\n')
    s.write(b'AT+CSCS="GSM"\r\n')
    s.write(('AT+CMGS=\"' + tel_num + '\"\r\n').encode())
    s.write(content.encode())
    s.write(b'\x1A\r\n')
    s.close()


if __name__ == '__main__':
    send_message("COM8", "15202917156", "hello world")

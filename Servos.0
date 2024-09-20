import time
import board
import pwmio
import socketpool
import wifi

# Conectar a WiFi
wifi.radio.connect("OPPO-A17", "euler-phi")
pool = socketpool.SocketPool(wifi.radio)

print("Conectado a WiFi:", wifi.radio.hostname, wifi.radio.ipv4_address)

# Configuración de servomotores 
pwm_servo1 = pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=50)
pwm_servo2 = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=50)
pwm_servo3 = pwmio.PWMOut(board.GP13, duty_cycle=0, frequency=50)

# Definir los valores de minimo y maximo
min_duty = 1638  # 5% duty cycle de 65535 (~1 ms, 0 grados)
max_duty = 8192  # 10% duty cycle de 65535 (~2 ms, 180 grados)

# Crear un socket de servidor
s = pool.socket()
s.setsockopt(pool.SOL_SOCKET, pool.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)

# Página web 
<!DOCTYPE html>
<head>
    <title>Control de Servos</title>
</head>
<body>
    <h1>Control de Servomotores</h1>
    <p>Servo 1: <input type="range" min="0" max="180" value="90" id="servo1" oninput="sendValue(1, this.value)"></p>
    <p>Servo 2: <input type="range" min="0" max="180" value="90" id="servo2" oninput="sendValue(2, this.value)"></p>
    <p>Servo 3: <input type="range" min="0" max="180" value="90" id="servo3" oninput="sendValue(3, this.value)"></p>

    <script>
    function sendValue(servo, angle) {
        fetch("/set?servo=" + servo + "&angle=" + angle);
    }
    </script>
</body>
</html>
"""

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    buffer = bytearray(1024)
    bytes_received = conn.recv_into(buffer)
    request = str(buffer[:bytes_received], 'utf-8')
    
    if "GET / " in request:
        response = html
    elif "GET /set?" in request:
        try:
            _, query = request.split("GET /set?")
            query, _ = query.split(" HTTP/1.1")
            params = query.split("&")
            servo_number = int(params[0].split("=")[1])
            angle = int(params[1].split("=")[1])
            
            duty_cycle = int(min_duty + (angle / 180) * (max_duty - min_duty))
            
            if servo_number == 1:
                pwm_servo1.duty_cycle = duty_cycle
            elif servo_number == 2:
                pwm_servo2.duty_cycle = duty_cycle
            elif servo_number == 3:
                pwm_servo3.duty_cycle = duty_cycle
            
            response = "HTTP/1.1 200 OK\n\nOK"
        except Exception as e:
            response = f"HTTP/1.1 400 Bad Request\n\nError: {e}"
    else:
        response = "HTTP/1.1 404 Not Found\n\nPage not found"
    
    conn.send(response)
    conn.close()



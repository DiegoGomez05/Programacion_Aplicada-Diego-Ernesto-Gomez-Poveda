import network
import socket
import time
import board
import pwmio
from adafruit_motor import servo
from math import pow, sqrt

# Conexión a la red Wi-Fi
ssid = "PruebaPi"
password = "11223344"

# Configuración del Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Conectando a Wi-Fi...")
while not wifi.isconnected():
    time.sleep(1)
print("Conectado a", ssid)
print("IP:", wifi.ifconfig()[0])

# Configuración de los servos
pwm_hombro = pwmio.PWMOut(board.GP0, frequency=50)
pwm_codo = pwmio.PWMOut(board.GP15, frequency=50)
servo_hombro = servo.Servo(pwm_hombro, min_pulse=500, max_pulse=2500)
servo_codo = servo.Servo(pwm_codo, min_pulse=500, max_pulse=2500)

# HTML para la página de control
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brazo Virtual</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body { margin: 0; background-color: black; }
        canvas { display: block; }
        .controls {
            position: absolute;
            bottom: 20px;
            right: 20px;
            background: rgba(220, 220, 220, 0.9);
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }
        h1 { color: white; text-align: center; }
    </style>
</head>
<body>
    <h1>Control de Servos del Brazo Robótico</h1>

    <script>
        function updateServo(value, type) {
            fetch('/move_' + type + '?angle=' + value)
                .then(response => response.text())
                .then(data => console.log(data))
                .catch(error => console.error('Error:', error));
        }
        
        class BrazoRobotico {
            constructor(escena) {
                this.hombro = new THREE.Group();
                this.crearBase(escena);
                this.crearBrazo();
                escena.add(this.hombro);
            }

            crearBase(escena) {
                const geometriaBase = new THREE.CylinderGeometry(3.5, 3.5, 0.5, 5);
                const materialBase = new THREE.MeshStandardMaterial({
                    color: 0xEAEAEA,
                    metalness: 0.9,
                    roughness: 0.1,
                    emissive: 0x333333,
                    emissiveIntensity: 0.3
                });
                const base = new THREE.Mesh(geometriaBase, materialBase);
                base.position.y = -0.25;
                escena.add(base);
            }

            crearBrazo() {
                const textura = new THREE.TextureLoader().load('https://threejsfundamentals.org/threejs/resources/images/wall.jpg');

                const materialBrazo = new THREE.MeshStandardMaterial({
                    map: textura,
                    metalness: 0.8,
                    roughness: 0.3,
                    emissive: 0xFF4500,
                    emissiveIntensity: 0.6
                });

                const materialCodo = new THREE.MeshStandardMaterial({
                    color: 0x87CEEB,
                    metalness: 0.9,
                    roughness: 0.2,
                    emissive: 0x4682B4,
                    emissiveIntensity: 0.6
                });

                const materialMagneto = new THREE.MeshStandardMaterial({
                    color: 0xEAEAEA,
                    metalness: 0.7,
                    roughness: 0.1,
                    emissive: 0xFFFFFF,
                    emissiveIntensity: 0.8
                });

                // Brazo
                const brazo = new THREE.Mesh(new THREE.BoxGeometry(1.3, 4, 1.3), materialBrazo);
                brazo.position.y = 2;
                this.hombro.add(brazo);

                // Codo
                const articulacionHombro = new THREE.Mesh(new THREE.SphereGeometry(0.80, 32, 32), materialCodo);
                articulacionHombro.position.y = 4;
                this.hombro.add(articulacionHombro);

                const codo = new THREE.Mesh(new THREE.BoxGeometry(1.5, 1.5, 1.5), materialCodo);
                codo.position.set(0, 4, 0);
                this.hombro.add(codo);

                const antebrazo = new THREE.Mesh(new THREE.BoxGeometry(0.8, 5, 0.8), materialBrazo);
                antebrazo.position.set(0, 2.5, 0);
                codo.add(antebrazo);

                const geometriaMagneto = new THREE.DodecahedronGeometry(1);
                const magneto = new THREE.Mesh(geometriaMagneto, materialMagneto);
                magneto.position.set(0, 3.5, 0);
                antebrazo.add(magneto);

                this.brazo = brazo;
                this.codo = codo;
            }

            rotarHombro(angulo) {
                this.hombro.rotation.z = THREE.MathUtils.degToRad(-angulo);
            }

            rotarCodo(angulo) {
                this.codo.rotation.z = THREE.MathUtils.degToRad(-angulo);
            }
        }

        const escena = new THREE.Scene();
        const camara = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderizador = new THREE.WebGLRenderer({ antialias: true });
        renderizador.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderizador.domElement);
        renderizador.setClearColor(0x000000);

        const brazo = new BrazoRobotico(escena);

        camara.position.set(0, 5, 10);
        camara.lookAt(0, 3, 0);

        const luzAmbiente = new THREE.AmbientLight(0x404040, 2);
        escena.add(luzAmbiente);

        const luzPuntual = new THREE.PointLight(0xFFFFFF, 2);
        luzPuntual.position.set(10, 10, 10);
        escena.add(luzPuntual);

        function animar() {
            requestAnimationFrame(animar);
            renderizador.render(escena, camara);
        }
        animar();

        // Crear controles de sliders
        const contenedorControles = document.createElement('div');
        contenedorControles.className = 'controls';
        document.body.appendChild(contenedorControles);

        const deslizadorHombro = document.createElement('input');
        deslizadorHombro.type = 'range';
        deslizadorHombro.min = -90;
        deslizadorHombro.max = 90;
        deslizadorHombro.step = 1;
        deslizadorHombro.value = 0;  // Ángulo inicial del hombro

        deslizadorHombro.oninput = function () {
            const angulo = parseFloat(this.value);
            brazo.rotarHombro(angulo);
            updateServo(angulo, 'hombro');
        };

        const deslizadorCodo = document.createElement('input');
        deslizadorCodo.type = 'range';
        deslizadorCodo.min = 0;
        deslizadorCodo.max = 90;
        deslizadorCodo.step = 1;
        deslizadorCodo.value = 0;  // Ángulo inicial del codo

        deslizadorCodo.oninput = function () {
            const angulo = 180 - parseFloat(this.value);  // Invertir el ángulo (0 se convierte en 180 y 180 en 0)
            brazo.rotarCodo(angulo);
            updateServo(angulo, 'codo');
        };

        const etiquetaHombro = document.createElement('label');
        etiquetaHombro.innerText = 'Hombro: ';
        const etiquetaCodo = document.createElement('label');
        etiquetaCodo.innerText = 'Codo: ';

        contenedorControles.appendChild(etiquetaHombro);
        contenedorControles.appendChild(deslizadorHombro);
        contenedorControles.appendChild(document.createElement('br'));
        contenedorControles.appendChild(etiquetaCodo);
        contenedorControles.appendChild(deslizadorCodo);

        // Rotación inicial del brazo y codo
        brazo.rotarHombro(0);  // Ángulo inicial de 45 grados para el hombro
        brazo.rotarCodo(90);   // Ángulo inicial de 120 grados para el codo
    </script>
</body>
</html>
"""

# Funciones para mover los servos con curvas de Bézier
def bezier_curve(t, p0, p1, p2):
    return (1 - t) * (1 - t) * p0 + 2 * (1 - t) * t * p1 + t * t * p2

def calcular_trayectoria(current_angle, target_angle, steps=50):
    trayectoria = []
    for i in range(steps + 1):
        t = i / steps
        interpolated_angle = bezier_curve(t, current_angle, (current_angle + target_angle) / 2, target_angle)
        trayectoria.append(interpolated_angle)
    return trayectoria

def mover_servo(servo_motor, current_angle, target_angle):
    trayectoria = calcular_trayectoria(current_angle, target_angle)
    for angle in trayectoria:
        servo_motor.angle = angle
        time.sleep(0.05)  # Tiempo entre pasos para suavizar el movimiento

def move_servo_hombro(angle):
    print(f"Moviendo el hombro a {angle} grados")
    current_angle = servo_hombro.angle if servo_hombro.angle is not None else 0
    mover_servo(servo_hombro, current_angle, angle)

def move_servo_codo(angle):
    print(f"Moviendo el codo a {angle} grados")
    current_angle = servo_codo.angle if servo_codo.angle is not None else 90
    mover_servo(servo_codo, current_angle, angle)

# Configuración del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 80))
server_socket.listen(1)

print("Esperando conexión en el puerto 80...")

while True:
    conn, addr = server_socket.accept()
    print("Conexión de", addr)
    
    # Crear un buffer para recibir los datos
    buffer = bytearray(1024)
    bytes_received = conn.recv_into(buffer)  # Usar recv_into en lugar de recv

    # Convertir los bytes recibidos a cadena
    request_str = str(buffer[:bytes_received], 'utf-8')
    
    if 'GET /move_hombro?' in request_str:
        try:
            angle = int(request_str.split('angle=')[1].split(' ')[0])
            move_servo_hombro(angle)
        except Exception as e:
            print(f"Error al mover el hombro: {e}")
    elif 'GET /move_codo?' in request_str:
        try:
            angle = int(request_str.split('angle=')[1].split(' ')[0])
            move_servo_codo(angle)
        except Exception as e:
            print(f"Error al mover el codo: {e}")

    # Enviar respuesta al cliente
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-Type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(html.encode('utf-8'))
    conn.close()



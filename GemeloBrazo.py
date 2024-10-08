#Falta convertir valores registros y  mem en hexa
#Mem y registros repetidos Quitar uno
#ordenar registros y memoria

import network
import socket
import ure
import json
import time


#BACKEND MEM#########################
import array
import uctypes

memory={}

struct_32 = {
    "value": uctypes.UINT32 | 0  # UINT32 es un entero sin signo de 32 bits, y 0 es el offset en la estructura
}

def get_uctype(address):
    if  address not in memory:
        memory[address]=uctypes.struct(address, struct_32)
    return memory[address]



   
    
def read_memory(address,rd):
    assert address % 4 == 0, f"The address {address} is not divisible by 4."
    print('read_memory',address)
    return get_uctype(address).value

def write_memory(address,data):
    assert address % 4 == 0, f"The address {address} is not divisible by 4."
    print( 'write_memory',address,data)
    get_uctype(address).value=data
     
 

def malloc(num_bytes,rd):
    assert num_bytes % 4 == 0, f"The number {num_bytes} is not divisible by 4."
    buff_0 = array.array('b', (10+_ for _ in range(num_bytes)))
    dir0 = uctypes.addressof(buff_0)
    print('malloc',num_bytes,dir0,type(dir0))
    for address in range(dir0,dir0+num_bytes,4):
        write_memory(address,0)
    
    return dir0

#################################


URL_other='https://gerardomunoz.github.io'

# Connect to Wi-Fi
ssid = 'Ejemplo'
password = '12345678'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection
while not wlan.isconnected():
    pass

print('Connected to Wi-Fi')
print(wlan.ifconfig())

# HTML content to serve

htmls = ["""
<!DOCTYPE html> 
<html>
<head lang="en">
    <meta charset="utf-8">
    <title>Gemelo virtual</title>
    <style>
        body { margin: 0; }
        #controls {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            padding: 10px;
            box-sizing: border-box;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 10px;
            color: white;
        }
        #controls label {
            margin-right: 10px;
        }
        #controls input[type="range"] {
            margin: 0 10px;
        }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/three@0.126.1/build/three.min.js"></script>
</head>
<body>
    
    <div id="arm"></div>
    <h1>BRAZO</h1>
    <div id="error"></div>


""", """
  

<div id="controls">
        <div>
            <label>Seleccione el archivo
            <input type="file" id="csvFile" accept=".csv">
            <button onclick="Tama()">Cargar CSV</button></label>
        </div>
        <button onclick="baile()">Bailar</button>
       
       
        <div> 
            <label for="rangeInput">Hombro:</label>
            <input type="range" id="rangeInput" name="rangeInput" min="-45" max="45" onchange="moverShoulder(this.value)">
         
            <label for="rangeInput1">Codo:</label>
            <input type="range" id="rangeInput1" name="rangeInput1" min="0" max="180" onchange="moverElbow(this.value)">
         
            <label for="rangeInput2">Camara:</label>
            <input type="range" id="rangeInput2" name="rangeInput2" min="0" max="360" onchange="moverPlat(this.value)">
        </div>

    <script>

	src="https://cdn.jsdelivr.net/npm/three@0.126.1/build/three.min.js"

		

		

		
		let a1 = 0.3;
		let a2 = 0.5;
		let a3 = 0.5;
		let plat_large = 1;
		let base_L = 0.2;
		let espesor_gen = 0.02;
		let ancho_arm_2 = 0.06;

""", """

        // Define a point in 3D space
		const point = new THREE.Vector3();

		// Set initial LED color and arm dimensions
		let color_led = 0x00fff0;
		const amarillo= 0x00F2E300;
		const cafe= 0x00A9540E;
		const negro=0x00000000;
		const blanco=0x00FFFFFF;
		const azul_osc =0x00044C80;
		const rojo = 0xff0000;
		// Set up Three.js scene and camera
		const width = window.innerWidth;
		const height = window.innerHeight*0.85;
		const scene = new THREE.Scene();
		const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
		camera.position.x = 0;
		camera.position.y = 8;
		camera.position.z = 0;
		camera.lookAt(0, 0, 0);
		// Create WebGL renderer and append it to the DOM
		const renderer = new THREE.WebGLRenderer();
		renderer.setSize(width, height);
		const arm_DOM = document.getElementById("arm");
		arm_DOM.appendChild(renderer.domElement);
		
		// Define a small dot for visualization
		let dot = new THREE.BoxGeometry(0.01, 0.01, 0.01);
		
		// error label
		const error_DOM = document.getElementById("error");
		error_DOM.innerHTML = "Error="
		

""", """

       // Set up the base of the mechanical arm
		let geometry = new THREE.BoxGeometry(plat_large, plat_large*0.05, plat_large*0.65);
		let material2 = new THREE.MeshBasicMaterial({ color:cafe});
		const plat = new THREE.Mesh(geometry, material2);
		scene.add(plat);
		

		
		// Base chiquita
		
		geometry = new THREE.BoxGeometry(base_L, espesor_gen, base_L);
		material = new THREE.MeshBasicMaterial({ color: amarillo});
		let base = new THREE.Mesh(geometry, material);
		base.translateY(base_L);
		plat.add(base);
		
		
		
		// Paredes laterales
		
		material = new THREE.MeshBasicMaterial({ color: cafe});
		geometry = new THREE.BoxGeometry(base_L, a1, espesor_gen);
		let pared1= new THREE.Mesh(geometry, material);
		pared1.translateZ(base_L/2);
		pared1.translateY(espesor_gen);
		base.add(pared1);
		
		let pared2= new THREE.Mesh(geometry, material);
		pared2.translateZ(-base_L/2);
		pared2.translateY(espesor_gen);
		base.add(pared2);
		
""", """

        // Vallas frontal y trasera
		geometry = new THREE.BoxGeometry(base_L, a1, espesor_gen);
		let valla1= new THREE.Mesh(geometry, material);
		valla1.translateX(base_L/2);
		valla1.translateY(espesor_gen);
		base.add(valla1); 
		
		let valla2= new THREE.Mesh(geometry, material);
		valla2.translateX(-base_L/2);
		valla2.translateY(espesor_gen);
		base.add(valla2); 
		
		
		// Triangulo medio
		geometry = new THREE.BoxGeometry(0.05, 0.25*a1, 0.2);
		material = new THREE.MeshBasicMaterial({ color: blanco});
		let trian = new THREE.Mesh( geometry, material );
		trian.translateY(0.05);
		base.add( trian);
		
		
		
		// Servos de los lados
		geometry = new THREE.BoxGeometry(0.1, 0.05, 0.05);
		material = new THREE.MeshBasicMaterial({ color: azul_osc});
		let servo1_1 = new THREE.Mesh( geometry, material );
		servo1_1.translateZ(espesor_gen);
		pared1.add( servo1_1);
		
		let servo2_2 = new THREE.Mesh( geometry, material );
		servo2_2.translateZ(-espesor_gen);
		pared2.add( servo2_2);
		
""", """

        // Tope arm a2 pared 2
		
		
        let shoulder_final = new THREE.Object3D();
		shoulder_final.translateY(a2/2);
        col_neg_2.add(shoulder_final);
		
		geometry = new THREE.BoxGeometry(base_L, ancho_arm_2, espesor_gen);
		material = new THREE.MeshBasicMaterial({ color: blanco});
		let tope_arm_a2_pared_2 = new THREE.Mesh( geometry, material );
		tope_arm_a2_pared_2.translateX(base_L/2);
		shoulder_final.add( tope_arm_a2_pared_2);
		
		
		// Brazo pared 1	
		
		// Base arm a2
		
		
		
		
		geometry = new THREE.BoxGeometry(base_L, espesor_gen, espesor_gen);
		material = new THREE.MeshBasicMaterial({ color: negro});
		
		let base_arm_a2_pared_1 = new THREE.Mesh( geometry, material );
		base_arm_a2_pared_1.translateZ(base_L);
		base_arm_a2_pared_1.translateX(-base_L/2);
		shoulder_pos.add( base_arm_a2_pared_1);
		
		let elbow = new THREE.Object3D();
		base_arm_a2_pared_1.add( elbow);
		
		
		// Brazo pared 1
		geometry = new THREE.BoxGeometry(ancho_arm_2, a2/3, espesor_gen);
		
		
        
""", """

material = new THREE.MeshBasicMaterial({ color: rojo});
		let col1_1 = new THREE.Mesh( geometry, material );
		elbow.add( col1_1);
		
		// Tope arm1 a2 pared 1
		

		
		let elbow_2 = new THREE.Object3D();
		elbow_2.translateY(a2 / 6);
		col1_1.add( elbow_2);
		
		geometry = new THREE.BoxGeometry(ancho_arm_2, a2, espesor_gen);
		material = new THREE.MeshBasicMaterial({ color: blanco});
		let col1_2 = new THREE.Mesh( geometry, material );
		col1_2.translateY(a2 / 2);
		elbow_2.add( col1_2);
		
		
		let elbow_3 = new THREE.Object3D();
		elbow_3.translateY(a2 / 2);
		col1_2.add( elbow_3);
		
		geometry = new THREE.BoxGeometry(ancho_arm_2, a2/3, espesor_gen);
		material = new THREE.MeshBasicMaterial({ color: color_led});
		let col1_3 = new THREE.Mesh( geometry, material );
		col1_3.translateY(-a2 / 6);
		
		elbow_3.add( col1_3);
	      
		
		/* 
		**********************************
		
		middle trian arm, a2 part
		
		**********************************
		*/
		
		
		// Brazo middle in trian
		
        let shoulder_central = new THREE.Object3D();
        base.add(shoulder_central);
""", """

        geometry = new THREE.BoxGeometry(ancho_arm_2, a2, base_L/1.5);
		material = new THREE.MeshBasicMaterial({ color: amarillo});
		let col_central_trian = new THREE.Mesh( geometry, material );
	
		col_central_trian.translateY(a2/2);
		shoulder_central.add( col_central_trian);

		geometry = new THREE.BoxGeometry(a3, ancho_arm_2, espesor_gen);
		material = new THREE.MeshBasicMaterial({ color: amarillo});
		let arm_a3_pared_1 = new THREE.Mesh( geometry, material );
		arm_a3_pared_1.rotateZ(Math.PI/2);
		arm_a3_pared_1.translateX(-a3/2);
		col1_3.add( arm_a3_pared_1);
		
        
		// Arm a3 pared 2
		geometry = new THREE.BoxGeometry(a3, ancho_arm_2, espesor_gen);
		material = new THREE.MeshBasicMaterial({ color: amarillo});
		let arm_a3_pared_2 = new THREE.Mesh( geometry, material );
		arm_a3_pared_2.translateY(-a3/2-0.01);
		arm_a3_pared_2.translateZ(-base_L);
		arm_a3_pared_2.translateX(base_L/2-2*ancho_arm_2);
		arm_a3_pared_2.rotateZ(-Math.PI/2);
		col1_3.add( arm_a3_pared_2);
		
        
        // Tope doble del arm a3
""", """

        let wrist = new THREE.Object3D();
		wrist.translateX(-a3/2);
		wrist.translateZ(-base_L/2);
        arm_a3_pared_1.add(wrist);
        
        
        
        geometry = new THREE.BoxGeometry(espesor_gen, espesor_gen, base_L);
        material = new THREE.MeshBasicMaterial({ color: blanco});
        let tope_arm_a3 = new THREE.Mesh( geometry, material );
        wrist.add( tope_arm_a3);
        
        /* 
        **********************************
        
        arm a3  
        
        **********************************
        */	
		
		material = new THREE.MeshBasicMaterial({ color: color_led});
		
		// Create a hand at the end of the arm
		geometry = new THREE.TorusGeometry(0.1, 0.01, 3, 9, 5.6);
		let hand = new THREE.Mesh(geometry, material);
        hand.translateZ(0.1)
        hand.translateY(-0.1)
		hand.rotation.y = Math.PI / 2;
		hand.rotation.x = 2*Math.PI;
		hand.rotation.z = -Math.PI/2;
		wrist.add(hand);

""", """

// Set up parameters for a line to visualize the arm trajectory
		const MAX_POINTS = 1000;
		material = new THREE.LineBasicMaterial({ color: 0x0000ff });
		geometry = new THREE.BufferGeometry();
		const positions = new Float32Array(MAX_POINTS * 3);
		let last_point = 0;
        
		// Set initial positions for the arm trajectory line
		geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
		const line = new THREE.Line(geometry, material);
		scene.add(line);
        
		// Define two points for the Bezier curve
		const P0 = new THREE.Vector3(a2, a1 / 2, -a3);
		const P1 = new THREE.Vector3(a2, a1 / 2, a3);
		var t = 0;

		var P0_camara = new THREE.Vector3(0, 5, 0);
		var P1_camara = new THREE.Vector3(0, 0, 5);
		var t_camara=0
		let tween;
		animate()
		

""", """
  

// Start the animation loop
		
		function cambiarSize(boxGeometry, new_X, new_Y, new_Z, new_SX, new_SY, new_SZ) {
			// Obtener las dimensiones actuales del boxGeometry
			var actual_X = boxGeometry.geometry.parameters.width;
			var actual_Y = boxGeometry.geometry.parameters.height;
			var actual_Z = boxGeometry.geometry.parameters.depth;
			console.log("**************************************");
			console.log(boxGeometry.geometry.parameters.width);
			console.log(boxGeometry.geometry.parameters.height);
			console.log(boxGeometry.geometry.parameters.depth);
			console.log("--");
			console.log(new_X);
			console.log("--");
			console.log(boxGeometry.geometry.parameters.width);
			// Calcular los factores de escala para cada dimensión
			var scaleX = new_X / actual_X;
			var scaleY = new_Y / actual_Y;
			var scaleZ = new_Z / actual_Z;
			
			// Escalar el boxGeometry para que coincida con las nuevas dimensiones
			boxGeometry.scale.set(scaleX, scaleY, scaleZ);
			
			// Actualizar las dimensiones del boxGeometry para que reflejen las nuevas dimensiones
			boxGeometry.geometry.parameters.width = new_X;
			boxGeometry.geometry.parameters.height = new_Y;
			boxGeometry.geometry.parameters.depth = new_Z;

""", """

// Actualizar las dimensiones del boxGeometry para que reflejen las nuevas dimensiones
			boxGeometry.geometry.parameters.width = new_X;
			boxGeometry.geometry.parameters.height = new_Y;
			boxGeometry.geometry.parameters.depth = new_Z;
			
			
			console.log(boxGeometry.geometry.parameters.width);
			console.log("******************************************");
			
			/*
			*/
			if (new_SX) {
				boxGeometry.translateX(-boxGeometry.position.x + new_SX);
			}
			if (new_SZ) {
				boxGeometry.translateZ(-boxGeometry.position.z + new_SZ);
			}
			if (new_SY) {
				boxGeometry.translateY(-boxGeometry.position.y + new_SY);
			}
		}
		
		function increaseWidth(a1,a2 ,a3 ,plat_large , base_L , espesor_gen , ancho_arm_2) {
			cambiarSize(arm_a3_pared_2,a3, ancho_arm_2, espesor_gen, new_SZ=a3/2);
		}
		

""", """
  
function  animate(){
			
			//if (t <= 1) {
				requestAnimationFrame(animate);
                //}
                
                // Calculate inverse kinematics and update arm positions
                let th1p, th2p, th3p, R;
                R = bezier2(P0, P1, t);
                [th1p, th2p, th3p] = inv_kin(R);
                // Loop through the Bezier curve parameter
                if (t <= 1) {
                    t = t + 0.01;
                }
                
                



                // Visualize the position of the wrist with a dot
                let dot_i = new THREE.Mesh(dot, material);
                wrist.getWorldPosition(point);
                scene.add(dot_i);
                
                // Update the arm trajectory line
                positions[last_point] = point.x;
                positions[last_point + 1] = point.y;
                positions[last_point + 2] = point.z;
                last_point = last_point + 3;
               
""", """
line.geometry.attributes.position.needsUpdate = true;
                error_DOM.innerHTML = "Error="+R.distanceTo(point)
                
                R_camara = bezier2(P0_camara, P1_camara, t_camara);
                camera.position.set(R_camara.x,R_camara.y,R_camara.z)
                //console.log(camera.position)
                camera.lookAt(0, 0, 0)
                if (t_camara <= 1) {
                    t_camara = t_camara + 0.00033;
                }
                else {
                    t_camara = 0
			}
            
			// Render the scene
			renderer.render(scene, camera);
            
            
            

		}

        function agregarOReemplazarParametroURL(parametro, valor) {
			var url = window.location.href;

			// Verificar si la URL ya tiene parámetros
			if (url.indexOf('?') !== -1) {
				// Si ya tiene parámetros, eliminarlos
				url = url.split('?')[0];
			}

			// Agregar el nuevo parámetro al final
			url += '?' + encodeURIComponent(parametro) + '=' + encodeURIComponent(valor);

		
""", """
  

// Actualizar la URL en la barra de direcciones del navegador
			window.history.replaceState(null, null, url);
		}
        
        function moverShoulder (angle) {


            console.log("Ángulo seleccionado:", angle);
			moverSh(angle);
			agregarOReemplazarParametroURL("Shoulder", angle);
            // Esta función puede realizar acciones basadas en el ángulo seleccionado
            // Por ejemplo, puedes actualizar algún elemento en la página con este valor
        }
        
        function moverElbow (angle) {
			console.log("Ángulo seleccionado:", angle);
			moverEb(angle);
			agregarOReemplazarParametroURL("Elbow", angle)
            
            // Esta función puede realizar acciones basadas en el ángulo seleccionado
            // Por ejemplo, puedes actualizar algún elemento en la página con este valor
        }
		
		
        function moverPlat (angle) {
			console.log("Ángulo seleccionado:", angle);
			agregarOReemplazarParametroURL("Plat", angle)
            moverPt(angle);

		

""", """
agregarOReemplazarParametroURL("Elbow", angle)
            
            // Esta función puede realizar acciones basadas en el ángulo seleccionado
            // Por ejemplo, puedes actualizar algún elemento en la página con este valor
        }
		
		
        function moverPlat (angle) {
			console.log("Ángulo seleccionado:", angle);
			agregarOReemplazarParametroURL("Plat", angle)
            moverPt(angle);
            // Esta función puede realizar acciones basadas en el ángulo seleccionado
            // Por ejemplo, puedes actualizar algún elemento en la página con este valor
        }
		
		
		function Tama() {
			const fileInput = document.getElementById('csvFile');
			const file = fileInput.files[0];
			const reader = new FileReader();
			
			reader.onload = function(e) {
				const contents = e.target.result;
				const lines = contents.split(/\r?\n|\r/);
				const data = [];
				
				lines.forEach(line => {
					const values = line.split(';');
					data.push(values);
				});

""", """
  

console.log(data);
				a1=parseFloat(data[0][1]);
				a2 =parseFloat(data[1][1]);
				a3 =parseFloat(data[2][1]);
				plat_large =parseFloat(data[3][1]); 
				base_L =parseFloat(data[4][1]); 
				espesor_gen =parseFloat(data[5][1]); 
				ancho_arm_2 =parseFloat(data[6][1]);
				console.log("a1");
				console.log(a1);
				console.log("a2");
				console.log(a2);
				console.log("a3");
				console.log(a3);
				console.log("plat_large");
				console.log(plat_large);
				console.log("base_L");
				console.log(base_L);
				console.log("espesor_gen");
				console.log(espesor_gen);
				console.log("ancho_arm_2");
				console.log(ancho_arm_2);
			};
			a1,a2 ,a3 ,plat_large , base_L , espesor_gen , ancho_arm_2
			reader.readAsText(file);
			increaseWidth(a1,a2 ,a3 ,plat_large , base_L , espesor_gen , ancho_arm_2);
		}
		
""", """
// Function to turn the LED on
		function led_on() {
			material.color.setRGB(1, 1, 1);
		}
		
		// Function to turn the LED off
		function led_off() {
			material.color.setRGB(0, 0, 1);
		}
		
		// Function to quit or reset
		function quit() {
			
			
			material.color.setRGB(0, 0, 0);
		}
		

			// Función para realizar un movimiento de baile
	function realizar_movimiento(Shoul, Elbow_1, Plat, angle, delay) {
		return new Promise(resolve => {
			setTimeout(() => {
				movimiento_de_baile(Shoul, Elbow_1, Plat, angle, 0); // No esperar después del movimiento
				resolve();
			}, delay);
		});
	}


""", """
  
function baile() {
    
		// Realizar secuencialmente cada movimiento con su respectivo tiempo de delay
		realizar_movimiento(false, false, false, 0, 1000).then(() => {
			return realizar_movimiento(true, false, false, 45, 100);
		}).then(() => {
			return realizar_movimiento(false, true, false, 80, 800);
		}).then(() => {
		
			return realizar_movimiento(false, false, false, 0, 1000);
		
		}).then(() => {
			return realizar_movimiento(true, false, false, -45, 100);
		}).then(() => {
			return realizar_movimiento(false, true, false, -80, 800);
		
		}).then(() => {

			return realizar_movimiento(false, false, false, 0, 1000);

		}).then(() => {
			return realizar_movimiento(true, false, false, 85, 100);
		}).then(() => {
			return realizar_movimiento(false, true, false, 60, 800);
		}).then(() => {

			return realizar_movimiento(false, false, false, 0, 1000);
		
		}).then(() => {
			return realizar_movimiento(false, true, false, 30, 800);
		}).then(() => {

			return realizar_movimiento(false, false, false, 0, 1000);
		
		}).then(() => {
			return realizar_movimiento(true, false, false, 0, 100);
		}).then(() => {
			return realizar_movimiento(false, true, false, 0, 800); // El último movimiento no espera después de ejecutarse
		}).then(() => {
			
			return realizar_movimiento(false, false, false, 0, 1000);
		});
	}

""", """
// Function to turn the LED on
		function led_on() {
			material.color.setRGB(1, 1, 1);
		}
		
		// Function to turn the LED off
		function led_off() {
			material.color.setRGB(0, 0, 1);
		}
		
		// Function to quit or reset
		function quit() {
			
			
			material.color.setRGB(0, 0, 0);
		}
		

			// Función para realizar un movimiento de baile
	function realizar_movimiento(Shoul, Elbow_1, Plat, angle, delay) {
		return new Promise(resolve => {
			setTimeout(() => {
				movimiento_de_baile(Shoul, Elbow_1, Plat, angle, 0); // No esperar después del movimiento
				resolve();
			}, delay);
		});
	}


""", """
  

// Función para mover el hombro
		function moverSh(angle) {
			// Lógica para mover el hombro
			shoulder_pos.rotation.z = angle*Math.PI/180;
			shoulder_neg.rotation.z = angle*Math.PI/180;
			shoulder_final.rotation.z = -angle*Math.PI/180;
			shoulder_central.rotation.z = angle*Math.PI/180;
			console.log("Moviendo hombro a " + angle + " grados");
		}
		
		// Función para mover el codo
		function moverEb(angle) {
			// Lógica para mover el codo
			console.log("Moviendo codo a " + angle + " grados");
			elbow.rotation.z = angle*Math.PI/180;
			elbow_3.rotation.z = angle*Math.PI/180;
			elbow_2.rotation.z = -angle*Math.PI/180;
		}
		
		// Función para mover la plataforma
		function moverPt(angle) {
			// Lógica para mover la plataforma
			console.log("Moviendo plataforma a " + angle + " grados");
			plat.rotation.y = angle*Math.PI/180;
		}
		
		function delay_baile(ms) {
			return new Promise(resolve => setTimeout(resolve, ms));
		}

""", """
function movimiento_de_baile(Shoul, Elbow_1, Plat_1, angle, delay) {
			
			// Lógica para ejecutar los movimientos de baile
			console.log(Shoul, Elbow_1, Plat_1, angle, delay );
			if (Shoul) {
				moverSh(angle);
			}
			if (Elbow_1) {
				moverEb(angle);
			}
			if (Plat_1) {
				moverPt(angle);
			}
			
			// Esperar el tiempo de delay antes de retornar
			delay_baile(delay);
		}





		// Function to calculate inverse kinematics
		function inv_kin(P) {
			const x03 = -P.x;
			const z03 = P.y;
			const y03 = P.z;
			const th1 = Math.atan2(y03, x03);
			const r1 = Math.sqrt(x03 ** 2 + y03 ** 2);
			const r2 = -(z03 - a1);
			const phi2 = Math.atan2(r2, r1);
			const r3 = Math.sqrt(r1 ** 2 + r2 ** 2);
			const phi1 = Math.acos((a3 ** 2 - a2 ** 2 - r3 ** 2) / (-2 * a2 * r3));
			const th2 = phi2 - phi1;
			const phi3 = Math.acos((r3 ** 2 - a2 ** 2 - a3 ** 2) / (-2 * a2 * a3));
			const th3 = Math.PI - phi3;
			return [th1, th2, th3];
		}

		// Function for Bezier interpolation between two points
		function bezier2(P0, P1, t) {
			const R = P0.clone().multiplyScalar(1 - t).add(P1.clone().multiplyScalar(t));
			return R;
		}
		
		</script>

	</body>
</html>
"""]
for i in range(len(htmls)):
    html = htmls[i].replace('\r\n', '\n')  # Primero aseguramos que todo sea \n
    htmls[i] = html.replace('\n', '\r\n')  # Luego los convertimos todos a \r\n

def str2tuple(txt):
    print('str2tuple',txt)
    return txt.strip("()[}").replace('%2C',',').split(",")
                  

# Function to handle incoming requests
def handle_request(client):
    request = client.recv(1024)
    request_str = request.decode('utf-8')
    
    print('Received request:')
    print(request_str)

    # Serve the HTML page
    if 'GET / ' in request_str or 'GET /api' not in request_str:
        client.send('HTTP/1.1 200 OK\r\n')
        client.send('Content-Type: text/html\r\n')
        client.send('Connection: close\r\n\r\n')
        for html in htmls:
            client.send(html)
            time.sleep_ms(100)
        client.close()
        
      
    
    # Handle the API request
    elif 'GET /api' in request_str:
        match = ure.search(r'GET /api\?([^\s]+) HTTP', request_str)
        response_dir={}
        if match:
            query_string = match.group(1)
            params = query_string.split('&')
            json_data = {}
            for param in params:
                key, value = param.split('=')
                json_data[key] = value
            
            print("Received JSON data:")
            dat_r=json.dumps(json_data)
            print(json_data)  # Pretty print the JSON data
            for key,val in json_data.items():
                print('dic',key,val)
                if key=='malloc':
                    numb,rd = str2tuple(val)
                    numb=int(numb)
                    address=malloc(numb,rd)
                    for addr_i in range(address,address+numb,4):
                        response_dir[addr_i]=0
                    response_dir[rd]=address
                elif key=='write_memory':
                    
                    #cleaned_string = val.strip("()")
                    #addr,dat = cleaned_string.split(",")
                    addr,dat = str2tuple(val)
                    addr=int(addr)
                    dat=int(dat)
                    write_memory(addr,dat)
                    response_dir[addr]=dat
                elif key=='read_memory':
                    addr,rd = str2tuple(val)
                    addr=int(addr)
                    dat=read_memory(addr,rd)
                    response_dir[addr]=dat
                    response_dir[rd]=dat
#     def malloc(num_bytes):
#     print('malloc',num_bytes)
# 
# 
# def write_memory(address,data):
#     print( 'write_memory',address,data)
#     
#     
# read_memory(address):
#     print('read_memory',address)
        response_json = json.dumps(response_dir)
        print(response_json)
        client.send('HTTP/1.1 200 OK\r\n')
        #client.send('Content-Type: text/plain\r\n')
        #client.send('Connection: close\r\n\r\n')
        #client.send('Request received and processed\r\n')
        client.send('Content-Type: application/json\r\n')
        client.send('Connection: close\r\n\r\n')
        client.send(response_json)  # Send JSON response
    
    client.close()

# Start the server
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    server_socket = socket.socket()
    server_socket.bind(addr)
    server_socket.listen(1)
    
    print('Server listening on', addr)
    
    while True:
        client, addr = server_socket.accept()
        print('Client connected from', addr)
        handle_request(client)

# Start the web server
start_server()
#Powered by ChatGPT

// Logica Servomotor 1

        let Servomotor_1_Led_1_Status = false;
        let Servomotor_1_Led_2_Status = false;
        let Servomotor_1_Led_3_Status = false;

        // Función para actualizar el valor del campo de texto
        function Servomotor_1_actualizarEstado() {
            const estadoLedInput = document.getElementById("Servomotor_1_Estado_Led_1_Input");
            estadoLedInput.value = Servomotor_1_Led_1_Status ? "On" : "Off";

            const Estado_Led_2_Input = document.getElementById("Servomotor_1_Estado_Led_2_Input");
            Estado_Led_2_Input.value = Servomotor_1_Led_2_Status ? "On" : "Off";

            const Estado_Led_3_Input = document.getElementById("Servomotor_1_Estado_Led_3_Input");
            Estado_Led_3_Input.value = Servomotor_1_Led_3_Status ? "On" : "Off";
        }

        // Función para encender el LED
        function Servomotor_1_Change_Led_1_Status_To_True() {
            Servomotor_1_Led_1_Status = true;
            Servomotor_1_Led_2_Status = false;
            Servomotor_1_Led_3_Status = false;
            Servomotor_1_actualizarEstado();
           // alert('El estado del LED es ' + (Led_1_Status ? "On" : "Off"));
        }

        // Función para apagar el LED
        function Servomotor_1_Change_Led_2_Status_To_True() {
            Servomotor_1_Led_1_Status = false;
            Servomotor_1_Led_2_Status = true;
            Servomotor_1_Led_3_Status = false;
            Servomotor_1_actualizarEstado();
           // alert('El estado del LED es ' + (Led_1_Status ? "On" : "Off"));
        }

        function Servomotor_1_Change_Led_3_Status_To_True() {
            Servomotor_1_Led_1_Status = false;
            Servomotor_1_Led_2_Status = false;
            Servomotor_1_Led_3_Status = true;
            Servomotor_1_actualizarEstado();
           // alert('El estado del LED es ' + (Led_1_Status ? "On" : "Off"));
        }

        // Llamar a la función de actualización al cargar la página
        Servomotor_1_actualizarEstado();

        //Transition
        //Transition
        //Transition
        //Transition

        // Logica Servomotor 2

        let Servomotor_2_Led_1_Status = false;
        let Servomotor_2_Led_2_Status = false;
        let Servomotor_2_Led_3_Status = false;

        // Función para actualizar el valor del campo de texto
        function Servomotor_2_actualizarEstado() {
            const estadoLedInput = document.getElementById("Servomotor_2_Estado_Led_1_Input");
            estadoLedInput.value = Servomotor_2_Led_1_Status ? "On" : "Off";

            const Estado_Led_2_Input = document.getElementById("Servomotor_2_Estado_Led_2_Input");
            Estado_Led_2_Input.value = Servomotor_2_Led_2_Status ? "On" : "Off";

            const Estado_Led_3_Input = document.getElementById("Servomotor_2_Estado_Led_3_Input");
            Estado_Led_3_Input.value = Servomotor_2_Led_3_Status ? "On" : "Off";
        }

        // Función para encender el LED
        function Servomotor_2_Change_Led_1_Status_To_True() {
            Servomotor_2_Led_1_Status = true;
            Servomotor_2_Led_2_Status = false;
            Servomotor_2_Led_3_Status = false;
            Servomotor_2_actualizarEstado();
           // alert('El estado del LED es ' + (Led_1_Status ? "On" : "Off"));
        }

        // Función para apagar el LED
        function Servomotor_2_Change_Led_2_Status_To_True() {
            Servomotor_2_Led_1_Status = false;
            Servomotor_2_Led_2_Status = true;
            Servomotor_2_Led_3_Status = false;
            Servomotor_2_actualizarEstado();
           // alert('El estado del LED es ' + (Led_1_Status ? "On" : "Off"));
        }

        function Servomotor_2_Change_Led_3_Status_To_True() {
            Servomotor_2_Led_1_Status = false;
            Servomotor_2_Led_2_Status = false;
            Servomotor_2_Led_3_Status = true;
            Servomotor_2_actualizarEstado();
           // alert('El estado del LED es ' + (Led_1_Status ? "On" : "Off"));
        }

        // Llamar a la función de actualización al cargar la página
        Servomotor_2_actualizarEstado();


        //Transition
        //Transition
        //Transition
        //Transition
        
        // Logica Servomotor 3

        let Servomotor_3_Led_1_Status = false;
        let Servomotor_3_Led_2_Status = false;
        let Servomotor_3_Led_3_Status = false;

        // Función para actualizar el valor del campo de texto
        function Servomotor_3_actualizarEstado() {
            const estadoLedInput = document.getElementById("Servomotor_3_Estado_Led_1_Input");
            estadoLedInput.value = Servomotor_3_Led_1_Status ? "On" : "Off";

            const Estado_Led_2_Input = document.getElementById("Servomotor_3_Estado_Led_2_Input");
            Estado_Led_2_Input.value = Servomotor_3_Led_2_Status ? "On" : "Off";

            const Estado_Led_3_Input = document.getElementById("Servomotor_3_Estado_Led_3_Input");
            Estado_Led_3_Input.value = Servomotor_3_Led_3_Status ? "On" : "Off";
        }

        // Función para encender el LED
        function Servomotor_3_Change_Led_1_Status_To_True() {
            Servomotor_3_Led_1_Status = true;
            Servomotor_3_Led_2_Status = false;
            Servomotor_3_Led_3_Status = false;
            Servomotor_3_actualizarEstado();
           // alert('El estado del LED es ' + (Led_1_Status ? "On" : "Off"));
        }

        // Función para apagar el LED
        function Servomotor_3_Change_Led_2_Status_To_True() {
            Servomotor_3_Led_1_Status = false;
            Servomotor_3_Led_2_Status = true;
            Servomotor_3_Led_3_Status = false;
            Servomotor_3_actualizarEstado();
           // alert('El estado del LED es ' + (Led_1_Status ? "On" : "Off"));
        }

        function Servomotor_3_Change_Led_3_Status_To_True() {
            Servomotor_3_Led_1_Status = false;
            Servomotor_3_Led_2_Status = false;
            Servomotor_3_Led_3_Status = true;
            Servomotor_3_actualizarEstado();
           // alert('El estado del LED es ' + (Led_1_Status ? "On" : "Off"));
        }

        // Llamar a la función de actualización al cargar la página
        Servomotor_3_actualizarEstado();
    
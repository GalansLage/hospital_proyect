// Obtén una lista de citas (esto se conectará a la base de datos más adelante)
const listaCitas = [
    { nombre: 'Dr. Pérez', fecha: '2024-03-10', hora: '12:30', especialidad: 'Medicina General' },
    // Agrega más citas aquí...
];

// Función para crear una tarjeta
function crearTarjeta(cita) {
    const tarjeta = document.createElement('div');
    tarjeta.className = 'col-md-4 mb-3';
    tarjeta.innerHTML = `
        <div class="card shadow degradadoClaro">
            <div class="card-body">
                <h5 class="card-title">Cita con ${cita.nombre}</h5>
                <p class="card-text">Fecha: ${cita.fecha}</p>
                <p class="card-text">Hora: ${cita.hora}</p>
                <p class="card-text">Especialidad: ${cita.especialidad}</p>
                <!-- Otros detalles de la cita -->
            </div>
        </div>
    `;
    return tarjeta;
}

// Itera sobre la lista de citas y crea las tarjetas dinámicamente
const contenedor = document.getElementById('contenedor-citas');
for (let i = 0; i < 20; i++) {
    const tarjeta = crearTarjeta(listaCitas[0]);
    contenedor.appendChild(tarjeta);
};

// Función para verificar si hay una sesión iniciada
function verificarSesion() {
    const sesionIniciada = localStorage.getItem('sesionIniciada');
    if (sesionIniciada === 'true') {
        
        mostrarMenu();
    } else {
        // No se muestra el modal automáticamente al cargar la página
    }
}

function showLoginModal() {
    $('#overlay').modal('show');

    // $('#loginForm').submit(function(e) {
    //     e.preventDefault();
        
    //     const usuario = $('#usuario').val();
    //     const contrasena = $('#contrasena').val();

    //     if (verificarCredenciales(usuario, contrasena)) {
    //         localStorage.setItem('sesionIniciada', true);
    //         localStorage.setItem('usuario', usuario);
    //         $('#overlay').modal('hide');
    //         window.location.href = usuario + ".html";
    //     } else {
    //         alert('Credenciales incorrectas. Inténtalo de nuevo.');
    //     }
    // });
}

function showRegisterModal() {
    $('#overlay2').modal('show');
    $('#overlay').modal('hide');
}

function verificarCredenciales(usuario, contrasena) {
    const usuarios = {
        'paciente': '1234',
        'medico': '1234',
        'admin': '1234'
    };

    return usuarios[usuario] === contrasena;
}

function mostrarMenu() {
    const usuario = localStorage.getItem('usuario');
    const miBoton = document.getElementById("btnLogin");
    const menuDesplegable = document.getElementById("menuDesplagable");
    const perfil = document.getElementById("perfil");

    

}

function cerrarSesion() {
    localStorage.setItem('sesionIniciada', false);
    $('#btnLogin').html('Iniciar Sesión');
    $('#btnLogin').attr('onclick', 'showLoginModal()');
}

$(document).ready(function() {
    verificarSesion();
});

function mostrarSeccion(idSeccion) {
    var secciones = document.querySelectorAll('article section');
    
    secciones.forEach(function(seccion) {
      seccion.classList.remove('seccion-visible');
      seccion.classList.add('seccion-oculta');
    });
    
    var seccionMostrar = document.getElementById(idSeccion);
    seccionMostrar.classList.remove('seccion-oculta');
    seccionMostrar.classList.add('seccion-visible');
  }

function habilitarEdicion() {
    // Habilita los campos para edición
    document.getElementById("nombre").readOnly = false;
    document.getElementById("apellidos").readOnly = false;
    document.getElementById("fechaNacimiento").readOnly = false;
    document.getElementById("genero").disabled = false;
    document.getElementById("correoElectronico").readOnly = false;
    document.getElementById("especialidad").readOnly = false;
}

function guardarCambios() {
    // Aquí puedes implementar la lógica para guardar los cambios en una base de datos o donde corresponda
    document.getElementById("nombre").readOnly = true;
    document.getElementById("apellidos").readOnly = true;
    document.getElementById("fechaNacimiento").readOnly = true;
    document.getElementById("genero").disabled = true;
    document.getElementById("correoElectronico").readOnly = true;
    document.getElementById("especialidad").readOnly = true;
    alert("Cambios guardados correctamente.");
}

document.getElementById('cita-form').addEventListener('submit', async (event) => {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Obtén los valores de los campos del formulario
    const idPaciente = 1;
    const idMedico = 1;
    const fecha = document.getElementById('cita').value;
    const hora = document.getElementById('hora').value;
    const motivo = document.getElementById('motivo').value;
    

    // Crea un objeto con los datos de la cita
    const citaData = {
        idPaciente,
        idMedico,
        fecha,
        hora,
        motivo,
    };

    try {
        // Realiza una solicitud POST al backend utilizando fetch
        const response = await fetch('/api/citas/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(citaData),
        });

        if (response.ok) {
            // La cita se creó correctamente
            console.log('Cita creada con éxito');
        } else {
            // Maneja errores de respuesta (por ejemplo, validación)
            console.error('Error al crear la cita');
        }
    } catch (error) {
        console.error('Error de red:', error);
    }
});

  




const form = document.getElementById('form');
if (form){
    form.addEventListener('submit', function() {
        document.querySelector('.loading').style.display = 'block';
        document.querySelector('.button').style.display = "none";
    });
}

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
  document.body.style.backgroundColor = "white";
}

const modals = document.querySelectorAll('.modal');
const btnAbrirModal = document.querySelectorAll('.boton_modal');
const btnCerrarModal = document.querySelectorAll('.cerrar_modal');

btnAbrirModal.forEach((btn, index) => {
    btn.addEventListener('click', () => {
        modals[index].showModal();
    })
})

btnCerrarModal.forEach((btn, index) => {
    btn.addEventListener('click', () => {
        modals[index].close();
    })
})
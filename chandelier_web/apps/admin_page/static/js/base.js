// Alert para eliminar
(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar la cotizacion, no podra recuperarla?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

})();

//validar imagenes
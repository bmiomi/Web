$(document).ready(function () {
    $("#example2").DataTable();
    $("#example2 tbody").on("click ", "tr", function (e) {
        $(this).addClass("selected").siblings().removeClass('selected')
        $.get("modalc", function (data) {
            $(".ajaxs").append(data);
        }).done(function () {
            $('#modalCliente').modal("show");
            console.log("proceso recibido");
        }).fail(function () {
            console.log("Error en el proceso");
        }).always(function () {
            console.log("proceso Finalizado");
        });
    });




});
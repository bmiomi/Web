$(document).ready(function () {

    var t = $("#example2").DataTable({
        ajax:"/Lp",
        columns:[
            {data:"Id"},
            {data:"Nombre"},
            {data:"Apellido"},
            {data:"FechaNacimiento"},
        ]    
    });

    
    $("#example2 tbody").on("click ","tr",function(e){ 
        $(this).addClass("selected").siblings().removeClass('selected');
        a=t.row(this).data();
        $.get("modalc", function (data) {
            $(".ajaxs").append(data);
        }).done(function () {
            $('#modalCliente').modal("show");
               $("#id").val(a.Id);
               $("#Nombre").val(a.Nombre); 
               $("#Apellido").val(a.Apellido); 
               $("#FechaNacimiento").val(a.FechaNacimiento); 
               console.log("proceso recibido");
            }).fail(function (e) {
            console.log("Error al Obtener la Peticion",e);
            alert("Erro De Peticion")
        }).always(function () {
            console.log("proceso Finalizado");
        });
    });
});




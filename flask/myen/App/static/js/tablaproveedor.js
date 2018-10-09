$(document).ready(function () {
    var t = $("#example2").DataTable();

$("#example2 tbody").on("click ","tr",function(e){ 
        $(this).addClass("selected").siblings().removeClass('selected');
        a=t.row(this).data();
        llamado(a);
    });
});

var llamado=function (row) { 
    $(".ajaxs").load("modalP",function (a) {
        $('#modalProveedor').modal("show");
           $("#CI").val( row[0]);
           $("#Nombre").val(row[1]); 
           $("#Apellido").val(row[2]); 
           $("#FechaNacimiento").val(row[3]); 
           $("#Sexo").val(row[4]); 
           var url= 'deleteP/'+ row[0]
           $("#Eliminar").attr('href',url);  
    });   
}
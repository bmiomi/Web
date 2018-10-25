
$(document).ready(function () {
    var t = $("#example2").DataTable();
    $("#example2 tbody").on("click ","tr",function(e){ 
        $(this).addClass("selected").siblings().removeClass('selected');
        a=t.row(this).data();
        llamado(a);
        console.log(a);
    });
    
});

var llamado=function (row) { 
    $(".ajaxs").load("modalP",function (a) {
        $('#modalProveedor').modal("show");
           $("#RasonSocial").val( row[0]);
           $("#CI").val( row[1]);
           $("#Direccion").val(row[2]); 
           $("#Correo").val(row[3]); 
           $("#Convencional").val(row[4]);
           $("#Celular").val(row[5]);

           var url = 'deleteP/'+row[1]
           $("#Eliminar").attr('href',url);  
       

    });
}

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
           $("#RasonSocial").val( row[0]);
           $("#CI").val( row[1]);
           $("#Nombre").val(row[2]); 
           $("#Apellido").val(row[3]); 
           $("#FechaNacimiento").val(row[4]);
           var a =row[5];
        if ( a == "M"){
            $("#Sexo #Sexo-0").attr('checked','true');
        }else if(a == "F"){
            $("#Sexo #Sexo-1").attr('checked','true');
        };
        var url= 'deleteP/'+ row[6]
        $("#Eliminar").attr('href',url);  
    });
}


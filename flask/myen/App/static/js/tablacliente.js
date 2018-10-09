$(document).ready(function () {
    var t = $("#example2").DataTable();

$("#example2 tbody").on("click ","tr",function(e){ 
        $(this).addClass("selected").siblings().removeClass('selected');
        a=t.row(this).data();
        llamado(a);
    });
});

var llamado=function (row) { 
    $(".ajaxs").load("modalc #modalCliente",function () {
        $('#modalCliente').modal("show");
           $("#id").val( row[0]);
           $("#Nombre").val(row[1]); 
           $("#Apellido").val(row[2]); 
           $("#FechaNacimiento").val(row[3]); 
           var url= 'delete/'+ row[0]
           $("#Eliminar").attr('href',url);  
      })   

/*     var t = $("#example2").DataTable({
        ajax:"/Lp",
        columns:[
            {data:"Id"},
            {data:"Nombre"},
            {data:"Apellido"},
            {data:"FechaNacimiento"},
        ]    
    });
 */    

}
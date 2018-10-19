$(document).ready(function () {    
var t = $("#example2").DataTable();
$("#example2 tbody").on("click ","tr",function(e){ 
        $(this).addClass("selected").siblings().removeClass('selected');
        a=t.row(this).data();
        llamado(a);
       getid()
   });
  );

var llamado=function (row) { 
    console.log(row);
    $(".ajaxs").load("modalPr",function (a) {
        $('#modalProducto').modal("show");  
           $("#Codigo").val( row[0]);
           $("#nombre").val(row[1]); 
           $("#Categoria").val(row[2]); 
           $("#Precio").val(row[3]); 
           $("#stock").val(row[4]); 
           var url= 'deleteP/'+ row[0]
           $("#Eliminar").attr('href',url);  
    });   
}

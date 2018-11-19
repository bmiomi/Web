$(document).ready(function () {    
var t = $("#example2").DataTable();

$("#example2 tbody").on("click ","tr",function(e){ 
        $(this).addClass("selected").siblings().removeClass('selected');
        a=t.row(this).data();
        llamado(a);
   });
   
});


var llamado=function (row) { 
    console.log(row);
    $(".ajaxs").load("modalPr",function (a) {
        $('#modalProducto').modal("show");  
           $("#Codigo").val( row[0]);
           $("#nombre").val(row[1]); 
           $("#P_U_C").val(row[2]); 
           $("#P_U_V").val(row[3]); 
           $("#stock").val(row[4]); 
           var url= '/Productos/deletePr/'+ row[0]
           console.log(url);
    });   
}

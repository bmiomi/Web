
$(document).ready(function () {
    var t = $("#example2").DataTable();

var elemento1=document.getElementById('ingreso').addEventListener("click",myClickListener);
var elemento2=document.getElementById('salida').addEventListener("click", myClickListener2);

});

function myClickListener(){
console.log("object");
llamado()
}

function myClickListener2(){
    console.log("object*x");
    llamado()
    }

var llamado=function () { 
    $("#example2 ").click( "#ingreso" ,function (e) { 
        e.preventDefault();
          $(".ajaxs").load("modalAl",function () {
        $('#modalalmacen').modal("show");
    });
    });
  
}




var salida =function(){

    $("#example2 tbody").on("click ","a",function(e){ 
        $(this).addClass("selected").siblings().removeClass('selected');
        llamado()
   });

}

var ingreso=function(){

    $("#example2 tbody").on("click ","a",function(e){ 
        $(this).addClass("selected").siblings().removeClass('selected');
        llamado()
   });

}
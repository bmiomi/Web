$(document).ready(function () {
   agregarmodal();
});
/**Insetado en modal em main */
function agregarmodal(){
    $("#cont").click(function(){ 
        $.ajax({
            url:"/modal",
            dataType: "html",
            success: function (result) {
                $("#callmodal").append(result);
                $("#exampleModal").modal();
            },
            error:function(error){
                console.log("Error"+error);
            }              
        });               
    });
};
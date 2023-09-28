$(document).ready(function () {

});
function showLoader(){
    $("#loaderContainer").show();
    $("body").css("overflow", "hidden");

}
function hideLoader(){
    $("#loaderContainer").hide();
    $("body").css("overflow", "auto");

}
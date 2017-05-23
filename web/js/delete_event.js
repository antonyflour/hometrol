/**
 * Created by anton on 09/05/2017.
 */

function deleteEvent(id){
    $("#div-first").hide();
    $("#div-loader").show();
    var request = new XMLHttpRequest();
    request.open('GET','deleteEvent.php?event_id='+id+'&rand='+Math.random(),true);
    request.send(null);
    request.onreadystatechange = function(){
        if(this.readyState == 4){
            if(this.status==200){
                location.reload();
            }
            else{
                window.alert("Impossibile eliminare l'evento");
            }
        }
    }

}
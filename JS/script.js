function showtime(){
    document.getElementById('currentTime').innerHTML=new Date().toUTCString();
}
showtime();
setInterval(function(){
    showtime();
},1000);
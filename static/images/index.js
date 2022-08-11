const sidebar = document.getElementsByClassName("list-items");
const openbtn = document.getElementById("sidebar_btn");
const closebtn = document.getElementsByClassName("btn-close");




openbtn.onclick =  function () {
    sidebar.style.display = "block"
}

closebtn.onclick =  function () {
    sidebar.style.display = "none"
    
}
let menu = document.querySelector(".menu");

document.oncontextmenu = function(e){
  e.preventDefault();
  menu.style.transform = "scale(1)"; 
  menu.style.left = `${e.clientX}px`;
  menu.style.top = `${e.clientY}px`;
}

document.onclick = function(e) {
  if (e.target != menu) {
    menu.style.transform = "scale(0)";
  }
}
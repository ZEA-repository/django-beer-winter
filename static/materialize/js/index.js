if ('serviceWorker' in navigator) {
	  navigator.serviceWorker.register("/sw.js", {scope: '/'})
	  	.then((reg) => console.log('sw reg', reg))
	  	.catch((err) => console.log('sw not reg', err));
	}

$(document).ready(function(){
	$('.scrollspy').scrollSpy();
	$('.sidenav').sidenav();
});
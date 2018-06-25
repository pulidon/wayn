var infoUsuario = {
	nombre:"",
	apellido:"",
	correo:"",
	contrasena:"",
	cafe:"",
	frutos:"",
	te:"",
	jugo:"",
	olor:"",
	tierra:"",
	estilo:"",
	balance:"",
	plan:""
};
var dataToStore;


function Next(pregunta, eleccion){
	switch (pregunta){
		case 1:
			$("#carouselArchitecture").carousel("next");
			infoUsuario.cafe=eleccion;
			break;
		case 2:
			$('#carouselArchitecture').carousel('next');
			infoUsuario.frutos=eleccion;
			break;
		case 3:
			$('#carouselArchitecture').carousel('next');
			infoUsuario.te=eleccion;
			break;
		case 4:
			$('#carouselArchitecture').carousel('next');
			infoUsuario.jugo=eleccion;
			break;
		case 5:
			$('#carouselArchitecture').carousel('next');
			infoUsuario.olor=eleccion;
			break;
		case 6:
			$('#carouselArchitecture').carousel('next');
			infoUsuario.tierra=eleccion;
			//var localData = JSON.parse(localStorage.getItem('someData'));
			break;
		case 7:
			$('#carouselArchitecture').carousel('next');
			infoUsuario.estilo=eleccion;
			dataToStore = JSON.stringify(infoUsuario);
			localStorage.setItem('someData', dataToStore);
			//console.log(infoUsuario);
			break;
		}
}



$(document).ready(function(){ //animacion barra progreso
				var progreso=14.28;
			  $('button').click(function(){
			  	 $('.progress-bar').html(Math.round(progreso)+'%');
			  	 $(".progress-bar").css("width", progreso+'%');
			  	 progreso=progreso+14.28;
				});
});


$('.nav-link').click(function() {
			    var sectionTo = $(this).attr('href');
			    $('html, body').animate({
			      scrollTop: $(sectionTo).offset().top
			    }, 1500);
});



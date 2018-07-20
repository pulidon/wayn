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


$(document).ready(function(){ //animacion barra progreso
	$("#plan-2").on( "click", function() {
  $( "#precio_ahorro" ).html("<span class='signo_peso'>$</span>30.200");
  $( "#precio_envio" ).html("<span class='signo_peso'>$</span>9.900");
  $( "#precio_envio" ).css("color","#333");
  $( "#precio_total" ).html("<span class='signo_peso'>$</span>79.800");
  $( "#precio_super" ).html("Precio supermercado: $110.000");
});

$("#plan-3").on( "click", function() {
  $( "#precio_ahorro" ).html("<span class='signo_peso'>$</span>46.300");
  $( "#precio_envio" ).html("GRATIS");
  $( "#precio_envio" ).css("color","#179b77");
  $( "#precio_total" ).html("<span class='signo_peso'>$</span>118.700");
  $( "#precio_super" ).html("Precio supermercado: $165.000");
});

$("#plan-4").on( "click", function() {
  $( "#precio_ahorro" ).html("<span class='signo_peso'>$</span>64.300");
  $( "#precio_envio" ).html("GRATIS");
  $( "#precio_envio" ).css("color","#179b77");
  $( "#precio_total" ).html("<span class='signo_peso'>$</span>155.700");
  $( "#precio_super" ).html("Precio supermercado: $220.000");
});
});

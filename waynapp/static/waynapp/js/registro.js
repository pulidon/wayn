$(document).ready(function(){

	var localData = JSON.parse(localStorage.getItem('someData'));
	//CUERPO
	if (localData.cafe=='expreso') {
			document.getElementById("cuerpo").value=100;
	} else if (localData.cafe=='tinto') {
			document.getElementById("cuerpo").value=80;
	}
	else if (localData.cafe=='latte') {
			document.getElementById("cuerpo").value=60;
	}
	else if (localData.cafe=='perico') {
			document.getElementById("cuerpo").value=40;
	}
	else {
			document.getElementById("cuerpo").value = 20;
	}
	//FRUTOS ROJOS
	if (localData.frutos=='rojos') {
			document.getElementById("frutos_rojos").value=90;
			document.getElementById("frutos_negros").value=20;
	} else if (localData.frutos=='negros') {
		 document.getElementById("frutos_rojos").value=20;
			document.getElementById("frutos_negros").value=90;
	}
	else if (localData.frutos=='mixtos') {
			document.getElementById("frutos_rojos").value=50;
			document.getElementById("frutos_negros").value=50;
	}
	//ASTRINGENCIA
	if (localData.te=='negro') {
			document.getElementById("astringencia").value=90;
	} else if (localData.te=='rojo') {
		 document.getElementById("astringencia").value=50;
	}
	else if (localData.te=='verde') {
			document.getElementById("astringencia").value=25;
	 }
	//FRUTAS
	if (localData.jugo=='citrico-tropical') { //sauvignon blanc
			document.getElementById("citrico").value=90;
			document.getElementById("fruta_hueso").value=25;
			document.getElementById("fruta_tropical").value=90;
	} else if (localData.jugo=='citrico-hueso') {
		 document.getElementById("citrico").value=90;
			document.getElementById("fruta_hueso").value=90;
			document.getElementById("fruta_tropical").value=25;
	}
	else if (localData.jugo=='tropical-hueso') {
			document.getElementById("citrico").value=25;
			document.getElementById("fruta_hueso").value=90;
			document.getElementById("fruta_tropical").value=90;
	 }
	//AROMA
	if (localData.olor=='hierba') { //sauvignon blanc
			document.getElementById("aroma_herbal").value=80;
			document.getElementById("aroma_floral").value=20;
			} else if (localData.olor=='floral') {
			document.getElementById("aroma_herbal").value=20;
			document.getElementById("aroma_floral").value=80;
		} else if (localData.olor=='mixto') {
			document.getElementById("aroma_herbal").value=50;
			document.getElementById("aroma_floral").value=50;
	}
	//TIERRA
	if (localData.tierra=='poco') { //sauvignon blanc
			document.getElementById("tierra").value=25;
			} else if (localData.tierra=='medio') {
			document.getElementById("tierra").value=50;
		}
		else if (localData.tierra=='mucho') {
			document.getElementById("tierra").value=90;
		}

});


$('.form').find('input, textarea').on('keyup blur focus', function (e) {

  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight');
			} else {
		    label.removeClass('highlight');
			}
    } else if (e.type === 'focus') {

      if( $this.val() === '' ) {
    		label.removeClass('highlight');
			}
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

$('.tab a').on('click', function (e) {

  e.preventDefault();

  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');

  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();

  $(target).fadeIn(600);

});

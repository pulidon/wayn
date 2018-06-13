var localData = JSON.parse(localStorage.getItem('someData'));
//CUERPO
if (localData.cafe=='expreso') {
    document.forms['registro']['cuerpo'].value=100;
} else if (localData.cafe=='tinto') {
    document.forms['registro']['cuerpo'].value=80;
}
else if (localData.cafe=='latte') {
    document.forms['registro']['cuerpo'].value=60;
}
else if (localData.cafe=='perico') {
    document.forms['registro']['cuerpo'].value=40;
}
else {
    document.forms['registro']['cuerpo'].value = 20;
}
//FRUTOS ROJOS
if (localData.frutos=='rojos') {
    fRojos=90;
    fNegros=20;
} else if (localData.frutos=='negros') {
   fRojos=20;
    fNegros=90;
}
else if (localData.frutos=='mixtos') {
    fRojos=50;
    fNegros=50;
}
//ASTRINGENCIA
if (localData.te=='negro') {
    astringencia=90;
} else if (localData.te=='rojo') {
   astringencia=50;
}
else if (localData.te=='verde') {
    astringencia=25;
 }
//FRUTAS
if (localData.jugo=='citrico-tropical') { //sauvignon blanc
    citrico=90;
    fHueso=25;
    fTropical=90;
} else if (localData.jugo=='citrico-hueso') {
   citrico=90;
    fHueso=90;
    fTropical=25;
}
else if (localData.jugo=='tropical-hueso') {
    citrico=25;
    fHueso=90;
    fTropical=90;
 }
//AROMA
if (localData.olor=='hierba') { //sauvignon blanc
    herbal=80;
    floral=20;
    } else if (localData.olor=='floral') {
    herbal=20;
    floral=80;
	} else if (localData.olor=='mixto') {
		herbal=50;
		floral=50;
}
//TIERRA
if (localData.tierra=='poco') { //sauvignon blanc
    tierra=25;
    } else if (localData.tierra=='medio') {
    tierra=50;
  }
  else if (localData.tierra=='mucho') {
    tierra=90;
  }


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

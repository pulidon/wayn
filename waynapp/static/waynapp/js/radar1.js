var localData = JSON.parse(localStorage.getItem('someData'));
//console.log(localData);
var cuerpo,fRojos,fNegros,astringencia,citrico,fHueso,fTropical,herbal,floral,tierra;
var dataToStore;


//CUERPO
if (localData.cafe=='expreso') {
    cuerpo=100;
} else if (localData.cafe=='tinto') {
    cuerpo=80;
}
else if (localData.cafe=='latte') {
    cuerpo=60;
}
else if (localData.cafe=='perico') {
    cuerpo=40;
}
else {
    cuerpo = 20;
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


var color = Chart.helpers.color;
var config = {
	type: 'radar',
	data: {
	labels: ['Cuerpo', 'Frutos Rojos', 'Frutos Negros','Astringencia','Citrico','Fruta hueso','Fruta tropical', 'Herbal','Floral','Tierra'],
	datasets: [{
	label: 'Tú',
	backgroundColor: 'rgba(52,230,165,0.5)',
	borderColor: 'rgba(52,230,165,0.7)',
	pointBackgroundColor: 'rgba(52,230,165,0.7)',
	data: [cuerpo,fRojos,fNegros,astringencia,citrico,fHueso,fTropical,herbal,floral,tierra

		]
	}
	]
},
	options: {
		legend: {
			position: 'top',
			labels:{
				fontSize: 12,
				fontStyle:'bold',
				fontColor: 'rgba(0, 0, 0, 0.7)'
			},
		},
		title: {
			display: false,
			fontSize: 20,
			fontStyle:'bold',
			fontColor: 'rgba(0, 0, 0, 0.7)'	,
			text: 'PERFIL DE VINO'
		},

		scale: {
			gridLines: {
				color:'rgba(0, 0, 0, .3)',
			},

			angleLines:{
			display: true,
			color:'rgba(0, 0, 0, 0)',//si se ponen parece una telaraña (george)
			},
			pointLabels:{
				fontColor:'rgba(0, 0, 0, .5)'
			},
			ticks:{
				min:0,
				max:100,
				stepSize:20,
				display:false,
			}
		},

	}
};

window.onload = function() {
	window.myRadar = new Chart(document.getElementById('canvas1'), config);
};

$(document).ready(function(){
	if(localData.plan=='2_botellas'){
		$('select').html('<option value="1">2 TINTOS</option><option value="2">1 TINTO 1 BLANCO</option><option value="3">2 BLANCOS</option>');
	}else if(localData.plan=='3_botellas'){
		$('select').html('<option value="1">3 TINTOS</option><option value="2">2 TINTOS 1 BLANCO</option><option value="3">1 TINTO 2 BLANCOS</option><option value="4">3 BLANCOS</option>');
	}else if (localData.plan=='4_botellas'){
		$('select').html('<option value="1">4 TINTOS</option><option value="2">3 TINTOS 1 BLANCO</option><option value="3">2 TINTOS 2 BLANCOS</option><option value="4">1 TINTO 3 BLANCOS</option><option value="5">4 BLANCOS</option>');
	}
});

$(document).ready(function(){
$("select").change(function() {
	var balance = "";
    $( "select option:selected" ).each(function() {
      balance += $( this ).text() + " ";
      localData.balance=balance;
      console.log(localData);
      dataToStore = JSON.stringify(localData);
	  localStorage.setItem('someData', dataToStore);
		document.getElementById("plan").value = localData.plan
		document.getElementById("balance").value = localData.balance
    });
    })
  .trigger( "change" );
});



//$('select').html('');

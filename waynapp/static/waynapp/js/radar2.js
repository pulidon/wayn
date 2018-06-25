var localData = JSON.parse(localStorage.getItem('someData'));
console.log(localData);
var cuerpo,fRojos,fNegros,astringencia,citrico,fHueso,fTropical,herbal,floral,tierra;


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
    fNegros=10;
} else if (localData.frutos=='negros') {
   fRojos=10;
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
    astringencia=10;
 }
//FRUTAS
if (localData.jugo=='citrico-tropical') { //sauvignon blanc
    citrico=90;
    fHueso=10;
    fTropical=90;
} else if (localData.jugo=='citrico-hueso') {
   citrico=90;
    fHueso=90;
    fTropical=10;
}
else if (localData.jugo=='tropical-hueso') {
    citrico=10;
    fHueso=90;
    fTropical=90;
 }
//AROMA
if (localData.olor=='hierba') { //sauvignon blanc
    herbal=90;
    floral=10;
    } else if (localData.olor=='floral') {
    herbal=10;
    floral=90;
  }
//TIERRA
if (localData.tierra=='poco') { //sauvignon blanc
    tierra=10;
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
	labels: ['Cuerpo', 'Frutos Rojos', 'Frutos Negros','Astringencia','Citrico','Fruta hueso','Fruta tropical', 'herbal','floral','tierra'],
	datasets: [{
	label: 'TU',
	backgroundColor: 'rgba(52,230,165,0.6)',
	borderColor: 'rgba(52,230,165,0.7)',
	pointBackgroundColor: 'rgba(52,230,165,0.7)',
	data: [cuerpo,fRojos,fNegros,astringencia,citrico,fHueso,fTropical,herbal,floral,tierra
		]
	}, {
	label: 'VINO',
		backgroundColor: 'rgba(158,87,149,0.8)',
		borderColor: 'rgba(158,87,149,0.7)',
		pointBackgroundColor: 'rgba(158,87,149,0.7)',
		data: [70,40,55,30,60,50,70,80,30,40]
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
			display: false,  //si se ponen parece una telaraña (george)
			color:'rgba(0, 0, 0, 0.5)',
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
	window.myRadar1 = new Chart(document.getElementById('canvas1'), config);
	window.myRadar2 = new Chart(document.getElementById('canvas2'), config);
	window.myRadar3 = new Chart(document.getElementById('canvas3'), config);
	window.myRadar4 = new Chart(document.getElementById('canvas4'), config);
};

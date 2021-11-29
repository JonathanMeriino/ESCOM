
		let today = new Date();
		let dd = today.getDate();
		let mm = today.getMonth() + 1; //January is 0!
		let yyyy = today.getFullYear();
		if (dd < 10)
			dd = '0' + dd;
		if (mm < 10)
			mm = '0' + mm;
			
		today = `${yyyy}-${mm}-${dd}`
		//today = yyyy + '-' + mm + '-' + dd;
		document.querySelector("input[type='date']").setAttribute("max", today);

		function calcCURP(form) {
			let name = form.name.value.toUpperCase();
			let psurnm = form.psurname.value.toUpperCase();
			let msurnm = form.msurname.value.toUpperCase();
			let birth = form.birth.value;
			let place = form.place.value;
			let gender = form.gender.value;
			
			let curpHTML = form.curp;
			let curp = psurnm[0]+psurnm[1]+msurnm[0]+name[0];

			birth = birth.split("-");
			birth.forEach(elem => {
				curp = curp.concat(elem.substr(elem.length-2));
			});
			curp += gender+place+getConsonant(psurnm)+getConsonant(msurnm)+getConsonant(name);
			curp += getHomokey(curp, parseInt(birth[0]));

			curpHTML.value = curp;
		}

		function getConsonant(str) {
			let vocals = ["A", "E", "I", "O", "U"];

			for (let i=1; i<str.length; i++) {
				let chr = str.substr(parseInt(i), 1);
	
				if (!vocals.some(vocal => {return vocal==chr}))
					return  chr=='Ñ'? "X" : chr;
			}
		}


function getHomokey(curp, birthYear) {
	function getHomokey(str, year) {
	
	var contador = 18;
	var contador1 = 0;
	var valor = 0;
	var sumatoria = 0;


	while (contador1 <= 15) {

		//pstCom = SUBSTRING(@str,@contador1,1)
		var pstCom = str.substr(parseInt(contador1), 1);

		if (pstCom == '0') {
			valor = 0 * contador;
		}
		if (pstCom == '1') {
			valor = 1 * contador;
		}
		if (pstCom == '2') {
			valor = 2 * contador;
		}
		if (pstCom == '3') {
			valor = 3 * contador;
		}
		if (pstCom == '4') {
			valor = 4 * contador;
		}
		if (pstCom == '5') {
			valor = 5 * contador;
		}
		if (pstCom == '6') {
			valor = 6 * contador;
		}
		if (pstCom == '7') {
			valor = 7 * contador;
		}
		if (pstCom == '8') {
			valor = 8 * contador;
		}
		if (pstCom == '9') {
			valor = 9 * contador;
		}
		if (pstCom == 'A') {
			valor = 10 * contador;
		}
		if (pstCom == 'B') {
			valor = 11 * contador;
		}
		if (pstCom == 'C') {
			valor = 12 * contador;
		}
		if (pstCom == 'D') {
			valor = 13 * contador;
		}
		if (pstCom == 'E') {
			valor = 14 * contador;
		}
		if (pstCom == 'F') {
			valor = 15 * contador;
		}
		if (pstCom == 'G') {
			valor = 16 * contador;
		}
		if (pstCom == 'H') {
			valor = 17 * contador;
		}
		if (pstCom == 'I') {
			valor = 18 * contador;
		}
		if (pstCom == 'J') {
			valor = 19 * contador;
		}
		if (pstCom == 'K') {
			valor = 20 * contador;
		}
		if (pstCom == 'L') {
			valor = 21 * contador;
		}
		if (pstCom == 'M') {
			valor = 22 * contador;
		}
		if (pstCom == 'N') {
			valor = 23 * contador;
		}
		if (pstCom == 'Ñ') {
			valor = 24 * contador;
		}
		if (pstCom == 'O') {
			valor = 25 * contador;
		}
		if (pstCom == 'P') {
			valor = 26 * contador;
		}
		if (pstCom == 'Q') {
			valor = 27 * contador;
		}
		if (pstCom == 'R') {
			valor = 28 * contador;
		}
		if (pstCom == 'S') {
			valor = 29 * contador;
		}
		if (pstCom == 'T') {
			valor = 30 * contador;
		}
		if (pstCom == 'U') {
			valor = 31 * contador;
		}
		if (pstCom == 'V') {
			valor = 32 * contador;
		}
		if (pstCom == 'W') {
			valor = 33 * contador;
		}
		if (pstCom == 'X') {
			valor = 34 * contador;
		}
		if (pstCom == 'Y') {
			valor = 35 * contador;
		}

		if (pstCom == 'Z') {
			valor = 36 * contador;
		}

		contador = contador - 1;
		contador1 = contador1 + 1;
		sumatoria = sumatoria + valor;

	}

	numVer = sumatoria % 10;
	numVer = Math.abs(10-numVer);
	if (numVer == 10)
		numVer = 0;


	if (year < 2000)
		pstDigVer = '0' + '' + numVer;
	else
		pstDigVer = 'A' + '' + numVer;
	

	return pstDigVer;
}
}



function query(){
    let request = new XMLHttpRequest();
	request.open("POST", "scriptName.ext?param1=value1&param2=value2..." + query, true);
	request.send();
	request.onreadystatechange = function(){
		if(request.readyState == 4 && request.status == 200){
			// csv
				// let data = request.responseText;
				// --> parse string manually
			//json 
				// let data= request.responseText;
				// let collect = data.split('\n'); //put breaks in method that sends it
				// let payload = array();
				/*
					for(let i=0; i < collect.length; i++){
						payload[i] = JSON.parse(collect[i]);
					}
				/*
			//xml is in request.response.XML
				//let data = request.XML;
				//let payload = data.getElementsByTagName('name');
				//let unique = data.getElementById('id'); //remember to put id's before sending
		}//end onreadystatechange()
	}
}//end runQuery()
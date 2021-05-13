

/*
 * Request the data from the server in xml format, this way it looks
 * like everything you're used to doing in JavaScript with your document:
 * in particular .getElementsByTagName(...) will work the same if you don't put
 * id's or any other attributes in the xml data
 */
function markup(){
	let request = new XMLHttpRequest();
	request.open("POST", "xml_and_json_from_php.php?mode=xml", true);
	request.send();
	request.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			processMarkup(this.responseXML);
		}
	}
}//end markup()



function processMarkup(xmlData){
		/*
		 * Remember to open the inspector on your favorite browser (push the
		 * F12 key) and put in a breakpoint so you
		 * can pause the script and expand these things in the scope window
		 * to see what all properties you have to work with then it's just
		 * element (dot) whatever is on that long list
		 */
	let names = xmlData.getElementsByTagName('name');
	let table = "<table border=\"1\">";
	table += "<thead><tr><th>NAME</th></tr></thead><tbody>";
	for(let i = 0; i < names.length; i++){
		table += "<tr><td>" + names[i].innerHTML + "</td></tr>";
	}
	table += "</tbody></table>";
	document.getElementById('outputXML').innerHTML += table;
}//end processMarkup()



//////////////////////////////////////////////////////////////////////////////////////////////


/*
 * Request the data from the server as JSON objects. Just call the normal
 * JSON.parse(...) method and you have an object ready to go in JavaScript
 */
function object(){
	let request = new XMLHttpRequest();
	request.open("POST", "xml_and_json_from_php.php?mode=json", true);
	request.send();
	request.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			processObject(this.responseText);
		}
	}
}//end object()




function processObject(jsonData){
		/*
		 * Remember to open the inspector on your favorite browser (push the
		 * F12 key) and put in a breakpoint so you
		 * can pause the script and expand these things in the scope window
		 * to see what all properties you have to work with, then it's just
		 * object (dot) whatever is on that long list
		 */
	let payload = jsonData.split('\n');
	let table = "<table border=\"1\">";
	table += "<thead><tr><th>AGE</th></tr></thead><tbody>";
	for(let i = 0; i < payload.length; i++){
		let obj = JSON.parse(payload[i]);
		table += "<tr><td>" + obj.age + "</td></tr>";
	}
	table += "</tbody></table>";
	document.getElementById('outputJSON').innerHTML = table;
}//end processObject()



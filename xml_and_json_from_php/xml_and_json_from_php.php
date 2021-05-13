<?php

		// put this in MySQL for this example
	/*
		
	CREATE DATABASE IF NOT EXISTS TestDB;
	USE TestDB;
	CREATE TABLE IF NOT EXISTS people(name VARCHAR(32), age INT, town VARCHAR(32));
	INSERT INTO people(name, age, town) VALUES('sally', 35, 'salem');
	INSERT INTO people(name, age, town) VALUES('chuck', 42, 'charleston');
	INSERT INTO people(name, age, town) VALUES('jeff', 42, 'jeffersonville');
		
	*/


		// modify connection details appropriately for your database
	$db = new mysqli("localhost", "root", "", "TestDB");
	$res = $db->query("SELECT * FROM people WHERE 1;");
	$data = array();
	if($res->num_rows > 0){
		while($row = $res->fetch_assoc()){
			array_push($data, $row);
		}
	}

	$mode = $_REQUEST['mode']; //get this from javascript function

	if($mode == "xml"){
			//in xml format
		$xml = new DOMDocument("1.0", "UTF-8");
		$root = $xml->createElement("root");
		$root = $xml->appendChild($root);
		foreach ($data as $record){
			$row = $xml->createElement("row");
			$row = $root->appendChild($row);
			$row->appendChild($xml->createElement("name", $record['name']));
			$row->appendChild($xml->createElement("age", $record['age']));
			$row->appendChild($xml->createElement("town", $record['town']));
		}
		header("Content-type: text/xml; charset=utf-8");
		echo $xml->saveXML();
		//now create a reference to a new doc as request.responseXML
		/*
		 * maybe write this to a file as well so you can see what 
		 * you have to work with, however, it's not in "pretty print" 
		 * so the whole xml file will be one line you might want to 
		 * modify that a little to read it.
		 * changet the file location appropriately
		 */
		$toFile = fopen("testXML.xml", "w");
		fwrite($toFile, $xml->saveXML());
		fclose($toFile);
	}//end XML
	else if($mode == "json"){
			//in json format
		$jsonData = "";
		foreach($data as $record){
			$jsonData .= json_encode(array("name"=>$record['name'], "age"=>$record['age'], "town"=>$record['town']));
			if(next($data)){
				$jsonData .= "\n";
			}
		}
		echo $jsonData;
		//now you're ready to get request.responseText, split at new line, and have json object in each element of array
		/*
		 * maybe write this to a file as well so you can see what 
		 * you have to work with. each line will contain an
		 * individual JSON object.
		 * changet the file location appropriately
		 */
		$toFile = fopen("testJSON.txt", "w");
		fwrite($toFile, $jsonData);
		fclose($toFile);
	}//end JSON

?>
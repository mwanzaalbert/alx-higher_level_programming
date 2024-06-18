#!/usr/bin/node
const numPrints = Number.parseInt(process.argv[2]);

if (numPrints === NaN){
	console.log("Missing number of occurrence");
}else if (numPrints >=1 ){
	for (let counter=0; counter < numPrints; counter++){
		console.log('C is fun');
	}
}

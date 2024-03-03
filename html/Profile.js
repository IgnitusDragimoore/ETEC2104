"use strict";

let R = new FileReader();

function submit(){
    let fname = document.getElementById("fname").value;
    let lname = document.getElementById("lname").value;
    let dob = document.getElementById("birthdate").value;
	let user = document.getElementById("user").value;
	R.readAsBinaryString(document.getElementById("ppic").files[0]);
	ppic = R.result;
	console.log(ppic);
	if(!ppic){
		console.log("No file!");
	} else {
		let J = {
			"firstName": fname,
			"lastName": lname,
			"birthDate": dob,
			"ppic":ppic
		};
		let postData = {
			method: 'POST',
			body: JSON.stringify(J)
		};
		fetch("/profile/" + user,postData
		).then( (resp) => {
			//can also use text(), blob(), or arrayBuffer()
			resp.json().then( (J) => {
				console.log("Server said:",J);
			});
		}).catch( (err) => {
			console.log("Uh oh",err);
		});
	}
}

function fileChange(event) {
    const file = event.target.files[0];
    const fileReader = new FileReader();
    fileReader.onload = (e) => uploadFile(e.target.result, file.name);
    fileReader.readAsText(file);
}

function uploadFile(fileContent, fileName) {
    // Encode the binary data to as base64.
    const data = {
        fileContent: btoa(fileContent),
        fileName: fileName
    };
    axios.post('http://localhost:8080/api/uploadFile', JSON.stringify(data));
}

/* R.addEventListener("load", () => {
     let profilepic = btoa(R.result);    //do base64 encoding
     let fname = document.getElementById("fName").value;
     let lname = document.getElementById("lname").value;
     let dob = document.getElementById("birthdate").value;
     let J = {
         firstName: fname,
         lastName: lname,
         birthDate: dob,
         profPic: profilepic
     };
     fetch( "/profile",
         {   method: "POST",
             body: JSON.stringify(J)
         }
     ).then( (resp) => {
         //can also use text(), blob(), or arrayBuffer()
         resp.json().then( (J) => {
             console.log("Server said:",J);
         });
     }).catch( (err) => {
         console.log("Uh oh",err);
     })
 })
*/

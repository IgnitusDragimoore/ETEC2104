"use script";



let num = [0, 34, 10, 21, 28, 4, 18, 9, 27, 22, 12, 3, 17, 20, 11, 33, 
    2, 10, 32, 0o0, 15, 8, 25, 1, 31, 20, 14, 30, 7, 24, 29, 35, 6, 13, 
    23, 19, 5, 36];

let sock = new WebSocket("ws://"+document.location.host+"/sock");


function getSpin(evt) {
    let li = document.createElement("li")
    li.appendChild(document.createTextNode(evt.data));
    document.getElementById("spinList").appendChild(li);
}

sock.addEventListener("message", getSpin );

function spinWheel() {
    let i = Math.floor(Math.random() * num.length);
    let randNum = num[i];
    console.log(randNum);

    let li = document.createElement("li")
    let result = "";

    result = randNum + ", ";
    //li.appendChild(document.createTextNode(randNum));
    //li.appendChild(document.createTextNode(", "));

    if (randNum % 2 == 0){
        console.log("Noir!");
        //li.appendChild(document.createTextNode("Noir"));
        result+= "Noir, ";

    }
    else{
        console.log("Rogue!");
        //li.appendChild(document.createTextNode("Rogue"));
        result+= "Rogue, ";
    }

    //li.appendChild(document.createTextNode(", "));

    if(randNum % 2 == 0){
        console.log("Pair!");
        //li.appendChild(document.createTextNode("Pair"));
        result+= "Pair, ";
    }
    else {
        console.log("Impair!");
        //li.appendChild(document.createTextNode("Impair"));
        result+= "Impair, ";
    }

    //li.appendChild(document.createTextNode(", "));

    if(randNum < 19){
        console.log("Manque!");
        //li.appendChild(document.createTextNode("Manque"));
        result+= "Manque";
    }
    else {
        console.log("Passe!");
        //li.appendChild(document.createTextNode("Passe"));
        result+= "Passe"
    }

    //li.appendChild(document.createTextNode(result));
    //document.getElementById("spinList").appendChild(li);
    sock.send(result);

}

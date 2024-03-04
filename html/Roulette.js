"use script";

let num = [0, 34, 10, 21, 28, 4, 18, 9, 27, 22, 12, 3, 17, 20, 11, 33, 
    2, 10, 32, 0o0, 15, 8, 25, 1, 31, 20, 14, 30, 7, 24, 29, 35, 6, 13, 
    23, 19, 5, 36];

let i = Math.floor(Math.random() * num.length);
let randNum = num[i];

console.log(randNum);

if (randNum % 2 == 0){
    console.log("Noir!")
}
else{
    console.log("Rogue!")
}

if(randNum % 2 == 0){
    console.log("Pair!")
}
else {
    console.log("Impair!")
}

if(randNum < 19){
    console.log("Manque!")
}
else {
    console.log("Passe!")
}

function checkAnswer(a,b){

var correct = a + b;
var user = document.getElementById("answer").value;

if(user == correct){
document.getElementById("result").innerHTML = "Correct!";
}
else{
document.getElementById("result").innerHTML = "Wrong answer";
}

}

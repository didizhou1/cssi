console.log('Hello World');

const name="Charlie";
console.log("Hello "+name);
//console.log('Hello ${name}!');

const age=16;
console.log("You are "+age+" years old");

// line comment
/* block comment */
/** documentation */
if(age>=18){
  console.log("You can get your driver's license and vote")
}
else if (age>=15){
  console.log("You can get your permit but you cannot vote")
}
else{
  console.log("You will have to wait to get your permit and cannot vote")
}

function makeGreetingMessage(name1, name2=null){
  if(name2==null)
    return "Hello "+name1;
  else
    return "Hello "+name1+" and "+name2;
}

function greet(name1, name2=null){
  if(name2[0]==='a'){
  }else {
    return;
  }
  console.log(makeGreetingMessage(name1, name2));
  return;
}

greet("bob", "alice");

const mult3=(x)=>x*3
console.log(mult3(3));

/*let n=0;
setInterval()(=>{
  console.log(new Date());
},1000);*/

// document.addEventListener("DOMContentLoaded", () => {
//   const likeButton = document.querySelector('.likebutton');
//   likeButton.addEventListener('click', () => {likebutton.innerText='Liked';});
//   const greetMess = makeGreetingMessage(Alice);
//   likeButton.innertext = greetMess;
//   likeButton.style.backgroundColor='blue';
// }

const names = ["Jo","Bob", "Alice", "Ted"];
console.log(names);

for(let i=0;i<names.length;i++){
  console.log(names[i]);
}
i=0;
while(i<5){
  console.log(names[i]);
  i++
}

// names.forEach(name) =>{
//   console.log('forEach: ${names}');
// }

const article = {
  name: "Dog family gives birth to a little of 10 puppies",
  views: 1234,
  datePublished: "03/25/2018",
  author: {
    name: "Joe Corgi",
    title: "Senior Canine Editor",
  },
  editors: [{
    name: "Bob",
    title: "Senior Editor"},
    {
    name: "Tim",
    title: "Editor"}],
}

const floatingBox = document.querySelector(".floatingBox");
document.addEventListener("keydown", (event)=>{
  let boxTop = 100;
  let boxLeft = 100;
  const key = event.key;
  if(key==="ArrowDown"){
    boxTop += 5;
  }
  else if(key==="ArrowUp"){
    boxTop -= 5;
  }
  else if(key==="ArrowLeft"){
    boxLeft -= 5;
  }else if(key==="ArrowRight"){
    boxLeft += 5;
  }else
    return;
  floatingBox.style.top = boxTop+"px";
  floatingBox.style.left = boxLeft+"px";
  console.log(event);
});

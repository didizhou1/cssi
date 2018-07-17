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

let n=0;
setInterval()(=>{
  console.log(new Date());
},1000);

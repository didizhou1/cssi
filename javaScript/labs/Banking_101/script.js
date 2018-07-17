// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;
let logged_in;
let password;

function openAccount(name, money="0", pass){
  balance = money;
  password = pass;
  // Set the value for customer_name equal to name below
  customer_name = name;
  return customer_name+" has opened a new accound with a balance of $"+balance;//write the statment you need to return here
}

function login(name, pass){
  if(name===customer_name){
    if(pass===password){
      logged_in===true;
      return customer_name+" has logged in.";
    }
  }
  return "Incorrect log in";
  logged_in===false;
}

function deposit(value){
  if(logged_in==false){
    return "User must log in.";
  }
  // update the value of balance
  balance+=value;
  //return the correct statement
  return customer_name+" has deposited $"+value+". "+customer_name+"'s total balance is now $"+balance;
}

function withdraw(money){
  if(logged_in===false){
    return "User must log in.";
  }
  if(money>balance){
    let difference = money-balance;
    return "Sorry, "+customer_name+", you do not have enough money in your account. You need "+difference+" more dollars";
  }
  //update the value of balance
  balance-=money;
  //return the correct statement
  return customer_name+" has withdrawn $"+money+". "+customer_name+" has $"+balance+" remaining";
}

function logoff(){
  logged_in===false;
  return customer_name+" has logged out.";
}
// Write your script below
console.log(openAccount("Bob", 300, "pass123"));
console.log(login("Bob","pass123"));
console.log(deposit(50));
console.log(withdraw(50));

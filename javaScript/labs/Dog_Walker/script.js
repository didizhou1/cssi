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

// Task 1
let dogName1 = "Steve";
let dogType1 = "beagle";

// Complete Task 1 Below
console.log("I will walk "+dogName1+" today at 12:00pm");


let dogName2 = "Joe";
let dogType2 = "Corgi";

// Complete Task 2 Below
if(dogType2.toLowerCase()==="corgi"){
  console.log("I will walk "+dogName2+" today at 12:00pm");
}
else{
  console.log("I will walk "+dogName1+" today at 1:00pm");
}


let dogName = "Lola";
let dogType = "poodle";

// Complete Task 3 Below
let faveDogs = ["spike", "jeremy", "lola", "peaches", "steve"];
let x = "";
if(faveDogs.includes(dogName.toLowerCase())){
  x= ", one of my favorite dogs, "
}
if(dogType.toLowerCase()==="corgi" || dogType.toLowerCase()==="beagle"){
  console.log("I will walk "+dogName+""+x+" today at 12:00pm");
}
else if(dogType.toLowerCase()==="bulldog"){
  console.log("I will walk "+dogName+""+x+" today at 1:00pm");
}
else{
  console.log("I will walk "+dogName+""+x+" today at 2:00pm");
}

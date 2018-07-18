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

let currentlily = 1;

let frogger = document.querySelector("#frog");/*use a querySelector to grab your frog from your HTML*/;

frogger.addEventListener("click", function(){
// Insert what should happen when you click on the frog!
console.log("hop");

  frogger.style.left = "33.5%";
  frogger.style.top = "23%";
  document.querySelector("#lilypad1").classList.remove("active");
  document.querySelector("#lilypad2").classList.add("active");
  currentlily++;

});

frogger.addEventListener("mouseover", function(){
  frogger.style.height = "80px" ;
  frogger.style.width = "80px" ;
});

frogger.addEventListener("mouseleave", function(){
  frogger.style.height = "70px" ;
  frogger.style.width = "70px" ;
});

// <input type="text" onkeypress="spaceClicked(event)">
function spaceClicked(event) {
    if(event.keyCode=='32'){
      frogger.style.right = "33.5%";
      frogger.style.bottom = "23%";
      document.querySelector("#lilypad2").classList.remove("active");
      document.querySelector("#lilypad1").classList.add("active");
      currentlily=1;
    }
}

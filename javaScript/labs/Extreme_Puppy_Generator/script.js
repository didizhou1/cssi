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

console.log(dataObject);

const button = document.querySelector('.button');
const clear = document.querySelector('.button');
button.addEventListener('click', () => {

let i=0
  for(i=0;i<10;i++){
    var dog = document.createElement("IMG");
    dog.src = dataObject.data[i].images.original.url;
    console.log(dog.src);
    dog.classList.add("gif");
    document.body.appendChild(dog);
    var title = document.createElement("text");
    title.innerText = dataObject.data[i].title;
    document.body.appendChild(title);
  }

});

clear.addEventListener('click', () => {
  
}

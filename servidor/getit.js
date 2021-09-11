function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function salvar(id) {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    }
};
xhttp.open("UPDATE", "http://localhost:8080", true);
titulo = document.getElementById(`titulo_${id}`).value;
detalhes = document.getElementById(`detalhes_${id}`).value
body = `${id}&${titulo}&${detalhes}`
xhttp.send(body);
this.innerHTML="Salvo"
carta = document.getElementById(id);
carta.innerHTML = `
<h3 class="card-title">${titulo}</h3>
<div class="card-content">
  <p>
    ${detalhes}
  </p>
</div>
<button class="edit" name = ${id} onClick="editar(${id})" id = "button_${id}" >Editar</button>`;

}

function editar(name) {
id = name;
carta = document.getElementById(id);
h3=carta.querySelector(".card-title");
p=carta.querySelector(".card-content");
carta.innerHTML = `<input class="input" type="text" value=${h3.textContent} id = "titulo_${id}" />
<div class="card-content">
<input class="input" type= "text" id="detalhes_${id}"  value=${p.textContent} />
</div>
<button class="edit" name = ${id} onClick="salvar(${id})" id = "button_${id}" >Salvar</button>
<button class="edit" name = ${id} onClick="apagar(${id})" id = "button_${id}" >X</button>`


}

function apagar(id) {


var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // Typical action to be performed when the document is ready:
      // document.getElementById("demo").innerHTML = xhttp.responseText;
    }
};
xhttp.open("DELETE", "http://localhost:8080", true);

body = id;
xhttp.send(body);

carta = document.getElementById(id);
carta.remove()

}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }

});

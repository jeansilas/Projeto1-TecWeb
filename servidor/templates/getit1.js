function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
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
    e = document.getElementsByClassName("edit")
    
    for (i of e) {
      if (i.innerHTML.value == "Editar") {
      i.addEventListener('click', function(event) {
        
        id = this.name
        this.innerHTML = `<button class="edit" name =`+id+` >Editar</button>`
        carta = document.getElementById(id)
  
  
        h3=carta.querySelector(".card-title")
        h3.innerHTML = `<input
        class="input"
        type="text"
        placeholder="Título"
      />`
  
        p = carta.querySelector(".card-content")
        p.innerHTML = `<textarea
        class="textarea"
        placeholder="Digite o conteúdo..."
      ></textarea>`
  
      
    })
    } 
    k = document.getElementsByClassName("edit")
    for (i of k) {
      
        if (i.innerHTML.value == "Salvar") {
        i.addEventListener('click', function(event) {
          id = this.name
          carta = document.getElementById(id)
    
          h3_value = carta.querySelector(".input").value
          p_value = carta.querySelector(".textarea").value
          carta.innerHTML = `<h3 class="card-title">`+h3_value+`</h3>
          <div class="card-content">
            <p>
              `+p_value+`
            </p>
          </div>
          <button class="edit" name = {id} >Salvo</button>`
  
    
    
    
    
    
        })
      }
  
    }
   }
  // else if (e.innerHTML=="Salvar") {
    
  
  // }
  
  });
  
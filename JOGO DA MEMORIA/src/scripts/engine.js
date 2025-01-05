const emojis = [
    "🌛",
    "🌛",
    "🌞",
    "🌞",
    "🌟",
    "🌟",
    "🌈",
    "🌈",
    "⚡",
    "⚡",
    "🔥",
    "🔥",
    "💧",
    "💧",
    "🌊",
    "🌊",
    ];
    
    let openCards = [];
    
    let shuffleEmojis = emojis.sort(()=>(
        Math.random()> 0.5 ? 2: -1));
    
    for(let i =0; i < emojis.length; i++){
        let box = document.createElement("div");
        box.className = "item";
        box.innerHTML = shuffleEmojis[i];
        box.onclick = handleClick;
        document.querySelector(".game").appendChild(box);
    }
    
    function handleClick(){
        if(openCards.length < 2){
            this.classList.add("boxOpen");
            openCards.push(this);
        }
        if(openCards.length == 2){
            setTimeout(checkMatch, 500);
        }
    }
    
    function checkMatch(){
        console.log("passou aqui")
        if(openCards[0].innerHTML === openCards[1].innerHTML){
            openCards[0].classList.add("boxMatch");
            openCards[1].classList.add("boxMatch");
        }else{
            openCards[0].classList.remove("boxOpen");
            openCards[1].classList.remove("boxOpen");
        }
        console.log("passou aqui também");
        openCards = [];
        console.log("passou aqui em")
    
        if(document.getElementsByClassName("boxMatch").length === emojis.length){
            document.querySelectorAll(".item").forEach(item => {
                item.style.display = "none";
            });
            document.querySelector(".imagem").style.display = "block";
            document.querySelector(".venceu").style.display = "block";
    
        }
    
    }
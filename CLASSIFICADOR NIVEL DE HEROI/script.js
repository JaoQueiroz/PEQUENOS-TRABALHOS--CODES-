function classificarHeroi() {
    // @ts-ignore
    const nome = document.getElementById('hero-name').value;
    // @ts-ignore
    const xp = parseInt(document.getElementById('hero-xp').value);
    let nivel = '';
    let fase = '';
    let resultado = '';
    let vitoria = false;

    if (xp < 100) {
        nivel = 'Ferro';
        fase = '1';
        resultado = `O vilão ou Heroína ${nome} está no nível ${nivel}, com pouca XP e perdeu esta fase. Tente novamente!`;
        vitoria = false;
    } else if (xp >= 101 && xp <= 2000) {
        nivel = 'Bronze';
        fase = '2';
        resultado = `Você, ${nome} precisa melhorar suas habilidades seu nível é ${nivel}.`;
        vitoria = false;
    } else if (xp >= 2001 && xp <= 5200) {
        nivel = 'Prata';
        fase = '3';
        vitoria = true;
    } else if (xp >= 5201 && xp <= 7300) {
        nivel = 'Ouro';
        fase = '4';
        vitoria = false;
        resultado = `Você ${nome}, está indo muito bem! mas pode ainda melhorar suas habilidades, seu nível é ${nivel}.`;
    } else if (xp >= 7301 && xp <= 8500) {
        nivel = 'Platina';
        fase = '5';
        vitoria = true;
    } else if (xp >= 8501 && xp <= 9000) {
        nivel = 'Ascendente';
        fase = '6';
        vitoria = true;
    } else if (xp >= 9001 && xp <= 10100) {
        nivel = 'Imortal';
        fase = '7';
        vitoria = true;
    } else if (xp >= 10101) {
        nivel = 'Radiante';
        fase = '8';
        vitoria = true;
    }

    if (vitoria) {
        resultado = `O vilão ou Heroína ${nome} está no nível ${nivel} e avançou para a fase ${fase}. Parabéns pela vitória!`;
    } else if (xp >= 4500) {
        resultado = `O vilão ou Heroína ${nome} está no nível ${nivel}, mas não passou para a fase ${fase}. Você precisa melhorar!`;
    }

    // @ts-ignore
    document.getElementById('resultado').textContent = resultado;

    // Alterar imagem conforme vitória ou derrota
    const heroMainImage = document.getElementById('hero-main-image');
    const resultadoImagem = document.getElementById('resultado-imagem');

    // Limpar imagens anteriores
    // @ts-ignore
    resultadoImagem.innerHTML = '';

    if (vitoria) {
        // @ts-ignore
        heroMainImage.src = `src/vitoria.png`;
        // @ts-ignore
        resultadoImagem.innerHTML = `<img src="src/vitoria${fase}.png alt="Venceu ${nome}">`;
    } else if (xp >= 5201 && xp <= 7300){
        // @ts-ignore
        heroMainImage.src = `src/vilao.png`;
        // @ts-ignore
        resultadoImagem.innerHTML = `<img src="src/vilao${fase}.png" alt="Vilão ${nome}">`;
    } else if (xp < 100) {
        // @ts-ignore
         heroMainImage.src = `src/derrota.png`;
        // @ts-ignore
        resultadoImagem.innerHTML = `<img src="src/derrota.png" alt="Derrota">`;
    }
}
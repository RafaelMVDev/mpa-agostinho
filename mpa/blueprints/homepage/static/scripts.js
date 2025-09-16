

const URL_ALVO = '/jokenpo';

// elementos do html    

// funcoes uteis
function setar_escolha(elemento){
    img_caminho = 'jokenpo\\static\\'  +  elemento.dataset.escolha +'_img.png';
    div_img_player.src = img_caminho;
    return elemento.dataset.escolha;
}

function criarNoticiaHTML(noticia) {
  return ` 
  <article class="bg-gray-800 rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow">
      <div class="flex flex-col md:flex-row gap-6">
        <div class="md:w-1/3">
          <img 
            src="${noticia.imageUrl}"
            alt="Imagem ilustrativa para notícia sobre ${noticia.category}"
            class="w-full h-48 object-cover rounded-lg"
          />
        </div>
        <div class="md:w-2/3">
          <div class="flex items-center mb-3">
            <span class="bg-blue-600 text-sm px-3 py-1 rounded-full mr-3">${noticia.category}</span>
            <span class="text-sm text-gray-400">${noticia.date}</span>
          </div>
          <h3 class="text-xl font-semibold mb-3 text-white hover:text-blue-300 cursor-pointer transition-colors">
            ${noticia.title}
          </h3>
          <p class="text-gray-300 mb-4 leading-relaxed">${noticia.description}</p>
          <div class="flex items-center justify-between">
            <button class="bg-blue-700 hover:bg-blue-600 px-4 py-2 rounded-md text-sm transition-colors">
              Ler Mais
            </button>
            <div class="flex items-center space-x-4">
              <span class="text-sm text-gray-400">Por: Redação</span>
              <div class="flex items-center space-x-2">
                <span class="text-sm text-gray-400">👁️ ${noticia.visualizacoes}</span>
                <span class="text-sm text-gray-400">💬 ${noticia.comentarios}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </article>
  `;
}

function atualizar_dados_rodada(pontuacao,msg,class_msg,escolha_bot){
    // alterando a mensagem de aviso que aparece depois de cada rodada
    msg_aviso.innerText = msg
    msg_aviso.className = class_msg
    placar.innerText = pontuacao
    div_img_bot.src = escolha_bot
    console.log(pontuacao)

}

function exibir_mensagem_vitoria(vencedor){
    if (div_vitoria.style.display === 'none' || div_vitoria.style.display === ''){
        div_vitoria.style.display = 'block'
        botao_jogar.style.display = 'none'
        div_img_player.src = "" // Limpa a imagem da escolha anterior do player
        placar.style.display = "none"
        if (vencedor === "player"){
            msg_final.innerText = "Você ganhou!";
            div_vitoria.style.backgroundColor = "green"
        }
        else{
            msg_final.innerText = "Você perdeu!"
            div_vitoria.style.backgroundColor = "red"
        }
        setTimeout(function() { // se setar direto, a animação de opacidade não ocorre, por isso a gente espera um pouco
            div_vitoria.style.opacity = 1
        }, 0);
       
    }
    else{
        div_vitoria.style.opacity = 0
        placar.style.display = "block"
        botao_jogar.style.display = "inline-block"
        div_vitoria.style.display = "none"
    }
   
    
}



async function mandar_escolha_player(novo_jogo){
    let body_data = ""
    if (novo_jogo){
        body_data = JSON.stringify("novo_jogo")
    }
    else{
        body_data = JSON.stringify({escolha_player : sessionStorage.getItem("escolha_player")})
    }
    const post_data = {
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: body_data
    }
    response = await fetch(URL_ALVO, post_data)
    if (!response.ok){
        throw new Error('Erro com a resposta...');
    }
    
    if (response.redirected) 
    { /* redirecionar se o tipo for para isso */
        window.location.href = response.url; 
    } 
    else 
    {   
        data = await response.json();
        /* se a chave "resultado_jogo" existe, indica o fim do jogo */
        if (data.resultado_jogo){ 
            // exibir tela final aqui
            exibir_mensagem_vitoria(data.resultado_jogo)
        }
        /* se não existir, os dados enviados 
        são só para atualizar o estado da rodada */
        console.log(data)

        atualizar_dados_rodada(data.placar,data.mensagem_aviso,data.cor_aviso,data.escolha_bot_url)
      
    }
}

botoes_escolha.forEach(function(botao){
    botao.addEventListener('click',function(){
        setar_escolha(botao);

        /*Guardando informação da escolha na sessão ativa ( post request ira manda-la para a aplicação python) */
        sessionStorage.setItem("escolha_player",botao.dataset.escolha)
        /* above it saves the choice on a sessiom */
    })
})



botao_jogar.addEventListener('click',function(){
    try{
        mandar_escolha_player()
    }catch(erro){
        console.log(erro)
    }
}
)

botao_novo_jogo.addEventListener('click',function(){
    try{
        exibir_mensagem_vitoria()
    }catch(erro){
        console.log(erro)
    }
})
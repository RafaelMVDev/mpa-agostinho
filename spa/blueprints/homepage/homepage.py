#  =====  Módulos =====
from flask import Blueprint,session,render_template,redirect,url_for,request,jsonify

noticias = {
    "noticia1" : {
        "titulo" : "Lei Felca é sancionada e loot box em jogos ficam proibidas",
        "descricao" : "Na quarta-feira da semana passada, dia 17 de setembro, foi sancionada a lei 15.211/2025, também conhecida popularmente como “Lei Felca”, que busca proteger crianças e adolescentes no meio digital (por isso é o “Estatuto Digital da Criança e Adolescente”)...",
        "imagem" : "https://ichef.bbci.co.uk/ace/standard/976/cpsprodpb/C98A/production/_130049515_gettyimages-1300036725.jpg",
        "visualizacoes" : 2301,
        "comentarios":50,
        "categoria" : "jogos"
    },
     "noticia2" : {
        "titulo" : "Você deve fazer o cardio antes ou depois da musculação? Uma nova pesquisa pode finalmente ter a resposta",
        "descricao" : "O especialista Ricardo Agostinho afirma: Fazer musculação antes do cardio mostra benefícios claros em certos aspectos da saúde e...",
        "imagem" : "https://s2-oglobo.glbimg.com/hyWCJ1ZKmdEcGZQfKaEExEXEoR8=/0x0:2000x1194/888x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_da025474c0c44edd99332dddb09cabe8/internal_photos/bs/2024/1/G/8KcXmbRASCU3zMIWuiug/arte-94-.png",
        "visualizacoes" : 53443,
        "comentarios":250,
        "categoria" : "saude"
    },
     "noticia3" : {
        "titulo" : "A Oracle lança o Java 25",
        "descricao" : "A nova versão traz 18 propostas de aprimoramento do JDK para melhorar a linguagem Java, expandir seus recursos de IA e ajudar os...",
        "imagem" : "https://miro.medium.com/v2/resize:fit:720/format:webp/1*cr2O7cIoBA2kozVfgCEEVA.jpeg",
        "visualizacoes" : 150,
        "comentarios":2,
        "categoria" : "tecnologia"
    }
}
#  =====  Inicializando objetos =====

homepage_bp = Blueprint("homepage",__name__,template_folder="templates",static_folder= "static",static_url_path="/homepage_static" )


def data():
    return session.setdefault("homepage", {
      
    })



'''
#  =====  Funções =====
def reinicializar_jokenpo() -> ():  
  
    data()["pts_player"] = 0
    data()["pts_bot"] = 0
    data()["escolha_player"] = ''
    data()["escolha_player_url"] = ''
    data()["escolha_bot"] = ''
    data()["escolha_bot_url"] = ''
    data()["placar"] = "0x0"
    data()["mensagem_aviso"] = ''
    data()["cor_aviso"] = ''
'''
# rota cuida tanto do botao jogar, quanto o botao de selecionar uma escolha
# Com base na escolha do player, realiza a rodada 
'''
def efetuar_rodada(escolha_player):
    data()["escolha_player"] = escolha_player
    data()["escolha_player_url"] = url_for('jokenpo.static',filename = f'{data()["escolha_player"]}_img.png')
    data()["escolha_bot"] = jk.escolherAleatorio()
    data()["escolha_bot_url"] =  url_for('jokenpo.static',filename = f'{data()["escolha_bot"]}_img.png')

    resultado_rodada = jk.validarVencedorRodada(escolha_player,data()["escolha_bot"])
    if resultado_rodada != "empate":
        data()["cor_aviso"] = resultado_rodada +'_ganhou'
        data()[f"pts_{resultado_rodada}"] += 1
        data()["mensagem_aviso"] = resultado_rodada.capitalize() + ' venceu!' #concatenação simples
        data()["placar"] = jk.formatarPlacar(session["jokenpo"]['pts_player'],session["jokenpo"]['pts_bot'])
    else:
        data()["cor_aviso"] = 'empate'
        data()["mensagem_aviso"] = 'Empate!' # exibir mensagem diferente se ele perder

    
    return resultado_rodada # Retorna o resultado da rodada
'''
@homepage_bp.route("",methods=['GET', 'POST'])
def homepage():

    if not session.get('homepage'): # inicializa as variaveis da sessão logo que a primeira requisição é feita
         data() # inicializa a sessao

    if request.method == "POST":

        dados = request.get_json() #aqui eu acesso os dados mandadados do client
        print(dados)
    
        resposta = {"noticias" : noticias}

        session.modified = True

        return resposta # vai ser enviado de volta pro js mostrar pro cliente

    #GET request so é atividado quando  a URL é acessada / página recarregada

    return render_template('homepage.html')

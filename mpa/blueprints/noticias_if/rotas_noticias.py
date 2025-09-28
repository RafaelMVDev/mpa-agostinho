
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
# 
#  =====  Módulos =====
from flask import Blueprint,session,render_template,redirect,url_for,request


#  =====  Inicializando objetos =====

nt_bp = Blueprint("noticias_if",__name__,template_folder="templates",static_folder= "static")

def data():
    return session.setdefault("noticias",{
        
    }
)

def reiniciar_forca():
    pass

@nt_bp.route("<string:noticia>", methods = ["GET"])
def handleNoticia(noticia : str):
    print(noticia)
    nt = noticias.get(noticia)
    if not nt: # inicializa as variaveis da sessão logo que a primeira requisição é feita
         return render_template("erro.html")
 
    #GET request so é atividado quando  a URL é acessada / página recarregada
    
    return render_template("noticia_base.html",
                           titulo = nt["titulo"],
                           imagem = nt["imagem"],
                           categoria = nt["categoria"],
                           descricao = nt["descricao"],
                           visitas = nt["visualizacoes"],
                           comentarios = nt["comentarios"]
                           )

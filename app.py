from flask import Flask, flash, redirect, render_template, request, session, jsonify
from model.usuario import cadastro
from model.usuario import verificar_usuario
from model.produtos import select_produtos
from model.carrinho import recuperar_carrinho, inserir_item, deletar

app = Flask(__name__)
app.secret_key = "mem424"


@app.route("/")
def home():
    return render_template("principal.html")

@app.route("/cadastro", methods=["GET"])
def pagina_cadastro():
    return render_template("cadastro.html")



@app.route("/cadastro/post", methods=["POST"])
def guardar_dados():
    nome_usuario = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    endereco = request.form.get("endereco")
    senha = request.form.get("senha")


    if cadastro(nome_usuario, email, telefone, endereco, senha):
        return redirect("/login")
    else:
        return "ERRO"


@app.route("/login", methods=["GET"])
def pagina_login():
    return render_template("login.html")


@app.route("/login/post", methods=["POST"])
def fazer_login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    usuario = verificar_usuario(email,senha)

    if usuario:
        session["usuario_logado"] = usuario
        return redirect ("/")
    else:
        return redirect("/login")
    

# @app.route("/api/categorias")
# def api_categorias():
    

@app.route("/produtos")
def pg_produtos():
    itens_produtos = select_produtos()
    return render_template ("produto.html", item_produtos = itens_produtos)


@app.route("/api/get/carrinho", methods=["GET"])
def api_get_carrinho():
    if "usuario_logado" in session:
        carrinho = recuperar_carrinho(session["usuario_logado"]["email"])
        return jsonify(carrinho), 200
    else:
        return jsonify({"message":"Usuário não logado"}), 401
    

@app.route("/api/post/item_carrinho", methods=["POST"])
def api_post_item_carrinho():
    if "usuario_logado" in session:
        email = session["usuario_logado"]["email"]
        dados_json = request.get_json()
        cod_prod = dados_json.get("cod_prod")
        quantidade = dados_json.get("quantidade")

        inserir_item(email, cod_prod, quantidade)
        return jsonify({"message":"Inserido com sucesso"}), 200

    else:
        return redirect("/login")
    
@app.route("/api/post/deletar_item_carrinho", methods=["POST"])
def api_post_deletar_carrinho():
    if "usuario_logado" in session:
        dados_json = request.get_json()
        cod_prod = dados_json.get("cod_prod")
        
        deletar(cod_prod)
        return jsonify({"message": "Deletado com sucesso"}), 200
    else:
        return jsonify({"message": "Usuário não logado"}), 401




if __name__ == "__main__":
    app.run(debug=True)







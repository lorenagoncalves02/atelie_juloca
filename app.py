from flask import Flask, jsonify, redirect, render_template, request, session
from model.comentarios import recuperar_comentario
from model.usuario import cadastro
from model.usuario import verificar_usuario
from model.produtos import recuperar_produto_unico, select_produtos

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
    


@app.route("/produtos")
def pg_produtos():
    itens_produtos = select_produtos()
    return render_template ("produto.html", item_produtos = itens_produtos)


@app.route("/produto/<cod_prod>")
def pg_produto_unico(cod_prod):
    unico = recuperar_produto_unico(cod_prod)
    comentarios = recuperar_comentario(cod_prod)
    return render_template("produto_unico.html", unico = unico, comentarios = comentarios)



@app.route("/produto/comentarios", methods=["POST"])
def adicionar_comentario():
    if not session.get("usuario_logado"):
        return redirect("/login")

    cod_prod = request.form.get("cod_prod")
    comentario = request.form.get("comentario")

    usuario = session["usuario_logado"]
    email = usuario["email"]

    adicionar_comentario(cod_prod, email, comentario)    
    return redirect("/")
    



if __name__ == "__main__":
    app.run(debug=True)







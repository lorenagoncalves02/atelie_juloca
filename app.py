from flask import Flask, flash, redirect, render_template, request, session
import mysql.connector
from model.comentarios import inserir_comentario
from model.usuario import cadastro
from model.usuario import verificar_usuario

app = Flask(__name__)
app.secret_key = "mem424"


@app.route("/")

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
        return redirect ("/cadastro")
    else:
        flash("Usuário ou senha inválidos.", "danger")
        return redirect("/login")
    

    
@app.route("/produto", methods=["GET"])
def pagina_produto_unico():
    return render_template("produto_unico.html")


@app.route("/produto/comentarios", methods=["POST"])
def pagina_comentarios():
    if "usuario_logado" in session:
        email = session["usuario_logado"]["email"]
        comentario = request.form.get("comentario")
        cod_produto = request.form.get("cod_prod")
        inserir_comentario(email, comentario, cod_produto)







    




















if __name__ == "__main__":
    app.run(debug=True)


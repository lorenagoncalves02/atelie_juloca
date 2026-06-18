from flask import Flask, flash, redirect, render_template, request, session
from model.usuario import cadastro
from model.usuario import verificar_usuario
from model.produtos import recuperar_produto_unico, select_produtos
from model.comentarios import inserir_comentario

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
        flash("Usuário ou senha inválidos.", "danger")
        return redirect("/login")
    

    


@app.route("/produtos")
def pg_produtos():
    itens_produtos = select_produtos()
    return render_template ("produto.html", item_produtos = itens_produtos)



@app.route("/produto", methods=["GET"])
def pg_produto_unico():
    return render_template("produto_unico.html")



@app.route("/produto/<int:cod_prod>")
def retornar_produto(cod_prod):
    unico = recuperar_produto_unico(cod_prod)
    return render_template("produto_unico.html", unico = unico)




# @app.route("/produto/comentarios", methods=["POST"])
# def pagina_comentarios():
#     if "usuario_logado" in session:
#         email = session["usuario_logado"]["email"]
#         comentario = request.form.get("comentario")
#         cod_produto = request.form.get("cod_prod")
#         inserir_comentario(email, comentario, cod_produto)






if __name__ == "__main__":
    app.run(debug=True)







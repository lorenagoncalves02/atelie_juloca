from flask import Flask, flash, redirect, render_template, request, session, jsonify
from model.usuario import cadastro
from model.usuario import verificar_usuario
from model.produtos import select_produtos
from model.categorias import select_categorias
from model.produtos import select_pro_cat
from flask import Flask, jsonify, redirect, render_template, request, session
from model.comentarios import inserir_comentario, recuperar_comentario
from model.usuario import cadastro
from model.usuario import verificar_usuario
from model.produtos import recuperar_produto_unico, select_produtos


app = Flask(__name__)

app.secret_key = "mem424"




@app.route("/")
def home():
    return render_template("principal.html")


@app.route("/api/header")
def api_header():
    categorias = select_categorias()
    return jsonify(categorias), 200


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
    categorias = select_categorias()
    return render_template ("produto.html", item_produtos = itens_produtos, categorias = categorias)

@app.route("/produtos/<id_categoria>")
def pg_prod_cat(id_categoria):
    itens_pro_cat = select_pro_cat(id_categoria)
    categorias = select_categorias()
    return render_template ("produto.html", item_produtos = itens_pro_cat, categorias = categorias)

@app.route("/categorias")
def categorias():
    categor = select_categorias()
    return render_template("produto.html", categoria = categor)


@app.route("/produto/<cod_prod>")
def pg_produto_unico(cod_prod):
    unico = recuperar_produto_unico(cod_prod)
    comentarios = recuperar_comentario(cod_prod)

    print("COMENTARIOS:", comentarios)

    return render_template("produto_unico.html", unico = unico, comentarios = comentarios)


@app.route("/produto/comentarios", methods=["POST"])
def adicionar_comentario():
    if not session.get("usuario_logado"):
        return redirect("/login")

    cod_prod = request.form.get("cod_prod")
    comentario = request.form.get("comentario")

    usuario = session["usuario_logado"]
    email = usuario["email"]

    inserir_comentario(email, comentario, cod_prod)   
    return redirect(f"/produto/{cod_prod}")
    

if __name__ == "__main__":
    app.run(debug=True)







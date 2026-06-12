from flask import Flask, render_template, request, redirect
from model.produtos import select_produtos



app = Flask(__name__)

@app.route("/")
def pg_index():
    return render_template ('index.html')

# @app.route("/api/categorias")
# def api_categorias():
    

@app.route("/produtos")
def pg_produtos():
    itens_produtos = select_produtos()
    return render_template ("produto.html", item_produtos = itens_produtos)

#Iniciando o servidor Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
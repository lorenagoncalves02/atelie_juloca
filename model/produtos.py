from database.conexao import conectar

###############################################################################################################
def select_produtos():
    conexao, cursor = conectar()
    
    cursor.execute("SELECT cod_prod, nome_prod, descricao_prod, preco_prod, img_1, img_2, img_3, id_categoria FROM produto;")
    itens_produtos = cursor.fetchall()

    conexao.close()
    return itens_produtos

def select_pro_cat(id_categoria):
    conexao, cursor = conectar()
    
    cursor.execute("SELECT cod_prod, nome_prod, descricao_prod, preco_prod, img_1, img_2, img_3, id_categoria FROM produto WHERE id_categoria=%s;",[id_categoria])
    itens_pro_cat = cursor.fetchall()

    conexao.close()
    return itens_pro_cat
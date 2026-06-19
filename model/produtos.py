from database.conexao import conectar

###############################################################################################################
def select_produtos():
    conexao, cursor = conectar()
    
    cursor.execute("SELECT cod_prod, nome_prod, descricao_prod, preco_prod, img_1, img_2, img_3, id_categoria FROM produto;")
    itens_produtos = cursor.fetchall()

    conexao.close()
    return itens_produtos


def recuperar_produto_unico(cod_prod:int):
    conexao,cursor = conectar()

    cursor.execute("SELECT cod_prod, nome_prod, descricao_prod, preco_prod, img_1, img_2, img_3, id_categoria FROM produto where cod_prod = %s;", [cod_prod])
    unico = cursor.fetchone()

    conexao.close()
    return unico





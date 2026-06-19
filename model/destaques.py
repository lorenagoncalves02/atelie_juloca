from database.conexao import conectar

def select_destaque():
    conexao, cursor = conectar()
    
    cursor.execute("SELECT cod_prod, nome_prod, img_1, id_categoria FROM produto;")
    itens_destaque = cursor.fetchall()

    conexao.close()
    return itens_destaque

def ver_mais():
    conexao, cursor = conectar()
    
    cursor.execute("SELECT cod_prod, nome_prod, img_1, id_categoria FROM produto;")
    itens_destaque = cursor.fetchall()

    conexao.close()
    return itens_destaque
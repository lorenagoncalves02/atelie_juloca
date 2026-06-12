from database.conexao import conectar

###############################################################################################################
def select_categorias():
    conexao, cursor = conectar()
    
    cursor.execute("SELECT id_categoria, nome_categoria FROM categoria")
    categorias = cursor.fetchall()

    conexao.close()
    return categorias
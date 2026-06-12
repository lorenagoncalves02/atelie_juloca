from database.conexao import conectar

def inserir_comentario(comentario, cod_prod):
    try: 

        conexao, cursor = conectar()

        cursor.execute("""
                       INSERT INTO comentarios (comentario, cod_prod) VALUES (%s, %s)
                       
                       """, [comentario, cod_prod])
        
        conexao.commit()
        conexao.close()

        return True
    
    except Exception as erro:
        print(erro)

# def recuperar_comentario():
#     try:
#         conexao, cursor = conectar()

#         cursor.execute()
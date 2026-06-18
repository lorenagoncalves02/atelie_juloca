from database.conexao import conectar

def recuperar_comentario(email:str)->list:
    conexao, cursor = conectar()

    cursor.execute("""SELECT comentarios.cod_comentario, 
                    comentarios.cod_prod, 
                    comentarios.email, 
                    comentarios.comentario
                    from comentarios
                    where comentarios.email = %s;""", [email]) 
    
    comentarios = cursor.fetchall()

    conexao.close()

    return comentarios


def inserir_comentario(comentario, cod_prod):

    conexao, cursor = conectar()

    cursor.execute("""
                    INSERT INTO comentarios (comentario, cod_prod) VALUES (%s, %s)
                    
                    """, [comentario, cod_prod])
    
    conexao.commit()
    conexao.close()

    return True
    


    




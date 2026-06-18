from database.conexao import conectar


def recuperar_comentario(email:str)->list:
    conexao, cursor = conectar()

    cursor.execute("""SELECT cod_comentario, 
                    cod_prod, 
                    email, 
                    comentario
                    from comentarios
                    where email = %s;""", [email]) 
    
    comentarios = cursor.fetchall()

    conexao.close()

    return comentarios


def inserir_comentario(email, comentario, cod_prod):

    conexao, cursor = conectar()

    cursor.execute("""
        INSERT INTO comentarios
        (cod_prod, email, comentario)
        VALUES (%s, %s, %s)
    """, [cod_prod, email, comentario])

    conexao.commit()
    conexao.close()
    


    




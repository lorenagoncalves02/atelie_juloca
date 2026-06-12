from database.conexao import conectar

def cadastro(nome:str, email:str, telefone:str, endereco:str, senha:str):
    try: 

        conexao, cursor = conectar()

        cursor.execute("""
                       INSERT INTO cadastro (nome_usu, email, telefone, endereco, senha) VALUES (%s, %s, %s, %s, %s)
                       
                       """, [nome, email, telefone, endereco, senha])
        
        conexao.commit()
        conexao.close()

        return True
    
    except Exception as erro:
        print(erro)


def verificar_usuario(email, senha):
    try:
        conexao, cursor = conectar()

        cursor.execute("""
                       SELECT email, nome_usu
                       FROM cadastro 
                       WHERE email = %s and senha = %s""", [email, senha])
        
        resultado = cursor.fetchone()
        conexao.close()

        return resultado
    
    except Exception as erro:
        print(erro)











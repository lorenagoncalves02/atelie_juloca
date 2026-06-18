from database.conexao import conectar

def recuperar_carrinho(email:str) -> list:
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT carrinho.cod_carrinho, carrinho.email, produto.nome_prod, item_carrinho.quantidade, produto.preco_prod, produto.img_1 FROM carrinho
                    INNER JOIN item_carrinho ON carrinho.cod_carrinho = item_carrinho.cod_carrinho
                    INNER JOIN produto ON produto.cod_prod = item_carrinho.cod_prod
                    WHERE carrinho.email = %s;
                    """,[email])
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def inserir_item (email,cod_prod,quantidade=1):
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT cod_carrinho from carrinho
                    WHERE email = %s
                    AND finalizado = 0
                    LIMIT 1
                    """,[email])
    resultado_carrinho = cursor.fetchone()

    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho["cod_carrinho"]
    else:
        cursor.execute("""
                        INSERT INTO carrinho (email)
                        VALUES (%s);
                        """,[email])
        codigo_carrinho = cursor.lastrowid
        
    cursor.execute("""
                    INSERT INTO item_carrinho
                            (cod_carrinho, cod_prod, quantidade)
                    VALUES (%s, %s, %s);
                    """,[codigo_carrinho, cod_prod, quantidade])
    
    conexao.commit()

    conexao.close()


def deletar(codigo:int):

    conexao, cursor = conectar()

    cursor.execute("DELETE FROM item_carrinho WHERE cod_prod = %s",[codigo])
    
    conexao.commit()

    conexao.close()
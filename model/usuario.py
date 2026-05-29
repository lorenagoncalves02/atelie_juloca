from database.conexao import conectar    

def cadastro(self):

        conexao, cursor = conectar()

        cursor.execute("INSERT INTO usuario (nome, senha, usuario) VALUES (%s, %s, %s)",(self.nome, self.senha, self.usuario))

        conexao.commit()
        conexao.close()

        return True
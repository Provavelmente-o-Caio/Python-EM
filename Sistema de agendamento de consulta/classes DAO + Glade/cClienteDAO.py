from cCliente import *
import sqlite3


class ClienteDAO:

    def __init__(self):
        self.conn = sqlite3.connect('central_dados.db')
        self.cria_tabela()

    def __del__(self):
        self.conn.close()

    def cria_tabela(self):
        cursor = self.conn.cursor()

        texte_Sql = """
        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf VARCHAR(11) AUTOINCREMENT,
            sintoma TEXT NOT NULL
        );
        """
        cursor.execute(texte_Sql)

    def cadastrar(self, p:Cliente):
        cursor = self.conn.cursor()

        texto_Sql = """
        INSERT INTO cliente (nome, idade, cpf, sintoma)
        VALUES (?,?,?,?);
        """

        tupla_valores = (p.get_nome(), str(p.get_idade()), p.get_cpf(), p.get_id_cliente())
        cursor.execute(texto_Sql, tupla_valores)

        id_cliente = cursor.lastrowid
        self.conn.commit()
        return id_cliente

    def listar_todos(self):
        lista = []
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM cliente
        """

        cursor.execute(texto_Sql)
        for linha in cursor.fetchall():
            c = Cliente()
            c.set_id_cliente(linha[0])
            c.set_nome(linha[1])
            c.set_idade(linha[2])
            c.set_cpf(linha[3])
            c.set_sintoma_principal(linha[4])
            lista.append(c)
        return lista

    def listar_nome(self, pedaco_nome):
        lista = []
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM cliente WHERE nome LIKE ?
        """

        tupla_valores = ((pedaco_nome+"%"),)
        cursor.execute(texto_Sql, tupla_valores)

        for linha in cursor.fetchall():
            c = Cliente()
            c.set_id_cliente(linha[0])
            c.set_nome(linha[1])
            c.set_idade(linha[2])
            c.set_cpf(linha[3])
            c.set_sintoma_principal(linha[4])
            lista.append(c)
        return lista

    def listar_id_cliente(self, idc):
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM cliente WHERE id_cliente=?;
        """
        tupla_valores = (str(idc),)

        cursor.execute(texto_Sql,tupla_valores)
        p = Cliente()
        for linha in cursor.fetchall():
            p.set_id_cliente(linha[0])
            p.set_nome(linha[1])
            p.set_idade(linha[2])
            p.set_cpf(linha[3])
            p.set_sintoma_principal(linha[4])

        return p

    def listar_sintoma_principal(self, sint_p):
        lista = []
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM cliente WHERE nome LIKE ?
        """

        tupla_valores = ((sint_p+"%"),)
        cursor.execute(texto_Sql, tupla_valores)

        for linha in cursor.fetchall():
            s = Cliente()
            s.set_id_cliente(linha[0])
            s.set_nome(linha[1])
            s.set_idade(linha[2])
            s.set_cpf(linha[3])
            s.set_sintoma_principal(linha[4])
            lista.append(s)
        return lista

    def editar(self, p):
        cursor = self.conn.cursor()

        texto_Sql = """
        UPDATE cliente
        SET nome = ?, idade = ?, cpf = ?, sintoma = ?
        WHERE id_cliente = ?
        """

        tupla_valores = (p.get_nome(), str(p.get_idade()), p.get_cpf(), p.get_sintoma_principal(), str(p.get_id_cliente()))
        cursor.execute(texto_Sql, tupla_valores)

        self.conn.commit()

    def apagar(self,idc):
        cursor = self.conn.cursor()

        texto_Sql = """
        DELETE FROM cliente
        WHERE id_cliente = ?
        """

        tupla_valores = (str(idc))
        cursor.execute(texto_Sql, tupla_valores)

        self.conn.commit()
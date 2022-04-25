from cMedico import *
import sqlite3


class MedicoDAO:

    def __init__(self):
        self.conn = sqlite3.connect('central_dados.db')
        self.cria_tabela()

    def __del__(self):
        self.conn.close()

    def cria_tabela(self):
        cursor = self.conn.cursor()

        texto_Sql = """
        CREATE TABLE IF NOT EXISTS medico(
            crm INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf VARCHAR(11),
            especializacao TEXT NOT NULL
        );
        """

        cursor.execute(texto_Sql)

    def cadastrar(self, p:Medico):
        cursor = self.conn.cursor()

        texto_Sql = """
        INSERT INTO medico (nome, idade, cpf, especializacao)
        VALUES (?,?,?,?);
        """

        tupla_Valores= (p.get_nome(), str(p.get_idade()), p.get_cpf(), p.get_especializacao())
        cursor.execute(texto_Sql, tupla_Valores)

        crm=cursor.lastrowid
        self.conn.commit()
        return crm

    def listar_todos(self):
        lista = []
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM medico;
        """

        cursor.execute(texto_Sql)
        for linha in cursor.fetchall():
            m = Medico()
            m.set_crm(linha[0])
            m.set_nome(linha[1])
            m.set_idade(linha[2])
            m.set_cpf(linha[3])
            m.set_especializacao(linha[4])
            lista.append(m)
        return lista

    def listar_nome(self, pedaco_nome):
        lista = []
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM medico WHERE nome LIKE ?
        """

        tupla_valores = ((pedaco_nome+"%"),)
        cursor.execute(texto_Sql, tupla_valores)

        for linha in cursor.fetchall():
            m = Medico()
            m.set_crm(linha[0])
            m.set_nome(linha[1])
            m.set_idade(linha[2])
            m.set_cpf(linha[3])
            m.set_especializacao(linha[4])
            lista.append(m)
        return lista

    def listar_crm(self, crm):
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM medico WHERE crm=?;
        """
        tupla_valores = (str(crm),)

        cursor.execute(texto_Sql, tupla_valores)
        p = Medico()
        for linha in cursor.fetchall():
            p.set_crm(linha[0])
            p.set_nome(linha[1])
            p.set_idade(linha[2])
            p.set_cpf(linha[3])
            p.set_especializacao(linha[4])

        return p

    def listar_especilizacao(self, esp):
        lista = []
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM medico WHERE especializacao LIKE ?
        """

        tupla_valores = ((esp+"%"),)
        cursor.execute(texto_Sql, tupla_valores)

        for linha in cursor.fetchall():
            e = Medico()
            e.set_crm(linha[0])
            e.set_nome(linha[1])
            e.set_idade(linha[2])
            e.set_cpf(linha[3])
            e.set_especializacao(linha[4])
            lista.append(e)
        return lista

    def editar(self, p):
        cursor = self.conn.cursor()

        texto_Sql = """
        UPDATE medico
        SET nome = ?, idade = ?, cpf = ?, especializacao = ?
        WHERE crm = ?
        """

        tupla_valores = (p.get_nome(), str(p.get_idade()), p.get_cpf(), p.get_especializacao(), str(p.get_crm()))
        cursor.execute(texto_Sql, tupla_valores)

        self.conn.commit()

    def apagar(self, crm):
        cursor = self.conn.cursor()

        texto_Sql = """
        DELETE FROM medico
        WHERE crm = ?
        """

        tupla_valores = (str(crm))
        cursor.execute(texto_Sql, tupla_valores)

        self.conn.commit()
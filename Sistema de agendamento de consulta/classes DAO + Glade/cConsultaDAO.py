import sqlite3
import datetime
from cConsulta import *

class ConsultaDAO:

    def __init__(self):
        self.conn = sqlite3.connect('central_dados.db')
        self.cria_tabela()

    def __del__(self):
        self.conn.close()

    def cria_tabela(self):
        cursor = self.conn.cursor()

        texto_Sql = """
        CREATE TABLE IF NOT EXISTS consulta(
            id_consulta INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            crm_medico INTEGER NOT NULL,
            FOREIGN KEY (crm_medico) REFERENCES medico(crm),
            id_cliente INTEGER NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
            inicio_consulta TIMESTAMP NOT NULL,
            fim_consulta TIMESTAMP NOT NULL,
        );
        """
        cursor.execute(texto_Sql)

    def cadastrar(self, c):
        cursor = self.conn.cursor()

        texto_Sql = """
        INSERT INTO consulta (crm_medico, id_cliente, inicio_consulta, fim_consulta)
        VALUES (?,?,?,?);
        """

        x = datetime.datetime(c.get_ano(), c.get_mes(), c.get_dia(), c.get_hora(), c.get_minuto())
        y = datetime.datetime(c.get_ano(), c.get_mes(), c.get_dia(), c.get_hora_fim(), c.get_minuto_fim())
        tupla_valores = (str(c.get_crm_medico()), str(c.get_id_cliente()), x, y)
        cursor.execute(texto_Sql, tupla_valores)

        id_consulta = cursor.lastrowid
        self.conn.commit()
        return id_consulta

    def listar_todos(self):
        lista = []
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM consulta;
        """

        cursor.execute(texto_Sql)
        for linha in cursor.fetchall():
            c = Consulta()
            c.set_id(linha[0])
            c.set_crm_medico(linha[1])
            c.set_id_cliente(linha[2])
            data_inicio = linha[3]
            c.set_ano(data_inicio.split()[0].split('-')[0])
            c.set_mes(data_inicio.split()[0].split('-')[1])
            c.set_dia(data_inicio.split()[0].split('-')[2])
            c.set_hora(data_inicio.split()[1].split(':')[0])
            c.set_minuto(data_inicio.split()[1].split(':')[1])
            data_fim = linha[4]
            c.set_ano(data_fim.split()[0].split('-')[0])
            c.set_mes(data_fim.split()[0].split('-')[1])
            c.set_dia(data_fim.split()[0].split('-')[2])
            c.set_hora_fim(data_fim.split()[1].split(':')[0])
            c.set_minuto_fim(data_fim.split()[1].split(':')[1])
            lista.append(c)
        return lista

    def listar_todos2t(self):
        lista = []
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT co.id_consulta, co.crm_medico, co.id_cliente, co.inicio_consulta, co.fim_consulta,
        cl.id_cliente, cl.nome, cl.idade, cl.cpf, cl.sintoma,
        m.crm, m.nome, m.idade, m.cpf, m.especializacao
        FROM consulta c, cliente cl, medico m
        WHERE co.id_consulta=cl.id_cliente
        WHERE co.crm_medico=m.crm;
        """
        cursor.execute(texto_Sql)
        for linha in cursor.fetchall():
            co = Consulta()
            co.set_id(linha[0])
            #co.set_crm_medico(linha[1])
            #co.set_id_cliente(linha[2])
            data_inicio = linha[3]
            co.set_ano(data_inicio.split()[0].split('-')[0])
            co.set_mes(data_inicio.split()[0].split('-')[1])
            co.set_dia(data_inicio.split()[0].split('-')[2])
            co.set_hora(data_inicio.split()[1].split(':')[0])
            co.set_minuto(data_inicio.split()[1].split(':')[1])
            data_fim = linha[4]
            co.set_ano(data_fim.split()[0].split('-')[0])
            co.set_mes(data_fim.split()[0].split('-')[1])
            co.set_dia(data_fim.split()[0].split('-')[2])
            co.set_hora_fim(data_fim.split()[1].split(':')[0])
            co.set_minuto_fim(data_fim.split()[1].split(':')[1])
            lista.append(co)

            cl = Cliente()
            cl.set_id_cliente(linha[5])
            cl.set_nome(linha[6])
            cl.set_idade(linha[7])
            cl.set_cpf(linha[8])
            cl.set_sintoma_principal(linha[9])

            m = Medico()
            m.set_crm(linha[10])
            m.set_nome(linha[11])
            m.set_idade(linha[12])
            m.set_cpf(linha[13])
            m.set_especializacao(linha[14])
            co.set_crm_medico(m)
            co.set_id_cliente(cl)
        return lista

    def listar_id(self, id):
        cursor = self.conn.cursor()

        texto_Sql = """
        SELECT * FROM consulta WHERE id_consulta=?;
        """

        tupla_valores = (str(id))

        cursor.execute(texto_Sql, tupla_valores)
        co = Consulta()
        for linha in cursor.fetchall():
            co.set_id(linha[0])
            co.set_crm_medico(linha[1])
            co.set_id_cliente(linha[2])
            data_inicio = linha[3]
            co.set_ano(data_inicio.split()[0].split('-')[0])
            co.set_mes(data_inicio.split()[0].split('-')[1])
            co.set_dia(data_inicio.split()[0].split('-')[2])
            co.set_hora(data_inicio.split()[1].split(':')[0])
            co.set_minuto(data_inicio.split()[1].split(':')[1])
            data_fim = linha[4]
            co.set_ano(data_fim.split()[0].split('-')[0])
            co.set_mes(data_fim.split()[0].split('-')[1])
            co.set_dia(data_fim.split()[0].split('-')[2])
            co.set_hora_fim(data_fim.split()[1].split(':')[0])
            co.set_minuto_fim(data_fim.split()[1].split(':')[1])
        return co

    def editar(self,c):
        cursor = self.conn.cursor()

        texto_Sql = """
        UPDATE consulta
        SET crm_medico = ?, id_cliente = ?, inicio_consulta = ?, fim_consulta = ?
        WHERE id_consulta = ?
        """

        x = datetime.datetime(c.get_ano(), c.get_mes(), c.get_dia(), c.get_hora(), c.get_minuto())
        y = datetime.datetime(c.get_ano(), c.get_mes(), c.get_dia(), c.get_hora_fim(), c.get_minuto_fim())
        tupla_valores = (str(c.get_crm_medico()), str(c.get_id_cliente()), x, y)
        cursor.execute(texto_Sql, tupla_valores)

        self.conn.commit()

    def apagar(self, idc):
        cursor = self.conn.cursor()

        texto_Sql = """
        DELECT FROM consulta
        WHERE id_consulta = ?
        """

        tupla_valores = (str(idc))
        cursor.execute(texto_Sql, tupla_valores)

        self.conn.commit()
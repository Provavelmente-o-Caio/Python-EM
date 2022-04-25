import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from cReferencias import *
from cBancoMedicos import *
from cBancoClientes import *
from cBancoConsulta import *
from cCadastraMedicos import *
from cCadastraClientes import *
from cCadastraConsultas import *
from cEditarMedicos import *
from cEditarClientes import *
from cEditarConsultas import *
from cListaMedicos import *
from cListaClientes import *
from cListaConsultas import *

class MenuGlade:

    def __init__(self):
        self.preDAOmed = BancoMedicos()
        self.preDAOcli = BancoClientes()
        self.preDAOcon = BancoConsulta()

        self.criador = Gtk.Builder()
        self.criador.add_from_file('tela.glade')
        self.janela = self.criador.get_object('wi_janela_principal')

        self.criador.connect_signals(Manipulador(self.criador, self.preDAOmed, self.preDAOcli, self.preDAOcon))
        self.janela.show_all()
        Gtk.main()

class Manipulador:

    def __init__(self, p_criador, p_preDAOmed, p_preDAOcli, p_preDAOcon):
        self.r = Referencias(p_criador)

        self.cadMedico = CadastraMedidos(p_preDAOmed, self.r)
        self.editMedico = EditarMedicos(p_preDAOmed, self.r)
        self.lisMedico = ListaMedicos(p_preDAOmed, self.r)

        self.cadCliente = CadastraClientes(p_preDAOcli, self.r)
        self.editCliente = EditarClientes(p_preDAOcli, self.r)
        self.lisCliente = ListaClientes(p_preDAOcli, self.r)

        self.cadConsulta = CadastraConsultas(p_preDAOcon, self.r)
        self.editConsulta = EditarConsultas(p_preDAOcon, self.r)
        self.lisConsulta = ListaConsultas(p_preDAOcon, self.r)

        self.r_pilha = self.r.r_pilha
        self.r_pilha.set_visible_child_name('pg_menu')

    #Página do Menu principal
    def on_wi_janela_principal_destroy(self, janela):
        Gtk.main_quit()

    def on_bt_ls_con_1_clicked(self, botao):
        self.lisConsulta.listar()

    def on_bt_cd_con_1_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_cadastrar_consulta')

    def on_bt_cd_pes_1_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_pessoas')

    def on_bt_sair_1_clicked(self, botao):
        Gtk.main_quit()

    #Página de listar consultas
    def on_bt_voltar_2_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_menu')

    def on_bt_editar_2_clicked(self, botao):
        self.lisConsulta.editar()

    def on_bt_apagar_2_clicked(self, botao):
        self.lisConsulta.apagar()

    #Página de cadastro de consulta
    def on_bt_voltar_3_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_menu')

    def on_bt_salvar_3_clicked(self, botao):
        self.cadConsulta.salvar()

    #Página de interação com pessoas
    def on_bt_cad_med_4_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_cadastro_medico')

    def on_bt_cad_cli_4_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_cadastro_cliente')

    def on_bt_ls_med_4_clicked(self, botao):
        self.lisMedico.listar()

    def on_bt_ls_cli_4_clicked(self, botao):
        self.lisCliente.listar()

    def on_bt_voltar_4_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_menu')

    #Página de cadastro de médico
    def on_bt_sair_5_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_pessoas')

    def on_bt_salvar_5_clicked(self, botao):
        self.cadMedico.salvar()

    #Página de cadastro de cliente
    def on_bt_sair_6_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_pessoas')

    def on_bt_salvar_6_clicked(self, botao):
        self.cadCliente.salvar()

    #Página de edição de medico
    def on_bt_sair_7_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_lista_medico')

    def on_bt_salvar_7_clicked(self, botao):
        self.editMedico.salvar()

    #Página de edição de Cliente
    def on_bt_sair_8_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_lista_cliente')

    def on_bt_salvar_8_clicked(self, botao):
        self.editCliente.salvar()

    #Página de listar medico
    def on_bt_sair_9_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_pessoas')

    def on_bt_editar_9_clicked(self, botao):
        self.lisMedico.editar()

    def on_bt_apagar_9_clicked(self, botao):
        self.lisMedico.apagar()

    #Página de listar cliente
    def on_bt_sair_10_clicked(self,botao):
        self.r_pilha.set_visible_child_name('pg_pessoas')

    def on_bt_editar_10_clicked(self, botao):
        self.lisCliente.editar()

    def on_bt_apagar_10_clicked(self, botao):
        self.lisCliente.apagar()

    #Página de editar cadastro da consulta
    def on_bt_voltar_11_clicked(self, botao):
        self.r_pilha.set_visible_child_name('pg_listar_consulta')

    def on_bt_salvar_11_clicked(self, botao):
        self.editConsulta.salvar()
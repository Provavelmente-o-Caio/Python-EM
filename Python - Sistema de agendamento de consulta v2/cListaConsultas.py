class ListaConsultas:

    def __init__(self, controle, r):
        self.ponteiro_controle = controle

        self.r_cad_id_c = r.r_cad_id_c
        self.r_cad_crm_c_e = r.r_cad_crm_c_e
        self.r_cad_idp_c_e = r.r_cad_idp_c_e
        self.r_cad_ano_c_e = r.r_cad_ano_c_e
        self.r_cad_mes_c_e = r.r_cad_mes_c_e
        self.r_cad_dia_c_e = r.r_cad_dia_c_e
        self.r_cad_hora_en_c_e = r.r_cad_hora_en_c_e
        self.r_cad_min_en_c_e = r.r_cad_min_en_c_e
        self.r_cad_hora_sd_c_e = r.r_cad_hora_sd_c_e
        self.r_cad_min_sd_c_e = r.r_cad_min_sd_c_e
        self.r_pilha = r.r_pilha
        self.r_lista = r.r_lista
        self.r_tabela = r.r_tabela

    def listar(self):
        self.r_pilha.set_visible_child_name('pg_listar_consulta')
        self.r_lista.clear()
        print(type(self.ponteiro_controle))
        l = self.ponteiro_controle.listar_todos()
        print(type(l))
        for pes in l:
            dataC=str(pes.get_ano())+"/"+str(pes.get_mes())+"/"+str(pes.get_dia())
            horaI=str(pes.get_hora())+":"+str(pes.get_minuto())
            horaF=str(pes.get_hora_fim())+":"+str(pes.get_minuto_fim())
            print(type(self.r_lista))
            self.r_lista.append((pes.get_id(),pes.get_crm_medico(), pes.get_id_cliente(), dataC, horaI, horaF))

    def apagar(self):
        modelo, caminhos = self.r_tabela.get_selection().get_selected_rows()
        for cam in caminhos:
            elemento = modelo.get_iter(cam)
            valor = modelo.get_value(elemento, 0)  # 0 é a coluna do código

            self.r_lista.remove(elemento)
            self.ponteiro_controle.apagar_id(valor)

    def editar(self):
        modelo, caminhos = self.r_tabela.get_selection().get_selected_rows()
        for cam in caminhos:
            elemento = modelo.get_iter(cam)
            id = modelo.get_value(elemento, 0)
            crm = modelo.get_value(elemento, 1)
            idc = modelo.get_value(elemento, 2)
            dataC = modelo.get_value(elemento, 3)
            l = []
            l = dataC.split("/")
            ano = l[0]
            mes = l[1]
            dia = l[2]
            l.clear()
            horaI = modelo.get_value(elemento, 4)
            x = []
            x = horaI.split(':')
            hora_en = x[0]
            min_en = x[1]
            x.clear()
            horaF = modelo.get_value(elemento, 5)
            y = []
            y = horaF.split(':')
            hora_sd = y[0]
            min_sd = y[1]
            self.id_consulta = id

            self.r_cad_id_c.set_text(str(id))
            self.r_cad_crm_c_e.set_text(str(crm))
            self.r_cad_idp_c_e.set_text(str(idc))
            self.r_cad_ano_c_e.set_text(ano)
            self.r_cad_mes_c_e.set_text(mes)
            self.r_cad_dia_c_e.set_text(dia)
            self.r_cad_hora_en_c_e.set_text(hora_en)
            self.r_cad_min_en_c_e.set_text(min_en)
            self.r_cad_hora_sd_c_e.set_text(hora_sd)
            self.r_cad_min_sd_c_e.set_text(min_sd)
            self.r_pilha.set_visible_child_name('pg_editar_consulta')
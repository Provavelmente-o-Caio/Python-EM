class EditarConsultas:

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

    def salvar(self):
        crm = int(self.r_cad_crm_c_e.get_text())
        idp = int(self.r_cad_idp_c_e.get_text())
        ano = int(self.r_cad_ano_c_e.get_text())
        mes = int(self.r_cad_mes_c_e.get_text())
        dia = int(self.r_cad_dia_c_e.get_text())
        hora_e = int(self.r_cad_hora_en_c_e.get_text())
        min_e = int(self.r_cad_min_en_c_e.get_text())
        hora_s = int(self.r_cad_hora_sd_c_e.get_text())
        min_s = int(self.r_cad_min_sd_c_e.get_text())
        i = int(self.r_cad_id_c.get_text())
        self.ponteiro_controle.editar(crm, idp, ano, mes, dia, hora_e, min_e, hora_s, min_s, i)
        self.r_pilha.set_visible_child_name('pg_menu')
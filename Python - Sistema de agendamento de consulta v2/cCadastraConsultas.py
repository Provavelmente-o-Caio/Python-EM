class CadastraConsultas:

    def __init__(self, preDAO, r):
        self.ponteiro_preDAOco = preDAO

        self.r_cad_id_c = r.r_cad_id_c
        self.r_cad_crm_c = r.r_cad_crm_c
        self.r_cad_idp_c = r.r_cad_idp_c
        self.r_cad_ano_c = r.r_cad_ano_c
        self.r_cad_mes_c = r.r_cad_mes_c
        self.r_cad_dia_c = r.r_cad_dia_c
        self.r_cad_hora_en_c = r.r_cad_hora_en_c
        self.r_cad_min_en_c = r.r_cad_min_en_c
        self.r_cad_hora_sd_c = r.r_cad_hora_sd_c
        self.r_cad_min_sd_c = r.r_cad_min_sd_c

    def salvar(self):
        id = int(self.r_cad_id_c.get_text())
        crm = int(self.r_cad_crm_c.get_text())
        idp = int(self.r_cad_idp_c.get_text())
        ano = int(self.r_cad_ano_c.get_text())
        mes = int(self.r_cad_mes_c.get_text())
        dia = int(self.r_cad_dia_c.get_text())
        hora_e = int(self.r_cad_hora_en_c.get_text())
        min_e = int(self.r_cad_min_en_c.get_text())
        hora_s = int(self.r_cad_hora_sd_c.get_text())
        min_s = int(self.r_cad_min_sd_c.get_text())
        print(type(self.ponteiro_preDAOco))
        self.ponteiro_preDAOco.Cadastrar(id, crm, idp, ano, mes, dia, hora_e, min_e, hora_s, min_s)
        self.r_cad_id_c.set_text("")
        self.r_cad_crm_c.set_text("")
        self.r_cad_idp_c.set_text("")
        self.r_cad_ano_c.set_text("")
        self.r_cad_mes_c.set_text("")
        self.r_cad_dia_c.set_text("")
        self.r_cad_hora_en_c.set_text("")
        self.r_cad_min_en_c.set_text("")
        self.r_cad_hora_sd_c.set_text("")
        self.r_cad_min_sd_c.set_text("")
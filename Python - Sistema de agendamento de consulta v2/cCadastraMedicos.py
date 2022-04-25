class CadastraMedidos:

    def __init__(self, preDAO, r):
        self.ponteiro_preDAOm = preDAO

        self.r_cad_crm_m = r.r_cad_crm_m
        self.r_cad_nome_m = r.r_cad_nome_m
        self.r_cad_idade_m = r.r_cad_idade_m
        self.r_cad_cpf_m  = r.r_cad_cpf_m
        self.r_cad_esp_m = r.r_cad_esp_m

    def salvar(self):
        crm = int(self.r_cad_crm_m.get_text())
        nome = self.r_cad_nome_m.get_text()
        idade = int(self.r_cad_idade_m.get_text())
        cpf = self.r_cad_cpf_m.get_text()
        esp = self.r_cad_esp_m.get_text()
        self.ponteiro_preDAOm.cadastrar(crm, nome, idade, cpf, esp)
        self.r_cad_crm_m.set_text("")
        self.r_cad_nome_m.set_text("")
        self.r_cad_idade_m.set_text("")
        self.r_cad_cpf_m.set_text("")
        self.r_cad_esp_m.set_text("")
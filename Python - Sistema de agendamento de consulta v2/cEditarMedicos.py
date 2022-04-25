class EditarMedicos:

    def __init__(self, controle, r):
        self.ponteiro_controle = controle

        self.r_cad_crm_m = r.r_cad_crm_m
        self.r_cad_nome_m_e = r.r_cad_nome_m_e
        self.r_cad_idade_m_e = r.r_cad_idade_m_e
        self.r_cad_cpf_m_e = r.r_cad_cpf_m_e
        self.r_cad_esp_m_e = r.r_cad_esp_m_e
        self.r_pilha = r.r_pilha

    def salvar(self):
        nome = self.r_cad_nome_m_e.get_text()
        idade = int(self.r_cad_idade_m_e.get_text())
        cpf = self.r_cad_cpf_m_e.get_text()
        esp = self.r_cad_esp_m_e.get_text()
        crm = int(self.r_cad_crm_m.get_text())

        self.ponteiro_controle.editar(nome, idade, cpf, esp, crm)
        self.r_pilha.set_visible_child_name('pg_pessoas')
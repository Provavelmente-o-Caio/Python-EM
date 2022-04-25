class CadastraClientes:

    def __init__(self, preDAO, r):
        self.ponteiro_preDAO_cl = preDAO

        self.r_cad_id_p = r.r_cad_id_p
        self.r_cad_nome_p = r.r_cad_nome_p
        self.r_cad_idade_p = r.r_cad_idade_p
        self.r_cad_cpf_p = r.r_cad_cpf_p
        self.r_cad_sp_p = r.r_cad_sp_p

    def salvar(self):
        id = int(self.r_cad_id_p.get_text())
        nome = self.r_cad_nome_p.get_text()
        idade = int(self.r_cad_idade_p.get_text())
        cpf = self.r_cad_cpf_p.get_text()
        sp = self.r_cad_sp_p.get_text()
        self.ponteiro_preDAO_cl.cadastrar(id, nome, idade, cpf, sp)
        self.r_cad_id_p.set_text("")
        self.r_cad_nome_p.set_text("")
        self.r_cad_idade_p.set_text("")
        self.r_cad_cpf_p.set_text("")
        self.r_cad_sp_p.set_text("")
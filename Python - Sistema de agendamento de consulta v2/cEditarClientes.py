class EditarClientes:

    def __init__(self, controle, r):
        self.ponteiro_controle = controle

        self.r_cad_id_p = r.r_cad_id_p
        self.r_cad_nome_p_e = r.r_cad_nome_p_e
        self.r_cad_idade_p_e = r.r_cad_idade_p_e
        self.r_cad_cpf_p_e = r.r_cad_cpf_p_e
        self.r_cad_sp_p_e = r.r_cad_sp_p_e
        self.r_pilha = r.r_pilha

    def salvar(self):
        nome = self.r_cad_nome_p_e.get_text()
        idade = int(self.r_cad_idade_p_e.get_text())
        cpf = self.r_cad_cpf_p_e.get_text()
        sp = self.r_cad_sp_p_e.get_text()
        idc = self.r_cad_id_p.get_text()

        self.ponteiro_controle.editar(nome, idade, cpf, sp, idc)
        self.r_pilha.set_visible_child_name('pg_pessoas')
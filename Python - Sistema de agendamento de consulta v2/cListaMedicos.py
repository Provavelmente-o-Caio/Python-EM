class ListaMedicos:

    def __init__(self, controle, r):
        self.ponteiro_controle = controle

        self.r_cad_crm_m = r.r_cad_crm_m
        self.r_cad_nome_m_e = r.r_cad_nome_m_e
        self.r_cad_idade_m_e = r.r_cad_idade_m_e
        self.r_cad_cpf_m_e = r.r_cad_cpf_m_e
        self.r_cad_esp_m_e = r.r_cad_esp_m_e
        self.r_pilha = r.r_pilha
        self.r_lista_med = r.r_lista_med
        self.r_tabela_medico = r.r_tabela_medico

    def listar(self):
        self.r_pilha.set_visible_child_name('pg_lista_medico')
        self.r_lista_med.clear()
        l = self.ponteiro_controle.listar_todos()
        for pes in l:
            self.r_lista_med.append((pes.get_crm(), pes.get_nome(), pes.get_idade(), pes.get_cpf(), pes.get_especializacao()))

    def apagar(self):
        modelo, caminhos = self.r_tabela_medico.get_selection().get_selected_rows()
        for cam in caminhos:
            elemento = modelo.get_iter(cam)
            valor = modelo.get_value(elemento, 0)

            self.r_lista_med.remove(elemento)
            self.ponteiro_controle.apagar_crm(valor)

    def editar(self):
        modelo, caminhos = self.r_tabela_medico.get_selection().get_selected_rows()
        for cam in caminhos:
            elemento = modelo.get_iter(str(cam))
            crm = modelo.get_value(elemento, 0)
            nome = modelo.get_value(elemento, 1)
            idade = modelo.get_value(elemento, 2)
            cpf = modelo.get_value(elemento, 3)
            esp = modelo.get_value(elemento, 4)
            self.crm_medico = crm

            self.r_cad_crm_m.set_text(str(crm))
            self.r_cad_nome_m_e.set_text(nome)
            self.r_cad_idade_m_e.set_text(str(idade))
            self.r_cad_cpf_m_e.set_text(cpf)
            self.r_cad_esp_m_e.set_text(esp)
            self.r_pilha.set_visible_child_name('pg_editar_medico')
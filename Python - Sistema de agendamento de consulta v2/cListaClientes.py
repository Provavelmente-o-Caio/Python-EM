class ListaClientes:

    def __init__(self, controle, r):
        self.ponteiro_controle = controle

        self.r_cad_id_p = r.r_cad_id_p
        self.r_cad_nome_p_e = r.r_cad_nome_p_e
        self.r_cad_idade_p_e = r.r_cad_idade_p_e
        self.r_cad_cpf_p_e = r.r_cad_cpf_p_e
        self.r_cad_sp_p_e = r.r_cad_sp_p_e
        self.r_pilha = r.r_pilha
        self.r_lista_cli = r.r_lista_cli
        self.r_tabela_cliente = r.r_tabela_cliente

    def listar(self):
        self.r_pilha.set_visible_child_name('pg_lista_cliente')
        self.r_lista_cli.clear()
        l = self.ponteiro_controle.listar_todos()
        for pes in l:
            self.r_lista_cli.append((pes.get_id_cliente(), pes.get_nome(), pes.get_idade(), pes.get_cpf(), pes.get_sintoma_principal()))

    def apagar(self):
        modelo, caminhos = self.r_tabela_cliente.get_selection().get_selected_rows()
        for cam in caminhos:
            elemento = modelo.get_iter(cam)
            valor = modelo.get_value(elemento, 0) #<-- Representa a colana do código

            self.r_lista_cli.remove(elemento)
            self.ponteiro_controle.apagar_id(valor)

    def editar(self):
        modelo, caminhos = self.r_tabela_cliente.get_selection().get_selected_rows()
        for cam in caminhos:
            elemento = modelo.get_iter(cam)
            idc = modelo.get_value(elemento, 0)
            nome = modelo.get_value(elemento, 1)
            idade = modelo.get_value(elemento, 2)
            cpf = modelo.get_value(elemento, 3)
            sp = modelo.get_value(elemento, 4)
            self.id_cliente = idc

            self.r_cad_id_p.set_text(str(idc))
            self.r_cad_nome_p_e.set_text(nome)
            self.r_cad_idade_p_e.set_text(str(idade))
            self.r_cad_cpf_p_e.set_text(cpf)
            self.r_cad_sp_p_e.set_text(sp)
            self.r_pilha.set_visible_child_name('pg_editar_cliente')
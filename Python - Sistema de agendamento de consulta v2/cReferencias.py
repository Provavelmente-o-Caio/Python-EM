

class Referencias:

    def __init__(self, criador):
        self.ponteiro_criador = criador

        self.r_pilha = self.ponteiro_criador.get_object('st_pilha')
        self.r_lista = self.ponteiro_criador.get_object('ls_lista')
        self.r_lista_med = self.ponteiro_criador.get_object('ls_lista_med')
        self.r_lista_cli = self.ponteiro_criador.get_object('ls_lista_cli')

        self.r_tabela = self.ponteiro_criador.get_object('tv_tabela')
        self.r_tabela_medico = self.ponteiro_criador.get_object('tv_medico')
        self.r_tabela_cliente = self.ponteiro_criador.get_object('tv_cliente')

        self.r_cad_id_p = self.ponteiro_criador.get_object('en_ID_6')
        self.r_cad_nome_p = self.ponteiro_criador.get_object('en_nome_6')
        self.r_cad_idade_p = self.ponteiro_criador.get_object('en_ida_6')
        self.r_cad_cpf_p = self.ponteiro_criador.get_object('en_CPF_6')
        self.r_cad_sp_p = self.ponteiro_criador.get_object('en_sp_6')

        self.r_cad_nome_p_e = self.ponteiro_criador.get_object('en_nome_8')
        self.r_cad_idade_p_e = self.ponteiro_criador.get_object('en_ida_8')
        self.r_cad_cpf_p_e = self.ponteiro_criador.get_object('en_CPF_8')
        self.r_cad_sp_p_e = self.ponteiro_criador.get_object('en_sp_8')

        self.r_cad_crm_m = self.ponteiro_criador.get_object('en_CRM_5')
        self.r_cad_nome_m = self.ponteiro_criador.get_object('en_nome_5')
        self.r_cad_idade_m = self.ponteiro_criador.get_object('en_ida_5')
        self.r_cad_cpf_m = self.ponteiro_criador.get_object('en_CPF_5')
        self.r_cad_esp_m = self.ponteiro_criador.get_object('en_esp_5')

        self.r_cad_nome_m_e = self.ponteiro_criador.get_object('en_nome_7')
        self.r_cad_idade_m_e = self.ponteiro_criador.get_object('en_ida_7')
        self.r_cad_cpf_m_e = self.ponteiro_criador.get_object('en_CPF_7')
        self.r_cad_esp_m_e = self.ponteiro_criador.get_object('en_esp_7')

        self.r_cad_id_c = self.ponteiro_criador.get_object('en_ID_3')
        self.r_cad_crm_c = self.ponteiro_criador.get_object('en_CRM_3')
        self.r_cad_idp_c = self.ponteiro_criador.get_object('en_IDp_3')
        self.r_cad_ano_c = self.ponteiro_criador.get_object('en_ano_3')
        self.r_cad_mes_c = self.ponteiro_criador.get_object('en_mes_3')
        self.r_cad_dia_c = self.ponteiro_criador.get_object('en_dia_3')
        self.r_cad_hora_en_c = self.ponteiro_criador.get_object('en_hora_en_3')
        self.r_cad_min_en_c = self.ponteiro_criador.get_object('en_min_en_3')
        self.r_cad_hora_sd_c = self.ponteiro_criador.get_object('en_hora_sd_3')
        self.r_cad_min_sd_c = self.ponteiro_criador.get_object('en_min_sd_3')

        self.r_cad_crm_c_e = self.ponteiro_criador.get_object('en_CRM_11')
        self.r_cad_idp_c_e = self.ponteiro_criador.get_object('en_IDp_11')
        self.r_cad_ano_c_e = self.ponteiro_criador.get_object('en_ano_11')
        self.r_cad_mes_c_e = self.ponteiro_criador.get_object('en_mes_11')
        self.r_cad_dia_c_e = self.ponteiro_criador.get_object('en_dia_11')
        self.r_cad_hora_en_c_e = self.ponteiro_criador.get_object('en_hora_en_11')
        self.r_cad_min_en_c_e = self.ponteiro_criador.get_object('en_min_en_11')
        self.r_cad_hora_sd_c_e = self.ponteiro_criador.get_object('en_hora_sd_11')
        self.r_cad_min_sd_c_e = self.ponteiro_criador.get_object('en_min_sd_11')
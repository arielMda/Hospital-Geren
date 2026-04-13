def normalizar_cpf(cpf):
    # Remove pontos e traço para padronizar o CPF em apenas dígitos
    return cpf.replace(".", "").replace("-", "")
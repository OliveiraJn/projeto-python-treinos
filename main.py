from cadastro import cadastrar_usuario
from planejamento import gerar_plano

print("=== SISTEMA DE PLANEJAMENTO DE TREINOS ===\n")

dados_usuario = cadastrar_usuario()

gerar_plano(dados_usuario)
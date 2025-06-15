import pandas as pd

# Caminho do arquivo
arquivo = "Analise_de_Dados.xlsx"

# Lê o arquivo Excel
df = pd.read_excel(arquivo)

# Lista de IDs únicos
ids_maquinas = sorted(df['ID MÁQUINA'].unique())
print("🔢 Lista de IDs das máquinas:")
for id_maquina in ids_maquinas:
    print(f"  - {id_maquina}")

# Quantidade de depósitos por máquina
depositos_por_maquina = df['ID MÁQUINA'].value_counts().sort_index()
print("\n📊 Quantidade de depósitos por máquina:")
for maquina_id, total in depositos_por_maquina.items():
    print(f"  - Máquina {maquina_id}: {total} depósitos")

# Total de pontos
total_pontos = df['PONTOS'].sum()
print(f"\n🎯 Total de pontos distribuídos: {total_pontos}")

# Detalhes de cada máquina
print("\n📋 Detalhes por máquina:\n")
for maquina_id, grupo in df.groupby('ID MÁQUINA'):
    print(f"🟩 Máquina {maquina_id} - {len(grupo)} depósitos:")
    print(grupo[['DATA HORA', 'PONTOS']].to_string(index=False))
    print("-" * 40)

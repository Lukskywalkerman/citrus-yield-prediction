#instalar a biblioteca pycaret se ainda não estiver instalada
# !pip install pycaret

import pandas as pd
from pycaret.regression import *

# 1. Carregar seu dataset (ajuste o caminho do arquivo)
df = pd.read_csv('C:\Users\Luktora\Documents\GitHub\Citrus Yeld Prediction\citrus-yield-prediction\data\dataset_citrus_master.csv')

# 2. Configuração do Experimento
# Aqui definimos a variável alvo e removemos colunas de ID ou ano se não quiser que entrem no cálculo
print("Iniciando Setup do PyCaret...")
s = setup(
    data=df, 
    target='produtividade', # ajuste para o nome exato da sua coluna alvo
    session_id=123,         # para garantir reprodutibilidade
    normalize=True,         # importante para modelos sensíveis à escala
    transformation=True,    # ajuda a tornar os dados mais "Gaussianos"
    ignore_features=['ano', 'municipio'], # se houver colunas que não devem ser preditoras
    remove_outliers=True,
    train_size=0.8
)

# 3. Comparação de Modelos
# O PyCaret vai testar cerca de 20 algoritmos (Random Forest, XGBoost, CatBoost, etc.)
print("Comparando modelos... Isso pode levar alguns minutos.")
best_models = compare_models(sort='R2', n_select=3)

# 4. Avaliação Profunda do Melhor Modelo
# Vamos pegar o #1 do ranking e gerar os gráficos de análise
best = best_models[0]
print(f"Melhor modelo encontrado: {best}")

# 5. Gerar Gráficos de Análise (vão abrir no VS Code ou salvar como imagem)
plot_model(best, plot='error')      # Gráfico de Erro (Predição vs Real)
plot_model(best, plot='feature')    # Importância das Variáveis
plot_model(best, plot='residuals')  # Análise de Resíduos

# 6. Finalizar o modelo (Treinar com 100% dos dados para teste final)
final_model = finalize_model(best)

# 7. Salvar para uso futuro
save_model(final_model, 'melhor_modelo_pycaret_citricultura')

print("Processo concluído!")
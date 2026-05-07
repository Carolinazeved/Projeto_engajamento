import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('dados.csv')

# Taxa de engajamento
df['engajamento'] = (
    df['curtidas'] +
    df['comentarios'] +
    df['compartilhamentos']
) / df['visualizacoes']

# Média por tipo de post
resultado = df.groupby('tipo_post')['engajamento'].mean()

# Gráfico
resultado.plot(kind='bar')

plt.title('Engajamento por Tipo de Post')
plt.ylabel('Taxa de Engajamento')
plt.show()

print(resultado)
import pandas as pd

# Carregar o DataFrame a partir do arquivo CSV
df = pd.read_csv(r"C:\Users\lluis\Downloads\argon-dashboard-master\argon-dashboard-master\pages\Plan3.CSV", sep=';', encoding='latin1')

# Converter o DataFrame para HTML
html_tabela = df.to_html(classes='table table-bordered table-striped', index=False)

# Salvar o HTML em um arquivo
with open("tabela.html", "w") as file:
    file.write(html_tabela)

print("Tabela HTML gerada com sucesso!")

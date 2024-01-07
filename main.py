# Import packages
import pandas as pd
from pySankey.sankey import sankey
import matplotlib.pyplot as plt

# Load data and filter
df = pd.read_excel("data.xlsx")
df =df[df["Descrição SH6"].isin(
["Soja, mesmo triturada, exceto para semeadura",
 "Óleos brutos de petróleo ou de minerais betuminosos",
 "Minérios de ferro não aglomerados e seus concentrados",
 "Carnes de bovino, desossadas, congeladas",
 "Milho, exceto para semeadura",
"Tortas e outros resíduos sólidos da extração do óleo de soja",
"Café não torrado, não descafeinado"
"Pasta química de madeira de não conífera, à soda ou sulfato, semibranqueada ou branqueada"
])]
df = df.head(120)
df = df.replace({"Soja, mesmo triturada, exceto para semeadura": "Saca de soja",
                 "Óleos brutos de petróleo ou de minerais betuminosos": "Barril de petróleo",
                 "Minérios de ferro não aglomerados e seus concentrados": "Minério de ferro",
                 "Carnes de bovino, desossadas, congeladas": "Carne bovina",
                 "Milho, exceto para semeadura": "Saca de milho",
                 "Países Baixos (Holanda)": "Holanda",
                 "Taiwan (Formosa)": "Taiwan",
                 "Tortas e outros resíduos sólidos da extração do óleo de soja": "Resíduos de óleo de soja",
                 "Café não torrado, não descafeinado": "Saca de café",
                 "Pasta química de madeira de não conífera, à soda ou sulfato, semibranqueada ou branqueada": "Celulose",
                 })
# Create Sankey diagram again
sankey(
    left=df["Descrição SH6"],
    leftWeight= df["2023 - Valor FOB (US$)"],
    right=df["Países"],
    rightWeight=df["2023 - Valor FOB (US$)"], 
    aspect=60,
    fontsize=8
)
# Get current figure
fig = plt.gcf()

# Set size in inches
fig.set_size_inches(18, 18)

# Set the color of the background to white
fig.set_facecolor("w")
plt.title("Principais exportações e parceiros do Brasil em 2023", fontsize=18)
# Save the figure
fig.savefig("sankey.png",
            bbox_inches="tight",
            dpi=150)
plt.show()

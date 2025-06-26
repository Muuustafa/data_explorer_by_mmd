from data_explorer import get_export, get_import, get_pib

# Récupérer les données d'exportations du Sénégal
df_export = get_export('SN', 2000, 2023)

# Récupérer les données d'importations du Sénégal
df_import = get_import('SN', 2000, 2023)

# Récupérer les données de PIB pour plusieurs pays
df_pib = get_pib(['SN', 'FR'], 2000, 2023)

# Afficher les premières lignes de chaque DataFrame
print("=== Exportations Sénégal ===")
print(df_export.head())

print("\n=== Importations Sénégal ===")
print(df_import.head())

print("\n=== PIB Sénégal et France ===")
print(df_pib.head())
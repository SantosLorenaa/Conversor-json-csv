import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

nome_arquivo = filedialog.askopenfilename(title="Selecione o arquivo JSON ou CSV", filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv")])

if not nome_arquivo:
    print("Nenhum arquivo selecionado. Saindo...")
    exit()
try:
    
     if nome_arquivo.lower().endswith('.json'):
        arquivo = pd.read_json(nome_arquivo)
        nome_final = nome_arquivo.replace('.json', '.csv')
        arquivo.to_csv(nome_final, index=False, encoding='utf-8-sig')
        print(f"Arquivo convertido e salvo como {nome_final}")
        
     elif nome_arquivo.lower().endswiwith('.csv'):
         arquivo = pd.read_csv(nome_arquivo)
         nome_final = nome_arquivo.replace('.csv', '.json')
         arquivo.to_json(nome_final, orient='records', lines=True)
         print(f"Arquivo convertido e salvo como {nome_final}")
         
         
     else:       
        print("Formato de arquivo não suportado. Por favor, selecione um arquivo JSON ou CSV.")
        
except Exception as e:
    print(f"Ocorreu um erro ao processar o arquivo: {e}")
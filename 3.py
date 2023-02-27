import pandas as pd
import statistics as sts

df = pd.read_xml('dados.xml')


##CONSIDERANDO QUE OS DIAS NAO FATURADOS NAO SAO LEVADOS EM CONSIDERACAO
df.remove(0);
menor = df[0]
maior = df[0]
superior_media = 0

for i in range(len(df)):
    if df[i] < menor:
        menor = df[i]
    if df[i] > maior:
        maior = df[i]
    if df[i] > sts.mean(df):
        superior_media += 1

print(menor)
print(maior)
print(superior_media)
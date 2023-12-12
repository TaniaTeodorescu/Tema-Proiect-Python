import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')

X=10
Y=18

plt.figure(figsize=(12, 8))
plt.plot(df.index, df['Durata'], label='Durata', marker='*', color = '#4CAF50')    
plt.plot(df.index, df['Puls'], label='Puls', marker='*', color = 'hotpink')
plt.plot(df.index, df['MaxPuls'], label='MaxPuls', marker='*', color = '#6A3DAC')
plt.plot(df.index, df['Calorii'], label='Calorii', marker='*', color = '#ffca33')
plt.title('Grafic - Puls, MaxPuls, Calorii in functie de Durata')
plt.xlabel('Durata')
plt.ylabel('Puls, MaxPuls, Calorii')
plt.legend()
plt.show()

plt.figure(figsize=(12, 8))
plt.plot(df.index[:10], df['Durata'][:10], label='Durata', marker='*', color = '#4CAF50')
plt.plot(df.index[:10], df['Puls'][:10], label='Puls', marker='*', color = 'hotpink')
plt.plot(df.index[:10], df['MaxPuls'][:10], label='MaxPuls', marker='*', color = '#6A3DAC')
plt.plot(df.index[:10], df['Calorii'][:10], label='Calorii', marker='*', color = '#ffca33')
plt.title('Grafic - Puls, MaxPuls, Calorii in functie de Durata (primele 10 valori)')
plt.xlabel('Durata')
plt.ylabel('Puls, MaxPuls, Calorii')
plt.legend()
plt.show()

plt.figure(figsize=(12, 8))
plt.plot(df.index[-18:], df['Durata'].tail(18), label='Durata', marker='*', color = '#4CAF50')
plt.plot(df.index[-18:], df['Puls'].tail(18), label='Puls', marker='*', color = 'hotpink')
plt.title('Grafic - Puls in functie de Durata (ultimele 18 valori)')
plt.xlabel('Durata')
plt.ylabel('Puls')
plt.legend()
plt.show()
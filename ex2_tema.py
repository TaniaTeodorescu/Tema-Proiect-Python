import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv') #importarea datelor din fisierul data.csv

X=10
Y=18
#Primul grafic in care se reprezinta Puls, MaxPuls si Calorii in functie de Durata
plt.figure(figsize=(12, 8)) #dimensionarea ferestrei unde se va afisa graficul
plt.plot(df.index, df['Durata'], label='Durata', marker='*', color = '#4CAF50') # plot() este o functie ce realizeaza desenarea liniilor graficului intre punctele specificate
plt.plot(df.index, df['Puls'], label='Puls', marker='*', color = 'hotpink')     # de exemplu prin df.index si df['Puls'], cu labelul 'Puls', marker '*' si culoare specificata  
plt.plot(df.index, df['MaxPuls'], label='MaxPuls', marker='*', color = '#6A3DAC')
plt.plot(df.index, df['Calorii'], label='Calorii', marker='*', color = '#ffca33')
plt.title('Grafic - Puls, MaxPuls, Calorii in functie de Durata') # denumirea graficului
plt.xlabel('Durata') # denumirea axei X
plt.ylabel('Puls, MaxPuls, Calorii') # denumirea axei Y
plt.legend() # afisarea legendei graficului
plt.show()
#Al doilea grafic in care se reprezinta primele X=10 valori pt Puls, MaxPuls si Calorii in functie de durata
plt.figure(figsize=(12, 8)) #dimensionarea ferestrei unde se va afisa graficul
plt.plot(df.index[:10], df['Durata'][:10], label='Durata', marker='*', color = '#4CAF50')
plt.plot(df.index[:10], df['Puls'][:10], label='Puls', marker='*', color = 'hotpink')
plt.plot(df.index[:10], df['MaxPuls'][:10], label='MaxPuls', marker='*', color = '#6A3DAC')
plt.plot(df.index[:10], df['Calorii'][:10], label='Calorii', marker='*', color = '#ffca33')
plt.title('Grafic - Puls, MaxPuls, Calorii in functie de Durata (primele 10 valori)')
plt.xlabel('Durata')
plt.ylabel('Puls, MaxPuls, Calorii')
plt.legend()
plt.show()
#Al treilea grafic in care se reprezinta ultimele Y=18 valori doar pt Puls si Durata
plt.figure(figsize=(12, 8)) #dimensionarea ferestrei unde se va afisa graficul
plt.plot(df.index[-18:], df['Durata'].tail(18), label='Durata', marker='*', color = '#4CAF50')
plt.plot(df.index[-18:], df['Puls'].tail(18), label='Puls', marker='*', color = 'hotpink')
plt.title('Grafic - Puls in functie de Durata (ultimele 18 valori)')
plt.xlabel('Durata')
plt.ylabel('Puls')
plt.legend()
plt.show()

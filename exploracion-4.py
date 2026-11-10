import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy as np 

 
fmax = 10                  # Frecuencia maxima [Hz]
 
# Frecuencia de muestreo = 5*fmax
fs = 5 * fmax              # 50 Hz
 
# Intervalo de muestreo
dt = 1 / fs
 
# Numero de muestras
N = 500
 
# Vector de tiempo
t = np.arange(N) * dt
 
archivo = 'Base de datos.xlxs'
df = pd.read_excel(archivo, sheet_name='Hoja1'
)


df.to_excel(
    r"C:\Users\DELL\Downloads\BASE_DE_DATOS.xlxs",
    index=False
)
    

df = pd.read_excelr"C:\Users\DELL\OneDrive\Documentos\alineación_FID.xlsx" index=False)


df['Grav Obs']
df['Grav Teorica 84']
df['Free_Air']
df['Bouguer_ABS']
df['']
# No se que mas definir
df['Grav Obs'] = df['Grav Obs'].astype(float)
df['Grav Teorica 84'] = df['Grav Teorica 84'].astype(float)
df['Free_Air'] = df['Free_Air'].astype(float)
df['Bouguer_ABS'] = df['Bouguer_ABS'].astype(float)
# df[''] = df[''].astype(float)
df['ABS'] = df['GRAV_OBS'].astype(float) - df['GRAV_TEORICA_84'].astype(float)
df['Bouguer'] = df['Bouguer_ABS'].astype(float) - df['Free_Air'].astype(float)
# df['Residual'] = df['ABS'].astype(float) 
df['Free_Air 67'] = df['Free Air'].astype(float)']


read = df.to_excel('Base de datos', index=False)
freq = fmax
 
x = 5 * np.sin(2 * np.pi * freq * t)
 

 
u = np.where(t >= 0, 1, 0)
 
x_causal = x * u
 

 
alpha = 0.7
 
envolvente = 5 * np.exp(-alpha * t)
 
x_decay = x_causal * np.exp(-alpha * t)
 


# PRIMER GRAFICO
plt.subplot(2, 1, 1)
 
plt.stem(t, x_causal, basefmt=" ")
 
plt.title("Señal sinusoidal causal - fs = 5fmax")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
 
# SEGUNDO GRAFICO
plt.subplot(2, 1, 2)
 
plt.plot(t, x_decay, 'b', label='Seno con decaimiento')
plt.plot(t, envolvente, 'r--', label='Envolvente')
 
plt.title("Señal sinusoidal causal con decaimiento - 500 muestras")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.ylim()
plt.xlim()

 
plt.tight_layout()
plt.show()
plt.show
 
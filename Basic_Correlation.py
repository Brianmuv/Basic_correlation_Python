import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

# 1. Cargar un archivo de audio y graficarlo.

# A Uso de read para leer el archivo.
archivo = 'audio.wav'
fs, x = waves.read(archivo)

# B Representacion de la señal x en funcion del tiempo.
t=np.arange(0, len(x)/fs, 1.0/fs)

# C Grafica de la señal en funcion del tiempo.
plt.plot(t,x)
plt.ylabel("Amplitud", fontsize = 20)
plt.xlabel("Tiempo (s)", fontsize = 20)
plt.title("Señal de audio", fontsize = 20)

# 2. almacene en una variable un segmento de la señal de audio donde haya registro de voz.

# rango de observación en segundos
inicia = 3.0
termina =3.2
# observación en número de muestra
a = int(inicia*fs)
b = int(termina*fs)

segmento = x[a:b]
s=segmento

# Gráfica
plt.figure()
t1=np.arange(0, len(segmento)/fs, 1.0/fs)

# Parametros de la grafica de la señal original
plt.subplot(211)
plt.ylabel("Amplitud", fontsize = 20)
plt.xlabel("Tiempo (s)", fontsize = 20)
plt.plot(t, x,label='Señal original')
plt.legend()

# Parametros de la grafica de el segmento de la señal
plt.subplot(212)
plt.plot (t1, segmento, color='r',label='Segmento de audio')
plt.legend()
plt.ylabel("Amplitud", fontsize = 20)
plt.xlabel("Tiempo (s)", fontsize = 20)
plt.show()

# 3  autocorrelacion

# Parametros de la grafica de la señal original
plt.figure()
plt.subplot(311)
plt.xlabel("Tiempo (s)", fontsize = 20)
plt.plot(t, x,label='Señal original')
plt.legend()

# Parametros de la grafica de el segmento de la señal
plt.subplot(312)
plt.plot (t1, segmento, color='r',label='Segmento de audio')
plt.legend()
plt.ylabel("Amplitud", fontsize = 20)
plt.xlabel("Tiempo (s)", fontsize = 20)

# Normalizamos el vector.
amplitud=(np.max(segmento))
s=s/amplitud

acor=np.correlate(s,s, mode='same')

t2=np.arange(0, (len(acor)/fs), 1.0/fs)

# Parametros para la grafica de autocorrelacion del segmento
plt.subplot(313)
plt.plot (t2, acor, color='g', label=' Correlacion Segmento de audio')
plt.legend()
plt.show()

# 4. Realizamos el proceso anterior para un segmento sordo

# rango de observación en segundos
inicias = 4.1
terminas =4.3
# observación en número de muestra
w = int(inicias*fs)
z = int(terminas*fs)

segmentos = x[w:z]
s1=segmentos

# Para hacer la autocorrelacion
amplitud=(np.max(segmentos))
s1=s1/amplitud

acors=np.correlate(s1,s1, mode='same')

t4=np.arange(0, (len(acors)/fs), 1.0/fs)

# Gráfica del segmento sordo
plt.figure()
plt.subplot(311)
t3=np.arange(0, len(segmentos)/fs, 1.0/fs)
plt.plot (t3, segmentos, color='r', label='Segmento de audio sordo')
plt.ylabel("Amplitud", fontsize = 20)
plt.legend()

# Grafica de su autocorrelacion
plt.figure()
plt.subplot(312)
plt.xlabel("Tiempo (s)", fontsize = 20)
plt.plot (t4, acors, color='g', label=' Autocorrelacion segmento sordo')
plt.ylabel("Amplitud", fontsize = 20)
plt.legend()
plt.show()

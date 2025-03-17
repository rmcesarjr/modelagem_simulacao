import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Parâmetros do sistema
fs = 44100  # Taxa de amostragem (Hz)
duration = 5.0  # Duração em segundos
frequency = 100  # Frequência do tom (Hz) - Nota Lá (A4)
A = 3.0  # Fator de amplificação
tau = 0.0001  # Tempo característico do megafone
dt = 1 / fs  # Passo de tempo

# Gera o sinal de entrada
T = np.arange(0, duration, dt)
x = 0.5 * np.sin(2 * np.pi * frequency * T)  # Sinal senoidal normalizado

# Solução Analítica (Estacionária)
phi = np.arctan(frequency * tau)
y_analitico = (A / np.sqrt(1 + (frequency * tau) ** 2)) * np.sin(2 * np.pi * frequency * T - phi)

# Solução Numérica via Método de Euler
y_euler = np.zeros_like(x)
for i in range(1, len(T)):
    dy_dt = (A * x[i - 1] - y_euler[i - 1]) / tau
    y_euler[i] = y_euler[i - 1] + dt * dy_dt

# Reproduz os sinais
print("Tocando som original...")
sd.play(x, samplerate=fs)
sd.wait()

print("Tocando som simulado (Euler)...")
sd.play(y_euler, samplerate=fs)
sd.wait()

print("Tocando som simulado (Analítico)...")
sd.play(y_analitico, samplerate=fs)
sd.wait()

# Plotando os resultados
plt.figure(figsize=(10, 5))
plt.plot(T[:1000], x[:1000], label="Entrada x(t)", linestyle="dotted")
plt.plot(T[:1000], y_euler[:1000], label="Saída Euler y(t)", linestyle="dashed")
plt.plot(T[:1000], y_analitico[:1000], label="Saída Analítica y(t)")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.title("Comparação entre entrada, saída Euler e saída Analítica")
plt.grid(True)
plt.show()

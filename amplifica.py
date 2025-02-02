import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Parâmetros do som
fs = 44100  # Taxa de amostragem (Hz)
duration = 5.0  # Duração em segundos
frequency = 440  # Frequência do tom (Hz) - Nota Lá (A4)

# Gera um som senoidal puro
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Amplitude normalizada

# Reproduz o som original
print("Tocando som original...")
sd.play(sine_wave, samplerate=fs)
sd.wait()

# Aplica o efeito de amplificação (megafone)
gain = 3.0  # Fator de amplificação (A > 1)
amplified_wave = np.clip(gain * sine_wave, -1.5, 1.5)  # Evita distorção

# Reproduz o som amplificado
print("Tocando som amplificado (megafone)...")
sd.play(amplified_wave, samplerate=fs)
sd.wait()

# Plota os sinais
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], sine_wave[:1000], label="Original")
plt.plot(t[:1000], amplified_wave[:1000], label="Amplificado (Megafone)", linestyle="dashed")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.title("Comparação entre o som original e amplificado")
plt.show()

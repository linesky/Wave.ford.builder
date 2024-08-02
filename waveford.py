
import numpy as np
import wave

def generate_tone(f_start, f_end, duration, sample_rate=44100):
    """Gera uma onda senoidal que varia de f_start para f_end ao longo de duration segundos."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    freqs = np.linspace(f_start, f_end, int(sample_rate * duration))
    audio_data = np.sin(2 * np.pi * freqs * t)
    return audio_data

def save_wave_file(filename, audio_data, sample_rate):
    """Salva os dados de áudio em um arquivo WAV."""
    audio_data = (audio_data * 32767).astype(np.int16)
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

def main():
    # Solicita os dados ao usuário
    f_start = float(input("Digite a frequência inicial (Hz): "))
    f_end = float(input("Digite a frequência final (Hz): "))
    duration = float(input("Digite a duração em segundos: "))
    
    # Gera o áudio
    audio_data = generate_tone(f_start, f_end, duration)
    
    # Salva o áudio em um arquivo WAV
    output_filename = "output.wav"
    save_wave_file(output_filename, audio_data, sample_rate=44100)
    
    print(f"Áudio salvo em {output_filename}")
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()

"""
Ajustar velocidade das narrações que excedem o tempo disponível na cena.
Usa ffmpeg atempo filter para acelerar levemente (max 1.15x).
"""
import subprocess
import os
from pydub import AudioSegment

# Tempo disponível para narração em cada cena (ms)
SCENE_AVAILABLE = {
    1: 19500,   # 20.5s - 1.0s offset
    2: 17300,   # 38.8s - 21.5s
    3: 11500,   # 51.3s - 39.8s
    4: 15600,   # 67.9s - 52.3s
    5: 13700,   # 82.6s - 68.9s
    6: 14200,   # 97.8s - 83.6s
    7: 18200,   # 117.0s - 98.8s
}

for lang in ["pt", "en", "es"]:
    narr_dir = f"/home/ubuntu/narration_{lang}_v7"
    print(f"\n=== {lang.upper()} ===")
    
    for i in range(1, 8):
        src = f"{narr_dir}/cena{i}.mp3"
        audio = AudioSegment.from_mp3(src)
        dur = len(audio)
        available = SCENE_AVAILABLE[i]
        
        if dur > available:
            # Calcular fator de aceleração
            speed = dur / available
            if speed > 1.25:
                print(f"  cena{i}: {dur/1000:.1f}s -> {available/1000:.1f}s (speed {speed:.2f}x - MUITO RÁPIDO, limitando a 1.25x)")
                speed = 1.25
            else:
                print(f"  cena{i}: {dur/1000:.1f}s -> {available/1000:.1f}s (speed {speed:.2f}x)")
            
            # Usar ffmpeg atempo para ajustar velocidade
            temp = f"{narr_dir}/cena{i}_temp.mp3"
            subprocess.run([
                "ffmpeg", "-y", "-i", src,
                "-filter:a", f"atempo={speed}",
                "-vn", temp
            ], check=True, capture_output=True)
            
            os.replace(temp, src)
            
            # Verificar resultado
            new_audio = AudioSegment.from_mp3(src)
            print(f"         Nova duração: {len(new_audio)/1000:.1f}s")
        else:
            print(f"  cena{i}: {dur/1000:.1f}s <= {available/1000:.1f}s [OK]")

print("\nTodas as narrações ajustadas!")

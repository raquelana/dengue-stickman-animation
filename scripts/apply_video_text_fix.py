"""
Editar o vídeo base substituindo textos visuais na Cena 6 (84s-97s):
1. "Accumulated trash" → "Accumulated rubbish" 
2. "Cleanup effort" → "Clean-up effort"

Abordagem: Usar ffmpeg drawtext com enable entre timestamps da cena 6,
cobrindo o texto antigo com retângulo branco e desenhando o novo texto.
"""
import subprocess
import os

VIDEO_IN = "/home/ubuntu/upload/video_only_EN.mp4"
VIDEO_OUT = "/home/ubuntu/video_only_EN_fixed.mp4"

# Cena 6: 84s a 98s (frames com quadrantes)
# Texto "Accumulated trash": y:65-90, x:655-790, cor marrom #855931
# Texto "Cleanup effort": y:400-430, x:10-200, cor verde #339542

# Fonte: LiberationSans
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

# "Accumulated trash" → "Accumulated rubbish"
# Original: size ~15 (124x11px matches 123px width), cor #855931
# Posição do texto original: x:661, y:72

# "Cleanup effort" → "Clean-up effort" 
# Original: Bold, cor verde #339542
# Preciso verificar o tamanho exato

# Estratégia com ffmpeg:
# 1. Desenhar retângulo branco sobre o texto antigo
# 2. Desenhar o texto novo na mesma posição

# Para "Accumulated trash": cobrir x:655-790, y:65-90 com branco, depois escrever "Accumulated rubbish"
# Para "Cleanup effort": cobrir x:5-200, y:398-430 com branco, depois escrever "Clean-up effort"

# Usar drawbox + drawtext com enable='between(t,84,98)'
filter_complex = (
    # Cobrir "Accumulated trash" com retângulo branco
    "drawbox=x=655:y=65:w=145:h=25:color=white:t=fill:enable='between(t,83.5,98.5)',"
    # Escrever "Accumulated rubbish" no mesmo lugar
    f"drawtext=fontfile={FONT}:text='Accumulated rubbish':fontcolor=#855931:fontsize=15:x=661:y=72:enable='between(t,83.5,98.5)',"
    # Cobrir "Cleanup effort" com retângulo branco
    "drawbox=x=5:y=398:w=200:h=35:color=white:t=fill:enable='between(t,83.5,98.5)',"
    # Escrever "Clean-up effort" no mesmo lugar
    f"drawtext=fontfile={FONT_BOLD}:text='Clean-up effort':fontcolor=#339542:fontsize=15:x=20:y=405:enable='between(t,83.5,98.5)'"
)

print("=== Aplicando correções de texto no vídeo base ===")
print(f"Input:  {VIDEO_IN}")
print(f"Output: {VIDEO_OUT}")
print(f"Filtro: {filter_complex}")
print()

cmd = [
    "ffmpeg", "-y",
    "-i", VIDEO_IN,
    "-vf", filter_complex,
    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
    "-c:a", "copy",
    VIDEO_OUT
]

result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    print("ERRO:")
    print(result.stderr[-2000:])
else:
    # Verificar resultado
    size = os.path.getsize(VIDEO_OUT) / (1024*1024)
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", VIDEO_OUT],
        capture_output=True, text=True
    )
    dur = float(probe.stdout.strip())
    print(f"SUCESSO! Duração: {dur:.1f}s, Tamanho: {size:.1f}MB")
    
    # Extrair frame de verificação
    subprocess.run([
        "ffmpeg", "-y", "-ss", "85", "-i", VIDEO_OUT,
        "-frames:v", "1", "/home/ubuntu/frame_cena6_fixed.png"
    ], capture_output=True)
    print("Frame de verificação salvo: /home/ubuntu/frame_cena6_fixed.png")

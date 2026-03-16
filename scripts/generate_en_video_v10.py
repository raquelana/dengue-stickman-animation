"""
Gerar vídeo EN v10 usando:
- Narrações v9 para cenas 1,2,3,5,7 (inalteradas)
- Narrações v10 para cenas 4 e 6 (corrigidas conforme roteiro fornecido)
Legendas atualizadas para cenas 4 e 6.
"""
import subprocess
import os
from pydub import AudioSegment

VIDEO_BASE = "/home/ubuntu/upload/video_only_EN.mp4"
VIDEO_DURATION_MS = 127000
BG_MUSIC = "/home/ubuntu/bg_music.wav"

SCENE_STARTS = {1: 1000, 2: 21500, 3: 39800, 4: 52300, 5: 68900, 6: 83600, 7: 98800}
SCENE_ENDS = {1: 20500, 2: 38800, 3: 51300, 4: 67900, 5: 82600, 6: 97800, 7: 117000}

# Narrações: usar v9 para cenas inalteradas, v10 para cenas 4 e 6
NARR_SOURCES = {}
for i in range(1, 8):
    if i in [4, 6]:
        NARR_SOURCES[i] = f"/home/ubuntu/narration_en_v10/cena{i}.mp3"
    else:
        NARR_SOURCES[i] = f"/home/ubuntu/narration_en_v9/cena{i}.mp3"

# Legendas EN com cenas 4 e 6 atualizadas
SUBTITLE_TEXTS = {
    1: [
        "This is the Aedes aegypti,",
        "it transmits the dengue virus.",
        "The Aedes albopictus,",
        "better known as the tiger mosquito,",
        "can also transmit dengue.",
        "Female Aedes lay their eggs",
        "in standing water.",
        "An egg takes between 7 and 10 days",
        "to become an adult mosquito."
    ],
    2: [
        "Without any control measures,",
        "dengue is passed to humans",
        "through mosquito bites.",
        "Only females bite humans,",
        "as they need blood",
        "for their eggs to develop.",
        "Dengue symptoms include high fever,",
        "intense headache, body aches,",
        "and red spots on the skin."
    ],
    3: [
        "With individual measures,",
        "such as repellent, long clothing,",
        "and mosquito nets,",
        "some people can protect themselves.",
        "But other measures can help too."
    ],
    4: [
        "Collective measures make",
        "a big difference!",
        "Vaccines, when available,",
        "protect people even when bitten.",
        "Chemical interventions",
        "that are safe for the environment,",
        "can reduce the mosquito population.",
        "The combination of different measures",
        "strengthens the fight",
        "against the disease."
    ],
    5: [
        "When we take care of the environment,",
        "removing rubbish,",
        "covering water containers,",
        "and eliminating breeding sites,",
        "mosquitoes lose them",
        "and have no place to lay their eggs",
        "and develop into adults!"
    ],
    6: [
        "The environment makes",
        "all the difference.",
        "Rain and discarded waste together",
        "produce more breeding sites.",
        "Cleaning and care eliminates them.",
        "In dense urban areas,",
        "the risk is even greater."
    ],
    7: [
        "The same mosquitoes that transmit",
        "dengue also transmit",
        "Zika and chikungunya.",
        "But with knowledge",
        "and collective action,",
        "we can win this battle.",
        "Protect yourself.",
        "Protect your community.",
        "Take care of the environment."
    ]
}

def ms_to_srt_time(ms):
    h = ms // 3600000
    m = (ms % 3600000) // 60000
    s = (ms % 60000) // 1000
    ms_rem = ms % 1000
    return f"{h:02d}:{m:02d}:{s:02d},{ms_rem:03d}"

print("=" * 50)
print("  Gerando vídeo EN (v10)")
print("=" * 50)

srt_file = "/home/ubuntu/legendas_EN_final_v10.srt"
output = "/home/ubuntu/dengue_final_EN.mp4"
temp_audio = "/home/ubuntu/temp_audio_en_v10.wav"
temp_video = "/home/ubuntu/temp_video_en_v10.mp4"

print("1. Carregando narrações...")
narrations = {}
for i in range(1, 8):
    audio = AudioSegment.from_mp3(NARR_SOURCES[i])
    narrations[i] = audio
    dur = len(audio) / 1000
    scene_available = (SCENE_ENDS[i] - SCENE_STARTS[i]) / 1000
    source = "v10" if i in [4, 6] else "v9"
    status = "OK" if dur <= scene_available else "LONGA"
    print(f"   cena{i} ({source}): {dur:.1f}s (disponível: {scene_available:.1f}s) [{status}]")

print("2. Combinando áudio...")
combined = AudioSegment.silent(duration=VIDEO_DURATION_MS)
for i in range(1, 8):
    start = SCENE_STARTS[i]
    narr = narrations[i]
    available = SCENE_ENDS[i] - start
    if len(narr) > available:
        narr = narr[:available]
        print(f"   AVISO: cena{i} cortada para {available/1000:.1f}s")
    combined = combined.overlay(narr, position=start)

if os.path.exists(BG_MUSIC):
    bg = AudioSegment.from_wav(BG_MUSIC)
    while len(bg) < VIDEO_DURATION_MS:
        bg = bg + bg
    bg = bg[:VIDEO_DURATION_MS]
    bg = bg - 18
    combined = combined.overlay(bg)

combined.export(temp_audio, format="wav")
print(f"   Áudio: {len(combined)/1000:.1f}s")

print("3. Gerando legendas SRT...")
srt_index = 1
srt_content = ""
for scene_num in range(1, 8):
    scene_start = SCENE_STARTS[scene_num]
    narr_duration = len(narrations[scene_num])
    available = SCENE_ENDS[scene_num] - scene_start
    effective_duration = min(narr_duration, available)
    lines = SUBTITLE_TEXTS[scene_num]
    line_duration = effective_duration / len(lines)
    for j, line in enumerate(lines):
        line_start = scene_start + int(j * line_duration)
        line_end = scene_start + int((j + 1) * line_duration)
        srt_content += f"{srt_index}\n"
        srt_content += f"{ms_to_srt_time(line_start)} --> {ms_to_srt_time(line_end)}\n"
        srt_content += f"{line}\n\n"
        srt_index += 1
with open(srt_file, "w", encoding="utf-8") as f:
    f.write(srt_content)
print(f"   SRT: {srt_index - 1} legendas")

print("4. Combinando vídeo + áudio...")
subprocess.run([
    "ffmpeg", "-y", "-i", VIDEO_BASE, "-i", temp_audio,
    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", temp_video
], check=True, capture_output=True)

print("5. Adicionando legendas burn-in...")
subprocess.run([
    "ffmpeg", "-y", "-i", temp_video,
    "-vf", f"subtitles={srt_file}:force_style='FontName=Liberation Sans,FontSize=22,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,BorderStyle=3,Outline=2,Shadow=1,BackColour=&H80000000,Alignment=2,MarginV=30'",
    "-c:v", "libx264", "-preset", "medium", "-crf", "23",
    "-c:a", "copy", output
], check=True, capture_output=True)

for f in [temp_audio, temp_video]:
    if os.path.exists(f):
        os.remove(f)

result = subprocess.run([
    "ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "csv=p=0", output
], capture_output=True, text=True)
final_dur = float(result.stdout.strip())
file_size = os.path.getsize(output) / (1024 * 1024)
print(f"\n   RESULTADO: {output}")
print(f"   Duração: {final_dur:.1f}s | Tamanho: {file_size:.1f} MB")
print("=" * 50)
print("  VÍDEO EN v10 GERADO COM SUCESSO!")
print("=" * 50)

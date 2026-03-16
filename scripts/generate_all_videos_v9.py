"""
Gerar 3 vídeos (PT, EN, ES) usando video_only_EN.mp4 como base visual.
v9: Correções de consistência entre idiomas:
  - PT Cena 4: "quando disponíveis"
  - ES Cena 4: "cuando estén disponibles" + "!"
  - EN Cena 6: "eliminate" (corrigido gramática)
  - EN Cena 5: "lose them" (mantido)
"""
import subprocess
import os
from pydub import AudioSegment

VIDEO_BASE = "/home/ubuntu/upload/video_only_EN.mp4"
VIDEO_DURATION_MS = 127000
BG_MUSIC = "/home/ubuntu/bg_music.wav"

SCENE_STARTS = {1: 1000, 2: 21500, 3: 39800, 4: 52300, 5: 68900, 6: 83600, 7: 98800}
SCENE_ENDS = {1: 20500, 2: 38800, 3: 51300, 4: 67900, 5: 82600, 6: 97800, 7: 117000}

NARR_DIRS = {
    "pt": "/home/ubuntu/narration_pt_v9",
    "en": "/home/ubuntu/narration_en_v9",
    "es": "/home/ubuntu/narration_es_v9",
}

SUBTITLE_TEXTS = {
    "pt": {
        1: [
            "Este é o Aedes aegypti,",
            "ele transmite o vírus Dengue.",
            "O Aedes albopictus, mais conhecido",
            "como mosquito tigre,",
            "também pode transmitir esse vírus.",
            "As fêmeas de Aedes colocam",
            "os ovos em água parada.",
            "Um ovo demora entre 7 e 10 dias",
            "para se tornar um mosquito adulto."
        ],
        2: [
            "Sem nenhuma medida de controle,",
            "a dengue se espalha por meio",
            "das picadas de mosquitos.",
            "Somente as fêmeas picam os humanos,",
            "pois precisam do sangue",
            "para os ovos se desenvolverem.",
            "Os sintomas da dengue incluem febre alta,",
            "dor de cabeça intensa, dores no corpo",
            "e manchas vermelhas na pele."
        ],
        3: [
            "Com medidas individuais —",
            "como repelente, roupas compridas",
            "e mosquiteiros —",
            "algumas pessoas conseguem se proteger.",
            "Mas outras medidas podem ajudar também."
        ],
        4: [
            "Medidas coletivas fazem",
            "uma grande diferença!",
            "Vacinas, quando disponíveis,",
            "protegem as pessoas",
            "mesmo quando picadas.",
            "Inseticidas reduzem",
            "a população de mosquitos.",
            "A combinação de diferentes medidas",
            "fortalece o combate à doença."
        ],
        5: [
            "Quando cuidamos do ambiente —",
            "removendo lixo,",
            "tampando recipientes com água",
            "e eliminando criadouros —",
            "os mosquitos perdem seus criadouros,",
            "e ficam sem lugares para depositar",
            "os seus ovos e desenvolverem",
            "até a fase adulta!"
        ],
        6: [
            "O ambiente faz toda a diferença.",
            "Chuva e lixo juntos",
            "produzem mais criadouros.",
            "Limpeza e cuidado os eliminam.",
            "Em áreas urbanas densas,",
            "o risco é ainda maior."
        ],
        7: [
            "A dengue possui 4 sorotipos diferentes",
            "e os mesmos mosquitos que transmitem",
            "a Zika e a chikungunya.",
            "Mas com conhecimento",
            "e ação coletiva,",
            "podemos vencer essa batalha.",
            "Proteja-se.",
            "Proteja sua comunidade.",
            "Cuide do ambiente."
        ]
    },
    "en": {
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
            "Insecticides reduce",
            "the mosquito population.",
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
            "Cleaning and care eliminate them.",
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
    },
    "es": {
        1: [
            "Este es el Aedes aegypti,",
            "transmite el virus del Dengue.",
            "El Aedes albopictus,",
            "más conocido como mosquito tigre,",
            "también puede transmitir este virus.",
            "Las hembras de Aedes depositan",
            "sus huevos en agua estancada.",
            "Un huevo tarda entre 7 y 10 días",
            "en convertirse en un mosquito adulto."
        ],
        2: [
            "Sin ninguna medida de control,",
            "el dengue se propaga a través",
            "de las picaduras de mosquitos.",
            "Solo las hembras pican a los humanos,",
            "ya que necesitan la sangre",
            "para que sus huevos se desarrollen.",
            "Los síntomas del dengue incluyen",
            "fiebre alta, dolor de cabeza intenso,",
            "dolores corporales y manchas rojas",
            "en la piel."
        ],
        3: [
            "Con medidas individuales,",
            "como repelente, ropa larga",
            "y mosquiteros,",
            "algunas personas logran protegerse.",
            "Pero otras medidas también",
            "pueden ayudar."
        ],
        4: [
            "Las medidas colectivas marcan",
            "una gran diferencia!",
            "Las vacunas, cuando estén disponibles,",
            "protegen a las personas",
            "incluso cuando son picadas.",
            "Los insecticidas reducen",
            "la población de mosquitos.",
            "La combinación de diferentes medidas",
            "fortalece la lucha",
            "contra la enfermedad."
        ],
        5: [
            "Cuando cuidamos el medio ambiente,",
            "retirando basura,",
            "tapando recipientes con agua",
            "y eliminando criaderos,",
            "los mosquitos pierden sus criaderos",
            "y no tienen dónde depositar sus huevos",
            "ni desarrollarse hasta la fase adulta!"
        ],
        6: [
            "El ambiente marca toda la diferencia.",
            "La lluvia y la basura juntos",
            "producen más criaderos.",
            "La limpieza y el cuidado los eliminan.",
            "En áreas urbanas densas,",
            "el riesgo es aún mayor."
        ],
        7: [
            "El dengue tiene 4 serotipos diferentes",
            "y los mismos mosquitos que transmiten",
            "el Zika y el chikunguña.",
            "Pero con conocimiento",
            "y acción colectiva,",
            "podemos ganar esta batalla.",
            "Protégete.",
            "Protege a tu comunidad.",
            "Cuida el medio ambiente."
        ]
    }
}

def ms_to_srt_time(ms):
    h = ms // 3600000
    m = (ms % 3600000) // 60000
    s = (ms % 60000) // 1000
    ms_rem = ms % 1000
    return f"{h:02d}:{m:02d}:{s:02d},{ms_rem:03d}"

def generate_video(lang):
    print(f"\n{'='*50}")
    print(f"  Gerando vídeo {lang.upper()} (v9)")
    print(f"{'='*50}")
    
    narr_dir = NARR_DIRS[lang]
    srt_file = f"/home/ubuntu/legendas_{lang.upper()}_final_v9.srt"
    output = f"/home/ubuntu/dengue_final_{lang.upper()}.mp4"
    temp_audio = f"/home/ubuntu/temp_audio_{lang}.wav"
    temp_video = f"/home/ubuntu/temp_video_{lang}.mp4"
    
    print("1. Carregando narrações...")
    narrations = {}
    for i in range(1, 8):
        audio = AudioSegment.from_mp3(f"{narr_dir}/cena{i}.mp3")
        narrations[i] = audio
        dur = len(audio) / 1000
        scene_available = (SCENE_ENDS[i] - SCENE_STARTS[i]) / 1000
        status = "OK" if dur <= scene_available else "LONGA"
        print(f"   cena{i}: {dur:.1f}s (disponível: {scene_available:.1f}s) [{status}]")
    
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
    texts = SUBTITLE_TEXTS[lang]
    for scene_num in range(1, 8):
        scene_start = SCENE_STARTS[scene_num]
        narr_duration = len(narrations[scene_num])
        available = SCENE_ENDS[scene_num] - scene_start
        effective_duration = min(narr_duration, available)
        lines = texts[scene_num]
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
    return output

for lang in ["pt", "en", "es"]:
    generate_video(lang)

print(f"\n{'='*50}")
print("  TODOS OS 3 VÍDEOS v9 GERADOS COM SUCESSO!")
print(f"{'='*50}")

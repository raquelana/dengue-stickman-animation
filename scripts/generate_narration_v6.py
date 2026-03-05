import asyncio
import edge_tts
import os

PT_DIR = "/home/ubuntu/narration_v6_pt"
EN_DIR = "/home/ubuntu/narration_v6_en"
ES_DIR = "/home/ubuntu/narration_v6_es"
for d in [PT_DIR, EN_DIR, ES_DIR]:
    os.makedirs(d, exist_ok=True)

PT_VOICE = "pt-BR-FranciscaNeural"
EN_VOICE = "en-US-JennyNeural"
ES_VOICE = "es-ES-ElviraNeural"

PT_RATE, PT_PITCH = "-5%", "+5Hz"
EN_RATE, EN_PITCH = "-3%", "+0Hz"
ES_RATE, ES_PITCH = "-3%", "+3Hz"

# Textos EXATOS do roteiro Roteiro_video_SiW.docx.pdf
narrations_pt = [
    {"id": "cena1", "text": "Este é o Aedes aegypti, ele transmite o vírus Dengue. O Aedes albopictus, mais conhecido como mosquito tigre, também pode transmitir esse vírus. As fêmeas de Aedes colocam os ovos em água parada. Um ovo demora entre 7 e 10 dias para se tornar um mosquito adulto."},
    {"id": "cena2", "text": "Sem nenhuma medida de controle, a dengue se espalha por meio das picadas de mosquitos. Somente as fêmeas picam os humanos, pois precisam do sangue para os ovos se desenvolverem. Os sintomas da dengue incluem febre alta, dor de cabeça intensa, dores no corpo e manchas vermelhas na pele."},
    {"id": "cena3", "text": "Com medidas individuais, como repelente, roupas compridas e mosquiteiros, algumas pessoas conseguem se proteger. Mas outras medidas podem ajudar também."},
    {"id": "cena4", "text": "Medidas coletivas fazem uma grande diferença! Vacinas protegem as pessoas mesmo quando picadas. Inseticidas reduzem a população de mosquitos. A combinação de diferentes medidas, fortalece o combate à doença."},
    {"id": "cena5", "text": "Quando cuidamos do ambiente, removendo lixo, tampando recipientes com água e eliminando criadouros, os mosquitos perdem seus criadouros, e ficam sem lugares para depositar os seus ovos e desenvolverem até a fase adulta!"},
    {"id": "cena6", "text": "O ambiente faz toda a diferença. Chuva e lixo juntos produzem mais criadouros. Limpeza e cuidado os eliminam. Em áreas urbanas densas, o risco é ainda maior."},
    {"id": "cena7", "text": "A dengue possui 4 sorotipos diferentes e os mesmos mosquitos que transmitem a Zika e a chikungunya. Mas com conhecimento e ação coletiva, podemos vencer essa batalha. Proteja-se. Proteja sua comunidade. Cuide do ambiente."},
]

narrations_en = [
    {"id": "cena1", "text": "This is the Aedes aegypti, it transmits the Dengue virus. The Aedes albopictus, better known as the tiger mosquito, can also transmit this virus. Female Aedes lay their eggs in standing water. An egg takes between 7 and 10 days to become an adult mosquito."},
    {"id": "cena2", "text": "Without any control measures, dengue spreads through mosquito bites. Only females bite humans, as they need blood for their eggs to develop. Dengue symptoms include high fever, intense headache, body aches, and red spots on the skin."},
    {"id": "cena3", "text": "With individual measures, such as repellent, long clothing, and mosquito nets, some people can protect themselves. But other measures can help too."},
    {"id": "cena4", "text": "Collective measures make a big difference! Vaccines protect people even when bitten. Insecticides reduce the mosquito population. The combination of different measures strengthens the fight against the disease."},
    {"id": "cena5", "text": "When we take care of the environment, removing trash, covering water containers, and eliminating breeding sites, mosquitoes lose their breeding grounds and have no place to lay their eggs and develop into adults!"},
    {"id": "cena6", "text": "The environment makes all the difference. Rain and trash together produce more breeding sites. Cleaning and care eliminate them. In dense urban areas, the risk is even greater."},
    {"id": "cena7", "text": "Dengue has 4 different serotypes and the same mosquitoes that transmit Zika and chikungunya. But with knowledge and collective action, we can win this battle. Protect yourself. Protect your community. Take care of the environment."},
]

narrations_es = [
    {"id": "cena1", "text": "Este es el Aedes aegypti, transmite el virus del Dengue. El Aedes albopictus, más conocido como mosquito tigre, también puede transmitir este virus. Las hembras de Aedes depositan sus huevos en agua estancada. Un huevo tarda entre 7 y 10 días en convertirse en un mosquito adulto."},
    {"id": "cena2", "text": "Sin ninguna medida de control, el dengue se propaga a través de las picaduras de mosquitos. Solo las hembras pican a los humanos, ya que necesitan la sangre para que sus huevos se desarrollen. Los síntomas del dengue incluyen fiebre alta, dolor de cabeza intenso, dolores corporales y manchas rojas en la piel."},
    {"id": "cena3", "text": "Con medidas individuales, como repelente, ropa larga y mosquiteros, algunas personas logran protegerse. Pero otras medidas también pueden ayudar."},
    {"id": "cena4", "text": "Las medidas colectivas marcan una gran diferencia. Las vacunas protegen a las personas incluso cuando son picadas. Los insecticidas reducen la población de mosquitos. La combinación de diferentes medidas fortalece la lucha contra la enfermedad."},
    {"id": "cena5", "text": "Cuando cuidamos el medio ambiente, retirando basura, tapando recipientes con agua y eliminando criaderos, los mosquitos pierden sus criaderos y no tienen dónde depositar sus huevos ni desarrollarse hasta la fase adulta!"},
    {"id": "cena6", "text": "El ambiente marca toda la diferencia. La lluvia y la basura juntos producen más criaderos. La limpieza y el cuidado los eliminan. En áreas urbanas densas, el riesgo es aún mayor."},
    {"id": "cena7", "text": "El dengue tiene 4 serotipos diferentes y los mismos mosquitos que transmiten el Zika y el chikunguña. Pero con conocimiento y acción colectiva, podemos ganar esta batalla. Protégete. Protege a tu comunidad. Cuida el medio ambiente."},
]

async def generate_audio(narration, voice, rate, pitch, output_dir):
    output_path = os.path.join(output_dir, f"{narration['id']}.mp3")
    communicate = edge_tts.Communicate(narration["text"], voice, rate=rate, pitch=pitch)
    await communicate.save(output_path)
    print(f"  Generated: {output_path}")

async def main():
    print("=== Generating PT narrations (Francisca) ===")
    tasks_pt = [generate_audio(n, PT_VOICE, PT_RATE, PT_PITCH, PT_DIR) for n in narrations_pt]
    await asyncio.gather(*tasks_pt)
    
    print("\n=== Generating EN narrations (Jenny) ===")
    tasks_en = [generate_audio(n, EN_VOICE, EN_RATE, EN_PITCH, EN_DIR) for n in narrations_en]
    await asyncio.gather(*tasks_en)
    
    print("\n=== Generating ES narrations (Elvira) ===")
    tasks_es = [generate_audio(n, ES_VOICE, ES_RATE, ES_PITCH, ES_DIR) for n in narrations_es]
    await asyncio.gather(*tasks_es)
    
    print("\nAll narrations generated!")

asyncio.run(main())

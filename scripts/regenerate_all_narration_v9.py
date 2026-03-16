"""
Regenerar narrações v9 para os 3 idiomas com correções de consistência:
- PT Cena 4: adicionado "quando disponíveis"
- ES Cena 4: adicionado "cuando estén disponibles" + "!" 
- EN Cena 6: "eliminates" → "eliminate"
- EN Cena 5: mantém "lose them" (já estava correto)
"""
import asyncio
import edge_tts
import os

# === PORTUGUÊS v9 ===
PT_DIR = "/home/ubuntu/narration_pt_v9"
os.makedirs(PT_DIR, exist_ok=True)
VOICE_PT = "pt-BR-FranciscaNeural"

SCENES_PT = {
    1: "Este é o Aedes aegypti, ele transmite o vírus Dengue. O Aedes albopictus, mais conhecido como mosquito tigre, também pode transmitir esse vírus. As fêmeas de Aedes colocam os ovos em água parada. Um ovo demora entre 7 e 10 dias para se tornar um mosquito adulto.",
    2: "Sem nenhuma medida de controle, a dengue se espalha por meio das picadas de mosquitos. Somente as fêmeas picam os humanos, pois precisam do sangue para os ovos se desenvolverem. Os sintomas da dengue incluem febre alta, dor de cabeça intensa, dores no corpo e manchas vermelhas na pele.",
    3: "Com medidas individuais — como repelente, roupas compridas e mosquiteiros — algumas pessoas conseguem se proteger. Mas outras medidas podem ajudar também.",
    4: "Medidas coletivas fazem uma grande diferença! Vacinas, quando disponíveis, protegem as pessoas mesmo quando picadas. Inseticidas reduzem a população de mosquitos. A combinação de diferentes medidas fortalece o combate à doença.",
    5: "Quando cuidamos do ambiente — removendo lixo, tampando recipientes com água e eliminando criadouros — os mosquitos perdem seus criadouros, e ficam sem lugares para depositar os seus ovos e desenvolverem até a fase adulta!",
    6: "O ambiente faz toda a diferença. Chuva e lixo juntos produzem mais criadouros. Limpeza e cuidado os eliminam. Em áreas urbanas densas, o risco é ainda maior.",
    7: "A dengue possui 4 sorotipos diferentes e os mesmos mosquitos que transmitem a Zika e a chikungunya. Mas com conhecimento e ação coletiva, podemos vencer essa batalha. Proteja-se. Proteja sua comunidade. Cuide do ambiente.",
}

# === INGLÊS v9 ===
EN_DIR = "/home/ubuntu/narration_en_v9"
os.makedirs(EN_DIR, exist_ok=True)
VOICE_EN = "en-US-JennyNeural"

SCENES_EN = {
    1: "This is the Aedes aegypti, it transmits the dengue virus. The Aedes albopictus, better known as the tiger mosquito, can also transmit dengue. Female Aedes lay their eggs in standing water. An egg takes between 7 and 10 days to become an adult mosquito.",
    2: "Without any control measures, dengue is passed to humans through mosquito bites. Only females bite humans, as they need blood for their eggs to develop. Dengue symptoms include high fever, intense headache, body aches, and red spots on the skin.",
    3: "With individual measures, such as repellent, long clothing, and mosquito nets, some people can protect themselves. But other measures can help too.",
    4: "Collective measures make a big difference! Vaccines, when available, protect people even when bitten. Insecticides reduce the mosquito population. The combination of different measures strengthens the fight against the disease.",
    5: "When we take care of the environment, removing rubbish, covering water containers, and eliminating breeding sites, mosquitoes lose them and have no place to lay their eggs and develop into adults!",
    6: "The environment makes all the difference. Rain and discarded waste together produce more breeding sites. Cleaning and care eliminate them. In dense urban areas, the risk is even greater.",
    7: "The same mosquitoes that transmit dengue also transmit Zika and chikungunya. But with knowledge and collective action, we can win this battle. Protect yourself. Protect your community. Take care of the environment.",
}

# === ESPANHOL v9 ===
ES_DIR = "/home/ubuntu/narration_es_v9"
os.makedirs(ES_DIR, exist_ok=True)
VOICE_ES = "es-ES-ElviraNeural"

SCENES_ES = {
    1: "Este es el Aedes aegypti, transmite el virus del Dengue. El Aedes albopictus, más conocido como mosquito tigre, también puede transmitir este virus. Las hembras de Aedes depositan sus huevos en agua estancada. Un huevo tarda entre 7 y 10 días en convertirse en un mosquito adulto.",
    2: "Sin ninguna medida de control, el dengue se propaga a través de las picaduras de mosquitos. Solo las hembras pican a los humanos, ya que necesitan la sangre para que sus huevos se desarrollen. Los síntomas del dengue incluyen fiebre alta, dolor de cabeza intenso, dolores corporales y manchas rojas en la piel.",
    3: "Con medidas individuales, como repelente, ropa larga y mosquiteros, algunas personas logran protegerse. Pero otras medidas también pueden ayudar.",
    4: "Las medidas colectivas marcan una gran diferencia! Las vacunas, cuando estén disponibles, protegen a las personas incluso cuando son picadas. Los insecticidas reducen la población de mosquitos. La combinación de diferentes medidas fortalece la lucha contra la enfermedad.",
    5: "Cuando cuidamos el medio ambiente, retirando basura, tapando recipientes con agua y eliminando criaderos, los mosquitos pierden sus criaderos y no tienen dónde depositar sus huevos ni desarrollarse hasta la fase adulta!",
    6: "El ambiente marca toda la diferencia. La lluvia y la basura juntos producen más criaderos. La limpieza y el cuidado los eliminan. En áreas urbanas densas, el riesgo es aún mayor.",
    7: "El dengue tiene 4 serotipos diferentes y los mismos mosquitos que transmiten el Zika y el chikunguña. Pero con conocimiento y acción colectiva, podemos ganar esta batalla. Protégete. Protege a tu comunidad. Cuida el medio ambiente.",
}

async def generate():
    for lang, scenes, voice, out_dir in [
        ("PT", SCENES_PT, VOICE_PT, PT_DIR),
        ("EN", SCENES_EN, VOICE_EN, EN_DIR),
        ("ES", SCENES_ES, VOICE_ES, ES_DIR),
    ]:
        print(f"\n=== Gerando narrações {lang} v9 ===")
        for scene_num, text in scenes.items():
            output_file = f"{out_dir}/cena{scene_num}.mp3"
            communicate = edge_tts.Communicate(text, voice, rate="-5%")
            await communicate.save(output_file)
            print(f"  cena{scene_num}: OK")

asyncio.run(generate())
print("\nSUCESSO! Todas as narrações v9 geradas.")

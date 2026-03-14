import asyncio
import edge_tts
import os

# PT - Francisca (suave, acolhedora)
# EN - Jenny (madura, amigável) - já gerado em narration_en_v7
# ES - Elvira (amigável, clara)

narrations_pt = {
    "cena1": "Este é o Aedes aegypti, ele transmite o vírus Dengue. O Aedes albopictus, mais conhecido como mosquito tigre, também pode transmitir esse vírus. As fêmeas de Aedes colocam os ovos em água parada. Um ovo demora entre 7 e 10 dias para se tornar um mosquito adulto.",
    "cena2": "Sem nenhuma medida de controle, a dengue se espalha por meio das picadas de mosquitos. Somente as fêmeas picam os humanos, pois precisam do sangue para os ovos se desenvolverem. Os sintomas da dengue incluem febre alta, dor de cabeça intensa, dores no corpo e manchas vermelhas na pele.",
    "cena3": "Com medidas individuais — como repelente, roupas compridas e mosquiteiros — algumas pessoas conseguem se proteger. Mas outras medidas podem ajudar também.",
    "cena4": "Medidas coletivas fazem uma grande diferença! Vacinas protegem as pessoas mesmo quando picadas. Inseticidas reduzem a população de mosquitos. A combinação de diferentes medidas fortalece o combate à doença.",
    "cena5": "Quando cuidamos do ambiente — removendo lixo, tampando recipientes com água e eliminando criadouros — os mosquitos perdem seus criadouros, e ficam sem lugares para depositar os seus ovos e desenvolverem até a fase adulta!",
    "cena6": "O ambiente faz toda a diferença. Chuva e lixo juntos produzem mais criadouros. Limpeza e cuidado os eliminam. Em áreas urbanas densas, o risco é ainda maior.",
    "cena7": "A dengue possui 4 sorotipos diferentes e os mesmos mosquitos que transmitem a Zika e a chikungunya. Mas com conhecimento e ação coletiva, podemos vencer essa batalha. Proteja-se. Proteja sua comunidade. Cuide do ambiente."
}

narrations_es = {
    "cena1": "Este es el Aedes aegypti, transmite el virus del Dengue. El Aedes albopictus, más conocido como mosquito tigre, también puede transmitir este virus. Las hembras de Aedes depositan sus huevos en agua estancada. Un huevo tarda entre 7 y 10 días en convertirse en un mosquito adulto.",
    "cena2": "Sin ninguna medida de control, el dengue se propaga a través de las picaduras de mosquitos. Solo las hembras pican a los humanos, ya que necesitan la sangre para que sus huevos se desarrollen. Los síntomas del dengue incluyen fiebre alta, dolor de cabeza intenso, dolores corporales y manchas rojas en la piel.",
    "cena3": "Con medidas individuales, como repelente, ropa larga y mosquiteros, algunas personas logran protegerse. Pero otras medidas también pueden ayudar.",
    "cena4": "Las medidas colectivas marcan una gran diferencia. Las vacunas protegen a las personas incluso cuando son picadas. Los insecticidas reducen la población de mosquitos. La combinación de diferentes medidas fortalece la lucha contra la enfermedad.",
    "cena5": "Cuando cuidamos el medio ambiente, retirando basura, tapando recipientes con agua y eliminando criaderos, los mosquitos pierden sus criaderos y no tienen dónde depositar sus huevos ni desarrollarse hasta la fase adulta!",
    "cena6": "El ambiente marca toda la diferencia. La lluvia y la basura juntos producen más criaderos. La limpieza y el cuidado los eliminan. En áreas urbanas densas, el riesgo es aún mayor.",
    "cena7": "El dengue tiene 4 serotipos diferentes y los mismos mosquitos que transmiten el Zika y el chikunguña. Pero con conocimiento y acción colectiva, podemos ganar esta batalla. Protégete. Protege a tu comunidad. Cuida el medio ambiente."
}

async def generate_lang(narrations, voice, output_dir, rate="-5%"):
    os.makedirs(output_dir, exist_ok=True)
    for name, text in narrations.items():
        output_file = os.path.join(output_dir, f"{name}.mp3")
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        await communicate.save(output_file)
        print(f"  Generated: {output_file}")

async def main():
    print("=== Gerando PT ===")
    await generate_lang(narrations_pt, "pt-BR-FranciscaNeural", "/home/ubuntu/narration_pt_v7")
    
    print("=== Gerando ES ===")
    await generate_lang(narrations_es, "es-ES-ElviraNeural", "/home/ubuntu/narration_es_v7")
    
    print("\nEN já existe em /home/ubuntu/narration_en_v7/")
    print("SUCESSO!")

asyncio.run(main())

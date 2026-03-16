"""
Regenerar narrações EN cena 4 e 6 conforme roteiro fornecido pelo usuário.
Cena 4: "Chemical interventions that are safe for the environment, can reduce"
Cena 6: "eliminates" (manter original do roteiro)
"""
import asyncio
import edge_tts
import os

OUTPUT_DIR = "/home/ubuntu/narration_en_v10"
os.makedirs(OUTPUT_DIR, exist_ok=True)

VOICE = "en-US-JennyNeural"

# Apenas cenas 4 e 6 mudaram
SCENES_TO_REGEN = {
    4: "Collective measures make a big difference! Vaccines, when available, protect people even when bitten. Chemical interventions that are safe for the environment, can reduce the mosquito population. The combination of different measures strengthens the fight against the disease.",
    6: "The environment makes all the difference. Rain and discarded waste together produce more breeding sites. Cleaning and care eliminates them. In dense urban areas, the risk is even greater.",
}

async def generate():
    for scene_num, text in SCENES_TO_REGEN.items():
        output_file = f"{OUTPUT_DIR}/cena{scene_num}.mp3"
        communicate = edge_tts.Communicate(text, VOICE, rate="-5%")
        await communicate.save(output_file)
        print(f"  cena{scene_num}: OK")

print("=== Regenerando narrações EN cena 4 e 6 (v10) ===")
asyncio.run(generate())
print("SUCESSO!")

"""
Regenerar narrações EN com textos corrigidos conforme commit 71fed48.
Alterações:
  Cena 1: "dengue virus" (minúscula), "can also transmit dengue" (não "this virus")
  Cena 2: "dengue is passed to humans through mosquito bites" (não "spreads")
  Cena 4: "Vaccines, when available, protect people" (adicionado "when available")
  Cena 5: "removing rubbish" (não "trash")
  Cena 6: "discarded waste" (não "trash"), "eliminates" (não "eliminate")
  Cena 7: "The same mosquitoes that transmit dengue also transmit" (removido "Dengue has 4 different serotypes")
"""
import asyncio
import edge_tts
import os

OUTPUT_DIR = "/home/ubuntu/narration_en_v8"
os.makedirs(OUTPUT_DIR, exist_ok=True)

VOICE = "en-US-JennyNeural"

# Textos corrigidos conforme commit 71fed48
SCENES_EN = {
    1: "This is the Aedes aegypti, it transmits the dengue virus. The Aedes albopictus, better known as the tiger mosquito, can also transmit dengue. Female Aedes lay their eggs in standing water. An egg takes between 7 and 10 days to become an adult mosquito.",
    
    2: "Without any control measures, dengue is passed to humans through mosquito bites. Only females bite humans, as they need blood for their eggs to develop. Dengue symptoms include high fever, intense headache, body aches, and red spots on the skin.",
    
    3: "With individual measures, such as repellent, long clothing, and mosquito nets, some people can protect themselves. But other measures can help too.",
    
    4: "Collective measures make a big difference! Vaccines, when available, protect people even when bitten. Insecticides reduce the mosquito population. The combination of different measures strengthens the fight against the disease.",
    
    5: "When we take care of the environment, removing rubbish, covering water containers, and eliminating breeding sites, mosquitoes lose them and have no place to lay their eggs and develop into adults!",
    
    6: "The environment makes all the difference. Rain and discarded waste together produce more breeding sites. Cleaning and care eliminates them. In dense urban areas, the risk is even greater.",
    
    7: "The same mosquitoes that transmit dengue also transmit Zika and chikungunya. But with knowledge and collective action, we can win this battle. Protect yourself. Protect your community. Take care of the environment.",
}

async def generate():
    for scene_num, text in SCENES_EN.items():
        output_file = f"{OUTPUT_DIR}/cena{scene_num}.mp3"
        communicate = edge_tts.Communicate(text, VOICE, rate="-5%")
        await communicate.save(output_file)
        print(f"  Generated: {output_file}")

print("=== Gerando narrações EN v8 (corrigidas) ===")
asyncio.run(generate())
print("SUCESSO!")

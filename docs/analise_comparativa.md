# Análise Comparativa: Roteiros GitHub vs Narrações vs Legendas (PT, EN, ES)

## Metodologia

Comparação cena a cena entre:
1. **Roteiro GitHub** — texto oficial em `roteiros/Roteiro_Dengue_XX.md`
2. **Narração (TTS)** — texto enviado ao edge-tts nos scripts `regenerate_*_narration_v8.py`
3. **Legendas (SRT)** — texto das legendas burn-in em `generate_all_videos_v8.py`

---

## CENA 1 — O que é a dengue?

### PT
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Este é o *Aedes aegypti*, ele transmite o vírus Dengue. O *Aedes albopictus*, mais conhecido como mosquito tigre, também pode transmitir esse vírus. As fêmeas de *Aedes* colocam os ovos em água parada. Um ovo demora entre 7 e 10 dias para se tornar um mosquito adulto." |
| **Narração TTS** | "Este é o Aedes aegypti, ele transmite o vírus Dengue. O Aedes albopictus, mais conhecido como mosquito tigre, também pode transmitir esse vírus. As fêmeas de Aedes colocam os ovos em água parada. Um ovo demora entre 7 e 10 dias para se tornar um mosquito adulto." |
| **Legendas** | "Este é o Aedes aegypti," / "ele transmite o vírus Dengue." / "O Aedes albopictus, mais conhecido" / "como mosquito tigre," / "também pode transmitir esse vírus." / "As fêmeas de Aedes colocam" / "os ovos em água parada." / "Um ovo demora entre 7 e 10 dias" / "para se tornar um mosquito adulto." |

**Status: OK** — Narração e legendas coincidem com o roteiro.

### EN
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "This is the *Aedes aegypti*, it transmits the dengue virus. The *Aedes albopictus*, better known as the tiger mosquito, can also transmit dengue. Female *Aedes* lay their eggs in standing water. An egg takes between 7 and 10 days to become an adult mosquito." |
| **Narração TTS** | "This is the Aedes aegypti, it transmits the dengue virus. The Aedes albopictus, better known as the tiger mosquito, can also transmit dengue. Female Aedes lay their eggs in standing water. An egg takes between 7 and 10 days to become an adult mosquito." |
| **Legendas** | "This is the Aedes aegypti," / "it transmits the dengue virus." / "The Aedes albopictus," / "better known as the tiger mosquito," / "can also transmit dengue." / "Female Aedes lay their eggs" / "in standing water." / "An egg takes between 7 and 10 days" / "to become an adult mosquito." |

**Status: OK** — Narração e legendas coincidem com o roteiro.

### ES
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Este es el *Aedes aegypti*, transmite el virus del Dengue. El *Aedes albopictus*, más conocido como mosquito tigre, también puede transmitir este virus. Las hembras de *Aedes* depositan sus huevos en agua estancada. Un huevo tarda entre 7 y 10 días en convertirse en un mosquito adulto." |
| **Narração TTS** | "Este es el Aedes aegypti, transmite el virus del Dengue. El Aedes albopictus, más conocido como mosquito tigre, también puede transmitir este virus. Las hembras de Aedes depositan sus huevos en agua estancada. Un huevo tarda entre 7 y 10 días en convertirse en un mosquito adulto." |
| **Legendas** | "Este es el Aedes aegypti," / "transmite el virus del Dengue." / "El Aedes albopictus," / "más conocido como mosquito tigre," / "también puede transmitir este virus." / "Las hembras de Aedes depositan" / "sus huevos en agua estancada." / "Un huevo tarda entre 7 y 10 días" / "en convertirse en un mosquito adulto." |

**Status: OK** — Narração e legendas coincidem com o roteiro.

---

## CENA 2 — Sem nenhum controle

### PT
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Sem nenhuma medida de controle, a dengue se espalha por meio das picadas de mosquitos. Somente as fêmeas picam os humanos, pois precisam do sangue para os ovos se desenvolverem. Os sintomas da dengue incluem febre alta, dor de cabeça intensa, dores no corpo e manchas vermelhas na pele." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 9 linhas) |

**Status: OK** — Consistente.

### EN
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Without any control measures, dengue is passed to humans through mosquito bites. Only females bite humans, as they need blood for their eggs to develop. Dengue symptoms include high fever, intense headache, body aches, and red spots on the skin." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 9 linhas) |

**Status: OK** — Consistente.

### ES
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Sin ninguna medida de control, el dengue se propaga a través de las picaduras de mosquitos. Solo las hembras pican a los humanos, ya que necesitan la sangre para que sus huevos se desarrollen. Los síntomas del dengue incluyen fiebre alta, dolor de cabeza intenso, dolores corporales y manchas rojas en la piel." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 10 linhas incluindo "en la piel.") |

**Status: OK** — Consistente.

---

## CENA 3 — Controle individual

### PT
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Com medidas individuais — como repelente, roupas compridas e mosquiteiros — algumas pessoas conseguem se proteger. Mas outras medidas podem ajudar também." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 5 linhas) |

**Status: OK** — Consistente.

### EN
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "With individual measures, such as repellent, long clothing, and mosquito nets, some people can protect themselves. But other measures can help too." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 5 linhas) |

**Status: OK** — Consistente.

### ES
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Con medidas individuales, como repelente, ropa larga y mosquiteros, algunas personas logran protegerse. Pero otras medidas también pueden ayudar." |
| **Narração TTS** | (idêntico) |
| **Legendas** | "Con medidas individuales," / "como repelente, ropa larga" / "y mosquiteros," / "algunas personas logran protegerse." / "Pero otras medidas también" / "pueden ayudar." |

**Status: OK** — Consistente. A divisão em 6 linhas (vs 5 no PT/EN) é aceitável.

---

## CENA 4 — Controle coletivo

### PT
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Medidas coletivas fazem uma grande diferença! Vacinas protegem as pessoas mesmo quando picadas. Inseticidas reduzem a população de mosquitos. A combinação de diferentes medidas fortalece o combate à doença." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 8 linhas) |

**Status: OK** — Consistente.

### EN
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Collective measures make a big difference! Vaccines, when available, protect people even when bitten. Insecticides reduce the mosquito population. The combination of different measures strengthens the fight against the disease." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 9 linhas) |

**Status: OK** — Consistente.

### ES
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Las medidas colectivas marcan una gran diferencia. Las vacunas protegen a las personas incluso cuando son picadas. Los insecticidas reducen la población de mosquitos. La combinación de diferentes medidas fortalece la lucha contra la enfermedad." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 9 linhas) |

**Status: OK** — Consistente.

### Inconsistência de tradução entre idiomas (Cena 4):

| Aspecto | PT | EN | ES |
|---------|----|----|-----|
| Vacinas | "Vacinas protegem as pessoas **mesmo quando picadas**" | "Vaccines, **when available**, protect people even when bitten" | "Las vacunas protegen a las personas **incluso cuando son picadas**" |
| Tom | "grande diferença**!**" (exclamação) | "big difference**!**" (exclamação) | "gran diferencia**.**" (ponto final) |

**INCONSISTÊNCIA DETECTADA #1:** O EN tem "when available" (quando disponíveis), que foi adicionado no commit 71fed48. Porém, **essa adição NÃO foi replicada no PT nem no ES**. O roteiro PT diz "Vacinas protegem as pessoas mesmo quando picadas" (sem "quando disponíveis") e o ES diz "Las vacunas protegen a las personas incluso cuando son picadas" (sem "cuando estén disponibles"). Isso reflete fielmente os roteiros do GitHub, mas pode ser uma inconsistência intencional ou um esquecimento na tradução.

**INCONSISTÊNCIA DETECTADA #2:** O PT usa exclamação "grande diferença**!**" e o EN também "big difference**!**", mas o ES usa ponto final "gran diferencia**.**". O roteiro ES no GitHub de fato tem ponto final, então está fiel ao roteiro, mas é uma diferença de tom.

---

## CENA 5 — Controle ambiental

### PT
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Quando cuidamos do ambiente — removendo lixo, tampando recipientes com água e eliminando criadouros — os mosquitos perdem seus criadouros, e ficam sem lugares para depositar os seus ovos e desenvolverem até a fase adulta!" |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 8 linhas) |

**Status: OK** — Consistente.

### EN
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "When we take care of the environment, removing rubbish, covering water containers, and eliminating breeding sites, mosquitoes lose their breeding grounds and have no place to lay their eggs and develop into adults!" |
| **Narração TTS** | "When we take care of the environment, removing rubbish, covering water containers, and eliminating breeding sites, mosquitoes lose **them** and have no place to lay their eggs and develop into adults!" |
| **Legendas** | "...mosquitoes lose **them**..." |

**INCONSISTÊNCIA DETECTADA #3:** O roteiro EN no GitHub diz "mosquitoes lose **their breeding grounds**", mas a narração e legendas usam "mosquitoes lose **them**". Essa alteração foi solicitada explicitamente pelo usuário durante a sessão anterior. Portanto, o texto do vídeo difere do roteiro GitHub neste ponto.

### ES
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "Cuando cuidamos el medio ambiente, retirando basura, tapando recipientes con agua y eliminando criaderos, los mosquitos pierden sus criaderos y no tienen dónde depositar sus huevos ni desarrollarse hasta la fase adulta!" |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 7 linhas) |

**Status: OK** — Consistente.

### Inconsistência de tradução entre idiomas (Cena 5):

| Aspecto | PT | EN | ES |
|---------|----|----|-----|
| Perdem criadouros | "os mosquitos perdem **seus criadouros**, e ficam sem lugares para depositar os seus ovos e **desenvolverem** até a fase adulta" | "mosquitoes lose **them** and have no place to lay their eggs and **develop** into adults" | "los mosquitos pierden **sus criaderos** y no tienen dónde depositar sus huevos ni **desarrollarse** hasta la fase adulta" |

O PT e ES mantêm "perdem seus criadouros/pierden sus criaderos", enquanto o EN usa "lose them" (conforme solicitação do usuário).

---

## CENA 6 — Condições que mudam tudo

### PT
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "O ambiente faz toda a diferença. Chuva e lixo juntos produzem mais criadouros. Limpeza e cuidado os eliminam. Em áreas urbanas densas, o risco é ainda maior." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 6 linhas) |

**Status: OK** — Consistente.

### EN
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "The environment makes all the difference. Rain and discarded waste together produce more breeding sites. Cleaning and care eliminates them. In dense urban areas, the risk is even greater." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 7 linhas) |

**Status: OK** — Consistente.

### ES
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "El ambiente marca toda la diferencia. La lluvia y la basura juntos producen más criaderos. La limpieza y el cuidado los eliminan. En áreas urbanas densas, el riesgo es aún mayor." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 6 linhas) |

**Status: OK** — Consistente.

### Inconsistência de tradução entre idiomas (Cena 6):

| Aspecto | PT | EN | ES |
|---------|----|----|-----|
| Lixo | "Chuva e **lixo** juntos" | "Rain and **discarded waste** together" | "La lluvia y **la basura** juntos" |
| Eliminam | "Limpeza e cuidado os **eliminam**" | "Cleaning and care **eliminates** them" | "La limpieza y el cuidado los **eliminan**" |

**OBSERVAÇÃO:** O EN usa "discarded waste" (resíduo descartado) enquanto PT usa "lixo" e ES usa "basura" (ambos = lixo). Isso é uma escolha estilística do roteiro EN (commit 71fed48 mudou de "trash" para "discarded waste"). Além disso, "Cleaning and care **eliminates**" tem um possível erro gramatical em inglês — o sujeito é composto ("Cleaning and care"), então o verbo deveria ser "**eliminate**" (plural). Porém, o roteiro EN no GitHub usa "eliminates", então está fiel ao roteiro.

---

## CENA 7 — Encerramento

### PT
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "A dengue possui 4 sorotipos diferentes e os mesmos mosquitos que transmitem a Zika e a chikungunya. Mas com conhecimento e ação coletiva, podemos vencer essa batalha. Proteja-se. Proteja sua comunidade. Cuide do ambiente." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 9 linhas) |

**Status: OK** — Consistente.

### EN
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "The same mosquitoes that transmit dengue also transmit Zika and chikungunya. But with knowledge and collective action, we can win this battle. Protect yourself. Protect your community. Take care of the environment." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 9 linhas) |

**Status: OK** — Consistente.

### ES
| Fonte | Texto |
|-------|-------|
| **Roteiro GitHub** | "El dengue tiene 4 serotipos diferentes y los mismos mosquitos que transmiten el Zika y el chikunguña. Pero con conocimiento y acción colectiva, podemos ganar esta batalla. Protégete. Protege a tu comunidad. Cuida el medio ambiente." |
| **Narração TTS** | (idêntico) |
| **Legendas** | (idêntico, dividido em 9 linhas) |

**Status: OK** — Consistente.

### Inconsistência de tradução entre idiomas (Cena 7):

| Aspecto | PT | EN | ES |
|---------|----|----|-----|
| Sorotipos | "A dengue possui **4 sorotipos diferentes** e os mesmos mosquitos que transmitem..." | "**The same mosquitoes** that transmit dengue **also** transmit..." | "El dengue tiene **4 serotipos diferentes** y los mismos mosquitos que transmiten..." |
| Estrutura | Começa com sorotipos, depois mosquitos | Começa direto com mosquitos (sem menção a sorotipos) | Começa com sorotipos, depois mosquitos |

**INCONSISTÊNCIA DETECTADA #4:** O EN **não menciona os 4 sorotipos**, enquanto PT e ES mencionam. Isso foi uma alteração intencional do commit 71fed48 (removeu "Dengue has 4 different serotypes" do EN). Os roteiros PT e ES no GitHub **mantêm** a menção aos 4 sorotipos. Portanto, está fiel aos roteiros, mas é uma diferença de conteúdo entre os idiomas.

| Aspecto | PT | EN | ES |
|---------|----|----|-----|
| "dengue also" | — | "dengue **also** transmit" | — |

O EN adicionou "also" (commit 71fed48), que não tem equivalente direto no PT/ES. No PT é "os mesmos mosquitos que transmitem" e no ES "los mismos mosquitos que transmiten" — o "mesmos/mismos" já carrega o sentido de "também".

---

## RESUMO DE INCONSISTÊNCIAS

### Inconsistências Narração/Legendas vs Roteiro GitHub

| # | Cena | Idioma | Tipo | Descrição |
|---|------|--------|------|-----------|
| 3 | 5 | EN | Texto difere do roteiro | Narração/legenda: "mosquitoes lose **them**" vs Roteiro: "mosquitoes lose **their breeding grounds**" (alteração solicitada pelo usuário) |

### Inconsistências de Tradução entre Idiomas (nos roteiros do GitHub)

| # | Cena | Tipo | Descrição |
|---|------|------|-----------|
| 1 | 4 | Conteúdo omitido | EN tem "when available" para vacinas; PT e ES não têm equivalente |
| 2 | 4 | Tom/pontuação | PT e EN usam "!" (exclamação); ES usa "." (ponto final) |
| 4 | 7 | Conteúdo omitido | EN não menciona "4 sorotipos diferentes"; PT e ES mencionam |

### Possível Erro Gramatical

| Cena | Idioma | Texto | Observação |
|------|--------|-------|------------|
| 6 | EN | "Cleaning and care **eliminates** them" | Sujeito composto deveria usar verbo no plural: "**eliminate**". Porém, o roteiro GitHub usa "eliminates". |

### Observação sobre Ortografia (PT)

| Cena | Texto | Observação |
|------|-------|------------|
| 2 | "Sem **nenhuma** medida de controle" | A forma padrão em português é "**nenhuma**" (feminino de "nenhum"). Está correto conforme o roteiro. |

---

## CONCLUSÃO

Os vídeos estão **fiéis aos roteiros do GitHub** em todos os 3 idiomas, com uma única exceção: a Cena 5 EN onde "their breeding grounds" foi substituído por "them" a pedido do usuário.

As inconsistências entre idiomas (#1, #2, #4) são **diferenças nos próprios roteiros do GitHub**, não erros de implementação. Se o objetivo é manter os 3 idiomas com conteúdo equivalente, seria necessário:

1. **Cena 4 PT:** Adicionar "quando disponíveis" → "Vacinas, quando disponíveis, protegem as pessoas mesmo quando picadas"
2. **Cena 4 ES:** Adicionar "cuando estén disponibles" → "Las vacunas, cuando estén disponibles, protegen a las personas incluso cuando son picadas"
3. **Cena 4 ES:** Mudar "." para "!" → "una gran diferencia**!**"
4. **Cena 5 EN:** Atualizar roteiro GitHub para "lose them" (conforme solicitação do usuário)
5. **Cena 7 PT/ES:** Decidir se mantém os "4 sorotipos" (ausente no EN) ou remove para consistência
6. **Cena 6 EN:** Considerar corrigir "eliminates" → "eliminate" (gramática)

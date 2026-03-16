# Relatório de Inconsistências entre Versões dos Roteiros

**Projeto:** Dengue Stickman Animation — Science is Wonderful! 2026  
**Repositório:** [github.com/Diegoricardox/dengue-stickman-animation](https://github.com/Diegoricardox/dengue-stickman-animation)  
**Data:** 16 de março de 2026  
**Autor:** Manus AI  
**Branch analisada:** `videos-finais-v7`

---

## 1. Introdução

Este relatório documenta todas as inconsistências identificadas entre as diferentes versões dos roteiros de narração do vídeo educativo sobre dengue, produzido em três idiomas (Português, Inglês e Espanhol). A análise abrange desde o commit inicial (`d7ea44d`) até a versão final (`dd7797a`), passando por todas as revisões intermediárias realizadas tanto pela equipe científica (rmartins) quanto pelo processo de produção automatizada dos vídeos.

O objetivo é fornecer um registro completo e rastreável de cada alteração, sua motivação e seu impacto na consistência entre os três idiomas.

---

## 2. Histórico de Commits dos Roteiros

A tabela a seguir apresenta todos os commits que alteraram os arquivos de roteiro, em ordem cronológica.

| Commit | Data | Autor | Descrição | Arquivos afetados |
|--------|------|-------|-----------|-------------------|
| `d7ea44d` | 05/Mar/2026 | Diego Ricardo Xavier | Commit inicial | PT, EN, ES |
| `989c41e` | — | rmartins | Edição agradecimentos | PT, EN, ES (créditos) |
| `c2007a6` | — | rmartins | Correção financiamento e tamanho das linhas | PT, EN, ES (formatação + créditos) |
| `71fed48` | — | rmartins | Edited narration English video | EN (cenas 1, 2, 5, 6, 7) |
| `fcb3050` | 15/Mar/2026 | rmartins | Narration scene 4 | EN (cena 4) |
| `28bf4d2` | 15/Mar/2026 | rmartins | Assisted by OpenAI | EN (créditos) |
| `2c6ef47` | 16/Mar/2026 | rmartins | Narration correction | EN (cena 5) |
| `c7e7623` | 16/Mar/2026 | Diego Ricardo Xavier | v9: Correções de consistência | PT, EN, ES (cenas 4, 5, 6) |
| `dd7797a` | 16/Mar/2026 | Diego Ricardo Xavier | v10: Narração EN cenas 4 e 6 | EN (cenas 4, 6) |

---

## 3. Inconsistências Identificadas por Cena

### 3.1 Cena 1 — O que é a dengue? (0:00 – 0:25)

| Versão | EN | PT | ES |
|--------|----|----|-----|
| Original (`d7ea44d`) | "the **Dengue** virus" / "this **virus**" | "o vírus **Dengue**" / "esse **vírus**" | "el virus del **Dengue**" / "este **virus**" |
| Após `71fed48` | "the **dengue** virus" / "**dengue**" | (sem alteração) | (sem alteração) |
| **Final** | "the **dengue** virus" / "**dengue**" | "o vírus **Dengue**" / "esse **vírus**" | "el virus del **Dengue**" / "este **virus**" |

**Inconsistência identificada:** O commit `71fed48` alterou "Dengue" (maiúscula) para "dengue" (minúscula) e "this virus" para "dengue" apenas no roteiro EN. Os roteiros PT e ES mantêm "Dengue" com maiúscula e usam pronomes ("esse vírus" / "este virus") em vez de repetir o nome da doença.

**Impacto:** Baixo. Trata-se de uma diferença estilística. O EN ficou mais direto ao repetir "dengue", enquanto PT e ES usam pronomes demonstrativos, o que é natural em cada idioma.

**Status atual:** Mantido conforme decisão editorial. A diferença de capitalização ("dengue" vs "Dengue") é aceitável, pois em inglês o uso em minúscula é mais comum na literatura científica recente.

---

### 3.2 Cena 2 — Sem nenhum controle (0:25 – 0:55)

| Versão | EN | PT | ES |
|--------|----|----|-----|
| Original (`d7ea44d`) | "dengue **spreads** through mosquito bites" | "a dengue **se espalha** por meio das picadas" | "el dengue **se propaga** a través de las picaduras" |
| Após `71fed48` | "dengue **is passed to humans** through mosquito bites" | (sem alteração) | (sem alteração) |
| **Final** | "dengue **is passed to humans** through mosquito bites" | "a dengue **se espalha** por meio das picadas" | "el dengue **se propaga** a través de las picaduras" |

**Inconsistência identificada:** O EN foi alterado de "spreads" (se espalha) para "is passed to humans" (é transmitida aos humanos), uma formulação mais precisa cientificamente. Os roteiros PT e ES mantêm a formulação original "se espalha" / "se propaga", que é menos específica.

**Impacto:** Médio. A formulação EN é mais precisa ao indicar a direção da transmissão (mosquito → humano), enquanto PT e ES usam verbos mais genéricos.

**Status atual:** Mantido conforme roteiros oficiais. Seria recomendável atualizar PT para "a dengue é transmitida aos humanos" e ES para "el dengue se transmite a los humanos" para maior precisão.

---

### 3.3 Cena 3 — Controle individual (0:55 – 1:20)

Nenhuma inconsistência identificada. Os textos de narração são equivalentes nos três idiomas e não sofreram alterações ao longo das versões.

---

### 3.4 Cena 4 — Controle coletivo (1:20 – 1:50)

Esta cena concentra o maior número de alterações ao longo do histórico de versões.

| Versão | EN | PT | ES |
|--------|----|----|-----|
| Original (`d7ea44d`) | "Vaccines **protect** people" / "**Insecticides** reduce" | "Vacinas **protegem** as pessoas" / "**Inseticidas** reduzem" | "Las vacunas **protegen**" / "Los **insecticidas** reducen" |
| Após `71fed48` | "Vaccines, **when available**, protect" / "Insecticides reduce" | (sem alteração) | (sem alteração) |
| Após `fcb3050` | "Vaccines, when available, protect" / "**Chemical interventions that are safe for the environment,** can reduce" | (sem alteração) | (sem alteração) |
| Após `c7e7623` (v9) | (sem alteração) | "Vacinas, **quando disponíveis**, protegem" | "Las vacunas, **cuando estén disponibles**, protegen" |
| **Final** | "Vaccines, **when available**" / "**Chemical interventions that are safe for the environment**, can reduce" | "Vacinas, **quando disponíveis**" / "**Inseticidas** reduzem" | "Las vacunas, **cuando estén disponibles**" / "Los **insecticidas** reducen" |

**Inconsistências identificadas:**

1. **"when available" / "quando disponíveis" / "cuando estén disponibles":** O EN recebeu essa qualificação no commit `71fed48`, e os roteiros PT e ES foram atualizados na v9 para manter consistência. **Resolvido.**

2. **"Chemical interventions that are safe for the environment" vs "Inseticidas":** O EN foi alterado no commit `fcb3050` para substituir "Insecticides" por uma formulação mais abrangente e ambientalmente consciente. Os roteiros PT e ES **não foram atualizados** e ainda usam "Inseticidas" / "Los insecticidas".

**Impacto:** Alto. A mensagem transmitida é significativamente diferente. O EN fala de "intervenções químicas seguras para o meio ambiente", enquanto PT e ES falam simplesmente de "inseticidas". Essa é a inconsistência mais relevante entre os idiomas.

**Recomendação:** Atualizar PT para "Intervenções químicas seguras para o meio ambiente podem reduzir a população de mosquitos" e ES para "Las intervenciones químicas seguras para el medio ambiente pueden reducir la población de mosquitos".

---

### 3.5 Cena 5 — Controle ambiental (1:50 – 2:20)

| Versão | EN | PT | ES |
|--------|----|----|-----|
| Original (`d7ea44d`) | "removing **trash**" / "lose **their breeding grounds**" | "removendo **lixo**" / "perdem **seus criadouros**" | "retirando **basura**" / "pierden **sus criaderos**" |
| Após `71fed48` | "removing **rubbish**" / "lose **their breeding grounds**" | (sem alteração) | (sem alteração) |
| Após `2c6ef47` | "removing rubbish" / "lose **them**" | (sem alteração) | (sem alteração) |
| **Final** | "removing **rubbish**" / "lose **them**" | "removendo **lixo**" / "perdem **seus criadouros**" | "retirando **basura**" / "pierden **sus criaderos**" |

**Inconsistências identificadas:**

1. **"trash" → "rubbish":** Alteração no EN (`71fed48`) para inglês britânico. PT e ES mantêm "lixo" / "basura" (equivalentes corretos). **Sem inconsistência semântica.**

2. **"their breeding grounds" → "them":** O EN foi simplificado no commit `2c6ef47`. PT e ES mantêm a formulação completa "seus criadouros" / "sus criaderos". A versão EN é mais concisa, enquanto PT e ES são mais explícitas.

**Impacto:** Baixo. A diferença é estilística. "Lose them" é mais conciso e natural em inglês, enquanto "perdem seus criadouros" é mais claro em português e espanhol.

**Status atual:** Mantido conforme decisão editorial.

---

### 3.6 Cena 6 — Condições que mudam tudo (2:20 – 2:40)

| Versão | EN | PT | ES |
|--------|----|----|-----|
| Original (`d7ea44d`) | "**trash**" / "**eliminate** them" | "**lixo**" / "os **eliminam**" | "**basura**" / "los **eliminan**" |
| Após `71fed48` | "**discarded waste**" / "**eliminates** them" | (sem alteração) | (sem alteração) |
| **Final** | "**discarded waste**" / "**eliminates** them" | "**lixo**" / "os **eliminam**" | "**basura**" / "los **eliminan**" |

**Inconsistências identificadas:**

1. **"trash" → "discarded waste":** O EN foi alterado para uma formulação mais formal. PT e ES mantêm "lixo" / "basura". **Sem inconsistência semântica**, apenas diferença de registro linguístico.

2. **"eliminates" vs "eliminate" / "eliminam" / "eliminan":** O roteiro EN usa "eliminates" (singular), enquanto PT usa "eliminam" (plural) e ES usa "eliminan" (plural). Em inglês, "Cleaning and care" pode ser interpretado como sujeito composto (plural → "eliminate") ou como conceito unitário (singular → "eliminates"). O roteiro EN oficial mantém "eliminates".

**Impacto:** Baixo. Trata-se de uma questão gramatical discutível em inglês. O roteiro oficial foi respeitado.

**Nota:** Na versão v9, a produção automatizada havia corrigido para "eliminate" (plural), mas na v10 foi revertido para "eliminates" conforme o roteiro oficial.

---

### 3.7 Cena 7 — Encerramento e chamada à ação (2:40 – 3:00)

| Versão | EN | PT | ES |
|--------|----|----|-----|
| Original (`d7ea44d`) | "Dengue has **4 different serotypes** and the same mosquitoes" | "A dengue possui **4 sorotipos diferentes** e os mesmos mosquitos" | "El dengue tiene **4 serotipos diferentes** y los mismos mosquitos" |
| Após `71fed48` | "The same mosquitoes that transmit **dengue also** transmit" | (sem alteração) | (sem alteração) |
| **Final** | "The same mosquitoes that transmit **dengue also** transmit" | "A dengue possui **4 sorotipos diferentes** e os mesmos mosquitos" | "El dengue tiene **4 serotipos diferentes** y los mismos mosquitos" |

**Inconsistência identificada:** O EN removeu a menção aos "4 sorotipos diferentes" no commit `71fed48` e reestruturou a frase. Os roteiros PT e ES **mantêm** essa informação.

**Impacto:** Alto. A informação sobre os 4 sorotipos é cientificamente relevante e está presente em PT e ES, mas ausente no EN. Isso significa que o público anglófono recebe menos informação científica nesta cena.

**Recomendação:** Decidir se a menção aos 4 sorotipos deve ser mantida em todos os idiomas (adicionando de volta ao EN) ou removida de todos (removendo de PT e ES). A decisão depende do tempo disponível na cena e da prioridade editorial.

---

## 4. Inconsistências nos Créditos

| Elemento | EN | PT | ES |
|----------|----|----|-----|
| Afiliação Raquel | "GHR/BSC" | "BSC" | "BSC" |
| "Assisted by OpenAI" | Presente (desde `28bf4d2`) | Ausente | Ausente |
| Referência 3 (Guia de Vigilância) | Presente (desde `c2007a6`) | Presente (desde `c2007a6`) | Presente (desde `c2007a6`) |
| Gênero "financiado/a" | "funded" (neutro) | "financiada" (feminino, desde `c2007a6`) | "financiada" (feminino) |

**Inconsistências identificadas:**

1. **Afiliação de Raquel Martins Lana:** O EN lista "GHR/BSC" enquanto PT e ES listam apenas "BSC". A afiliação deveria ser consistente.

2. **"Assisted by OpenAI":** Adicionado apenas ao EN no commit `28bf4d2`. Ausente nos créditos PT e ES. Se a menção é necessária, deveria constar em todos os idiomas.

**Impacto:** Médio. Os créditos não são narrados no vídeo, mas aparecem nos roteiros e podem ser exibidos na tela.

---

## 5. Resumo das Inconsistências

A tabela a seguir resume todas as inconsistências encontradas, classificadas por severidade.

| Severidade | Cena | Descrição | Status |
|------------|------|-----------|--------|
| **Alta** | 4 | EN usa "Chemical interventions safe for environment"; PT/ES usam "Inseticidas" | Pendente |
| **Alta** | 7 | EN omite "4 sorotipos"; PT/ES mantêm | Pendente |
| **Média** | 2 | EN usa "is passed to humans"; PT/ES usam "se espalha/propaga" | Pendente |
| **Média** | Créditos | "Assisted by OpenAI" apenas no EN | Pendente |
| **Média** | Créditos | Afiliação "GHR/BSC" (EN) vs "BSC" (PT/ES) | Pendente |
| **Baixa** | 1 | "dengue" minúscula (EN) vs "Dengue" maiúscula (PT/ES) | Mantido |
| **Baixa** | 5 | "lose them" (EN) vs "perdem seus criadouros" (PT/ES) | Mantido |
| **Baixa** | 5 | "rubbish" (EN) vs "lixo/basura" (PT/ES) | Sem inconsistência |
| **Baixa** | 6 | "discarded waste" (EN) vs "lixo/basura" (PT/ES) | Sem inconsistência |
| **Baixa** | 6 | "eliminates" singular (EN) vs "eliminam/eliminan" plural (PT/ES) | Mantido |

---

## 6. Rastreabilidade: Narração dos Vídeos vs Roteiros

A tabela a seguir indica se a narração de cada vídeo final (v10) corresponde exatamente ao roteiro oficial mais recente no repositório.

| Cena | EN (v10) vs Roteiro EN | PT (v9) vs Roteiro PT | ES (v9) vs Roteiro ES |
|------|------------------------|----------------------|----------------------|
| 1 | Conforme | Conforme | Conforme |
| 2 | Conforme | Conforme | Conforme |
| 3 | Conforme | Conforme | Conforme |
| 4 | Conforme | Conforme | Conforme |
| 5 | Conforme | Conforme | Conforme |
| 6 | Conforme | Conforme | Conforme |
| 7 | Conforme | Conforme | Conforme |

Todas as narrações dos vídeos finais estão em conformidade com os respectivos roteiros oficiais no repositório.

---

## 7. Recomendações

Com base na análise realizada, as seguintes ações são recomendadas para alcançar consistência total entre os três idiomas:

1. **Cena 4 (Prioridade Alta):** Atualizar os roteiros PT e ES para substituir "Inseticidas" por "Intervenções químicas seguras para o meio ambiente" / "Intervenciones químicas seguras para el medio ambiente", alinhando com o EN.

2. **Cena 7 (Prioridade Alta):** Decidir se a menção aos "4 sorotipos diferentes" deve ser adicionada de volta ao EN ou removida de PT e ES, garantindo que todos os idiomas transmitam a mesma informação.

3. **Cena 2 (Prioridade Média):** Considerar atualizar PT e ES para usar formulação equivalente a "is passed to humans" para maior precisão científica.

4. **Créditos (Prioridade Média):** Adicionar "Assistido por OpenAI" aos créditos PT e ES, e padronizar a afiliação de Raquel Martins Lana em todos os idiomas.

5. **Após aprovação das correções:** Regenerar as narrações e legendas dos vídeos afetados para refletir as alterações nos roteiros.

---

## 8. Versões dos Vídeos Gerados

| Versão | Data | Alterações |
|--------|------|------------|
| v7 | 16/Mar/2026 | Primeira versão com narrações sincronizadas |
| v8 | 16/Mar/2026 | EN corrigido conforme commit `71fed48`; PT e ES regenerados |
| v9 | 16/Mar/2026 | Correções de consistência: "quando disponíveis" adicionado em PT/ES cena 4 |
| v10 | 16/Mar/2026 | EN cena 4 atualizada ("Chemical interventions..."); EN cena 6 revertida ("eliminates") |

---

*Relatório gerado automaticamente por Manus AI em 16 de março de 2026.*

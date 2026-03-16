# Dengue Stickman Animation — Science is Wonderful! 2026

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Vídeo educativo de animação de bonecos palito sobre a dengue, desenvolvido para exibição 
na feira de ciências **Science is Wonderful! 2026** em Bruxelas (Booth #18 — *Health 
detectives: how diseases spread through insects*).

O vídeo explica de forma lúdica e acessível o ciclo de vida do mosquito *Aedes aegypti*, 
a transmissão da dengue e as diferentes estratégias de controle (individual, coletivo e ambiental), 
voltado para o público de 7 a 18 anos.

---

## Créditos

**Conteúdo científico:** Equipe SiW 2026 — Raquel Martins Lana (GHR/BSC), Andria Nicodemou (ESS/BSC) 
e Tatiana Docile (UERJ).  
Acesse o site do [Science is Wonderful](https://marie-sklodowska-curie-actions.ec.europa.eu/science-is-wonderful/science-is-wonderful).

**Adaptação, roteiro e produção audiovisual:** Diego Ricardo Xavier (ICICT/Fiocruz), 
com auxílio de inteligência artificial generativa para animação e narração sintética.

**Financiamento:** RML foi financiada pela União Europeia (Marie Sklodowska-Curie Actions, 
nº projeto 101109642). Agradecemos o apoio do projeto HARMONIZE (Wellcome Trust, 
nº projeto: 224694/Z/21/Z) e Conselho Nacional de Desenvolvimento Científico e Tecnológico 
(CNPq) (processo 445194/2024-3), Observatório de Clima e Saúde (Fiocruz), do Laboratório de 
Informação em Saúde (LIS) do ICICT/Fiocruz.

**Referências Científicas:**
1. Instituto Oswaldo Cruz (IOC/Fiocruz) — Ciclo de transmissão do *Aedes aegypti* e dengue
2. Centers for Disease Control and Prevention (CDC) — Sorotipos e sintomas da dengue
3. Guia de Vigilância em Saúde, Ministério da Saúde do Brasil, 6ª edição

---

## Estrutura do Repositório

```
dengue-stickman-animation/
│
├── README.md                          # Este arquivo
├── LICENSE                            # Licença do projeto
├── Ferramentas_Gratuitas_Edicao.md    # Guia de ferramentas gratuitas para pós-produção
│
├── videos/                            # Vídeos finais legendados (MP4, H.264, 1280x720)
│   ├── dengue_final_PT.mp4            # Versão final em Português com legendas (2min 07s)
│   ├── dengue_final_EN.mp4            # Versão final em Inglês com legendas (2min 07s)
│   ├── dengue_final_ES.mp4            # Versão final em Espanhol com legendas (2min 07s)
│   ├── video_only_EN.mp4              # Vídeo base sem áudio (visual compartilhado)
│   ├── dengue_stickman_v6_PT.mp4      # Versão anterior v6 — Português
│   ├── dengue_stickman_v6_EN.mp4      # Versão anterior v6 — Inglês
│   └── dengue_stickman_v6_ES.mp4      # Versão anterior v6 — Espanhol
│
├── legendas/                          # Arquivos de legenda (SRT) para edição
│   ├── legendas_PT_final_v8.srt       # Legendas finais em Português (v8)
│   ├── legendas_EN_final_v8.srt       # Legendas finais em Inglês (v8)
│   ├── legendas_ES_final_v8.srt       # Legendas finais em Espanhol (v8)
│   ├── legendas_PT_final_v7.srt       # Legendas anteriores — Português (v7)
│   ├── legendas_EN_final_v7.srt       # Legendas anteriores — Inglês (v7)
│   ├── legendas_ES_final_v7.srt       # Legendas anteriores — Espanhol (v7)
│   ├── legendas_PT.srt                # Legendas anteriores — Português (v6)
│   ├── legendas_EN.srt                # Legendas anteriores — Inglês (v6)
│   └── legendas_ES.srt                # Legendas anteriores — Espanhol (v6)
│
├── roteiros/                          # Roteiros completos com descrição visual
│   ├── Roteiro_Dengue_PT.md           # Roteiro em Português
│   ├── Roteiro_Dengue_EN.md           # Roteiro em Inglês (Script)
│   └── Roteiro_Dengue_ES.md           # Roteiro em Espanhol (Guión)
│
├── assets_edicao/                     # Assets separados para edição e pós-produção
│   ├── musica_fundo.mp3               # Música de fundo instrumental
│   ├── audio_PT.wav                   # Áudio completo (narração + música) — PT
│   ├── audio_EN.wav                   # Áudio completo (narração + música) — EN
│   ├── audio_ES.wav                   # Áudio completo (narração + música) — ES
│   ├── video_only_PT.mp4              # Vídeo sem áudio — PT
│   ├── video_only_EN.mp4              # Vídeo sem áudio — EN
│   ├── video_only_ES.mp4              # Vídeo sem áudio — ES
│   ├── narracoes_PT/                  # Narrações individuais por cena (PT)
│   │   ├── cena1.mp3 ... cena7.mp3
│   ├── narracoes_EN/                  # Narrações individuais por cena (EN)
│   │   ├── cena1.mp3 ... cena7.mp3
│   └── narracoes_ES/                  # Narrações individuais por cena (ES)
│       ├── cena1.mp3 ... cena7.mp3
│
├── logos/                             # Logos institucionais
│   └── logos_new.png                  # Composição de logos para créditos
│
└── scripts/                           # Scripts Python para geração do vídeo
    ├── generate_all_videos_v8.py      # Script principal de geração dos 3 vídeos (v8)
    ├── regenerate_en_narration_v8.py  # Script de regeneração da narração EN (v8)
    ├── generate_all_videos.py         # Script de geração dos 3 vídeos (v7)
    ├── generate_narration_all_v7.py   # Script de geração de narrações (edge-tts, v7)
    ├── fix_narration_speed.py         # Script de ajuste de velocidade das narrações
    ├── create_video_v5.py             # Script anterior de renderização (v5)
    └── generate_narration_v6.py       # Script anterior de narrações (v6)
```

---

## Conteúdo do Vídeo

O vídeo é composto por 7 cenas + créditos, cobrindo os seguintes tópicos:

| Cena | Título | Conteúdo |
|---|---|---|
| 1 | O que é a dengue? | Ciclo de vida do *Aedes aegypti* (ovo → larva → pupa → adulto), menção ao *Aedes albopictus* (mosquito tigre) |
| 2 | Sem nenhum controle | Mosquitos atacam livremente — Picados: 8/8, Infectados: 6/8. Sintomas: febre, dor de cabeça, manchas vermelhas |
| 3 | Controle individual | Repelente, roupas compridas, mosquiteiros — Picados: 5/8, Infectados: 3/8 |
| 4 | Controle coletivo | Vacinação e fumacê — Picados: 4/8, Infectados: 1/8 |
| 5 | Controle ambiental | Mutirão de limpeza, eliminação de criadouros — Picados: 1/8, Infectados: 0/8 |
| 6 | Condições que mudam tudo | 4 quadrantes: chuva, lixo, limpeza, área urbana densa |
| 7 | Encerramento | Chamada à ação, menção a Zika, chikungunya, malária, leishmaniose e Chagas |
| Créditos | Financiamento e equipe | Logos institucionais, referências científicas |

---

## Especificações Técnicas

| Parâmetro | Valor |
|---|---|
| Resolução | 1280 x 720 (HD) |
| FPS | 12 |
| Codec | H.264 (MP4) |
| Duração | ~2 minutos e 7 segundos |
| Estilo visual | Fundo branco, bonecos palito pretos, objetos em emoji |
| Legendas | Burn-in (texto branco, contorno preto, fundo semi-transparente) |
| Narração PT | Francisca (pt-BR) — voz feminina suave |
| Narração EN | Jenny (en-US) — voz feminina madura e amigável |
| Narração ES | Elvira (es-ES) — voz feminina clara e amigável |
| Música de fundo | Instrumental suave a -18dB |

---

## Histórico de Versões

| Versão | Data | Descrição |
|---|---|---|
| v8 (final) | 2025-03-16 | Narração EN corrigida conforme commit 71fed48: "dengue" minúscula, "is passed to humans", "when available", "rubbish", "discarded waste", "lose them", remoção de "4 serotypes" |
| v7 | 2025-03-14 | Vídeos com roteiros atualizados do GitHub, narrações resincronizadas via scene detection |
| v6 | 2025-03-05 | Vídeos com legendas burn-in, logos institucionais e créditos |
| v5 | 2025-03-04 | Primeira versão com animação completa de 7 cenas |

---

## Como Editar

Os assets de edição permitem remontar o vídeo em qualquer editor. Consulte o arquivo 
`Ferramentas_Gratuitas_Edicao.md` para um guia completo de ferramentas gratuitas recomendadas para:

- Melhorar a naturalidade da voz (remover tom de IA)
- Aumentar a resolução (upscaling de 720p para 1080p/4K)
- Adicionar legendas em outros idiomas (francês, holandês)
- Edição geral (cortes, transições, efeitos)

---

## Como Regenerar o Vídeo (v7)

Para regenerar os vídeos a partir dos scripts Python:

```bash
# Instalar dependências
pip install edge-tts pydub ffmpeg-python

# 1. Gerar narrações nos 3 idiomas
python scripts/generate_narration_all_v7.py

# 2. Ajustar velocidade das narrações (se necessário)
python scripts/fix_narration_speed.py

# 3. Gerar os 3 vídeos finais (requer video_only_EN.mp4 e bg_music.wav)
python scripts/generate_all_videos.py
```

**Nota:** O script `generate_all_videos.py` utiliza `video_only_EN.mp4` como base visual 
e combina com narrações, legendas burn-in e música de fundo para cada idioma.

---

## Referências Científicas

1. Instituto Oswaldo Cruz (IOC/Fiocruz) — Ciclo de transmissão do *Aedes aegypti* e dengue
2. Centers for Disease Control and Prevention (CDC) — Sorotipos e sintomas da dengue
3. Guia de Vigilância em Saúde, Ministério da Saúde do Brasil, 6ª edição

---

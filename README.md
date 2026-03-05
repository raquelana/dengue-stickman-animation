# Dengue Stickman Animation — Science is Wonderful! 2026

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)]
(https://creativecommons.org/licenses/by-nc-sa/4.0/)

Vídeo educativo de animação de bonecos palito sobre a dengue, desenvolvido para exibição 
na feira de ciências **Science is Wonderful! 2026** em Bruxelas (Booth #18 — *Health 
detectives: how diseases spread through insects*).

O vídeo explica de forma lúdica e acessível o ciclo de vida do mosquito *Aedes aegypti*, 
a transmissão da dengue e as diferentes estratégias de controle (individual, coletivo e ambiental), 
voltado para o público de 7 a 18 anos.

---

## Créditos

**Conteúdo científico:** Equipe SiW 2026 — Raquel Martins Lana (BSC), Andria Nicodemou (BSC) 
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
│   ├── dengue_stickman_v6_PT.mp4      # Versão em Português com legendas (2min 09s)
│   ├── dengue_stickman_v6_EN.mp4      # Versão em Inglês com legendas (2min 07s)
│   └── dengue_stickman_v6_ES.mp4      # Versão em Espanhol com legendas (2min 15s)
│
├── legendas/                          # Arquivos de legenda (SRT) para edição
│   ├── legendas_PT.srt                # Legendas em Português
│   ├── legendas_EN.srt                # Legendas em Inglês
│   └── legendas_ES.srt                # Legendas em Espanhol
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
    ├── create_video_v5.py             # Script principal de renderização
    └── generate_narration_v6.py       # Script de geração de narrações (edge-tts)
```

---

## Conteúdo do Vídeo

O vídeo é composto por 7 cenas + créditos, cobrindo os seguintes tópicos:

| Cena | Título | Conteúdo |
|---|---|---|
| 1 | O que é a dengue? | Ciclo de vida do *Aedes aegypti* (ovo → larva → pupa → adulto), 
menção ao *Aedes albopictus* (mosquito tigre) |
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
| Estilo visual | Fundo branco, bonecos palito pretos, objetos em emoji |
| Narração PT | Francisca (pt-BR) — voz feminina suave |
| Narração EN | Jenny (en-US) — voz feminina madura e amigável |
| Narração ES | Elvira (es-ES) — voz feminina clara e amigável |

---

## Como Editar

Os assets de edição permitem remontar o vídeo em qualquer editor. Consulte o arquivo 
`Ferramentas_Gratuitas_Edicao.md` para um guia completo de ferramentas gratuitas recomendadas para:

- Melhorar a naturalidade da voz (remover tom de IA)
- Aumentar a resolução (upscaling de 720p para 1080p/4K)
- Adicionar legendas em outros idiomas (francês, holandês)
- Edição geral (cortes, transições, efeitos)

---

## Como Regenerar o Vídeo

Para regenerar o vídeo a partir dos scripts Python:

```bash
# Instalar dependências
pip install edge-tts moviepy pydub Pillow

# Gerar narrações
python scripts/generate_narration_v6.py

# Renderizar vídeo (pt, en ou es)
python scripts/create_video_v5.py pt
python scripts/create_video_v5.py en
python scripts/create_video_v5.py es
```

---

## Referências Científicas

1. Instituto Oswaldo Cruz (IOC/Fiocruz) — Ciclo de transmissão do *Aedes aegypti* e dengue
2. Centers for Disease Control and Prevention (CDC) — Sorotipos e sintomas da dengue
3. Guia de Vigilância em Saúde, Ministério da Saúde do Brasil, 6ª edição

---

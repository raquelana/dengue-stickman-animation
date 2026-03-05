# Ferramentas Gratuitas para Melhorar Voz, Resolução e Edição do Vídeo

Este documento lista ferramentas online gratuitas que podem ser usadas para aprimorar a qualidade da narração (removendo o tom de IA), aumentar a resolução do vídeo e realizar edições adicionais.

---

## 1. Melhorar a Voz (Remover Tom de IA)

Estas ferramentas ajudam a tornar a narração mais natural, removendo artefatos de síntese e melhorando a entonação.

| Ferramenta | URL | O que faz | Limitações gratuitas |
|---|---|---|---|
| **Adobe Podcast (Enhance Speech)** | [podcast.adobe.com](https://podcast.adobe.com/enhance) | Remove ruído, melhora clareza e naturalidade da voz. Excelente para "limpar" vozes TTS. | Até 1 hora de áudio por arquivo, conta Adobe gratuita necessária |
| **Auphonic** | [auphonic.com](https://auphonic.com) | Normalização de volume, equalização inteligente, remoção de ruído. Processa áudio para soar profissional. | 2 horas/mês gratuitas |
| **Descript** | [descript.com](https://www.descript.com) | Editor de áudio/vídeo com IA. Permite ajustar velocidade, tom e pausas da narração de forma granular. | Plano gratuito com 1 hora de transcrição/mês |
| **Audacity** | [audacityteam.org](https://www.audacityteam.org) | Software desktop gratuito e open-source. Permite equalização, compressão, ajuste de pitch e remoção de ruído manualmente. | Totalmente gratuito, sem limites |
| **ElevenLabs (Speech-to-Speech)** | [elevenlabs.io](https://elevenlabs.io) | Converte a voz TTS em uma voz mais natural usando clonagem de voz. Pode transformar completamente o tom. | 10 minutos/mês no plano gratuito |

**Recomendação:** Para o melhor resultado gratuito, use o **Adobe Podcast Enhance Speech** para limpar o áudio, e depois ajuste manualmente no **Audacity** (equalizando graves e agudos para soar mais quente e natural).

---

## 2. Melhorar a Resolução do Vídeo (Upscaling)

Estas ferramentas aumentam a resolução do vídeo de 720p para 1080p ou 4K usando inteligência artificial.

| Ferramenta | URL | O que faz | Limitações gratuitas |
|---|---|---|---|
| **CapCut** | [capcut.com](https://www.capcut.com) | Editor de vídeo com função "Enhance" que melhora resolução e nitidez automaticamente. | Gratuito, disponível na web e desktop |
| **Pixop** | [pixop.com](https://www.pixop.com) | Upscaling profissional com IA. Aumenta resolução mantendo nitidez. | Trial gratuito com créditos limitados |
| **Video2X** | [github.com/k4yt3x/video2x](https://github.com/k4yt3x/video2x) | Software open-source de upscaling de vídeo usando Waifu2x, SRMD e Real-ESRGAN. | Totalmente gratuito, requer instalação local |
| **Clideo Video Enhancer** | [clideo.com/video-enhancer](https://clideo.com/video-enhancer) | Ferramenta online simples para melhorar brilho, contraste e nitidez. | Gratuito com marca d'água (removível) |
| **Topaz Video AI** | [topazlabs.com](https://www.topazlabs.com/topaz-video-ai) | O melhor upscaler de vídeo do mercado. Resultados impressionantes. | Trial gratuito (com marca d'água) |

**Recomendação:** O **CapCut** é a opção mais prática e totalmente gratuita. Para resultados profissionais sem marca d'água, use o **Video2X** (open-source, instalação local).

---

## 3. Edição Geral do Vídeo

Programas completos para editar, cortar, adicionar legendas e efeitos ao vídeo.

| Ferramenta | URL | O que faz | Limitações gratuitas |
|---|---|---|---|
| **DaVinci Resolve** | [blackmagicdesign.com](https://www.blackmagicdesign.com/products/davinciresolve) | Editor profissional completo: edição, correção de cor, efeitos visuais, mixagem de áudio. O mais poderoso gratuito. | Versão gratuita completa (sem 8K e alguns efeitos avançados) |
| **CapCut** | [capcut.com](https://www.capcut.com) | Editor intuitivo com legendas automáticas, transições, efeitos de texto e templates. Ideal para legendar em múltiplos idiomas. | Gratuito na web e desktop |
| **Shotcut** | [shotcut.org](https://shotcut.org) | Editor open-source leve com suporte a múltiplas trilhas, filtros e exportação em diversos formatos. | Totalmente gratuito |
| **Kdenlive** | [kdenlive.org](https://kdenlive.org) | Editor open-source avançado com edição em múltiplas trilhas e efeitos. | Totalmente gratuito |
| **OpenShot** | [openshot.org](https://www.openshot.org) | Editor simples e intuitivo, ideal para iniciantes. | Totalmente gratuito |

**Recomendação:** Use o **DaVinci Resolve** para edição profissional completa, ou o **CapCut** para adicionar legendas automáticas em francês e holandês rapidamente (útil para a Science is Wonderful!).

---

## 4. Adicionar Legendas em Múltiplos Idiomas

Para a Science is Wonderful! em Bruxelas, pode ser útil adicionar legendas em francês e holandês.

| Ferramenta | URL | O que faz | Limitações gratuitas |
|---|---|---|---|
| **CapCut (Auto Captions)** | [capcut.com](https://www.capcut.com) | Gera legendas automáticas e permite tradução para múltiplos idiomas. | Gratuito |
| **VEED.io** | [veed.io](https://www.veed.io) | Legendas automáticas com tradução, editor online completo. | 2 GB de armazenamento, marca d'água no plano gratuito |
| **Kapwing** | [kapwing.com](https://www.kapwing.com) | Editor online com legendas automáticas e tradução. | Vídeos até 4 min gratuitos |

---

## Fluxo de Trabalho Recomendado

Para obter o melhor resultado final a partir dos vídeos gerados, recomenda-se o seguinte fluxo de trabalho:

1. **Melhorar a narração:** Processar cada arquivo de áudio individual (cena1.mp3 a cena7.mp3, disponíveis na pasta `edicao_assets/narracoes_XX/`) no Adobe Podcast Enhance Speech, e depois ajustar no Audacity.

2. **Remontar o áudio:** No DaVinci Resolve ou CapCut, importar o vídeo sem áudio (`video_only_XX.mp4`) e substituir a trilha de áudio pelas narrações melhoradas, adicionando a música de fundo (`musica_fundo.mp3`) em volume baixo.

3. **Melhorar a resolução:** Exportar o vídeo final e processá-lo no CapCut (Enhance) ou Video2X para upscaling de 720p para 1080p.

4. **Adicionar legendas:** No CapCut, usar Auto Captions para gerar legendas em francês e holandês automaticamente.

5. **Exportar:** Salvar em MP4 (H.264) para máxima compatibilidade com projetores e telas da feira.

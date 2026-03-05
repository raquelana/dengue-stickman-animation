#!/usr/bin/env python3
"""
Dengue Stickman Animation V5 - Final Version
3 languages: PT, EN, ES
Follows the final script exactly
Enhanced visuals, logos credits, Aedes albopictus mention
"""
import sys, os, math, subprocess, shutil
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FPS = 12
BG_COLOR = (255, 255, 255)

# Fonts
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"

# Colors
NAVY = (20, 30, 70)
ORANGE = (255, 120, 30)
RED = (220, 50, 50)
GREEN = (40, 160, 60)
BLUE = (50, 100, 200)
GOLD = (220, 180, 40)
GRAY = (120, 120, 120)
LIGHT_GRAY = (200, 200, 200)
DARK_GREEN = (30, 100, 40)
SKY_BLUE = (180, 220, 255)
BROWN = (139, 90, 43)

LANG = sys.argv[1] if len(sys.argv) > 1 else "pt"

# Titles per language
TITLES = {
    "pt": {
        1: 'O que é a dengue?',
        2: 'Sem nenhum controle',
        3: 'Controle individual',
        4: 'Controle coletivo',
        5: 'Controle ambiental',
        6: 'Condições que mudam tudo',
        7: 'Encerramento',
        "bitten": "Picados", "infected": "Infectados",
        "final_text": "Dengue: conhecer para prevenir.\nJá pensou também em pesquisar sobre outras\ndoenças como a malária, leishmaniose e Chagas?",
        "siw": "Science is Wonderful! 2026 — Bruxelas",
        "credits_title": "Créditos",
        "credits_text": "Equipe SiW 2026: Raquel Martins Lana (BSC), Andria Nicodemou (BSC)\ne Tatiana Docile (UERJ).\nBooth #18 - Health detectives: how diseases spread through insects.\nRoteiro e vídeo: Diego Ricardo Xavier (ICICT/Fiocruz).\n\nRML foi financiado pela União Europeia\n(Ações Marie Sklodowska-Curie, nº projeto 101109642).\nAgradecemos o apoio do projeto HARMONIZE\n(Wellcome Trust, nº projeto: 224694/Z/21/Z)\ne Conselho Nacional de Desenvolvimento Científico\ne Tecnológico (CNPq) (processo 445194/2024-3),\nObservatório de Clima e Saúde (Fiocruz),\ndo Laboratório de Informação em Saúde (LIS)\ndo ICICT/Fiocruz.",
        "refs_title": "Referências Científicas",
        "refs": "[1] Instituto Oswaldo Cruz (IOC/Fiocruz)\n[2] Centers for Disease Control and Prevention (CDC)\n[3] Guia de Vigilância em Saúde, Min. da Saúde do Brasil, 6ª ed.",
    },
    "en": {
        1: 'What is dengue?',
        2: 'No control measures',
        3: 'Individual control',
        4: 'Collective control',
        5: 'Environmental control',
        6: 'Conditions that change everything',
        7: 'Closing',
        "bitten": "Bitten", "infected": "Infected",
        "final_text": "Dengue: know to prevent.\nHave you also thought about researching other\ndiseases like malaria, leishmaniasis and Chagas?",
        "siw": "Science is Wonderful! 2026 — Brussels",
        "credits_title": "Credits",
        "credits_text": "SiW Team 2026: Raquel Martins Lana (BSC), Andria Nicodemou (BSC),\nand Tatiana Docile (UERJ).\nBooth #18 - Health detectives: how diseases spread through insects.\nScript and video: Diego Ricardo Xavier (ICICT/Fiocruz).\n\nRML was funded by the European Union\n(Marie Sklodowska-Curie Actions, grant agreement 101109642).\nWe acknowledge the support of the HARMONIZE project\n(Wellcome Trust award reference: 224694/Z/21/Z)\nand Conselho Nacional de Desenvolvimento Científico\ne Tecnológico (CNPq) (processo 445194/2024-3).",
        "refs_title": "Scientific References",
        "refs": "[1] Oswaldo Cruz Institute (IOC/Fiocruz)\n[2] Centers for Disease Control and Prevention (CDC)\n[3] Health Surveillance Guide, Min. of Health of Brazil, 6th ed.",
    },
    "es": {
        1: '¿Qué es el dengue?',
        2: 'Sin ningún control',
        3: 'Control individual',
        4: 'Control colectivo',
        5: 'Control ambiental',
        6: 'Condiciones que cambian todo',
        7: 'Cierre',
        "bitten": "Picados", "infected": "Infectados",
        "final_text": "Dengue: conocer para prevenir.\n¿Has pensado también en investigar otras\nenfermedades como la malaria, leishmaniasis y Chagas?",
        "siw": "Science is Wonderful! 2026 — Bruselas",
        "credits_title": "Créditos",
        "credits_text": "Equipo SiW 2026: Raquel Martins Lana (BSC), Andria Nicodemou (BSC)\ny Tatiana Docile (UERJ).\nBooth #18 - Health detectives: how diseases spread through insects.\nGuión y vídeo: Diego Ricardo Xavier (ICICT/Fiocruz).\n\nRML fue financiado por la Unión Europea\n(Acciones Marie Sklodowska-Curie, nº 101109642).\nAgradecemos el apoyo del proyecto HARMONIZE\n(Wellcome Trust, nº proyecto: 224694/Z/21/Z)\ny Conselho Nacional de Desenvolvimento Científico\ne Tecnológico (CNPq) (proceso 445194/2024-3),\nObservatório de Clima e Saúde (Fiocruz),\ndel Laboratório de Informação em Saúde (LIS)\ndel ICICT/Fiocruz.",
        "refs_title": "Referencias Científicas",
        "refs": "[1] Instituto Oswaldo Cruz (IOC/Fiocruz)\n[2] Centers for Disease Control and Prevention (CDC)\n[3] Guía de Vigilancia en Salud, Min. de Salud de Brasil, 6ª ed.",
    }
}

T = TITLES[LANG]

# Audio directories
AUDIO_DIR = f"/home/ubuntu/narration_v6_{LANG}"

def get_font(size, bold=False, italic=False):
    path = FONT_BOLD if bold else (FONT_ITALIC if italic else FONT_REG)
    return ImageFont.truetype(path, size)

def draw_stickman(draw, x, y, scale=1.0, color=(0,0,0), arms="down", legs="stand",
                  has_glasses=False, has_coat=False, has_thermometer=False,
                  has_repellent=False, has_long_clothes=False, has_shield=False,
                  face="normal", shield_color=GOLD):
    """Draw a detailed stickman with various accessories"""
    s = scale
    lw = max(2, int(3 * s))
    head_r = int(14 * s)
    
    # Head
    draw.ellipse([x - head_r, y - head_r, x + head_r, y + head_r], outline=color, width=lw)
    
    # Face
    eye_y = y - int(4*s)
    if face == "normal":
        draw.ellipse([x-int(6*s), eye_y-2, x-int(3*s), eye_y+2], fill=color)
        draw.ellipse([x+int(3*s), eye_y-2, x+int(6*s), eye_y+2], fill=color)
        draw.arc([x-int(5*s), y+int(1*s), x+int(5*s), y+int(8*s)], 0, 180, fill=color, width=max(1,int(1.5*s)))
    elif face == "sick":
        draw.ellipse([x-int(6*s), eye_y-2, x-int(3*s), eye_y+2], fill=RED)
        draw.ellipse([x+int(3*s), eye_y-2, x+int(6*s), eye_y+2], fill=RED)
        draw.arc([x-int(5*s), y+int(3*s), x+int(5*s), y+int(10*s)], 180, 360, fill=RED, width=max(1,int(1.5*s)))
    elif face == "happy":
        draw.ellipse([x-int(6*s), eye_y-3, x-int(3*s), eye_y+1], fill=color)
        draw.ellipse([x+int(3*s), eye_y-3, x+int(6*s), eye_y+1], fill=color)
        draw.arc([x-int(6*s), y, x+int(6*s), y+int(10*s)], 0, 180, fill=color, width=max(1,int(2*s)))
    
    # Glasses
    if has_glasses:
        draw.rectangle([x-int(9*s), eye_y-4, x-int(2*s), eye_y+4], outline=NAVY, width=max(1,int(1.5*s)))
        draw.rectangle([x+int(2*s), eye_y-4, x+int(9*s), eye_y+4], outline=NAVY, width=max(1,int(1.5*s)))
        draw.line([x-int(2*s), eye_y, x+int(2*s), eye_y], fill=NAVY, width=max(1,int(s)))
    
    # Body
    body_top = y + head_r
    body_bot = body_top + int(40 * s)
    
    if has_coat:
        # Lab coat
        coat_w = int(18*s)
        draw.polygon([
            (x-coat_w, body_top+int(5*s)), (x+coat_w, body_top+int(5*s)),
            (x+coat_w+int(3*s), body_bot+int(5*s)), (x-coat_w-int(3*s), body_bot+int(5*s))
        ], fill=(240,240,240), outline=GRAY, width=1)
        draw.line([x, body_top+int(5*s), x, body_bot+int(5*s)], fill=GRAY, width=1)
    
    if has_long_clothes:
        # Long sleeves and pants (blue tint)
        cloth_w = int(12*s)
        draw.polygon([
            (x-cloth_w, body_top+int(5*s)), (x+cloth_w, body_top+int(5*s)),
            (x+cloth_w, body_bot), (x-cloth_w, body_bot)
        ], fill=(180,200,230), outline=(100,130,180), width=1)
    
    draw.line([x, body_top, x, body_bot], fill=color, width=lw)
    
    # Arms
    arm_y = body_top + int(12 * s)
    arm_len = int(25 * s)
    if arms == "down":
        draw.line([x, arm_y, x - arm_len, arm_y + int(20*s)], fill=color, width=lw)
        draw.line([x, arm_y, x + arm_len, arm_y + int(20*s)], fill=color, width=lw)
    elif arms == "up":
        draw.line([x, arm_y, x - arm_len, arm_y - int(15*s)], fill=color, width=lw)
        draw.line([x, arm_y, x + arm_len, arm_y - int(15*s)], fill=color, width=lw)
    elif arms == "wave":
        draw.line([x, arm_y, x - arm_len, arm_y + int(20*s)], fill=color, width=lw)
        draw.line([x, arm_y, x + arm_len, arm_y - int(18*s)], fill=color, width=lw)
    elif arms == "hold_sign":
        draw.line([x, arm_y, x - int(30*s), arm_y - int(10*s)], fill=color, width=lw)
        draw.line([x, arm_y, x + int(30*s), arm_y - int(10*s)], fill=color, width=lw)
    
    # Legs
    leg_len = int(30 * s)
    if legs == "stand":
        draw.line([x, body_bot, x - int(15*s), body_bot + leg_len], fill=color, width=lw)
        draw.line([x, body_bot, x + int(15*s), body_bot + leg_len], fill=color, width=lw)
    elif legs == "walk":
        draw.line([x, body_bot, x - int(20*s), body_bot + leg_len], fill=color, width=lw)
        draw.line([x, body_bot, x + int(10*s), body_bot + leg_len], fill=color, width=lw)
    
    # Feet
    foot_y = body_bot + leg_len
    draw.line([x - int(15*s), foot_y, x - int(15*s) - int(8*s), foot_y], fill=color, width=lw)
    draw.line([x + int(15*s), foot_y, x + int(15*s) + int(8*s), foot_y], fill=color, width=lw)
    
    # Thermometer
    if has_thermometer:
        tx = x + int(12*s)
        ty = y - int(5*s)
        draw.rectangle([tx, ty, tx+int(4*s), ty+int(20*s)], fill=(240,240,240), outline=RED, width=1)
        draw.ellipse([tx-int(2*s), ty+int(18*s), tx+int(6*s), ty+int(26*s)], fill=RED)
    
    # Repellent glow
    if has_repellent:
        for r in range(3):
            rr = head_r + int((15 + r*8)*s)
            draw.ellipse([x-rr, y-rr+int(10*s), x+rr, y+rr+int(30*s)],
                        outline=(100,150,255,80), width=1)
    
    # Shield
    if has_shield:
        sx = x - int(25*s)
        sy = body_top + int(5*s)
        shield_pts = [
            (sx, sy), (sx+int(20*s), sy-int(5*s)),
            (sx+int(20*s), sy+int(25*s)), (sx+int(10*s), sy+int(35*s)),
            (sx, sy+int(25*s))
        ]
        draw.polygon(shield_pts, fill=shield_color, outline=(180,140,20), width=2)

def draw_mosquito(draw, x, y, scale=1.0, infected=False, frame=0):
    """Draw a detailed mosquito with animated wings"""
    s = scale
    lw = max(2, int(2*s))
    color = (0, 0, 0)
    
    # Body
    body_len = int(20*s)
    draw.ellipse([x-int(5*s), y-int(3*s), x+body_len, y+int(3*s)], fill=(40,40,40), outline=color, width=lw)
    
    # White stripes on body
    for i in range(3):
        sx = x + int((5 + i*6)*s)
        draw.line([sx, y-int(2*s), sx, y+int(2*s)], fill=(200,200,200), width=max(1,int(s)))
    
    # Head
    draw.ellipse([x-int(10*s), y-int(5*s), x, y+int(5*s)], fill=(30,30,30), outline=color, width=lw)
    
    # Proboscis
    draw.line([x-int(10*s), y, x-int(25*s), y+int(8*s)], fill=color, width=max(1,int(1.5*s)))
    
    # Wings (animated)
    wing_angle = math.sin(frame * 0.8) * 15
    wing_y_off = int(wing_angle * s * 0.5)
    # Left wing
    draw.polygon([
        (x+int(3*s), y-int(2*s)),
        (x-int(5*s), y-int(18*s)+wing_y_off),
        (x+int(12*s), y-int(15*s)+wing_y_off),
    ], fill=(200,200,200,100), outline=(150,150,150), width=1)
    # Right wing
    draw.polygon([
        (x+int(3*s), y+int(2*s)),
        (x-int(5*s), y+int(18*s)-wing_y_off),
        (x+int(12*s), y+int(15*s)-wing_y_off),
    ], fill=(200,200,200,100), outline=(150,150,150), width=1)
    
    # Legs (6 legs)
    for i in range(3):
        lx = x + int((2 + i*5)*s)
        draw.line([lx, y+int(3*s), lx-int(8*s), y+int(15*s)], fill=color, width=max(1,int(s)))
        draw.line([lx, y-int(3*s), lx-int(8*s), y-int(15*s)], fill=color, width=max(1,int(s)))
    
    # Infected glow
    if infected:
        glow_r = int(25*s) + int(math.sin(frame*0.3)*5*s)
        for r in range(3):
            draw.ellipse([x-glow_r-r*3, y-glow_r-r*3, x+glow_r+r*3, y+glow_r+r*3],
                        outline=(255,50,50,60), width=2)

def draw_house(draw, x, y, w, h, roof_color=(180,60,60), wall_color=(240,235,220)):
    """Draw a detailed house"""
    # Wall
    draw.rectangle([x, y, x+w, y+h], fill=wall_color, outline=(100,100,100), width=2)
    
    # Roof
    roof_h = int(h*0.4)
    draw.polygon([(x-int(w*0.1), y), (x+w+int(w*0.1), y), (x+w//2, y-roof_h)],
                fill=roof_color, outline=(80,40,40), width=2)
    
    # Door
    dw, dh = w//4, h//2
    dx = x + w//2 - dw//2
    dy = y + h - dh
    draw.rectangle([dx, dy, dx+dw, dy+dh], fill=BROWN, outline=(60,30,10), width=2)
    draw.ellipse([dx+dw-8, dy+dh//2-2, dx+dw-4, dy+dh//2+2], fill=GOLD)
    
    # Windows
    ww, wh = w//5, h//4
    for wx_off in [x+w//6, x+w-w//6-ww]:
        wy = y + h//5
        draw.rectangle([wx_off, wy, wx_off+ww, wy+wh], fill=(180,220,255), outline=(80,80,80), width=2)
        draw.line([wx_off+ww//2, wy, wx_off+ww//2, wy+wh], fill=(80,80,80), width=1)
        draw.line([wx_off, wy+wh//2, wx_off+ww, wy+wh//2], fill=(80,80,80), width=1)
    
    # Chimney
    cx = x + w - w//4
    draw.rectangle([cx, y-roof_h+int(roof_h*0.3), cx+int(w*0.12), y], fill=(150,80,60), outline=(80,40,30), width=1)

def draw_ground(draw, y_start):
    """Draw textured ground with grass"""
    draw.rectangle([0, y_start, W, H], fill=(200, 230, 180))
    # Grass tufts
    import random
    random.seed(123)
    for i in range(60):
        gx = random.randint(0, W)
        gy = random.randint(y_start, y_start+15)
        for j in range(3):
            draw.line([gx+j*3, gy, gx+j*3-2, gy-random.randint(5,12)], fill=DARK_GREEN, width=1)

def draw_sky(draw):
    """Draw gradient sky"""
    for yy in range(0, 200):
        ratio = yy / 200
        r = int(135 + (255-135)*ratio)
        g = int(190 + (255-190)*ratio)
        b = int(255)
        draw.line([(0, yy), (W, yy)], fill=(r, g, b))

def draw_title_bar(draw, text, scene_num, color=NAVY):
    """Draw a title bar at the top"""
    bar_h = 55
    draw.rectangle([0, 0, W, bar_h], fill=color)
    # Accent line
    draw.rectangle([0, bar_h, W, bar_h+4], fill=ORANGE)
    font = get_font(26, bold=True)
    full_text = text
    bbox = draw.textbbox((0,0), full_text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((W-tw)//2, 12), full_text, fill=(255,255,255), font=font)

def draw_counter(draw, bitten, infected, total=8):
    """Draw counter box in bottom-right"""
    bx, by = W-260, H-75
    bw, bh = 245, 60
    draw.rounded_rectangle([bx, by, bx+bw, by+bh], radius=10, fill=(255,255,255), outline=NAVY, width=2)
    
    font_s = get_font(14, bold=True)
    font_n = get_font(20, bold=True)
    
    # Bitten
    draw.text((bx+10, by+5), T["bitten"], fill=ORANGE, font=font_s)
    draw.text((bx+10, by+22), f"{bitten}/{total}", fill=ORANGE, font=font_n)
    # Bar
    bar_x, bar_y = bx+70, by+28
    bar_w = 40
    draw.rectangle([bar_x, bar_y, bar_x+bar_w, bar_y+12], fill=LIGHT_GRAY, outline=GRAY, width=1)
    fill_w = int(bar_w * bitten / total)
    if fill_w > 0:
        draw.rectangle([bar_x, bar_y, bar_x+fill_w, bar_y+12], fill=ORANGE)
    
    # Infected
    draw.text((bx+125, by+5), T["infected"], fill=RED, font=font_s)
    draw.text((bx+125, by+22), f"{infected}/{total}", fill=RED, font=font_n)
    bar_x2 = bx+195
    draw.rectangle([bar_x2, bar_y, bar_x2+bar_w, bar_y+12], fill=LIGHT_GRAY, outline=GRAY, width=1)
    fill_w2 = int(bar_w * infected / total)
    if fill_w2 > 0:
        draw.rectangle([bar_x2, bar_y, bar_x2+fill_w2, bar_y+12], fill=RED)

def draw_emoji_text(draw, x, y, text, size=30):
    """Draw emoji-like text using font"""
    font = get_font(size)
    draw.text((x, y), text, fill=(0,0,0), font=font)

def draw_water_container(draw, x, y, w, h, has_water=True):
    """Draw a water container (tire, can, etc)"""
    draw.ellipse([x, y, x+w, y+h], fill=(80,80,80), outline=(40,40,40), width=2)
    if has_water:
        draw.ellipse([x+4, y+h//3, x+w-4, y+h-4], fill=(100,160,220), outline=(60,120,180), width=1)

def create_scene_frames(scene_num, duration_s, frame_func):
    """Generate frames for a scene and save to disk"""
    n_frames = int(duration_s * FPS)
    frames = []
    for i in range(n_frames):
        progress = i / max(1, n_frames - 1)
        img = Image.new("RGB", (W, H), BG_COLOR)
        draw = ImageDraw.Draw(img)
        frame_func(draw, img, i, progress, n_frames)
        frames.append(img)
    return frames

# ========== SCENE FUNCTIONS ==========

def scene1_func(draw, img, frame, progress, total):
    """Scene 1: What is dengue? - Life cycle of Aedes aegypti"""
    draw_title_bar(draw, T[1], 1)
    
    # Narrator stickman on left
    nx = 120
    ny = 300
    alpha = min(1.0, progress * 4) if progress < 0.25 else 1.0
    if alpha > 0.3:
        draw_stickman(draw, nx, ny, scale=1.2, has_glasses=True, has_coat=True, arms="wave", face="happy")
    
    # Life cycle stages appearing sequentially
    stages_x = [350, 530, 710, 890, 1070]
    stage_labels_pt = ["Ovo", "Larva", "Pupa", "Adulto", "Voa!"]
    stage_labels_en = ["Egg", "Larva", "Pupa", "Adult", "Flies!"]
    stage_labels_es = ["Huevo", "Larva", "Pupa", "Adulto", "¡Vuela!"]
    stage_labels = stage_labels_pt if LANG == "pt" else (stage_labels_en if LANG == "en" else stage_labels_es)
    stage_colors = [(139,90,43), (100,160,60), (80,130,80), (40,40,40), (40,40,40)]
    
    font_stage = get_font(16, bold=True)
    
    for idx, sx in enumerate(stages_x):
        appear_at = 0.15 + idx * 0.15
        if progress >= appear_at:
            local_p = min(1.0, (progress - appear_at) / 0.1)
            sy = 280
            
            # Draw stage circle
            r = int(30 * local_p)
            draw.ellipse([sx-r, sy-r, sx+r, sy+r], fill=stage_colors[idx], outline=(0,0,0), width=2)
            
            if idx == 0:  # Egg
                draw.ellipse([sx-8, sy-12, sx+8, sy+12], fill=(200,180,140), outline=(139,90,43), width=2)
            elif idx == 1:  # Larva
                pts = [(sx-15, sy), (sx-5, sy-8), (sx+5, sy+5), (sx+15, sy-3)]
                draw.line(pts, fill=(80,140,40), width=3)
            elif idx == 2:  # Pupa
                draw.ellipse([sx-10, sy-8, sx+5, sy+8], fill=(60,110,60), outline=(40,80,40), width=2)
                draw.arc([sx-5, sy-15, sx+10, sy-2], 180, 360, fill=(60,110,60), width=2)
            elif idx == 3:  # Adult mosquito
                draw_mosquito(draw, sx, sy, scale=1.2, frame=frame)
            elif idx == 4:  # Flying
                fly_y = sy + int(math.sin(frame*0.3)*15)
                draw_mosquito(draw, sx, fly_y, scale=1.0, frame=frame)
            
            # Label
            if local_p > 0.5:
                label = stage_labels[idx]
                bbox = draw.textbbox((0,0), label, font=font_stage)
                lw = bbox[2]-bbox[0]
                draw.text((sx-lw//2, sy+40), label, fill=NAVY, font=font_stage)
            
            # Arrow to next
            if idx < len(stages_x)-1 and progress >= appear_at + 0.1:
                ax = sx + 40
                draw.line([ax, sy, ax+30, sy], fill=ORANGE, width=3)
                draw.polygon([(ax+30, sy-6), (ax+40, sy), (ax+30, sy+6)], fill=ORANGE)
    
    # Water container at bottom
    if progress > 0.3:
        draw_water_container(draw, 400, 450, 60, 40, has_water=True)
        draw_water_container(draw, 600, 460, 50, 35, has_water=True)
        font_sm = get_font(13, italic=True)
        water_label = "Água parada" if LANG == "pt" else ("Standing water" if LANG == "en" else "Agua estancada")
        draw.text((470, 470), water_label, fill=BLUE, font=font_sm)
    
    # "7-10 dias" label
    if progress > 0.5:
        font_days = get_font(18, bold=True)
        days_text = "7-10 dias" if LANG == "pt" else ("7-10 days" if LANG == "en" else "7-10 días")
        draw.rounded_rectangle([480, 370, 700, 400], radius=8, fill=ORANGE, outline=None)
        bbox = draw.textbbox((0,0), days_text, font=font_days)
        tw = bbox[2]-bbox[0]
        draw.text((590-tw//2, 374), days_text, fill=(255,255,255), font=font_days)

def scene2_func(draw, img, frame, progress, total):
    """Scene 2: No control - dengue spreads freely"""
    draw_sky(draw)
    draw_ground(draw, 520)
    draw_title_bar(draw, T[2], 2)
    
    # Houses in background
    draw_house(draw, 50, 380, 120, 130, roof_color=(180,60,60))
    draw_house(draw, 220, 390, 110, 120, roof_color=(60,100,160))
    draw_house(draw, 900, 385, 115, 125, roof_color=(60,140,80))
    draw_house(draw, 1080, 395, 100, 115, roof_color=(160,120,60))
    
    # Water containers and trash
    draw_water_container(draw, 380, 490, 40, 25, has_water=True)
    draw_water_container(draw, 550, 495, 35, 22, has_water=True)
    draw_water_container(draw, 750, 488, 45, 28, has_water=True)
    
    # 8 stickman residents
    positions = [(420, 380), (490, 390), (560, 385), (630, 395),
                 (700, 380), (770, 390), (840, 385), (910, 395)]
    
    sick_indices = [0, 1, 2, 4, 5, 7]  # 6 out of 8 get infected
    
    for idx, (px, py) in enumerate(positions):
        is_sick = idx in sick_indices and progress > 0.6
        f = "sick" if is_sick else "normal"
        draw_stickman(draw, px, py, scale=0.8, face=f,
                     has_thermometer=is_sick)
        if is_sick:
            # Symptom icons above head
            font_sym = get_font(14)
            draw.text((px-15, py-50), "🤒", font=font_sym, fill=RED)
    
    # 3 mosquitoes flying around
    for mi in range(3):
        mx = 400 + int(math.sin(frame*0.15 + mi*2.1) * 250)
        my = 300 + int(math.cos(frame*0.12 + mi*1.7) * 80)
        is_inf = (mi == 0)
        draw_mosquito(draw, mx, my, scale=1.0, infected=is_inf, frame=frame)
    
    # Colored tokens being distributed
    if progress > 0.3 and progress < 0.6:
        for idx, (px, py) in enumerate(positions):
            if idx in sick_indices:
                token_y = py - 30 - int((progress-0.3)/0.3 * 20)
                draw.ellipse([px-6, token_y-6, px+6, token_y+6], fill=RED, outline=(180,30,30), width=1)
    
    # Counter
    if progress > 0.5:
        bitten = 8
        infected = min(6, int((progress-0.5)/0.4 * 6) + 1) if progress < 0.9 else 6
        draw_counter(draw, bitten, infected)

def scene3_func(draw, img, frame, progress, total):
    """Scene 3: Individual control"""
    draw_sky(draw)
    draw_ground(draw, 520)
    draw_title_bar(draw, T[3], 3)
    
    # Houses
    draw_house(draw, 80, 385, 110, 125, roof_color=(100,140,180))
    draw_house(draw, 1050, 390, 120, 120, roof_color=(140,100,60))
    
    # 8 stickman residents - 3 protected, 5 not
    positions = [(350, 380), (430, 390), (510, 385), (590, 395),
                 (670, 380), (750, 390), (830, 385), (910, 395)]
    
    protected = [0, 1, 2]  # 3 with individual protection
    sick_unprotected = [4, 6, 7]  # 3 of 5 unprotected get sick
    
    for idx, (px, py) in enumerate(positions):
        is_protected = idx in protected
        is_sick = idx in sick_unprotected and progress > 0.6
        
        draw_stickman(draw, px, py, scale=0.8,
                     has_repellent=is_protected,
                     has_long_clothes=is_protected,
                     face="sick" if is_sick else ("happy" if is_protected else "normal"),
                     has_thermometer=is_sick)
        
        # Protection icons
        if is_protected and progress > 0.2:
            font_icon = get_font(16)
            # Blue glow around protected
            for r in range(2):
                rr = 35 + r*8
                draw.ellipse([px-rr, py-rr+10, px+rr, py+rr+40],
                            outline=(100,150,255), width=1)
    
    # Mosquitoes bouncing off protected ones
    for mi in range(3):
        mx = 350 + int(math.sin(frame*0.2 + mi*2) * 300)
        my = 300 + int(math.cos(frame*0.15 + mi*1.5) * 60)
        draw_mosquito(draw, mx, my, scale=0.9, infected=(mi==0), frame=frame)
        
        # "Boing" effect when near protected
        if progress > 0.4:
            for pidx in protected:
                ppx = positions[pidx][0]
                if abs(mx - ppx) < 40:
                    font_b = get_font(14, bold=True)
                    draw.text((mx-10, my-25), "✕", fill=BLUE, font=font_b)
    
    # Speech bubbles for protection items
    if progress > 0.1 and progress < 0.4:
        font_bubble = get_font(12)
        items = ["🧴", "👕", "🛏️"]
        for i, pidx in enumerate(protected):
            bx = positions[pidx][0] - 15
            by = positions[pidx][1] - 70
            draw.rounded_rectangle([bx-5, by-5, bx+30, by+22], radius=5, fill=(255,255,255), outline=GRAY, width=1)
            draw.text((bx, by), items[i], font=font_bubble)
    
    if progress > 0.5:
        draw_counter(draw, 5, 3)

def scene4_func(draw, img, frame, progress, total):
    """Scene 4: Collective control - vaccination + fumigation"""
    draw_sky(draw)
    draw_ground(draw, 520)
    draw_title_bar(draw, T[4], 4)
    
    # Vaccination post
    draw.rectangle([100, 420, 280, 510], fill=(240,240,240), outline=GRAY, width=2)
    font_vac = get_font(14, bold=True)
    vac_label = "Vacinação" if LANG == "pt" else ("Vaccination" if LANG == "en" else "Vacunación")
    draw.text((120, 425), vac_label, fill=RED, font=font_vac)
    # Syringe icon
    draw.rectangle([200, 440, 260, 448], fill=(200,200,200), outline=GRAY, width=1)
    draw.polygon([(260, 440), (275, 444), (260, 448)], fill=GRAY)
    
    # Nurse stickman
    draw_stickman(draw, 190, 360, scale=0.9, has_coat=True, arms="wave", face="happy")
    
    # Residents in line getting vaccinated
    positions = [(340, 385), (410, 390), (480, 385), (550, 395),
                 (620, 385), (690, 390), (760, 385), (830, 395)]
    
    vaccinated = [0, 1, 2, 3, 4]  # 5 vaccinated
    sick_idx = [7]  # Only 1 gets infected
    
    for idx, (px, py) in enumerate(positions):
        is_vacc = idx in vaccinated
        is_sick = idx in sick_idx and progress > 0.7
        
        draw_stickman(draw, px, py, scale=0.75,
                     has_shield=is_vacc and progress > 0.3,
                     shield_color=GOLD,
                     face="sick" if is_sick else ("happy" if is_vacc else "normal"),
                     has_thermometer=is_sick)
    
    # Fumigation truck in background
    if progress > 0.4:
        truck_x = int(900 + (1-progress)*200)
        # Truck body
        draw.rectangle([truck_x, 430, truck_x+100, 510], fill=(80,120,80), outline=(40,60,40), width=2)
        draw.rectangle([truck_x+100, 450, truck_x+140, 510], fill=(60,100,60), outline=(40,60,40), width=2)
        # Wheels
        draw.ellipse([truck_x+15, 505, truck_x+35, 525], fill=(40,40,40), outline=(0,0,0), width=2)
        draw.ellipse([truck_x+75, 505, truck_x+95, 525], fill=(40,40,40), outline=(0,0,0), width=2)
        # Smoke/fumigation
        for si in range(5):
            sx = truck_x - 20 - si*25
            sy = 440 + int(math.sin(frame*0.3+si)*10)
            sr = 12 + si*5
            draw.ellipse([sx-sr, sy-sr, sx+sr, sy+sr], fill=(200,200,200), outline=(180,180,180), width=1)
    
    # Mosquitoes (fewer, 2 remaining)
    if progress > 0.5:
        for mi in range(2):
            mx = 500 + int(math.sin(frame*0.2+mi*3)*200)
            my = 280 + int(math.cos(frame*0.15+mi*2)*50)
            draw_mosquito(draw, mx, my, scale=0.8, infected=(mi==0), frame=frame)
    
    if progress > 0.5:
        draw_counter(draw, 4, 1)

def scene5_func(draw, img, frame, progress, total):
    """Scene 5: Environmental control - cleanup"""
    draw_sky(draw)
    draw_ground(draw, 520)
    draw_title_bar(draw, T[5], 5)
    
    # Clean plaza with flowers
    if progress > 0.5:
        # Flowers
        flower_positions = [(200,510), (400,515), (600,508), (800,512), (1000,510)]
        for fx, fy in flower_positions:
            # Stem
            draw.line([fx, fy, fx, fy-20], fill=GREEN, width=2)
            # Petals
            for angle in range(0, 360, 72):
                px2 = fx + int(8*math.cos(math.radians(angle)))
                py2 = fy - 20 + int(8*math.sin(math.radians(angle)))
                draw.ellipse([px2-4, py2-4, px2+4, py2+4], fill=(255,100,150))
            draw.ellipse([fx-3, fy-23, fx+3, fy-17], fill=(255,200,50))
    
    # Houses (clean)
    draw_house(draw, 50, 380, 120, 130, roof_color=(100,160,100))
    draw_house(draw, 1080, 385, 110, 125, roof_color=(100,130,180))
    
    # Stickmen cleaning (early) or celebrating (late)
    positions = [(300, 380), (420, 390), (540, 385), (660, 395),
                 (780, 380), (900, 390), (350, 420), (700, 420)]
    
    for idx, (px, py) in enumerate(positions):
        if progress < 0.5:
            # Cleaning phase
            draw_stickman(draw, px, py, scale=0.75, arms="up" if idx%2==0 else "wave", face="normal")
            # Cleaning items
            if idx % 3 == 0:
                draw.rectangle([px+20, py+10, px+35, py+50], fill=(100,100,100), outline=(60,60,60), width=1)
        else:
            # Celebrating
            draw_stickman(draw, px, py, scale=0.75, arms="up", face="happy")
    
    # Trash disappearing
    if progress < 0.4:
        trash_alpha = 1.0 - progress/0.4
        n_trash = max(0, int(5 * trash_alpha))
        trash_positions = [(350, 490), (500, 495), (650, 488), (800, 492), (950, 490)]
        for i in range(n_trash):
            tx, ty = trash_positions[i]
            draw_water_container(draw, tx, ty, 30, 20, has_water=True)
    
    # Mosquitoes disappearing
    if progress < 0.6:
        n_mosq = max(0, int(3 * (1 - progress/0.6)))
        for mi in range(n_mosq):
            mx = 400 + mi * 200
            my = 300 + int(math.sin(frame*0.2)*20)
            draw_mosquito(draw, mx, my, scale=0.7*(1-progress/0.6), frame=frame)
    
    # Last mosquito confused and leaving
    if progress > 0.5 and progress < 0.8:
        leave_p = (progress - 0.5) / 0.3
        mx = 640 + int(leave_p * 400)
        my = 280 - int(leave_p * 100)
        draw_mosquito(draw, mx, my, scale=0.6, frame=frame)
        font_q = get_font(18, bold=True)
        draw.text((mx-10, my-30), "?", fill=GRAY, font=font_q)
    
    if progress > 0.5:
        draw_counter(draw, 1, 0)

def scene6_func(draw, img, frame, progress, total):
    """Scene 6: Environmental conditions - 4 quadrants"""
    draw_title_bar(draw, T[6], 6)
    
    mid_x, mid_y = W//2, (H+60)//2 + 10
    
    # Dividing lines
    draw.line([(mid_x, 60), (mid_x, H)], fill=NAVY, width=3)
    draw.line([(0, mid_y), (W, mid_y)], fill=NAVY, width=3)
    
    font_label = get_font(14, bold=True)
    
    # Quadrant 1: Rainy season (top-left) - +1 mosquito
    q1_labels = {"pt": "Estação chuvosa", "en": "Rainy season", "es": "Estación lluviosa"}
    draw.text((20, 70), q1_labels[LANG], fill=BLUE, font=font_label)
    # Rain
    for ri in range(15):
        rx = 50 + ri * 38
        ry = 120 + (frame * 5 + ri * 17) % 200
        if rx < mid_x - 10:
            draw.line([rx, ry, rx-2, ry+10], fill=BLUE, width=2)
    # Puddles
    draw.ellipse([80, 320, 160, 345], fill=(100,160,220), outline=BLUE, width=1)
    draw.ellipse([250, 330, 340, 350], fill=(100,160,220), outline=BLUE, width=1)
    # Mosquito appearing
    if progress > 0.3:
        draw_mosquito(draw, 200, 250, scale=1.0, frame=frame)
        font_plus = get_font(20, bold=True)
        draw.text((230, 240), "+1", fill=RED, font=font_plus)
    
    # Quadrant 2: Accumulated trash (top-right) - +1 mosquito
    q2_labels = {"pt": "Lixo acumulado", "en": "Accumulated trash", "es": "Basura acumulada"}
    draw.text((mid_x+20, 70), q2_labels[LANG], fill=BROWN, font=font_label)
    # Trash pile
    trash_colors = [(120,120,120), (100,80,60), (80,100,80), (140,100,80)]
    for ti in range(6):
        tx = mid_x + 100 + ti*40
        ty = 300 - ti%3 * 20
        if tx < W - 30:
            draw.rectangle([tx, ty, tx+35, ty+40], fill=trash_colors[ti%4], outline=(60,60,60), width=1)
    if progress > 0.4:
        draw_mosquito(draw, mid_x+250, 230, scale=1.0, frame=frame)
        font_plus = get_font(20, bold=True)
        draw.text((mid_x+280, 220), "+1", fill=RED, font=font_plus)
    
    # Quadrant 3: Cleanup (bottom-left) - -1 mosquito
    q3_labels = {"pt": "Mutirão de limpeza", "en": "Cleanup effort", "es": "Jornada de limpieza"}
    draw.text((20, mid_y+10), q3_labels[LANG], fill=GREEN, font=font_label)
    # Clean area with stickmen working
    draw_stickman(draw, 120, mid_y+80, scale=0.6, arms="up", face="happy")
    draw_stickman(draw, 250, mid_y+85, scale=0.6, arms="wave", face="happy")
    draw_stickman(draw, 380, mid_y+80, scale=0.6, arms="up", face="happy")
    if progress > 0.5:
        font_minus = get_font(20, bold=True)
        draw.text((300, mid_y+60), "-1 🦟", fill=GREEN, font=font_minus)
    
    # Quadrant 4: Dense urban area (bottom-right) - mosquitoes bite more easily
    q4_labels = {"pt": "Área urbana densa", "en": "Dense urban area", "es": "Área urbana densa"}
    draw.text((mid_x+20, mid_y+10), q4_labels[LANG], fill=GRAY, font=font_label)
    # Crowded stickmen
    for ci in range(6):
        cx = mid_x + 80 + ci * 55
        cy = mid_y + 90
        if cx < W - 40:
            draw_stickman(draw, cx, cy, scale=0.5, face="normal")
    # Buildings
    for bi in range(3):
        bx = mid_x + 50 + bi * 150
        if bx < W - 80:
            draw.rectangle([bx, mid_y+40, bx+60, mid_y+130], fill=(180,180,180), outline=(120,120,120), width=1)
            for wy in range(3):
                for wx in range(2):
                    draw.rectangle([bx+10+wx*30, mid_y+50+wy*25, bx+25+wx*30, mid_y+65+wy*25],
                                  fill=(180,220,255), outline=(120,120,120), width=1)
    if progress > 0.6:
        draw_mosquito(draw, mid_x+300, mid_y+70, scale=0.8, frame=frame)
        draw_mosquito(draw, mid_x+180, mid_y+65, scale=0.7, frame=frame)

def scene7_func(draw, img, frame, progress, total):
    """Scene 7: Closing - circle of stickmen, call to action"""
    # White background
    
    if progress < 0.5:
        # Circle of stickmen holding hands
        center_x, center_y = W//2, 320
        radius = 160
        n_people = 8
        for i in range(n_people):
            angle = (2 * math.pi * i / n_people) - math.pi/2
            px = center_x + int(radius * math.cos(angle))
            py = center_y + int(radius * math.sin(angle))
            draw_stickman(draw, px, py, scale=0.6, arms="up", face="happy")
        
        # Lines connecting them (holding hands)
        for i in range(n_people):
            a1 = (2 * math.pi * i / n_people) - math.pi/2
            a2 = (2 * math.pi * ((i+1)%n_people) / n_people) - math.pi/2
            x1 = center_x + int((radius-20) * math.cos(a1))
            y1 = center_y + int((radius-20) * math.sin(a1))
            x2 = center_x + int((radius-20) * math.cos(a2))
            y2 = center_y + int((radius-20) * math.sin(a2))
            draw.line([x1, y1+20, x2, y2+20], fill=ORANGE, width=2)
        
        # Defeated mosquito outside
        mx = center_x + radius + 80
        my = center_y + 50
        draw_mosquito(draw, mx, my, scale=0.5, frame=frame)
        # X over mosquito
        draw.line([mx-15, my-15, mx+15, my+15], fill=RED, width=3)
        draw.line([mx-15, my+15, mx+15, my-15], fill=RED, width=3)
        
        # Narrator with sign
        draw_stickman(draw, center_x, center_y, scale=0.8, has_glasses=True, has_coat=True, arms="hold_sign", face="happy")
        
        # Sign
        sign_text_map = {
            "pt": "A dengue pode ser\nprevenida!",
            "en": "Dengue can be\nprevented!",
            "es": "¡El dengue se puede\nprevenir!"
        }
        font_sign = get_font(16, bold=True)
        sign_text = sign_text_map[LANG]
        draw.rounded_rectangle([center_x-80, center_y-120, center_x+80, center_y-70], radius=8, fill=(255,255,220), outline=ORANGE, width=2)
        draw.multiline_text((center_x-70, center_y-115), sign_text, fill=NAVY, font=font_sign, align="center")
    
    else:
        # Final text fade in
        fade = min(1.0, (progress - 0.5) / 0.2)
        
        font_final = get_font(24, bold=True)
        font_siw = get_font(20, italic=True)
        
        # Final message
        final_text = T["final_text"]
        lines = final_text.split("\n")
        y_start = 200
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0,0), line, font=font_final)
            tw = bbox[2]-bbox[0]
            color_val = int(255 * (1-fade))
            text_color = (color_val, color_val, max(0, color_val-50))
            draw.text(((W-tw)//2, y_start + i*35), line, fill=NAVY, font=font_final)
        
        # SiW label
        siw_text = T["siw"]
        bbox = draw.textbbox((0,0), siw_text, font=font_siw)
        tw = bbox[2]-bbox[0]
        draw.text(((W-tw)//2, 450), siw_text, fill=ORANGE, font=font_siw)

def scene_credits_func(draw, img, frame, progress, total):
    """Credits scene with logos and funding text"""
    # Background
    draw.rectangle([0, 0, W, H], fill=(255,255,255))
    
    # Title
    font_title = get_font(20, bold=True)
    title = T["credits_title"]
    bbox = draw.textbbox((0,0), title, font=font_title)
    tw = bbox[2]-bbox[0]
    draw.text(((W-tw)//2, 8), title, fill=NAVY, font=font_title)
    draw.rectangle([W//2-50, 32, W//2+50, 35], fill=ORANGE)
    
    # Credits text - compact at top
    font_credits = get_font(10)
    credits_text = T["credits_text"]
    draw.multiline_text((30, 42), credits_text, fill=(40,40,40), font=font_credits, spacing=2)
    
    # Logos image - new image, centered and prominent
    try:
        logos_img = Image.open("/home/ubuntu/logos_new.png")
        # Convert RGBA to RGB with white background
        if logos_img.mode == 'RGBA':
            bg = Image.new('RGB', logos_img.size, (255,255,255))
            bg.paste(logos_img, mask=logos_img.split()[3])
            logos_img = bg
        # Resize to fit nicely centered in bottom portion
        logo_max_w = 900
        logo_max_h = 380
        logos_img.thumbnail((logo_max_w, logo_max_h), Image.LANCZOS)
        lw_img, lh_img = logos_img.size
        paste_x = (W - lw_img) // 2
        paste_y = H - lh_img - 15
        img.paste(logos_img, (paste_x, paste_y))
    except Exception as e:
        print(f"Warning: Could not load logos: {e}")
    
    # References - small at very bottom
    font_ref = get_font(8)
    refs_title = T["refs_title"]
    draw.text((15, H-45), refs_title, fill=NAVY, font=get_font(9, bold=True))
    draw.multiline_text((15, H-33), T["refs"], fill=GRAY, font=font_ref, spacing=1)

def main():
    lang = LANG.upper()
    print(f"=== Dengue Stickman Animation V5 ===")
    print(f"--- {lang} version ---")
    
    # Get audio durations
    from pydub import AudioSegment
    
    scene_audios = []
    total_dur = 0
    for i in range(1, 8):
        audio_path = os.path.join(AUDIO_DIR, f"cena{i}.mp3")
        audio = AudioSegment.from_mp3(audio_path)
        dur = len(audio) / 1000.0
        # Add padding
        dur += 2.0  # 2s padding per scene
        scene_audios.append((audio_path, dur, audio))
        total_dur += dur
    
    # Credits scene: 10 seconds
    credits_dur = 10.0
    total_dur += credits_dur
    
    print(f"  Total duration: {total_dur:.1f}s, ~{int(total_dur*FPS)} frames")
    
    # Create frame directory
    frame_dir = f"/home/ubuntu/{LANG}_frames_v6"
    if os.path.exists(frame_dir):
        shutil.rmtree(frame_dir)
    os.makedirs(frame_dir)
    
    scene_funcs = [scene1_func, scene2_func, scene3_func, scene4_func,
                   scene5_func, scene6_func, scene7_func, scene_credits_func]
    scene_durs = [d for _, d, _ in scene_audios] + [credits_dur]
    
    frame_idx = 0
    for si, (func, dur) in enumerate(zip(scene_funcs, scene_durs)):
        scene_label = f"Scene {si+1}" if si < 7 else "Credits"
        print(f"  [{lang}] {scene_label} ({dur:.1f}s)...")
        n_frames = int(dur * FPS)
        
        # Fade in/out frames
        fade_frames = int(0.5 * FPS)  # 0.5s fade
        
        for fi in range(n_frames):
            progress = fi / max(1, n_frames - 1)
            img = Image.new("RGB", (W, H), BG_COLOR)
            draw = ImageDraw.Draw(img)
            func(draw, img, fi, progress, n_frames)
            
            # Fade in
            if fi < fade_frames:
                alpha = fi / fade_frames
                overlay = Image.new("RGB", (W, H), BG_COLOR)
                img = Image.blend(overlay, img, alpha)
            # Fade out
            elif fi > n_frames - fade_frames:
                alpha = (n_frames - fi) / fade_frames
                overlay = Image.new("RGB", (W, H), BG_COLOR)
                img = Image.blend(overlay, img, alpha)
            
            img.save(os.path.join(frame_dir, f"frame_{frame_idx:05d}.png"))
            frame_idx += 1
    
    print(f"  Total frames: {frame_idx}")
    
    # Combine audio
    print(f"  Combining audio...")
    combined_audio = AudioSegment.silent(duration=0)
    for audio_path, dur, audio in scene_audios:
        # Pad audio to match scene duration
        padding = int(dur * 1000) - len(audio)
        if padding > 0:
            audio = audio + AudioSegment.silent(duration=padding)
        else:
            audio = audio[:int(dur*1000)]
        combined_audio += audio
    
    # Credits: silence
    combined_audio += AudioSegment.silent(duration=int(credits_dur * 1000))
    
    # Add background music
    bg_music = AudioSegment.from_wav("/home/ubuntu/bg_music.wav")
    bg_music = bg_music[:len(combined_audio)]
    bg_music = bg_music.apply_gain(-15)  # Make it quieter
    
    final_audio = combined_audio.overlay(bg_music)
    
    audio_out = f"/home/ubuntu/{LANG}_audio_v6.wav"
    final_audio.export(audio_out, format="wav")
    
    # Encode video
    output = f"/home/ubuntu/dengue_stickman_v6_{lang}.mp4"
    print(f"  Encoding video...")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", os.path.join(frame_dir, "frame_%05d.png"),
        "-i", audio_out,
        "-c:v", "libx264", "-preset", "ultrafast", "-tune", "stillimage",
        "-crf", "23", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        output
    ]
    subprocess.run(cmd, check=True)
    
    # Cleanup
    shutil.rmtree(frame_dir)
    os.remove(audio_out)
    
    print(f"  Done: {output}")
    print("=== All done! ===")

if __name__ == "__main__":
    main()

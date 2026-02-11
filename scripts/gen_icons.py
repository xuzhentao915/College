#!/usr/bin/env python3
"""
Refined Icon Generator v2.0 - Modern Linear Style
生成更具高级感的 TabBar 图标
"""
import struct, zlib, math, os

SIZE = 81
GRAY = (148, 163, 184, 255)   # #94A3B8 (Slate 400)
BLUE = (59, 130, 246, 255)    # #3B82F6 (Primary)
TRANSPARENT = (0, 0, 0, 0)

def create_png(width, height, pixels):
    sig = b'\x89PNG\r\n\x1a\n'
    def chunk(ctype, data):
        return struct.pack('>I', len(data)) + ctype + data + struct.pack('>I', zlib.crc32(ctype + data) & 0xFFFFFFFF)
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0))
    raw = b''
    for y in range(height):
        raw += b'\x00' + b''.join(bytes(p) for p in pixels[y])
    idat = chunk(b'IDAT', zlib.compress(raw, 9))
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

def make_blank(): return [[TRANSPARENT for _ in range(SIZE)] for _ in range(SIZE)]

def draw_stroke_rect(p, x1, y1, x2, y2, r, thickness, color):
    """绘制圆角描边矩形"""
    for y in range(SIZE):
        for x in range(SIZE):
            d = 1000
            if x1+r <= x <= x2-r: d = min(d, abs(y-y1), abs(y-y2)) if y1 <= y <= y2 else d
            if y1+r <= y <= y2-r: d = min(d, abs(x-x1), abs(x-x2)) if x1 <= x <= x2 else d
            # 四个圆角描边
            for cx, cy in [(x1+r, y1+r), (x2-r, y1+r), (x1+r, y2-r), (x2-r, y2-r)]:
                dist = math.sqrt((x-cx)**2 + (y-cy)**2)
                d = min(d, abs(dist - r)) if (x-cx)*(1 if cx>SIZE/2 else -1)>=0 and (y-cy)*(1 if cy>SIZE/2 else -1)>=0 else d
            if d <= thickness/2: p[y][x] = color

def draw_line(p, x1, y1, x2, y2, thickness, color):
    length = max(math.sqrt((x1-x2)**2 + (y1-y2)**2), 1)
    for t in range(int(length * 4)):
        tt = t / (length * 4)
        nx, ny = int(x1 + (x2-x1)*tt), int(y1 + (y2-y1)*tt)
        if 0 <= nx < SIZE and 0 <= ny < SIZE: p[ny][nx] = color

# ===== 图标定义 =====
def draw_home(color):
    p = make_blank()
    # 极简屋顶线
    draw_line(p, 15, 42, 40, 20, 3, color)
    draw_line(p, 40, 20, 65, 42, 3, color)
    # 房屋主体描边
    draw_stroke_rect(p, 22, 40, 58, 68, 4, 3, color)
    return p

def draw_schedule(color):
    p = make_blank()
    draw_stroke_rect(p, 18, 25, 62, 65, 6, 3, color)
    draw_line(p, 18, 38, 62, 38, 3, color) # 顶部横线
    draw_line(p, 30, 18, 30, 30, 3, color) # 挂钩1
    draw_line(p, 50, 18, 50, 30, 3, color) # 挂钩2
    return p

def draw_grade(color):
    p = make_blank()
    # 奖杯杯身
    draw_stroke_rect(p, 28, 20, 52, 45, 10, 3, color)
    draw_line(p, 40, 45, 40, 58, 3, color) # 支柱
    draw_line(p, 30, 58, 50, 58, 3, color) # 底座
    return p

def draw_user(color):
    p = make_blank()
    # 头部圆圈
    cx, cy, r = 40, 32, 10
    for y in range(SIZE):
        for x in range(SIZE):
            d = math.sqrt((x-cx)**2 + (y-cy)**2)
            if abs(d - r) <= 1.5: p[y][x] = color
    # 身体线条
    for x in range(20, 61):
        y = 70 - math.sqrt(400 - (x-40)**2) * 0.8
        if 0 <= int(y) < SIZE: p[int(y)][x] = color
    return p

out_dir = 'images/tabbar'
os.makedirs(out_dir, exist_ok=True)
icons = {'home': draw_home, 'schedule': draw_schedule, 'grade': draw_grade, 'user': draw_user}

for name, func in icons.items():
    for suffix, color in [('', GRAY), ('_active', BLUE)]:
        pix = func(color)
        with open(os.path.join(out_dir, f'{name}{suffix}.png'), 'wb') as f: f.write(create_png(SIZE, SIZE, pix))
print("✅ 新版线性图标已生成")

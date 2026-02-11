#!/usr/bin/env python3
"""
生成 TabBar 图标 (81x81 PNG)
使用纯 Python 内建模块，无需 PIL/Pillow
"""
import struct, zlib, math, os

SIZE = 81
GRAY = (160, 165, 178, 255)   # #A0A5B2
BLUE = (91, 140, 255, 255)    # #5B8CFF
TRANSPARENT = (0, 0, 0, 0)

def create_png(width, height, pixels):
    """从 RGBA 像素列表创建 PNG 二进制数据"""
    def chunk(ctype, data):
        c = ctype + data
        crc = struct.pack('>I', zlib.crc32(c) & 0xFFFFFFFF)
        return struct.pack('>I', len(data)) + c + crc

    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0))

    raw = b''
    for y in range(height):
        raw += b'\x00'
        for x in range(width):
            raw += bytes(pixels[y][x])

    idat = chunk(b'IDAT', zlib.compress(raw, 9))
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

def make_blank():
    return [[TRANSPARENT for _ in range(SIZE)] for _ in range(SIZE)]

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def fill_circle(pixels, cx, cy, r, color):
    for y in range(SIZE):
        for x in range(SIZE):
            if dist(x, y, cx, cy) <= r:
                pixels[y][x] = color

def fill_rect(pixels, x1, y1, x2, y2, color):
    for y in range(int(y1), int(y2)+1):
        for x in range(int(x1), int(x2)+1):
            if 0 <= x < SIZE and 0 <= y < SIZE:
                pixels[y][x] = color

def fill_rounded_rect(pixels, x1, y1, x2, y2, r, color):
    """绘制圆角矩形"""
    for y in range(int(y1), int(y2)+1):
        for x in range(int(x1), int(x2)+1):
            if 0 <= x < SIZE and 0 <= y < SIZE:
                # 四个角
                if x < x1+r and y < y1+r:
                    if dist(x, y, x1+r, y1+r) <= r: pixels[y][x] = color
                elif x > x2-r and y < y1+r:
                    if dist(x, y, x2-r, y1+r) <= r: pixels[y][x] = color
                elif x < x1+r and y > y2-r:
                    if dist(x, y, x1+r, y2-r) <= r: pixels[y][x] = color
                elif x > x2-r and y > y2-r:
                    if dist(x, y, x2-r, y2-r) <= r: pixels[y][x] = color
                else:
                    pixels[y][x] = color

def draw_line(pixels, x1, y1, x2, y2, thickness, color):
    """绘制线段"""
    length = max(dist(x1, y1, x2, y2), 1)
    for t in range(int(length * 3)):
        tt = t / (length * 3)
        px = x1 + (x2-x1)*tt
        py = y1 + (y2-y1)*tt
        for dy in range(-thickness, thickness+1):
            for dx in range(-thickness, thickness+1):
                nx, ny = int(px+dx), int(py+dy)
                if 0 <= nx < SIZE and 0 <= ny < SIZE and abs(dx)+abs(dy) <= thickness:
                    pixels[ny][nx] = color

# ===== 首页图标 (房子) =====
def draw_home(color):
    p = make_blank()
    cx = 40
    # 屋顶三角形
    for y in range(15, 40):
        half_w = int((y - 15) * 1.1)
        for x in range(cx-half_w, cx+half_w+1):
            if 0 <= x < SIZE:
                p[y][x] = color
    # 房体
    fill_rounded_rect(p, 22, 38, 58, 65, 4, color)
    # 门 (透明)
    fill_rect(p, 35, 48, 45, 65, TRANSPARENT)
    return p

# ===== 课表图标 (日历) =====
def draw_calendar(color):
    p = make_blank()
    # 日历主体
    fill_rounded_rect(p, 15, 22, 65, 68, 6, color)
    # 顶部横条 (加粗)
    fill_rect(p, 15, 22, 65, 32, color)
    # 挂钩
    fill_rect(p, 28, 14, 31, 26, color)
    fill_rect(p, 49, 14, 52, 26, color)
    # 内部空白 (日历面板)
    fill_rect(p, 20, 36, 60, 63, TRANSPARENT)
    # 日期点阵 3x3
    dot_size = 3
    for row in range(3):
        for col in range(3):
            cx = 28 + col * 12
            cy = 42 + row * 8
            fill_rect(p, cx-dot_size, cy-1, cx+dot_size, cy+1, color)
    return p

# ===== 成绩图标 (奖杯/星星) =====
def draw_star(color):
    p = make_blank()
    cx, cy = 40, 38
    outer_r = 24
    inner_r = 10
    points = 5
    for y in range(SIZE):
        for x in range(SIZE):
            # 判断点是否在星形内部 (射线法简化)
            angle = math.atan2(y-cy, x-cx)
            d = dist(x, y, cx, cy)
            # 计算该角度上星形边界距离
            a = angle + math.pi/2
            sector = (a % (2*math.pi/points)) / (2*math.pi/points)
            if sector < 0.5:
                boundary = inner_r + (outer_r - inner_r) * (1 - sector*2)
            else:
                boundary = inner_r + (outer_r - inner_r) * ((sector-0.5)*2)
            if d <= boundary:
                p[y][x] = color
    return p

# ===== 我的图标 (人形) =====
def draw_user(color):
    p = make_blank()
    # 头部圆形
    fill_circle(p, 40, 26, 13, color)
    # 身体弧形 (半圆)
    for y in range(48, 70):
        for x in range(SIZE):
            d = dist(x, y, 40, 70)
            if d <= 30 and d >= 0:
                p[y][x] = color
    return p

# ===== 生成所有图标 =====
out_dir = 'images/tabbar'
icons = {
    'home': draw_home,
    'schedule': draw_calendar,
    'grade': draw_star,
    'user': draw_user,
}

for name, draw_func in icons.items():
    # 普通态 (灰色)
    pixels = draw_func(GRAY)
    with open(os.path.join(out_dir, f'{name}.png'), 'wb') as f:
        f.write(create_png(SIZE, SIZE, pixels))

    # 选中态 (蓝色)
    pixels = draw_func(BLUE)
    with open(os.path.join(out_dir, f'{name}_active.png'), 'wb') as f:
        f.write(create_png(SIZE, SIZE, pixels))

print('✅ 已生成 8 个 TabBar 图标:')
for name in icons:
    print(f'   {out_dir}/{name}.png')
    print(f'   {out_dir}/{name}_active.png')

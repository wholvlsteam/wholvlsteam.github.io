# -*- coding: utf-8 -*-
"""
旅行足迹页 · 经纬度 -> 地图百分比坐标

用法：改 PLACES 里的 (编号, 地名, 经度, 纬度, 徽章偏移x, 徽章偏移y)，
      python _pins.py，把输出的 <span class="pin"> 贴进 index.md。

底图：自然资源部标准地图服务，中国地图 1:1000 万 竖版 分省设色 无邻国
      审图号 GS(2022)4312号，原图 5825 x 7248，网页版等比缩到 2000 x 2488。

坐标怎么来的：底图用 Lambert 正形圆锥投影（标准纬线 23°N / 49°N，
中央经线 104°E），投影后是平面直角坐标；再用最小二乘拟合一个仿射变换
把投影坐标对齐到像素坐标。拟合用 5 个目视定位的地标（北京、西安、上海、
乌鲁木齐、哈尔滨），在 5825px 的原图上最大残差 16.5px、平均 10.7px，
约合 0.26%，足够标城市用。

换底图的话这组常数全部作废，要重新拟合。
"""

from __future__ import print_function
import math

# ---- 拟合出来的常数（对应 5825 x 7248 的原图）----
R = 6371000.0
PHI1, PHI2, LON0 = 23.0, 49.0, 104.0
CX = [0.0011948048788721478, 1.360841944591639e-05, 3017.075768387778]
CY = [1.0077179253475234e-05, -0.0011917962994077236, 7884.021339555499]
DX, DY = 40.0, 15.0
OW, OH = 5825.0, 7248.0

# ---- 网页版图片尺寸 ----
W, H = 2000.0, 2488.0


def pct(lon, lat):
    """经纬度 -> (left%, top%)"""
    p1, p2, l0 = map(math.radians, (PHI1, PHI2, LON0))
    phi = math.radians(lat)
    n = (math.log(math.cos(p1) / math.cos(p2)) /
         math.log(math.tan(math.pi / 4 + p2 / 2) / math.tan(math.pi / 4 + p1 / 2)))
    F = math.cos(p1) * math.tan(math.pi / 4 + p1 / 2) ** n / n
    rho = R * F / math.tan(math.pi / 4 + phi / 2) ** n
    rho0 = R * F / math.tan(math.pi / 4) ** n
    th = n * (math.radians(lon) - l0)
    x, y = rho * math.sin(th), rho0 - rho * math.cos(th)
    px = CX[0] * x + CX[1] * y + CX[2] + DX
    py = CY[0] * x + CY[1] * y + CY[2] + DY
    return 100.0 * px / OW, 100.0 * py / OH


# 徽章偏移（--tx / --ty，单位是 CSS px，不随地图缩放）是怎么定的：
#   徽章固定 17px，而点间距随地图缩小 —— 页面里地图只有约 795px 宽，
#   陕西那一簇 5 个点全挤在 20px 内。所以要挨个把徽章推开，用引线连回原点。
#   约束：徽章之间 >= 20px、徽章不压到别的圆点(>=16px)、引出地图边界。
#   这些值是手调+脚本排出来的，改完请重新截图确认没有叠住。
#
#   is_next=True 的点在网页上是空心徽章，表示还没去。
#
#            编号  地名        经度     纬度    tx   ty   is_next
PLACES = [
    (1,  u'西安',     108.94, 34.34,  16,   0,  False),
    (2,  u'咸阳',     108.71, 34.33,  -8,  14,  False),
    (3,  u'铜川',     108.95, 34.90, -16,   0,  False),
    (4,  u'黄陵',     109.26, 35.58, -14,  -8,  False),
    (5,  u'榆林',     109.73, 38.29,   0,   0,  False),
    (6,  u'府谷',     111.07, 39.03,   0,   0,  False),
    (7,  u'壶口瀑布', 110.44, 36.15,   0,   0,  False),
    (8,  u'阿拉善',   104.50, 38.50,   0,   0,  False),   # 腾格里沙漠中部
    (9,  u'北京',     116.40, 39.90,   0,   0,  False),
    (10, u'苏州',     120.62, 31.30,   4,  18,  False),
    (11, u'无锡',     120.30, 31.57,  -6, -18,  False),
    (12, u'合肥',     117.28, 31.86, -14,   8,  False),
    (13, u'安阳',     114.35, 36.10,   0,   0,  True),
]

if __name__ == '__main__':
    out = []
    for n, name, lon, lat, tx, ty, nxt in PLACES:
        L, T = pct(lon, lat)
        ln = math.hypot(tx, ty)
        ang = math.degrees(math.atan2(ty, tx))
        cls = u'pin is-next' if nxt else u'pin'
        title = name + (u'（计划中）' if nxt else u'')
        out.append(
            u'  <span class="%s" style="left:%.2f%%; top:%.2f%%; '
            u'--tx:%dpx; --ty:%dpx; --len:%.1fpx; --ang:%.1fdeg" '
            u'title="%s"><i></i><b>%d</b></span>'
            % (cls, L, T, tx, ty, ln, ang, title, n))
    print(u'\n'.join(out).encode('utf-8'))

    # 顺带报一下挨得太近、需要错开徽章的点对
    pos = dict((p[0], pct(p[2], p[3])) for p in PLACES)
    print(u'\n# 间距 < 20px 的点对（徽章必须岔开）:'.encode('utf-8'))
    for a in PLACES:
        for b in PLACES:
            if b[0] <= a[0]:
                continue
            d = math.hypot((pos[a[0]][0] - pos[b[0]][0]) * W / 100,
                           (pos[a[0]][1] - pos[b[0]][1]) * H / 100)
            if d < 20:
                print(u'#   %s <-> %s : %.1f px' % (a[1], b[1], d))

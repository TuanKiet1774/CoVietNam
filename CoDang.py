#=====CỜ ĐẢNG CỘNG SẢN VIÊT NAM=====
import turtle
import math
import time
import re

FLAG_W, FLAG_H = 600, 400
BG_RED = "#da251d"
FG_YELLOW = "yellow"

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.title("Cờ Đảng Cộng Sản Việt Nam")

flag = turtle.Turtle()
flag.hideturtle()
flag.speed(0)

symbol = turtle.Turtle()
symbol.hideturtle()
symbol.speed(0)
symbol.color(FG_YELLOW)

def draw_waving_flag(phase):
    flag.clear()
    flag.color(BG_RED)
    flag.penup()
    flag.goto(-FLAG_W/2, -FLAG_H/2)
    flag.pendown()
    flag.begin_fill()

    for x in range(-FLAG_W//2, FLAG_W//2 + 1, 10):
        y = -FLAG_H/2 + 10*math.sin(x/50 + phase)
        flag.goto(x, y)
    for y in range(-FLAG_H//2, FLAG_H//2 + 1, 10):
        x = FLAG_W/2 + 10*math.sin(FLAG_W/50 + phase + y/100)
        flag.goto(x, y)
    for x in range(FLAG_W//2, -FLAG_W//2 - 1, -10):
        y = FLAG_H/2 + 10*math.sin(x/50 + phase + 0.5)
        flag.goto(x, y)
    for y in range(FLAG_H//2, -FLAG_H//2 - 1, -10):
        x = -FLAG_W/2 + 10*math.sin(-FLAG_W/50 + phase + y/100 + 0.5)
        flag.goto(x, y)

    flag.end_fill()

def tokenize_path(d):
    d = d.replace(',', ' ')
    tokens = []
    i = 0
    while i < len(d):
        ch = d[i]
        if ch in 'MmLlCcZz':
            tokens.append(ch)
            i += 1
        elif ch in ' \t\r\n':
            i += 1
        else:
            j = i
            while j < len(d) and d[j] not in 'MmLlCcZz \t\r\n':
                j += 1
            tokens.append(d[i:j])
            i = j
    return tokens

def cubic_bezier_points(p0, p1, p2, p3, steps=40):
    pts = []
    for k in range(steps+1):
        t = k/steps
        x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
        y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts

def path_to_polylines(d):
    tokens = tokenize_path(d)
    i = 0
    polylines = []
    cx = cy = 0.0
    sx = sy = 0.0       
    last_cmd = None

    def read_num():
        nonlocal i
        val = float(tokens[i]); i += 1
        return val

    while i < len(tokens):
        tok = tokens[i]
        if tok in 'MmLlCcZz':
            cmd = tok; i += 1
        else:
            cmd = last_cmd

        if cmd in ('M', 'm'):
            x = read_num(); y = read_num()
            if cmd == 'm':
                cx += x; cy += y
            else:
                cx, cy = x, y
            sx, sy = cx, cy
            polylines.append([(cx, cy)]) 

            while i < len(tokens) and tokens[i] not in 'MmLlCcZz':
                x = read_num(); y = read_num()
                if tok == 'm':
                    cx += x; cy += y
                else:
                    cx, cy = x, y
                polylines[-1].append((cx, cy))

        elif cmd in ('L', 'l'):
            if not polylines:
                polylines.append([(cx, cy)])
            while i < len(tokens) and tokens[i] not in 'MmLlCcZz':
                x = read_num(); y = read_num()
                if cmd == 'l':
                    cx += x; cy += y
                else:
                    cx, cy = x, y
                polylines[-1].append((cx, cy))

        elif cmd in ('C', 'c'):
            if not polylines:
                polylines.append([(cx, cy)])
            while i < len(tokens) and tokens[i] not in 'MmLlCcZz':
                x1 = read_num(); y1 = read_num()
                x2 = read_num(); y2 = read_num()
                x3 = read_num(); y3 = read_num()
                if cmd == 'c':
                    p0 = (cx, cy)
                    p1 = (cx + x1, cy + y1)
                    p2 = (cx + x2, cy + y2)
                    p3 = (cx + x3, cy + y3)
                    cx, cy = p3
                else:
                    p0 = (cx, cy)
                    p1 = (x1, y1); p2 = (x2, y2); p3 = (x3, y3)
                    cx, cy = p3
                pts = cubic_bezier_points(p0, p1, p2, p3, steps=40)
                polylines[-1].extend(pts[1:])

        elif cmd in ('Z', 'z'):
            if polylines:
                polylines[-1].append((sx, sy))
                cx, cy = sx, sy

        last_cmd = cmd
    return polylines

PATH1 = ("m -6436.471547371615,1742.926950096642 "
         "c 6.38779271804,7.230641357446 14.963163305737,12.502793149194 24.298667889062,14.938860558647 "
         "6.056211101325,1.5803471957 12.472708435771,1.978650572228 18.596462444365,0.684499497231 "
         "6.123754008594,-1.294151074997 11.937748010956,-4.335579482059 16.158102214692,-8.957678632632 "
         "4.574893298958,-5.010387614465 7.112965317221,-11.701447693132 7.640977625143,-18.465679781602 "
         "0.528012307931,-6.76423208847 -0.871424851367,-13.593465851735 -3.428046439768,-19.878155088105 "
         " -4.560331599745,-11.210210791164 -12.883741385267,-20.851111282196 -23.308680635365,-26.998150562502 "
         "8.512796781266,0.709574410866 16.805946699762,3.8827694509 23.618107102883,9.036959544979 "
         "6.812160403116,5.154190094079 12.120611342006,12.272184963572 15.117966521428,20.271376598489 "
         "2.997355179421,7.999191634919 3.673617806543,16.852901094338 1.925932041966,25.214527691603 "
         "-1.747685764577,8.361626597266 -5.913491031185,16.203282596691 -11.863819649182,22.332295096395 "
         "-8.683007967653,8.943752149713 -21.180068232394,14.055514292711 -33.64194922505,13.760807647735 "
         "-12.461880992656,-0.294706644979 -24.703333498127,-5.991501184333 -32.953855939355,-15.335708444904 "
         "l -14.556480332948,14.556690177998 -9.381909223252,-9.381909223192 z")

PATH2 = ("m -6392.699744590418,1702.503831581282 "
         "-10.959354263905,10.959354263781 49.262553323164,49.262553323191 "
         "-11.130862671953,11.240941835746 -49.317592904992,-49.317592905071 "
         "-8.654444010462,8.654444010525 -12.790755991701,-12.790755991717 "
         "21.572665110517,-21.572665110577 "
         "c 2.680889538451,0.275819129839 5.402702461607,0.150469066643 8.046892630834,-0.370590679184 "
         "2.581477478967,-0.508701686704 5.088366413035,-1.394314604689 7.416535436053,-2.62005208911 z")

def prepare_symbol_polylines():
    polys1 = path_to_polylines(PATH1)
    polys2 = path_to_polylines(PATH2)
    polys = polys1 + polys2

    xs = [x for poly in polys for (x, y) in poly]
    ys = [y for poly in polys for (x, y) in poly]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)

    cx = (minx + maxx) / 2.0
    cy = (miny + maxy) / 2.0
    centered = [[(x - cx, -(y - cy)) for (x, y) in poly] for poly in polys]

    width = maxx - minx
    height = maxy - miny
    target_w, target_h = 260, 220
    s = min(target_w / width, target_h / height)

    scaled = [[(x*s, y*s) for (x, y) in poly] for poly in centered]

    OFFSET_X = 0
    OFFSET_Y = 20
    shifted = [[(x + OFFSET_X, y + OFFSET_Y) for (x, y) in poly] for poly in scaled]
    return shifted

SYMBOL_POLYS = prepare_symbol_polylines()

def wave_point(x, y, phase):
    offset = 10 * math.sin(x / 50 + phase + y / 100)
    return (x, y + offset)

def draw_symbol(phase):
    symbol.clear()
    symbol.color(FG_YELLOW)
    for poly in SYMBOL_POLYS:
        waved_poly = [wave_point(x, y, phase) for (x, y) in poly]
        symbol.penup()
        symbol.goto(waved_poly[0])
        symbol.pendown()
        symbol.begin_fill()
        for (x, y) in waved_poly[1:]:
            symbol.goto(x, y)
        symbol.end_fill()
        symbol.penup()


phase = 0.0
try:
    while True:
      draw_waving_flag(phase)
      draw_symbol(phase)
      screen.update()
      phase += 0.2
      time.sleep(0.05)

except:
    pass

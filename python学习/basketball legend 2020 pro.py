import pygame
import sys
import math
import random
import os

# 让 Pygame 窗口在屏幕中央显示
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# ---------- 窗口和显示设置 ----------
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SHOWN | pygame.HWSURFACE)
pygame.display.set_caption("Basketball Legends - 投篮练习")
clock = pygame.time.Clock()                # 控制帧率
font = pygame.font.Font(None, 36)          # 普通字体
big_font = pygame.font.Font(None, 72)      # 大字体（备用）

# ---------- 颜色常量 ----------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (233, 69, 96)
BLUE = (30, 144, 255)
GREEN = (45, 90, 39)
LIGHT_GREEN = (61, 122, 55)
ORANGE = (224, 112, 48)
YELLOW = (250, 204, 21)
DARK_ORANGE = (180, 80, 30)
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 90, 43)

# ---------- 物理常量 ----------
GRAVITY = 0.6          # 重力加速度（每帧）
FRICTION = 0.92        # 水平摩擦力（速度衰减）
MAX_SPEED = 6.0        # 玩家最大水平速度
PLAYER_RADIUS = 22     # 玩家圆形半径
BALL_RADIUS = 12       # 篮球半径
GROUND_Y = 530         # 地面在屏幕上的 Y 坐标

# ---------- 篮筐和篮板位置 ----------
HOOP_X = 780           # 篮筐中心 X
HOOP_Y = 180           # 篮筐顶部 Y
RIM_WIDTH = 90         # 篮筐宽度
RIM_HEIGHT = 10        # 篮筐高度（厚度）
BACKBOARD_X = HOOP_X - 5    # 篮板 X 位置（紧贴篮筐左侧）
BACKBOARD_Y = HOOP_Y - 30   # 篮板顶部 Y

# ============================================================
# 玩家类
# ============================================================
class Player:
    def __init__(self, x, y):
        """初始化玩家位置和状态"""
        self.x = x
        self.y = y
        self.vx = 0          # 水平速度
        self.vy = 0          # 垂直速度
        self.radius = PLAYER_RADIUS
        self.has_ball = True # 是否持球
        self.on_ground = True # 是否在地面
        self.direction = 1   # 朝向（1=右，-1=左）

    def update(self):
        """更新玩家物理（位置、速度、碰撞）"""
        # 水平移动和摩擦力
        self.x += self.vx
        self.vx *= FRICTION
        if abs(self.vx) < 0.05:
            self.vx = 0

        # 垂直移动和重力
        self.vy += GRAVITY
        self.y += self.vy

        # 地面碰撞
        if self.y + self.radius > GROUND_Y:
            self.y = GROUND_Y - self.radius
            self.vy = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # 左右边界限制
        self.x = max(30 + self.radius, min(WIDTH - 30 - self.radius, self.x))

        # 根据速度更新朝向
        if self.vx > 0.5:
            self.direction = 1
        elif self.vx < -0.5:
            self.direction = -1

    def draw(self, screen):
        """绘制玩家（带阴影、渐变、文字和持球标记）"""
        # 阴影
        shadow = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        pygame.draw.circle(shadow, (0,0,0,50), (self.radius, self.radius+8), self.radius)
        screen.blit(shadow, (self.x - self.radius, self.y - self.radius + 5))

        # 渐变圆形（从中心向外透明度降低）
        grad = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        for r in range(self.radius, 0, -1):
            alpha = int(255 * (1 - r/self.radius))
            color = (233, 69, 96, alpha)
            pygame.draw.circle(grad, color, (self.radius, self.radius), r)
        screen.blit(grad, (self.x - self.radius, self.y - self.radius))

        # 白色边框
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius, 2)

        # 显示字母 "P" 代表玩家
        text = font.render("P", True, WHITE)
        text_rect = text.get_rect(center=(self.x, self.y-2))
        screen.blit(text, text_rect)

        # 如果持球，显示闪电标记
        if self.has_ball:
            text = font.render("⚡", True, YELLOW)
            screen.blit(text, (self.x + self.radius + 8, self.y - 18))

    def move(self, dx):
        """根据按键方向移动（平滑加速）"""
        speed = 5.0
        target_vx = dx * speed
        self.vx += (target_vx - self.vx) * 0.25  # 平滑过渡
        if abs(self.vx) > MAX_SPEED:
            self.vx = MAX_SPEED * (1 if self.vx > 0 else -1)

    def jump(self):
        """跳跃：仅在地面时起跳"""
        if self.on_ground:
            self.vy = -17.0
            self.on_ground = False

    def collides_with_ball(self, ball):
        """检测玩家与篮球是否碰撞（圆-圆碰撞）"""
        dx = self.x - ball.x
        dy = self.y - ball.y
        return dx*dx + dy*dy < (self.radius + ball.radius) ** 2

# ============================================================
# 篮球类
# ============================================================
class Ball:
    def __init__(self):
        """初始化篮球位置和状态"""
        self.x = 450
        self.y = 400
        self.vx = 0
        self.vy = 0
        self.radius = BALL_RADIUS
        self.scored = False   # 是否已得分（防止重复计分）
        self.trail = []       # 轨迹点列表

    def update(self):
        # 重力
        self.vy += GRAVITY
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.995

        # 地面碰撞
        if self.y + self.radius > GROUND_Y:
            self.y = GROUND_Y - self.radius
            self.vy *= -0.4
            self.vx *= 0.9
            if abs(self.vy) < 0.3:
                self.vy = 0

        # 左右墙壁碰撞
        if self.x - self.radius < 30:
            self.x = 30 + self.radius
            self.vx *= -0.5
        if self.x + self.radius > WIDTH - 30:
            self.x = WIDTH - 30 - self.radius
            self.vx *= -0.5

        # ---------- 篮筐碰撞（新） ----------
        rim_left = HOOP_X - RIM_WIDTH / 2
        rim_right = HOOP_X + RIM_WIDTH / 2
        rim_top = HOOP_Y
        rim_bottom = HOOP_Y + RIM_HEIGHT

        # 1. 空心入网检测：球从上方穿过篮筐顶部平面
        # 条件：球的上边缘刚刚低于顶部（即穿越顶部），且球心水平在筐内（留出半径余量）
        if (self.vy > 0 and
                self.y - self.radius < rim_top and self.y + self.radius > rim_top and
                self.x + self.radius > rim_left + 2 and self.x - self.radius < rim_right - 2):
            if not self.scored:
                self.scored = True
                return True  # 得分

        # 2. 四边碰撞（从外部撞击边框）
        # 左边框
        if self.vx < 0 and self.x - self.radius < rim_left and rim_top < self.y < rim_bottom:
            self.x = rim_left - self.radius
            self.vx = -self.vx * 0.5
            self.scored = False
        # 右边框
        elif self.vx > 0 and self.x + self.radius > rim_right and rim_top < self.y < rim_bottom:
            self.x = rim_right + self.radius
            self.vx = -self.vx * 0.5
            self.scored = False
        # 上边框
        elif self.vy < 0 and self.y - self.radius < rim_top and rim_left < self.x < rim_right:
            self.y = rim_top - self.radius
            self.vy = -self.vy * 0.5
            self.scored = False
        # 下边框
        elif self.vy > 0 and self.y + self.radius > rim_bottom and rim_left < self.x < rim_right:
            self.y = rim_bottom + self.radius
            self.vy = -self.vy * 0.5
            self.scored = False

        # 篮板碰撞
        if (BACKBOARD_X - 5 < self.x < BACKBOARD_X + 5 and
                BACKBOARD_Y < self.y < BACKBOARD_Y + 60):
            self.vx *= -0.6
            self.x = BACKBOARD_X - 5 - self.radius if self.vx < 0 else BACKBOARD_X + 5 + self.radius
            self.scored = False

        return False

    def reset(self):
        """重置篮球到初始位置，清除轨迹"""
        self.x = 450
        self.y = 400
        self.vx = 0
        self.vy = 0
        self.scored = False
        self.trail = []

    def draw(self, screen):
        """绘制篮球（带轨迹拖尾和纹理装饰）"""
        # 记录轨迹点并限制长度
        self.trail.append((self.x, self.y))
        if len(self.trail) > 8:
            self.trail.pop(0)

        # 绘制轨迹（从旧到新透明度渐强）
        for i, pos in enumerate(self.trail):
            alpha = i / len(self.trail) * 0.3
            radius = self.radius * (i / len(self.trail))
            surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (255, 150, 50, int(alpha*255)), (radius, radius), radius)
            screen.blit(surf, (pos[0]-radius, pos[1]-radius))

        # 篮球主体（橙色）
        pygame.draw.circle(screen, ORANGE, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, DARK_ORANGE, (int(self.x), int(self.y)), self.radius, 2)

        # 装饰：篮球纹路（两个弧线）
        pygame.draw.arc(screen, (80,40,20,80),
                        (self.x-self.radius*0.6, self.y-self.radius*0.6,
                         self.radius*1.2, self.radius*1.2),
                        -0.8, 0.8, 1)
        pygame.draw.arc(screen, (80,40,20,80),
                        (self.x-self.radius*0.6, self.y-self.radius*0.6,
                         self.radius*1.2, self.radius*1.2),
                        math.pi-0.8, math.pi+0.8, 1)

    def shoot(self, from_x, from_y, power_x, power_y):
        self.x = from_x
        self.y = from_y
        self.vx = power_x  # 不再乘以 1.1，因为我们已经精确计算
        self.vy = power_y  # 不再减去常数
        self.scored = False
        self.trail = []

# ============================================================
# 全局对象和变量
# ============================================================
player = Player(300, GROUND_Y - PLAYER_RADIUS)
ball = Ball()
player.has_ball = True
score = 0

# ============================================================
# 核心游戏函数
# ============================================================
def shoot_ball():
    """无论位置如何，保证球砸到篮筐，命中由时机决定"""
    global score

    start_x = ball.x
    start_y = ball.y

    # ---- 1. 根据垂直速度判断出手时机，选择目标点 ----
    vy_player = player.vy
    if vy_player < -3.0:          # 过早（上升中）
        target_y = HOOP_Y - 3     # 瞄准后沿（偏高）
    elif vy_player > 3.0:         # 过晚（下落中）
        target_y = HOOP_Y + RIM_HEIGHT + 3   # 瞄准前沿（偏低）
    else:                         # 完美时机
        target_y = HOOP_Y + RIM_HEIGHT / 2   # 瞄准中心

    target_x = HOOP_X   # 水平始终瞄准篮筐中心

    # ---- 2. 计算水平和垂直距离 ----
    dx = target_x - start_x
    dy = target_y - start_y

    # 如果太近（在篮筐下方），直接轻投
    if abs(dx) < 15:
        ball.shoot(start_x, start_y, 0, -4.0)
        player.has_ball = False
        return

    # ---- 3. 固定水平速度 ----
    HORIZONTAL_SPEED = 6.0   # 像素/帧，推荐 5~7
    vx = HORIZONTAL_SPEED if dx > 0 else -HORIZONTAL_SPEED
    T = abs(dx / vx)   # 飞行时间（帧）

    # ---- 4. 反推垂直初速度 ----
    vy_initial = (dy - 0.5 * GRAVITY * T * T) / T

    # ---- 5. 落地检查：确保球在到达目标前不会落地 ----
    # 计算球在飞行过程中的最低点（顶点）的 y 坐标
    # 顶点时间 t_peak = -vy_initial / GRAVITY
    # 顶点高度 = start_y + vy_initial * t_peak + 0.5 * GRAVITY * t_peak^2
    # 如果顶点高度 > GROUND_Y - 半径，说明球会在到达目标前落地，需要提高 vy_initial
    if vy_initial < 0:
        t_peak = -vy_initial / GRAVITY
        peak_y = start_y + vy_initial * t_peak + 0.5 * GRAVITY * t_peak * t_peak
        if peak_y > GROUND_Y - BALL_RADIUS:
            # 需要增加 vy_initial 使得峰值刚好在地面之上
            # 我们直接增加 vy_initial 的绝对值，直到峰值低于地面
            # 简单方法：将 vy_initial 乘以一个系数，或增加一个固定值
            # 更精确：解方程 peak_y = GROUND_Y - BALL_RADIUS - 5
            # 但为了简单，我们直接增加 vy_initial 的绝对值 2 个单位
            vy_initial -= 2.0   # 向上加速
            # 重新计算 T 不变，但因为我们改了 vy，顶点会变高，没问题

    # ---- 6. 保底：防止垂直速度太小 ----
    if abs(vy_initial) < 1.0:
        vy_initial = 1.0 if vy_initial > 0 else -1.0

    # ---- 7. 限制最大速度 ----
    max_speed = 25.0
    speed = math.sqrt(vx*vx + vy_initial*vy_initial)
    if speed > max_speed:
        scale = max_speed / speed
        vx *= scale
        vy_initial *= scale

    # ---- 8. 执行投篮 ----
    ball.shoot(start_x, start_y, vx, vy_initial)
    player.has_ball = False

def handle_ball():
    """处理篮球与玩家的交互：得分检测、捡球"""
    global score
    if not player.has_ball:
        # 篮球在空中时更新物理，并检测是否得分
        if ball.update():
            score += 1
            ball.reset()
            player.has_ball = True

        # 如果篮球几乎静止且靠近玩家，自动捡球
        if (abs(ball.vy) < 0.1 and ball.y > GROUND_Y - 30 and
            abs(ball.x - player.x) < 60 and not ball.scored):
            if player.collides_with_ball(ball):
                player.has_ball = True
                ball.vx = ball.vy = 0
    else:
        # 持球时篮球跟随玩家
        offset_x = 30 if player.direction > 0 else -30
        ball.x = player.x + offset_x
        ball.y = player.y - 15
        ball.vx = ball.vy = 0

def draw_court(screen):
    """绘制球场背景、地面、篮筐、篮板、支柱等"""
    # 天空
    screen.fill(SKY_BLUE)

    # 地面
    pygame.draw.rect(screen, GROUND_BROWN, (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
    # 地面纹理（横条）
    for x in range(0, WIDTH, 40):
        pygame.draw.rect(screen, (180, 130, 70), (x, GROUND_Y, 20, 4))

    # 墙壁（背景墙）
    wall_color = (220, 200, 170)
    pygame.draw.rect(screen, wall_color, (0, 0, WIDTH, GROUND_Y - 10))
    for y in range(50, GROUND_Y - 10, 40):
        pygame.draw.line(screen, (200, 180, 150), (0, y), (WIDTH, y), 1)

    # 半圆弧装饰（三分线效果）
    pygame.draw.arc(screen, (255,255,255,80),
                    (HOOP_X - 180, HOOP_Y + 20, 360, 200),
                    0.1, math.pi - 0.1, 2)

    # 篮板（半透明蓝色矩形）
    board_rect = pygame.Rect(BACKBOARD_X - 5, BACKBOARD_Y, 10, 65)
    pygame.draw.rect(screen, (200, 230, 255, 150), board_rect)
    pygame.draw.rect(screen, (200, 230, 255, 200), board_rect, 2)
    # 篮板上的小方框标记
    pygame.draw.rect(screen, (255,255,255,80),
                     (BACKBOARD_X - 2, BACKBOARD_Y + 20, 4, 25), 1)

    # 篮筐（红色矩形）
    pygame.draw.rect(screen, RED, (HOOP_X - RIM_WIDTH//2, HOOP_Y, RIM_WIDTH, RIM_HEIGHT))

    # 网（用几条斜线模拟）
    for i in range(8):
        x = HOOP_X - RIM_WIDTH//2 + 6 + i*8
        pygame.draw.line(screen, (200,200,200,80),
                         (x, HOOP_Y + RIM_HEIGHT),
                         (x + (i-3.5)*1.5, HOOP_Y + RIM_HEIGHT + 35), 2)

    # 支柱（从篮筐到地面的竖线）
    pygame.draw.line(screen, (150,150,150,150),
                     (HOOP_X, GROUND_Y), (HOOP_X, HOOP_Y + RIM_HEIGHT), 4)

    # 地面上的阴影/标记
    pygame.draw.rect(screen, (255,255,255,30),
                     (HOOP_X - 100, GROUND_Y - 5, 200, 5))

# ============================================================
# 主循环
# ============================================================
running = True
keys = {'a': False, 'd': False, 'w': False, 's': False}  # 按键状态

while running:
    dt = clock.tick(60) / 1000.0   # 控制帧率，dt 未使用（但保留）

    # ---------- 事件处理 ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 按键按下
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: keys['a'] = True
            if event.key == pygame.K_d: keys['d'] = True
            if event.key == pygame.K_w: keys['w'] = True
            if event.key == pygame.K_s: keys['s'] = True
            if event.key == pygame.K_l:
                if player.has_ball:
                    shoot_ball()
            if event.key == pygame.K_r:   # 重置游戏
                score = 0
                player.x, player.y = 300, GROUND_Y - PLAYER_RADIUS
                player.vx = player.vy = 0
                ball.reset()
                player.has_ball = True
        # 按键释放
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: keys['a'] = False
            if event.key == pygame.K_d: keys['d'] = False
            if event.key == pygame.K_w: keys['w'] = False
            if event.key == pygame.K_s: keys['s'] = False

    # ---------- 玩家移动控制 ----------
    move_dir = 0
    if keys['a']: move_dir = -1
    if keys['d']: move_dir = 1
    if move_dir != 0:
        player.move(move_dir)

    if keys['w']:
        player.jump()

    # 按 S 键在空中加速下落（快速落地）
    if keys['s'] and not player.on_ground:
        player.vy += 0.5

    # ---------- 更新 ----------
    player.update()
    handle_ball()

    # ---------- 绘制 ----------
    screen.fill(SKY_BLUE)
    draw_court(screen)

    # 如果持球，在篮筐附近显示投篮辅助圈（半透明提示）
    if player.has_ball:
        s = pygame.Surface((140,140), pygame.SRCALPHA)
        pygame.draw.circle(s, (233,69,96,25), (70,70), 70)
        screen.blit(s, (HOOP_X-70, HOOP_Y-40))

    ball.draw(screen)
    player.draw(screen)

    # ---------- 显示文字信息 ----------
    score_text = font.render(f"进球: {score}", True, WHITE)
    screen.blit(score_text, (30, 15))

    if player.has_ball:
        tip = font.render("按 L 投篮", True, YELLOW)
        screen.blit(tip, (WIDTH//2 - tip.get_width()//2, 20))

    hint = font.render("A/D 移动 | W 跳跃 | L 投篮 | R 重置", True, (200,200,200))
    screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT - 30))

    # ---------- 刷新屏幕 ----------
    pygame.display.flip()

# 退出游戏
pygame.quit()
sys.exit()
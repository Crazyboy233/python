import pygame
import random
import math

# 初始化 Pygame
pygame.init()

# 设置屏幕
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("烟花粒子效果")

# 粒子类
class Particle:
    def __init__(self, x, y, color, angle, speed):
        self.x = x  # 粒子初始横坐标
        self.y = y  # 粒子初始纵坐标
        self.color = color  # 粒子颜色
        self.angle = angle  # 运动角度
        self.speed = speed  # 运动速度
        self.life = 100  # 粒子生命周期（以帧为单位）
        self.size = random.randint(2, 4)  # 粒子大小（随机）

    def update(self):
        """更新粒子的位置"""
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= 1  # 粒子生命值减小
        self.speed *= 0.98  # 粒子逐渐减速

    def draw(self, screen):
        """在屏幕上绘制粒子"""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# 烟花类
class Firework:
    def __init__(self, x, y):
        self.x = x  # 烟花发射点横坐标
        self.y = y  # 烟花发射点纵坐标
        self.particles = []  # 存储粒子的列表
        self.exploded = False  # 烟花是否已爆炸

    def explode(self):
        """爆炸并生成粒子"""
        if not self.exploded:
            self.exploded = True
            for _ in range(100):  # 爆炸产生100个粒子
                angle = random.uniform(0, 2 * math.pi)  # 随机角度
                speed = random.uniform(3, 8)  # 随机速度
                color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)])
                self.particles.append(Particle(self.x, self.y, color, angle, speed))

    def update(self):
        """更新粒子"""
        for particle in self.particles:
            particle.update()

        # 移除生命周期已结束的粒子
        self.particles = [p for p in self.particles if p.life > 0]

    def draw(self, screen):
        """绘制粒子"""
        for particle in self.particles:
            particle.draw(screen)

# 主程序
def main():
    clock = pygame.time.Clock()  # 控制帧率
    fireworks = []  # 存储烟花对象

    while True:
        screen.fill((0, 0, 0))  # 清屏，填充黑色背景

        # 监听退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # 随机发射烟花
        if random.random() < 0.03:  # 30%的概率发射烟花
            firework = Firework(random.randint(100, width - 100), height)  # 从屏幕底部随机发射
            fireworks.append(firework)

        # 更新和绘制所有烟花
        for firework in fireworks:
            firework.explode()  # 爆炸
            firework.update()  # 更新粒子位置
            firework.draw(screen)  # 绘制粒子

        pygame.display.flip()  # 更新显示
        clock.tick(60)  # 每秒60帧

if __name__ == "__main__":
    main()

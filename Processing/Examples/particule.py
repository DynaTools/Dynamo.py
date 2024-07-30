# Definindo parâmetros iniciais
particleCount = 100
connectionDistance = 100
particles = []
run = True

def setup():
    size(1000, 800)
    noStroke()
    for _ in range(particleCount):
        particles.append(Particle())

def draw():
    background(255)
    if run:
        for p in particles:
            p.update()
            p.display()
        for i in range(particleCount):
            for j in range(i + 1, particleCount):
                p1 = particles[i]
                p2 = particles[j]
                distance = dist(p1.position.x, p1.position.y, p2.position.x, p2.position.y)
                if distance < connectionDistance:
                    stroke(150, map(distance, 0, connectionDistance, 255, 0))
                    line(p1.position.x, p1.position.y, p2.position.x, p2.position.y)
                    noStroke()

def mousePressed():
    global run
    run = not run

class Particle:
    def __init__(self):
        self.radius = floor(random(2, 7))  # Reduzindo o tamanho das partículas
        self.position = PVector(random(self.radius, width - self.radius), random(self.radius, height - self.radius))
        self.velocity = PVector(random(-0.5, 0.5), random(-0.5, 0.5))
        self.size = self.radius * self.radius  # Ajustando o tamanho

    def update(self):
        self.position.add(self.velocity)
        if self.position.x > width - self.radius or self.position.x < self.radius:
            self.velocity.x *= -1
        if self.position.y > height - self.radius or self.position.y < self.radius:
            self.velocity.y *= -1

    def display(self):
        fill(map(self.position.x, 0, width, 255, 0), 0, map(self.position.x, 0, width, 0, 255))
        ellipse(self.position.x, self.position.y, self.size, self.size)

import pygame, random, time

playSurface = pygame.display.set_mode((720, 460))

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

fpsController = pygame.time.Clock()

snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

def gameOver():
	time.sleep(8)
	pygame.quit()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				changeto = 'DOWN'

	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'
	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -= 10
	if direction == 'DOWN':
		snakePos[1] += 10

	snakeBody.insert(0, list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		foodSpawn = False
	else:
		snakeBody.pop()

	if foodSpawn == False:
		foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
	foodSpawn = True

	playSurface.fill(white)

	for pos in snakeBody:
		pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

	pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

	if snakePos[0] > 710 or snakePos[0] < 0:
		gameOver()
	if snakePos[1] > 450 or snakePos[1] < 0:
		gameOver()

	for block in snakeBody[1:]:
		if snakePos[0] == block[0] and snakePos[1] == block[1]:
			gameOver()

	pygame.display.flip()

	fpsController.tick(24)

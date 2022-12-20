import pygame
import os

###################################################################################################
# 기본 초기화 반드시해야하는 것들
pygame.init() # 초기화 (반드시필요)

# 화면 크기 설정
screen_width = 640  # 가로 크기
screen_height = 480  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
# 화면 타이틀 설정
pygame.display.set_caption( "PIKA Game" ) # 게임 이름

# FPS
clock = pygame.time.Clock()

###################################################################################################

# 1. 사용자 게임 초기화( 배경화면, 게임 이미지, 좌표, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background2.jpg"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]

character = pygame.image.load(os.path.join(image_path, "character.jpeg"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = (screen_height - character_height - stage_height)

running = True 
while running:
    #이벤트 처리
    dt = clock.tick(50)

    # 2. 이벤트 처리( 키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,((0,screen_height-stage_height)))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update() # 게임화면을 다시 그리기(계속 실행이 되어야함 )
# pygame.time.delay(3000)
# pygame 종료
pygame.quit()

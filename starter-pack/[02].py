import pygame, sys
import maryolib

pygame.init()

# Ekranimizi olusturuyoruz
DISPLAY_X = 800
DISPLAY_Y = 480
main_display = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y), 0, 32)
pygame.display.set_caption("Project-Maryo")

# Oyunun kac fps'de calisacagini ayarlayacagiz
clock = pygame.time.Clock()
FPS = 60

# RGB renk tanimlamalarimiz
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Beyaz rengi arka plana uygula
main_display.fill(WHITE)

# Ekranda gorulecek grafiksel objeleri bu listede tutacagiz
graph_list = pygame.sprite.Group()

# Yeni bir grafik olusturuyoruz
maryo = maryolib.MaryoImageObject(35, 50, "maryo.png")
maryo.move_to(50, 100)  # Grafigin konumunu degistir
graph_list.add(maryo)  # yeni grafigimizi listeye ekliyoruz

# Programin ana dongusu burasi
while True:
    # Event demek bir tusa basilmasi vs. demek. Eventler pygame.event.get()
    # fonksiyonunun dondurdugu listede birikiyor. Bunlari tek tek isliyoruz.
    for event in pygame.event.get():
        # Eger pencere kapatilmissa asagiyi calistir
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Bir tusa basilirsa asagiyi caltir
        if event.type == pygame.KEYDOWN:
            # Eger basilan tus esc ise bunu yap
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Eger basilan tus "space" tusu ise bunu yap
            elif event.key == pygame.K_SPACE:
                print("Space tusuna basildi.")

    # Event'taki kisim, butona bastiginiz an 1 kere calisir. Asagidaki kisim
    # butona basili tuttugunuz surece calisir.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print("Sol ok tusuna basili tutuluyor.")
    if keys[pygame.K_RIGHT]:
        print("Sag ok tusuna basili tutuluyor.")
        maryo.move_right(5)  # 5 pixel saga hareket et

    # Onceki ekrani tamamen temizle
    main_display.fill(WHITE)
    # Yukaridaki degisiklikleri ekrana yansitmak icin asagidaki kodlari girmeliyiz
    graph_list.draw(main_display)
    pygame.display.update()

    # Belli bir sure bekleyecegiz
    clock.tick(FPS)

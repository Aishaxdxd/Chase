from pygame import *

window = display.set_mode((700, 500)) #500 px yukseklik ve 700 px lik boyutlara sahip bos pencere
display.set_caption("Kovalamaca") # Pencere basligi
background = transform.scale(image.load("background.png"), (700, 500))
#Arkaplan gorselinin aktarilmasi ve ekrana boyutlandirilmasi

x1 = 100
y1 = 300

x2 = 300
y2 = 300

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100)) #Karakter 1'in ekrana yerlestirilmesi
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100)) #Karakter 2'nin ekrana yerlestirilmesi
speed = 10

#Oyun dongusu:
run = True
clock = time.Clock() #bir tane clock nesnesi olusturduk. Oyun dongumuz saniyede kac defa tekrarlayacak
FPS = 60 #dongu tekrar hizi icin olusturuldu

while run:
    window.blit(background, (0, 0)) # Ekrana arkaplani yerlestiriyoruz
    window.blit(sprite1, (x1, y1)) # Ekrana karakter 1'i yerlestiriyoruz
    window.blit(sprite2, (x2, y2)) # Ekrana karakter ikiyi yerlestiriyoruz
    
    for e in event.get(): #Burada event.get listesi icerisindeki tuslara basilma olaylarini atadik
        if e.type == QUIT: # Eger bu listedeki degerlerden bir tanesi QUIT'e esitse yani x e basilmissa
            run = False # Oyunu sonlandirmak
    keys_pressed = key.get_pressed()
#karakter1
    if keys_pressed[K_LEFT] and x1 > 5: #eger sol ok tusuna basilmissa ve x1 konumu 5'ten buyukse
        x1 -= speed #sola git
    if keys_pressed[K_RIGHT] and x1 < 595: #eger sag ok tusuna basilmissa ve x1 konumu 595 'ten kucukse
        x1 += speed #saga git
    if keys_pressed[K_UP] and y1 > 5: #eger yukari tusuna basilmissa ve x1 konumu 5'ten buyukse
        y1 -= speed #yukari git
    if keys_pressed[K_DOWN] and y1 < 395: #eger asagi ok tusuna basilmissa ve y1 konumu 595'ten kucukse
        y1 += speed #asagi git  
    
#karakter2
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed #sola git
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed #saga git
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed #yukari git
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed #asagi git

    display.update() #pencereyi dongu her calistiginda gunceller
    clock.tick(FPS)















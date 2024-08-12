from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL.GLUT as glut
import pygame
import sys
w, h = 760, 760



# Warna
hitam = 0, 0, 0
putih = 255, 255, 255
coklat = 132, 82, 83
coklat_tua = 94, 54, 54
kuning = 254, 195, 90
kuning_tua = 255, 173, 17
hijau = 72, 179, 82
hijau_tua = 42, 123, 39
biru_tua = 27, 29, 98
biru_langit = 61, 200, 255
biru_awan1 = 87, 214, 255
biru_awan2 = 164, 235, 255
biru_awan3 = 221, 255, 255
hijau_button1 = 184, 222, 125
hijau_button2 = 148, 186, 86
matahari1 = 241, 233, 0
matahari2 = 229, 157, 1
tanah1 = 148, 136, 64
tanah2 = 109, 84, 47
pohon1 = 124, 96, 26
pohon2 = 93, 70, 11
level_box1 = 230, 230, 230
biru_level_box = 76, 189, 227
oren = 238, 186, 107
merah = 219, 89, 87
biru1 = 12, 80, 177
biru2 = 35, 50, 141
cream1 = 204, 132, 117
cream2 = 177, 98, 86
rumah1 = 154, 119, 89
rumah2 = 196, 155, 102
rumah3 = 232, 219, 151
rumah4 = 57, 66, 67
rumah5 = 77, 79, 128
rumah6 = 100, 177, 124

pos_x = 260
pos_y = 440
pos_x2 = 540
pos_y2 = 440
nyawa1_visible = True
nyawa2_visible = True
nyawa3_visible = True
sisa_nyawa = 3
kotak_weight = 1
game_over = False
yah_kalah = False
jawaban_salah = 0
waktu = True
notif = True

pygame.mixer.init()
pygame.mixer.music.load('Romantic Doctor.mp3')
pygame.mixer.music.play(-1)
suara_klik = pygame.mixer.Sound('klik.mp3')
suara_button = pygame.mixer.Sound('button.mp3')

HOME_SCREEN = 0
LEVEL_SCREEN = 1
GAME_SCREEN = 2
GAME_SCREEN2 = 3
GAME_SCREEN3 = 4
GAME_SCREEN4 = 5
GAME_SCREEN5 = 6
GAME_SCREEN6 = 7
GAME_SCREEN7 = 8
GAME_SCREEN8 = 9

game_mode = HOME_SCREEN
in_game_screen = False
selected_level = None
current_level = None


def load_texture(file_path):
    image = pygame.image.load(file_path)
    image_data = pygame.image.tostring(image, "RGBA_PREMULT", 1)
    width, height = image.get_size()
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    return texture_id


def draw_image(texture_id, x, y, width, height):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(x, y)
    glTexCoord2f(1, 0)
    glVertex2f(x + width, y)
    glTexCoord2f(1, 1)
    glVertex2f(x + width, y + height)
    glTexCoord2f(0, 1)
    glVertex2f(x, y + height)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def tampilan_awal():
    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def orang():
        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, kuning_tua)
        square(56, 224, 12, 20, kuning_tua)
        square(62, 244, 6, 6, kuning_tua)
        square(114, 224, 12, 13, kuning_tua)

        square(94, 212, 20, 44, kuning)
        square(114, 237, 12, 7, kuning)
        square(114, 244, 6, 6, kuning)
        square(88, 218, 6, 38, kuning)
        square(82, 230, 6, 26, kuning)
        square(74, 230, 8, 20, kuning)

        # Tangan
        square(62, 180, 6, 44, coklat)
        square(56, 186, 6, 38, coklat)

        square(120, 212, 13, 6, coklat)
        square(114, 218, 25, 6, coklat)
        square(126, 224, 13, 7, coklat)
        square(133, 231, 13, 6, coklat)
        square(139, 237, 13, 7, coklat)
        square(139, 244, 19, 6, coklat)
        square(139, 250, 6, 6, coklat)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 80, 12, hitam)

        # Leher
        square(81, 256, 19, 7, coklat_tua)

        # Kepala
        square(68, 263, 46, 83, coklat)

        square(62, 269, 6, 71, coklat)
        square(56, 276, 6, 64, coklat)
        square(49, 282, 7, 45, coklat)
        square(42, 295, 7, 19, coklat)
        square(36, 302, 6, 12, coklat)

        square(114, 269, 6, 71, coklat)
        square(120, 276, 6, 64, coklat)
        square(126, 288, 7, 32, coklat)
        square(133, 295, 6, 19, coklat)
        square(139, 302, 7, 12, coklat)

        # Bayangan
        square(68, 263, 13, 6, coklat_tua)
        square(62, 269, 13, 7, coklat_tua)
        square(56, 276, 12, 6, coklat_tua)
        square(49, 282, 13, 6, coklat_tua)
        square(49, 288, 7, 20, coklat_tua)
        square(42, 295, 7, 13, coklat_tua)
        square(36, 302, 6, 6, coklat_tua)

        square(133, 295, 6, 7, coklat_tua)
        square(139, 302, 7, 6, coklat_tua)

        square(62, 334, 13, 6, coklat_tua)
        square(68, 340, 46, 6, coklat_tua)
        square(107, 334, 19, 6, coklat_tua)
        square(120, 328, 6, 6, coklat_tua)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

    def pohon():
        # Batang
        square(662, 130, 95, 22, pohon1)
        square(672, 152, 76, 10, pohon1)
        square(684, 162, 53, 12, pohon1)
        square(694, 174, 32, 126, pohon1)
        square(716, 162, 9, 138, pohon2)
        square(725, 162, 12, 12, pohon2)
        square(737, 152, 11, 10, pohon2)
        square(748, 130, 9, 22, pohon2)

        # Daun
        square(673, 300, 73, 160, hijau)
        square(662, 311, 11, 149, hijau)
        square(651, 322, 11, 138, hijau)
        square(746, 311, 12, 149, hijau)
        square(758, 322, 10, 138, hijau)
        square(662, 460, 96, 10, hijau)
        square(673, 470, 74, 11, hijau)
        square(683, 481, 53, 10, hijau)
        square(736, 460, 22, 10, hijau_tua)
        square(747, 450, 21, 10, hijau_tua)
        square(758, 322, 10, 128, hijau_tua)
        square(746, 311, 12, 11, hijau_tua)
        square(735, 300, 11, 11, hijau_tua)

    def matahari():
        # Warna Utama
        square(625, 649, 124, 68, matahari1)
        square(618, 663, 7, 41, matahari1)
        square(749, 663, 7, 41, matahari1)

        square(632, 642, 110, 7, matahari1)
        square(639, 635, 96, 7, matahari1)
        square(646, 628, 84, 7, matahari1)
        square(653, 621, 68, 7, matahari1)
        square(666, 615, 41, 6, matahari1)

        square(632, 717, 110, 7, matahari1)
        square(639, 724, 96, 7, matahari1)
        square(646, 731, 84, 7, matahari1)
        square(653, 738, 68, 7, matahari1)
        square(666, 745, 41, 6, matahari1)

        # Bayangan
        square(666, 615, 41, 6, matahari2)
        square(701, 621, 13, 7, matahari2)
        square(653, 621, 34, 7, matahari2)
        square(646, 628, 14, 7, matahari2)
        square(666, 628, 20, 7, matahari2)
        square(639, 635, 14, 7, matahari2)
        square(660, 635, 13, 7, matahari2)
        square(632, 642, 14, 7, matahari2)
        square(653, 642, 7, 7, matahari2)
        square(625, 649, 14, 7, matahari2)
        square(646, 649, 7, 7, matahari2)
        square(625, 656, 7, 7, matahari2)
        square(639, 656, 7, 7, matahari2)
        square(618, 663, 21, 41, matahari2)
        square(625, 669, 7, 28, matahari1)
        square(653, 663, 7, 6, matahari2)
        square(646, 669, 7, 28, matahari2)
        square(625, 704, 21, 13, matahari2)
        square(632, 704, 7, 7, matahari1)
        square(632, 717, 14, 7, matahari2)
        square(639, 724, 7, 7, matahari2)
        square(653, 738, 20, 7, matahari2)
        square(666, 745, 14, 7, matahari2)

        # Percikan
        square(680, 580, 14, 28, matahari1)
        square(687, 580, 7, 21, matahari2)

        square(742, 614, 7, 7, matahari1)
        square(749, 607, 7, 7, matahari1)
        square(756, 600, 7, 7, matahari1)
        square(763, 593, 7, 7, matahari1)
        square(749, 614, 7, 7, matahari2)
        square(756, 607, 7, 7, matahari2)
        square(763, 600, 7, 7, matahari2)
        square(770, 593, 7, 7, matahari2)

        square(762, 676, 21, 14, matahari1)
        square(783, 676, 7, 14, matahari2)
        square(769, 683, 14, 7, matahari2)

        square(742, 745, 7, 7, matahari1)
        square(749, 752, 7, 7, matahari1)
        square(756, 759, 7, 7, matahari1)
        square(763, 766, 7, 7, matahari1)
        square(749, 745, 7, 7, matahari2)
        square(756, 752, 7, 7, matahari2)
        square(763, 759, 7, 7, matahari2)
        square(770, 766, 7, 7, matahari2)

        square(680, 759, 14, 28, matahari1)
        square(680, 766, 7, 21, matahari2)

        square(598, 766, 7, 7, matahari2)
        square(605, 759, 7, 7, matahari2)
        square(612, 752, 7, 7, matahari2)
        square(619, 745, 7, 7, matahari2)
        square(604, 766, 7, 7, matahari1)
        square(611, 759, 7, 7, matahari1)
        square(618, 752, 7, 7, matahari1)
        square(625, 745, 7, 7, matahari1)

        square(591, 676, 21, 14, matahari1)
        square(584, 676, 7, 14, matahari2)
        square(591, 676, 14, 7, matahari2)

        square(598, 594, 7, 7, matahari2)
        square(605, 601, 7, 7, matahari2)
        square(612, 608, 7, 7, matahari2)
        square(619, 615, 7, 7, matahari2)
        square(604, 594, 7, 7, matahari1)
        square(611, 601, 7, 7, matahari1)
        square(618, 608, 7, 7, matahari1)
        square(625, 615, 7, 7, matahari1)

    def textbox():
        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        draw_text1("Is it the sun right?", 150, 445, hitam)

    def button_start():
        # Frame
        square(290, 240, 220, 10, hitam)
        square(280, 250, 10, 10, hitam)
        square(510, 250, 10, 10, hitam)
        square(270, 260, 10, 60, hitam)
        square(520, 260, 10, 60, hitam)
        square(280, 320, 10, 10, hitam)
        square(510, 320, 10, 10, hitam)
        square(290, 330, 220, 10, hitam)

        square(290, 250, 220, 80, hijau_button1)
        square(280, 260, 10, 60, hijau_button1)
        square(510, 260, 10, 60, hijau_button1)

        square(310, 250, 200, 10, hijau_button2)
        square(500, 260, 20, 10, hijau_button2)
        square(510, 270, 10, 30, hijau_button2)

        # Text
        square(300, 265, 25, 10, hitam)
        square(325, 275, 5, 10, hitam)
        square(305, 285, 20, 5, hitam)
        square(300, 290, 5, 10, hitam)
        square(305, 300, 25, 10, hitam)

        square(350, 265, 10, 35, hitam)
        square(340, 300, 30, 10, hitam)

        square(380, 265, 5, 35, hitam)
        square(385, 280, 20, 10, hitam)
        square(385, 300, 20, 10, hitam)
        square(405, 265, 5, 35, hitam)

        square(420, 265, 10, 45, hitam)
        square(430, 285, 20, 5, hitam)
        square(430, 300, 20, 10, hitam)
        square(440, 275, 10, 10, hitam)
        square(450, 265, 10, 10, hitam)
        square(450, 290, 10, 10, hitam)

        square(480, 265, 10, 35, hitam)
        square(470, 300, 30, 10, hitam)

        # draw_text1("Click anywhere to start", 300, 210, hitam)

    langit()
    rumput()
    tanah_b()
    tanah_u()
    pohon()
    matahari()
    orang()
    textbox()
    button_start()


def tampilan_pilih_level():
    def overlay_putih():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()

    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def pohon():
        # Batang
        square(662, 130, 95, 22, pohon1)
        square(672, 152, 76, 10, pohon1)
        square(684, 162, 53, 12, pohon1)
        square(694, 174, 32, 126, pohon1)
        square(716, 162, 9, 138, pohon2)
        square(725, 162, 12, 12, pohon2)
        square(737, 152, 11, 10, pohon2)
        square(748, 130, 9, 22, pohon2)

        # Daun
        square(673, 300, 73, 160, hijau)
        square(662, 311, 11, 149, hijau)
        square(651, 322, 11, 138, hijau)
        square(746, 311, 12, 149, hijau)
        square(758, 322, 10, 138, hijau)
        square(662, 460, 96, 10, hijau)
        square(673, 470, 74, 11, hijau)
        square(683, 481, 53, 10, hijau)
        square(736, 460, 22, 10, hijau_tua)
        square(747, 450, 21, 10, hijau_tua)
        square(758, 322, 10, 128, hijau_tua)
        square(746, 311, 12, 11, hijau_tua)
        square(735, 300, 11, 11, hijau_tua)

    def matahari():
        # Warna Utama
        square(625, 649, 124, 68, matahari1)
        square(618, 663, 7, 41, matahari1)
        square(749, 663, 7, 41, matahari1)

        square(632, 642, 110, 7, matahari1)
        square(639, 635, 96, 7, matahari1)
        square(646, 628, 84, 7, matahari1)
        square(653, 621, 68, 7, matahari1)
        square(666, 615, 41, 6, matahari1)

        square(632, 717, 110, 7, matahari1)
        square(639, 724, 96, 7, matahari1)
        square(646, 731, 84, 7, matahari1)
        square(653, 738, 68, 7, matahari1)
        square(666, 745, 41, 6, matahari1)

        # Bayangan
        square(666, 615, 41, 6, matahari2)
        square(701, 621, 13, 7, matahari2)
        square(653, 621, 34, 7, matahari2)
        square(646, 628, 14, 7, matahari2)
        square(666, 628, 20, 7, matahari2)
        square(639, 635, 14, 7, matahari2)
        square(660, 635, 13, 7, matahari2)
        square(632, 642, 14, 7, matahari2)
        square(653, 642, 7, 7, matahari2)
        square(625, 649, 14, 7, matahari2)
        square(646, 649, 7, 7, matahari2)
        square(625, 656, 7, 7, matahari2)
        square(639, 656, 7, 7, matahari2)
        square(618, 663, 21, 41, matahari2)
        square(625, 669, 7, 28, matahari1)
        square(653, 663, 7, 6, matahari2)
        square(646, 669, 7, 28, matahari2)
        square(625, 704, 21, 13, matahari2)
        square(632, 704, 7, 7, matahari1)
        square(632, 717, 14, 7, matahari2)
        square(639, 724, 7, 7, matahari2)
        square(653, 738, 20, 7, matahari2)
        square(666, 745, 14, 7, matahari2)

        # Percikan
        square(680, 580, 14, 28, matahari1)
        square(687, 580, 7, 21, matahari2)

        square(742, 614, 7, 7, matahari1)
        square(749, 607, 7, 7, matahari1)
        square(756, 600, 7, 7, matahari1)
        square(763, 593, 7, 7, matahari1)
        square(749, 614, 7, 7, matahari2)
        square(756, 607, 7, 7, matahari2)
        square(763, 600, 7, 7, matahari2)
        square(770, 593, 7, 7, matahari2)

        square(762, 676, 21, 14, matahari1)
        square(783, 676, 7, 14, matahari2)
        square(769, 683, 14, 7, matahari2)

        square(742, 745, 7, 7, matahari1)
        square(749, 752, 7, 7, matahari1)
        square(756, 759, 7, 7, matahari1)
        square(763, 766, 7, 7, matahari1)
        square(749, 745, 7, 7, matahari2)
        square(756, 752, 7, 7, matahari2)
        square(763, 759, 7, 7, matahari2)
        square(770, 766, 7, 7, matahari2)

        square(680, 759, 14, 28, matahari1)
        square(680, 766, 7, 21, matahari2)

        square(598, 766, 7, 7, matahari2)
        square(605, 759, 7, 7, matahari2)
        square(612, 752, 7, 7, matahari2)
        square(619, 745, 7, 7, matahari2)
        square(604, 766, 7, 7, matahari1)
        square(611, 759, 7, 7, matahari1)
        square(618, 752, 7, 7, matahari1)
        square(625, 745, 7, 7, matahari1)

        square(591, 676, 21, 14, matahari1)
        square(584, 676, 7, 14, matahari2)
        square(591, 676, 14, 7, matahari2)

        square(598, 594, 7, 7, matahari2)
        square(605, 601, 7, 7, matahari2)
        square(612, 608, 7, 7, matahari2)
        square(619, 615, 7, 7, matahari2)
        square(604, 594, 7, 7, matahari1)
        square(611, 601, 7, 7, matahari1)
        square(618, 608, 7, 7, matahari1)
        square(625, 615, 7, 7, matahari1)

    def window_level_box():
        # Window
        square(160, 120, 470, 10, hitam)
        square(150, 130, 10, 70, hitam)
        square(630, 130, 10, 70, hitam)
        square(140, 200, 10, 390, hitam)
        square(640, 200, 10, 390, hitam)
        square(150, 590, 10, 70, hitam)
        square(630, 590, 10, 70, hitam)
        square(160, 660, 470, 10, hitam)

        square(160, 130, 470, 530, level_box1)
        square(150, 200, 10, 390, level_box1)
        square(630, 200, 10, 390, level_box1)

        # Judul
        square(240, 580, 5, 35, hitam)
        square(245, 575, 30, 5, hitam)
        square(245, 615, 30, 5, hitam)
        square(275, 580, 5, 10, hitam)
        square(275, 605, 5, 10, hitam)

        square(285, 575, 5, 45, hitam)
        square(290, 590, 10, 5, hitam)
        square(300, 595, 10, 5, hitam)
        square(310, 575, 5, 20, hitam)

        square(325, 575, 15, 5, hitam)
        square(325, 600, 15, 5, hitam)
        square(320, 580, 5, 20, hitam)
        square(340, 580, 5, 20, hitam)

        square(350, 575, 20, 5, hitam)
        square(355, 605, 20, 5, hitam)
        square(355, 590, 15, 5, hitam)
        square(350, 595, 5, 10, hitam)
        square(370, 580, 5, 10, hitam)

        square(380, 580, 5, 25, hitam)
        square(385, 575, 20, 5, hitam)
        square(385, 605, 20, 5, hitam)
        square(385, 595, 15, 5, hitam)
        square(400, 580, 5, 5, hitam)
        square(400, 595, 5, 10, hitam)

        square(420, 575, 5, 45, hitam)
        square(425, 575, 30, 5, hitam)

        square(460, 580, 5, 25, hitam)
        square(465, 575, 20, 5, hitam)
        square(465, 605, 20, 5, hitam)
        square(465, 595, 15, 5, hitam)
        square(480, 580, 5, 5, hitam)
        square(480, 595, 5, 10, hitam)

        square(490, 590, 5, 10, hitam)
        square(495, 580, 5, 10, hitam)
        square(515, 590, 5, 10, hitam)
        square(510, 580, 5, 10, hitam)
        square(500, 575, 10, 5, hitam)

        square(525, 580, 5, 25, hitam)
        square(530, 575, 20, 5, hitam)
        square(530, 605, 20, 5, hitam)
        square(530, 595, 15, 5, hitam)
        square(545, 580, 5, 5, hitam)
        square(545, 595, 5, 10, hitam)

        square(555, 575, 5, 40, hitam)

    def level_box():
        def level1():
            square(230, 480, 70, 60, biru_level_box)
            square(300, 480, 270, 60, hijau_button1)

            square(240, 470, 320, 10, hitam)
            square(240, 540, 320, 10, hitam)
            square(230, 480, 10, 10, hitam)
            square(230, 530, 10, 10, hitam)
            square(300, 480, 10, 10, hitam)
            square(300, 530, 10, 10, hitam)
            square(560, 480, 10, 10, hitam)
            square(560, 530, 10, 10, hitam)
            square(220, 490, 10, 40, hitam)
            square(290, 490, 10, 40, hitam)
            square(570, 490, 10, 40, hitam)

        def level2():
            glPushMatrix()
            glTranslatef(0.0, -100.0, 0.0)

            level1()
            glPopMatrix()

        def level3():
            glPushMatrix()
            glTranslatef(0.0, -200.0, 0.0)

            level1()

            glPopMatrix()

        def level4():
            glPushMatrix()
            glTranslatef(0.0, -300.0, 0.0)

            level1()

            glPopMatrix()

        def angka_angka():
            # Angka 1
            square(255, 493, 20, 5, hitam)
            square(262, 498, 6, 31, hitam)
            square(257, 517, 5, 5, hitam)

            # Angka 2
            square(255, 393, 20, 5, hitam)
            square(255, 398, 5, 5, hitam)
            square(260, 403, 5, 5, hitam)
            square(265, 408, 5, 5, hitam)
            square(270, 413, 5, 10, hitam)
            square(255, 413, 5, 10, hitam)
            square(260, 423, 10, 5, hitam)

            # Angka 3
            square(250, 298, 5, 5, hitam)
            square(250, 318, 5, 5, hitam)
            square(260, 308, 10, 5, hitam)
            square(255, 293, 15, 5, hitam)
            square(255, 323, 15, 5, hitam)
            square(270, 298, 5, 10, hitam)
            square(270, 313, 5, 10, hitam)

            # Angka 4
            square(250, 197, 25, 5, hitam)
            square(267, 192, 5, 35, hitam)
            square(250, 202, 5, 10, hitam)
            square(255, 212, 5, 5, hitam)
            square(260, 217, 7, 5, hitam)

        def huruf_huruf():
            # In Home
            square(353, 498, 15, 5, hitam)
            square(353, 518, 15, 5, hitam)
            square(358, 503, 5, 15, hitam)

            square(373, 498, 5, 20, hitam)
            square(388, 498, 5, 15, hitam)
            square(378, 513, 10, 5, hitam)

            square(403, 498, 5, 25, hitam)
            square(418, 498, 5, 25, hitam)
            square(408, 508, 10, 5, hitam)

            square(433, 498, 10, 5, hitam)
            square(433, 513, 10, 5, hitam)
            square(428, 503, 5, 10, hitam)
            square(443, 503, 5, 10, hitam)

            square(453, 498, 5, 20, hitam)
            square(468, 498, 5, 15, hitam)
            square(458, 513, 10, 5, hitam)
            square(483, 498, 5, 15, hitam)
            square(473, 513, 10, 5, hitam)

            square(498, 498, 15, 5, hitam)
            square(498, 513, 15, 5, hitam)
            square(498, 508, 10, 2, hitam)
            square(493, 503, 5, 10, hitam)
            square(508, 508, 5, 5, hitam)

            # Out Home
            square(342, 398, 15, 5, hitam)
            square(342, 418, 15, 5, hitam)
            square(337, 403, 5, 15, hitam)
            square(357, 403, 5, 15, hitam)

            square(367, 403, 5, 15, hitam)
            square(382, 403, 5, 15, hitam)
            square(372, 398, 15, 5, hitam)

            square(392, 413, 15, 5, hitam)
            square(397, 403, 5, 20, hitam)
            square(402, 398, 5, 5, hitam)

            square(417, 398, 5, 25, hitam)
            square(432, 398, 5, 25, hitam)
            square(422, 408, 10, 5, hitam)

            square(447, 398, 10, 5, hitam)
            square(447, 413, 10, 5, hitam)
            square(442, 403, 5, 10, hitam)
            square(457, 403, 5, 10, hitam)

            square(467, 398, 5, 20, hitam)
            square(482, 398, 5, 15, hitam)
            square(472, 413, 10, 5, hitam)
            square(497, 398, 5, 15, hitam)
            square(487, 413, 10, 5, hitam)

            square(512, 398, 15, 5, hitam)
            square(512, 413, 15, 5, hitam)
            square(512, 408, 10, 2, hitam)
            square(507, 403, 5, 10, hitam)
            square(522, 408, 5, 5, hitam)

            # At School
            square(340, 298, 5, 20, hitam)
            square(355, 298, 5, 20, hitam)
            square(345, 308, 10, 5, hitam)
            square(345, 318, 10, 5, hitam)

            square(365, 313, 15, 5, hitam)
            square(370, 303, 5, 20, hitam)
            square(375, 298, 5, 5, hitam)

            square(390, 298, 15, 5, hitam)
            square(395, 318, 15, 5, hitam)
            square(390, 313, 5, 5, hitam)
            square(405, 303, 5, 5, hitam)
            square(395, 308, 10, 5, hitam)

            square(420, 298, 10, 5, hitam)
            square(420, 313, 10, 5, hitam)
            square(415, 303, 5, 10, hitam)
            square(430, 303, 3, 3, hitam)
            square(430, 310, 3, 3, hitam)

            square(440, 298, 5, 25, hitam)
            square(445, 308, 5, 5, hitam)
            square(450, 313, 5, 5, hitam)
            square(455, 298, 5, 15, hitam)

            square(470, 298, 10, 5, hitam)
            square(470, 312, 10, 5, hitam)
            square(465, 303, 5, 10, hitam)
            square(480, 303, 5, 10, hitam)

            square(495, 298, 10, 5, hitam)
            square(495, 313, 10, 5, hitam)
            square(490, 303, 5, 10, hitam)
            square(505, 303, 5, 10, hitam)

            square(515, 298, 5, 25, hitam)

            # At Park
            square(360, 198, 5, 20, hitam)
            square(375, 198, 5, 20, hitam)
            square(365, 208, 10, 5, hitam)
            square(365, 218, 10, 5, hitam)

            square(385, 213, 15, 5, hitam)
            square(390, 203, 5, 20, hitam)
            square(395, 198, 5, 5, hitam)

            square(410, 198, 5, 25, hitam)
            square(415, 208, 10, 5, hitam)
            square(415, 218, 10, 5, hitam)
            square(425, 213, 5, 5, hitam)

            square(440, 198, 10, 5, hitam)
            square(440, 208, 10, 2, hitam)
            square(435, 203, 5, 5, hitam)
            square(435, 213, 15, 5, hitam)
            square(450, 198, 5, 15, hitam)

            square(460, 198, 5, 15, hitam)
            square(465, 213, 10, 5, hitam)

            square(480, 198, 5, 25, hitam)
            square(490, 198, 5, 10, hitam)
            square(485, 208, 5, 5, hitam)
            square(490, 213, 5, 5, hitam)

        level1()
        level2()
        level3()
        level4()
        angka_angka()
        huruf_huruf()

    def button_back():
        square(40, 35, 90, 5, hitam)
        square(40, 80, 90, 5, hitam)

        square(30, 40, 10, 5, hitam)
        square(30, 75, 10, 5, hitam)
        square(130, 40, 10, 5, hitam)
        square(130, 75, 10, 5, hitam)

        square(25, 45, 5, 30, hitam)
        square(140, 45, 5, 30, hitam)

        square(40, 40, 90, 40, oren)
        square(30, 45, 10, 30, oren)
        square(130, 45, 10, 30, oren)

        square(68, 48, 5, 5, hitam)
        square(63, 53, 5, 5, hitam)
        square(68, 68, 5, 5, hitam)
        square(63, 63, 5, 5, hitam)
        square(58, 58, 5, 5, hitam)
        square(68, 58, 40, 5, hitam)

        # draw_text2("Press 'B' to go back", 27, 20, hitam)

    def gamepad():
        glPushMatrix()
        glRotate(25, 0, 0, 1)
        glScalef(0.8, 0.8, 0.8)
        glTranslatef(160.0, -340.0, 0.0)

        square(570, 100, 90, 100, putih)

        square(520, 80, 40, 110, putih)
        square(510, 90, 10, 60, putih)
        square(530, 70, 30, 10, putih)

        square(670, 80, 40, 110, putih)
        square(710, 90, 10, 60, putih)
        square(670, 70, 30, 10, putih)

        square(560, 90, 10, 110, putih)
        square(660, 90, 10, 110, putih)

        square(530, 60, 30, 10, hitam)
        square(670, 60, 30, 10, hitam)
        square(530, 190, 30, 10, hitam)
        square(670, 190, 30, 10, hitam)

        square(520, 70, 10, 10, hitam)
        square(510, 80, 10, 10, hitam)
        square(700, 70, 10, 10, hitam)
        square(710, 80, 10, 10, hitam)
        square(520, 180, 10, 10, hitam)
        square(700, 180, 10, 10, hitam)
        square(570, 90, 10, 10, hitam)
        square(650, 90, 10, 10, hitam)

        square(500, 90, 10, 60, hitam)
        square(720, 90, 10, 60, hitam)

        square(510, 150, 10, 30, hitam)
        square(710, 150, 10, 30, hitam)

        square(560, 70, 10, 20, hitam)
        square(660, 70, 10, 20, hitam)

        square(580, 100, 70, 10, hitam)

        square(560, 200, 110, 10, hitam)

        square(550, 120, 15, 45, hitam)
        square(535, 135, 45, 15, hitam)

        square(650, 135, 15, 15, kuning)
        square(680, 135, 15, 15, merah)
        square(665, 120, 15, 15, hijau_button1)
        square(665, 150, 15, 15, biru_level_box)

        square(590, 120, 20, 5, hitam)
        square(630, 120, 20, 5, hitam)

        glPopMatrix()

    langit()
    rumput()
    tanah_b()
    tanah_u()
    pohon()
    matahari()
    overlay_putih()
    window_level_box()
    level_box()
    button_back()
    gamepad()


def tampilan_in_game():
    global sisa_nyawa, yah_kalah

    def overlay_putih():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()    

    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def rumah():
        square(450, 130, 170, 100, rumah1)
        square(480, 230, 120, 190, rumah1)
        square(480, 420, 20, 20, rumah1)
        square(540, 420, 90, 60, rumah1)
        square(600, 230, 50, 210, rumah2)
        square(630, 130, 120, 290, rumah1)
        square(640, 280, 110, 20, rumah1)
        square(630, 420, 120, 30, rumah1)

        square(750, 130, 70, 290, rumah2)
        square(640, 390, 110, 20, rumah2)
        square(645, 270, 105, 10, rumah2)

        square(455, 230, 10, 10, rumah4)
        square(500, 230, 90, 20, rumah4)
        square(500, 300, 90, 90, rumah4)
        square(670, 140, 80, 130, rumah4)
        square(670, 300, 80, 90, rumah4)
        
        square(510, 230, 70, 10, rumah3)
        square(510, 310, 70, 70, rumah3)
        square(680, 140, 70, 120, rumah3)
        square(680, 310, 70, 70, rumah3)
        square(445, 240, 30, 20, rumah3)

        square(530, 470, 60, 20, rumah5)
        square(570, 460, 60, 20, rumah5)
        square(610, 450, 60, 20, rumah5)
        square(650, 440, 60, 20, rumah5)
        square(690, 430, 60, 20, rumah5)
        square(730, 420, 60, 20, rumah5)
        square(790, 420, 40, 10, rumah5)

        square(500, 425, 100, 10, rumah6)
        square(620, 130, 10, 100, rumah6)
        square(740, 130, 10, 100, rumah6)
        square(630, 130, 110, 10, rumah6)
        square(630, 220, 110, 10, rumah6)
        square(640, 140, 10, 80, rumah6)
        square(660, 140, 10, 80, rumah6)
        square(680, 140, 10, 80, rumah6)
        square(700, 140, 10, 80, rumah6)
        square(720, 140, 10, 80, rumah6)

    def orang1():
        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, biru2)
        square(56, 224, 12, 20, biru2)
        square(62, 244, 6, 6, biru2)
        square(114, 224, 12, 13, biru2)

        square(94, 212, 20, 44, biru1)
        square(114, 237, 12, 7, biru1)
        square(114, 244, 6, 6, biru1)
        square(88, 218, 6, 38, biru1)
        square(82, 230, 6, 26, biru1)
        square(74, 230, 8, 20, biru1)

        # Tangan
        square(62, 180, 6, 44, cream1)
        square(56, 186, 6, 38, cream1)

        square(120, 212, 13, 6, cream1)
        square(114, 218, 25, 6, cream1)
        square(126, 224, 13, 7, cream1)
        square(133, 231, 13, 6, cream1)
        square(139, 237, 13, 7, cream1)
        square(139, 244, 19, 6, cream1)
        square(139, 250, 6, 6, cream1)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 82, 12, hitam)
        square(100, 384, 10, 6, hitam)
        square(110, 384, 10, 16, hitam)
        square(120, 384, 12, 26, hitam)

        # Leher
        square(81, 256, 19, 7, cream2)

        # Kepala
        square(68, 263, 46, 83, cream1)

        square(62, 269, 6, 71, cream1)
        square(56, 276, 6, 64, cream1)
        square(49, 282, 7, 45, cream1)
        square(42, 295, 7, 19, cream1)
        square(36, 302, 6, 12, cream1)

        square(114, 269, 6, 71, cream1)
        square(120, 276, 6, 64, cream1)
        square(126, 288, 7, 32, cream1)
        square(133, 295, 6, 19, cream1)
        square(139, 302, 7, 12, cream1)

        # Bayangan
        square(68, 263, 13, 6, cream2)
        square(62, 269, 13, 7, cream2)
        square(56, 276, 12, 6, cream2)
        square(49, 282, 13, 6, cream2)
        square(49, 288, 7, 20, cream2)
        square(42, 295, 7, 13, cream2)
        square(36, 302, 6, 6, cream2)

        square(133, 295, 6, 7, cream2)
        square(139, 302, 7, 6, cream2)

        square(62, 334, 13, 6, cream2)
        square(68, 340, 46, 6, cream2)
        square(107, 334, 19, 6, cream2)
        square(120, 328, 6, 6, cream2)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

    def orang2():
        glPushMatrix()
        glScalef(-1.0, 1.0, 1.0)  
        glTranslatef(-800.0, 0.0, 0.0)

        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, kuning_tua)
        square(56, 224, 12, 20, kuning_tua)
        square(62, 244, 6, 6, kuning_tua)
        square(114, 224, 12, 13, kuning_tua)

        square(94, 212, 20, 44, kuning)
        square(114, 237, 12, 7, kuning)
        square(114, 244, 6, 6, kuning)
        square(88, 218, 6, 38, kuning)
        square(82, 230, 6, 26, kuning)
        square(74, 230, 8, 20, kuning)

        # Tangan
        square(62, 180, 6, 44, coklat)
        square(56, 186, 6, 38, coklat)

        square(120, 212, 13, 6, coklat)
        square(114, 218, 25, 6, coklat)
        square(126, 224, 13, 7, coklat)
        square(133, 231, 13, 6, coklat)
        square(139, 237, 13, 7, coklat)
        square(139, 244, 19, 6, coklat)
        square(139, 250, 6, 6, coklat)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 80, 12, hitam)

        # Leher
        square(81, 256, 19, 7, coklat_tua)

        # Kepala
        square(68, 263, 46, 83, coklat)

        square(62, 269, 6, 71, coklat)
        square(56, 276, 6, 64, coklat)
        square(49, 282, 7, 45, coklat)
        square(42, 295, 7, 19, coklat)
        square(36, 302, 6, 12, coklat)

        square(114, 269, 6, 71, coklat)
        square(120, 276, 6, 64, coklat)
        square(126, 288, 7, 32, coklat)
        square(133, 295, 6, 19, coklat)
        square(139, 302, 7, 12, coklat)

        # Bayangan
        square(68, 263, 13, 6, coklat_tua)
        square(62, 269, 13, 7, coklat_tua)
        square(56, 276, 12, 6, coklat_tua)
        square(49, 282, 13, 6, coklat_tua)
        square(49, 288, 7, 20, coklat_tua)
        square(42, 295, 7, 13, coklat_tua)
        square(36, 302, 6, 6, coklat_tua)

        square(133, 295, 6, 7, coklat_tua)
        square(139, 302, 7, 6, coklat_tua)

        square(62, 334, 13, 6, coklat_tua)
        square(68, 340, 46, 6, coklat_tua)
        square(107, 334, 19, 6, coklat_tua)
        square(120, 328, 6, 6, coklat_tua)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

        glPopMatrix()

    def textbox1():
        glPushMatrix()
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("Is it a ...", 200, 342, hitam)

    def textbox2():
        glPushMatrix()
        glScale(-1.0, 1.0, 1.0)
        glTranslatef(-800.0, 0.0, 0.0)
        
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("What is that?", 517, 342, hitam)

    def pilihan1():
        square(220, 60, 120, 10, hitam)
        square(220, 150, 120, 10, hitam)

        square(210, 70, 10, 10, hitam)
        square(210, 140, 10, 10, hitam)
        square(340, 70, 10, 10, hitam)
        square(340, 140, 10, 10, hitam)

        square(200, 80, 10, 60, hitam)
        square(350, 80, 10, 60, hitam)

        square(220, 70, 120, 80, biru_level_box)
        square(210, 80, 10, 60, biru_level_box)
        square(340, 80, 10, 60, biru_level_box)

        draw_text1("Flag", 258, 105, hitam)

    def pilihan2():
        square(460, 60, 120, 10, hitam)
        square(460, 150, 120, 10, hitam)

        square(450, 70, 10, 10, hitam)
        square(450, 140, 10, 10, hitam)
        square(580, 70, 10, 10, hitam)
        square(580, 140, 10, 10, hitam)

        square(440, 80, 10, 60, hitam)
        square(590, 80, 10, 60, hitam)

        square(460, 70, 120, 80, oren)
        square(450, 80, 10, 60, oren)
        square(580, 80, 10, 60, oren)

        draw_text1("Frog", 498, 105, hitam)

    def bar_waktu():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(260, 440)
        glVertex2f(540, 440)
        glVertex2f(540, 460)
        glVertex2f(260, 460)
        glEnd()

        # square(260, 440, 140, 20, merah)

        square(258, 438, 284, 2, hitam)
        square(258, 460, 284, 2, hitam)

        square(258, 440, 2, 20, hitam)
        

    def box_benda():
        square(330, 540, 140, 120, putih)

        square(340, 530, 120, 10, hitam)
        square(340, 660, 120, 10, hitam)

        square(330, 540, 10, 20, hitam)
        square(330, 640, 10, 20, hitam)
        square(460, 540, 10, 20, hitam)
        square(460, 640, 10, 20, hitam)

        square(320, 560, 10, 80, hitam)
        square(470, 560, 10, 80, hitam)

        draw_image(load_texture('bendera.png'), 320, 520, 160, 160)

    
    
    langit()
    rumah()
    overlay_putih()
    rumput()
    tanah_b()
    tanah_u()
    orang1()
    orang2()
    textbox1()
    textbox2()
    pilihan1()
    pilihan2()
    bar_waktu()
    box_benda()

    if sisa_nyawa > 0:
        nyawa1()
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 2:
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 1:
        nyawa3()
    else:
        if not yah_kalah:
            print("Notif Kalah")
            yah_kalah = True

def tampilan_in_game2():
    global sisa_nyawa, yah_kalah

    def overlay_putih():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()    

    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def rumah():
        square(450, 130, 170, 100, rumah1)
        square(480, 230, 120, 190, rumah1)
        square(480, 420, 20, 20, rumah1)
        square(540, 420, 90, 60, rumah1)
        square(600, 230, 50, 210, rumah2)
        square(630, 130, 120, 290, rumah1)
        square(640, 280, 110, 20, rumah1)
        square(630, 420, 120, 30, rumah1)

        square(750, 130, 70, 290, rumah2)
        square(640, 390, 110, 20, rumah2)
        square(645, 270, 105, 10, rumah2)

        square(455, 230, 10, 10, rumah4)
        square(500, 230, 90, 20, rumah4)
        square(500, 300, 90, 90, rumah4)
        square(670, 140, 80, 130, rumah4)
        square(670, 300, 80, 90, rumah4)
        
        square(510, 230, 70, 10, rumah3)
        square(510, 310, 70, 70, rumah3)
        square(680, 140, 70, 120, rumah3)
        square(680, 310, 70, 70, rumah3)
        square(445, 240, 30, 20, rumah3)

        square(530, 470, 60, 20, rumah5)
        square(570, 460, 60, 20, rumah5)
        square(610, 450, 60, 20, rumah5)
        square(650, 440, 60, 20, rumah5)
        square(690, 430, 60, 20, rumah5)
        square(730, 420, 60, 20, rumah5)
        square(790, 420, 40, 10, rumah5)

        square(500, 425, 100, 10, rumah6)
        square(620, 130, 10, 100, rumah6)
        square(740, 130, 10, 100, rumah6)
        square(630, 130, 110, 10, rumah6)
        square(630, 220, 110, 10, rumah6)
        square(640, 140, 10, 80, rumah6)
        square(660, 140, 10, 80, rumah6)
        square(680, 140, 10, 80, rumah6)
        square(700, 140, 10, 80, rumah6)
        square(720, 140, 10, 80, rumah6)

    def orang1():
        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, biru2)
        square(56, 224, 12, 20, biru2)
        square(62, 244, 6, 6, biru2)
        square(114, 224, 12, 13, biru2)

        square(94, 212, 20, 44, biru1)
        square(114, 237, 12, 7, biru1)
        square(114, 244, 6, 6, biru1)
        square(88, 218, 6, 38, biru1)
        square(82, 230, 6, 26, biru1)
        square(74, 230, 8, 20, biru1)

        # Tangan
        square(62, 180, 6, 44, cream1)
        square(56, 186, 6, 38, cream1)

        square(120, 212, 13, 6, cream1)
        square(114, 218, 25, 6, cream1)
        square(126, 224, 13, 7, cream1)
        square(133, 231, 13, 6, cream1)
        square(139, 237, 13, 7, cream1)
        square(139, 244, 19, 6, cream1)
        square(139, 250, 6, 6, cream1)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 82, 12, hitam)
        square(100, 384, 10, 6, hitam)
        square(110, 384, 10, 16, hitam)
        square(120, 384, 12, 26, hitam)

        # Leher
        square(81, 256, 19, 7, cream2)

        # Kepala
        square(68, 263, 46, 83, cream1)

        square(62, 269, 6, 71, cream1)
        square(56, 276, 6, 64, cream1)
        square(49, 282, 7, 45, cream1)
        square(42, 295, 7, 19, cream1)
        square(36, 302, 6, 12, cream1)

        square(114, 269, 6, 71, cream1)
        square(120, 276, 6, 64, cream1)
        square(126, 288, 7, 32, cream1)
        square(133, 295, 6, 19, cream1)
        square(139, 302, 7, 12, cream1)

        # Bayangan
        square(68, 263, 13, 6, cream2)
        square(62, 269, 13, 7, cream2)
        square(56, 276, 12, 6, cream2)
        square(49, 282, 13, 6, cream2)
        square(49, 288, 7, 20, cream2)
        square(42, 295, 7, 13, cream2)
        square(36, 302, 6, 6, cream2)

        square(133, 295, 6, 7, cream2)
        square(139, 302, 7, 6, cream2)

        square(62, 334, 13, 6, cream2)
        square(68, 340, 46, 6, cream2)
        square(107, 334, 19, 6, cream2)
        square(120, 328, 6, 6, cream2)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

    def orang2():
        glPushMatrix()
        glScalef(-1.0, 1.0, 1.0)  
        glTranslatef(-800.0, 0.0, 0.0)

        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, kuning_tua)
        square(56, 224, 12, 20, kuning_tua)
        square(62, 244, 6, 6, kuning_tua)
        square(114, 224, 12, 13, kuning_tua)

        square(94, 212, 20, 44, kuning)
        square(114, 237, 12, 7, kuning)
        square(114, 244, 6, 6, kuning)
        square(88, 218, 6, 38, kuning)
        square(82, 230, 6, 26, kuning)
        square(74, 230, 8, 20, kuning)

        # Tangan
        square(62, 180, 6, 44, coklat)
        square(56, 186, 6, 38, coklat)

        square(120, 212, 13, 6, coklat)
        square(114, 218, 25, 6, coklat)
        square(126, 224, 13, 7, coklat)
        square(133, 231, 13, 6, coklat)
        square(139, 237, 13, 7, coklat)
        square(139, 244, 19, 6, coklat)
        square(139, 250, 6, 6, coklat)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 80, 12, hitam)

        # Leher
        square(81, 256, 19, 7, coklat_tua)

        # Kepala
        square(68, 263, 46, 83, coklat)

        square(62, 269, 6, 71, coklat)
        square(56, 276, 6, 64, coklat)
        square(49, 282, 7, 45, coklat)
        square(42, 295, 7, 19, coklat)
        square(36, 302, 6, 12, coklat)

        square(114, 269, 6, 71, coklat)
        square(120, 276, 6, 64, coklat)
        square(126, 288, 7, 32, coklat)
        square(133, 295, 6, 19, coklat)
        square(139, 302, 7, 12, coklat)

        # Bayangan
        square(68, 263, 13, 6, coklat_tua)
        square(62, 269, 13, 7, coklat_tua)
        square(56, 276, 12, 6, coklat_tua)
        square(49, 282, 13, 6, coklat_tua)
        square(49, 288, 7, 20, coklat_tua)
        square(42, 295, 7, 13, coklat_tua)
        square(36, 302, 6, 6, coklat_tua)

        square(133, 295, 6, 7, coklat_tua)
        square(139, 302, 7, 6, coklat_tua)

        square(62, 334, 13, 6, coklat_tua)
        square(68, 340, 46, 6, coklat_tua)
        square(107, 334, 19, 6, coklat_tua)
        square(120, 328, 6, 6, coklat_tua)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

        glPopMatrix()

    def textbox1():
        glPushMatrix()
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("Is it a ...", 200, 342, hitam)

    def textbox2():
        glPushMatrix()
        glScale(-1.0, 1.0, 1.0)
        glTranslatef(-800.0, 0.0, 0.0)
        
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("What is that?", 517, 342, hitam)

    def pilihan1():
        square(220, 60, 120, 10, hitam)
        square(220, 150, 120, 10, hitam)

        square(210, 70, 10, 10, hitam)
        square(210, 140, 10, 10, hitam)
        square(340, 70, 10, 10, hitam)
        square(340, 140, 10, 10, hitam)

        square(200, 80, 10, 60, hitam)
        square(350, 80, 10, 60, hitam)

        square(220, 70, 120, 80, biru_level_box)
        square(210, 80, 10, 60, biru_level_box)
        square(340, 80, 10, 60, biru_level_box)

        draw_text1("Bed", 258, 105, hitam)

    def pilihan2():
        square(460, 60, 120, 10, hitam)
        square(460, 150, 120, 10, hitam)

        square(450, 70, 10, 10, hitam)
        square(450, 140, 10, 10, hitam)
        square(580, 70, 10, 10, hitam)
        square(580, 140, 10, 10, hitam)

        square(440, 80, 10, 60, hitam)
        square(590, 80, 10, 60, hitam)

        square(460, 70, 120, 80, oren)
        square(450, 80, 10, 60, oren)
        square(580, 80, 10, 60, oren)

        draw_text1("Bad", 498, 105, hitam)

    def bar_waktu():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(260, 440)
        glVertex2f(540, 440)
        glVertex2f(540, 460)
        glVertex2f(260, 460)
        glEnd()

        # square(260, 440, 140, 20, merah)

        square(258, 438, 284, 2, hitam)
        square(258, 460, 284, 2, hitam)

        square(258, 440, 2, 20, hitam)
        

    def box_benda():
        square(330, 540, 140, 120, putih)

        square(340, 530, 120, 10, hitam)
        square(340, 660, 120, 10, hitam)

        square(330, 540, 10, 20, hitam)
        square(330, 640, 10, 20, hitam)
        square(460, 540, 10, 20, hitam)
        square(460, 640, 10, 20, hitam)

        square(320, 560, 10, 80, hitam)
        square(470, 560, 10, 80, hitam)

        draw_image(load_texture('kasur.png'), 340, 540, 120, 120)


    
    langit()
    rumah()
    overlay_putih()
    rumput()
    tanah_b()
    tanah_u()
    orang1()
    orang2()
    textbox1()
    textbox2()
    pilihan1()
    pilihan2()
    bar_waktu()
    box_benda()

    if sisa_nyawa > 0:
        nyawa1()
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 2:
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 1:
        nyawa3()
    else:
        if not yah_kalah:
            print("Notif Kalah")
            yah_kalah = True

def tampilan_in_game3():
    global sisa_nyawa, yah_kalah

    def overlay_putih():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()    

    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def rumah():
        square(450, 130, 170, 100, rumah1)
        square(480, 230, 120, 190, rumah1)
        square(480, 420, 20, 20, rumah1)
        square(540, 420, 90, 60, rumah1)
        square(600, 230, 50, 210, rumah2)
        square(630, 130, 120, 290, rumah1)
        square(640, 280, 110, 20, rumah1)
        square(630, 420, 120, 30, rumah1)

        square(750, 130, 70, 290, rumah2)
        square(640, 390, 110, 20, rumah2)
        square(645, 270, 105, 10, rumah2)

        square(455, 230, 10, 10, rumah4)
        square(500, 230, 90, 20, rumah4)
        square(500, 300, 90, 90, rumah4)
        square(670, 140, 80, 130, rumah4)
        square(670, 300, 80, 90, rumah4)
        
        square(510, 230, 70, 10, rumah3)
        square(510, 310, 70, 70, rumah3)
        square(680, 140, 70, 120, rumah3)
        square(680, 310, 70, 70, rumah3)
        square(445, 240, 30, 20, rumah3)

        square(530, 470, 60, 20, rumah5)
        square(570, 460, 60, 20, rumah5)
        square(610, 450, 60, 20, rumah5)
        square(650, 440, 60, 20, rumah5)
        square(690, 430, 60, 20, rumah5)
        square(730, 420, 60, 20, rumah5)
        square(790, 420, 40, 10, rumah5)

        square(500, 425, 100, 10, rumah6)
        square(620, 130, 10, 100, rumah6)
        square(740, 130, 10, 100, rumah6)
        square(630, 130, 110, 10, rumah6)
        square(630, 220, 110, 10, rumah6)
        square(640, 140, 10, 80, rumah6)
        square(660, 140, 10, 80, rumah6)
        square(680, 140, 10, 80, rumah6)
        square(700, 140, 10, 80, rumah6)
        square(720, 140, 10, 80, rumah6)

    def orang1():
        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, biru2)
        square(56, 224, 12, 20, biru2)
        square(62, 244, 6, 6, biru2)
        square(114, 224, 12, 13, biru2)

        square(94, 212, 20, 44, biru1)
        square(114, 237, 12, 7, biru1)
        square(114, 244, 6, 6, biru1)
        square(88, 218, 6, 38, biru1)
        square(82, 230, 6, 26, biru1)
        square(74, 230, 8, 20, biru1)

        # Tangan
        square(62, 180, 6, 44, cream1)
        square(56, 186, 6, 38, cream1)

        square(120, 212, 13, 6, cream1)
        square(114, 218, 25, 6, cream1)
        square(126, 224, 13, 7, cream1)
        square(133, 231, 13, 6, cream1)
        square(139, 237, 13, 7, cream1)
        square(139, 244, 19, 6, cream1)
        square(139, 250, 6, 6, cream1)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 82, 12, hitam)
        square(100, 384, 10, 6, hitam)
        square(110, 384, 10, 16, hitam)
        square(120, 384, 12, 26, hitam)

        # Leher
        square(81, 256, 19, 7, cream2)

        # Kepala
        square(68, 263, 46, 83, cream1)

        square(62, 269, 6, 71, cream1)
        square(56, 276, 6, 64, cream1)
        square(49, 282, 7, 45, cream1)
        square(42, 295, 7, 19, cream1)
        square(36, 302, 6, 12, cream1)

        square(114, 269, 6, 71, cream1)
        square(120, 276, 6, 64, cream1)
        square(126, 288, 7, 32, cream1)
        square(133, 295, 6, 19, cream1)
        square(139, 302, 7, 12, cream1)

        # Bayangan
        square(68, 263, 13, 6, cream2)
        square(62, 269, 13, 7, cream2)
        square(56, 276, 12, 6, cream2)
        square(49, 282, 13, 6, cream2)
        square(49, 288, 7, 20, cream2)
        square(42, 295, 7, 13, cream2)
        square(36, 302, 6, 6, cream2)

        square(133, 295, 6, 7, cream2)
        square(139, 302, 7, 6, cream2)

        square(62, 334, 13, 6, cream2)
        square(68, 340, 46, 6, cream2)
        square(107, 334, 19, 6, cream2)
        square(120, 328, 6, 6, cream2)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

    def orang2():
        glPushMatrix()
        glScalef(-1.0, 1.0, 1.0)  
        glTranslatef(-800.0, 0.0, 0.0)

        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, kuning_tua)
        square(56, 224, 12, 20, kuning_tua)
        square(62, 244, 6, 6, kuning_tua)
        square(114, 224, 12, 13, kuning_tua)

        square(94, 212, 20, 44, kuning)
        square(114, 237, 12, 7, kuning)
        square(114, 244, 6, 6, kuning)
        square(88, 218, 6, 38, kuning)
        square(82, 230, 6, 26, kuning)
        square(74, 230, 8, 20, kuning)

        # Tangan
        square(62, 180, 6, 44, coklat)
        square(56, 186, 6, 38, coklat)

        square(120, 212, 13, 6, coklat)
        square(114, 218, 25, 6, coklat)
        square(126, 224, 13, 7, coklat)
        square(133, 231, 13, 6, coklat)
        square(139, 237, 13, 7, coklat)
        square(139, 244, 19, 6, coklat)
        square(139, 250, 6, 6, coklat)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 80, 12, hitam)

        # Leher
        square(81, 256, 19, 7, coklat_tua)

        # Kepala
        square(68, 263, 46, 83, coklat)

        square(62, 269, 6, 71, coklat)
        square(56, 276, 6, 64, coklat)
        square(49, 282, 7, 45, coklat)
        square(42, 295, 7, 19, coklat)
        square(36, 302, 6, 12, coklat)

        square(114, 269, 6, 71, coklat)
        square(120, 276, 6, 64, coklat)
        square(126, 288, 7, 32, coklat)
        square(133, 295, 6, 19, coklat)
        square(139, 302, 7, 12, coklat)

        # Bayangan
        square(68, 263, 13, 6, coklat_tua)
        square(62, 269, 13, 7, coklat_tua)
        square(56, 276, 12, 6, coklat_tua)
        square(49, 282, 13, 6, coklat_tua)
        square(49, 288, 7, 20, coklat_tua)
        square(42, 295, 7, 13, coklat_tua)
        square(36, 302, 6, 6, coklat_tua)

        square(133, 295, 6, 7, coklat_tua)
        square(139, 302, 7, 6, coklat_tua)

        square(62, 334, 13, 6, coklat_tua)
        square(68, 340, 46, 6, coklat_tua)
        square(107, 334, 19, 6, coklat_tua)
        square(120, 328, 6, 6, coklat_tua)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

        glPopMatrix()

    def textbox1():
        glPushMatrix()
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("Is it a ...", 200, 342, hitam)

    def textbox2():
        glPushMatrix()
        glScale(-1.0, 1.0, 1.0)
        glTranslatef(-800.0, 0.0, 0.0)
        
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("What is that?", 517, 342, hitam)

    def pilihan1():
        square(220, 60, 120, 10, hitam)
        square(220, 150, 120, 10, hitam)

        square(210, 70, 10, 10, hitam)
        square(210, 140, 10, 10, hitam)
        square(340, 70, 10, 10, hitam)
        square(340, 140, 10, 10, hitam)

        square(200, 80, 10, 60, hitam)
        square(350, 80, 10, 60, hitam)

        square(220, 70, 120, 80, biru_level_box)
        square(210, 80, 10, 60, biru_level_box)
        square(340, 80, 10, 60, biru_level_box)

        draw_text1("Chair", 258, 105, hitam)

    def pilihan2():
        square(460, 60, 120, 10, hitam)
        square(460, 150, 120, 10, hitam)

        square(450, 70, 10, 10, hitam)
        square(450, 140, 10, 10, hitam)
        square(580, 70, 10, 10, hitam)
        square(580, 140, 10, 10, hitam)

        square(440, 80, 10, 60, hitam)
        square(590, 80, 10, 60, hitam)

        square(460, 70, 120, 80, oren)
        square(450, 80, 10, 60, oren)
        square(580, 80, 10, 60, oren)

        draw_text1("Car", 498, 105, hitam)

    def bar_waktu():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(260, 440)
        glVertex2f(540, 440)
        glVertex2f(540, 460)
        glVertex2f(260, 460)
        glEnd()

        # square(260, 440, 140, 20, merah)

        square(258, 438, 284, 2, hitam)
        square(258, 460, 284, 2, hitam)

        square(258, 440, 2, 20, hitam)
        

    def box_benda():
        square(330, 540, 140, 120, putih)

        square(340, 530, 120, 10, hitam)
        square(340, 660, 120, 10, hitam)

        square(330, 540, 10, 20, hitam)
        square(330, 640, 10, 20, hitam)
        square(460, 540, 10, 20, hitam)
        square(460, 640, 10, 20, hitam)

        square(320, 560, 10, 80, hitam)
        square(470, 560, 10, 80, hitam)

        draw_image(load_texture('kursi.png'), 345, 540, 120, 120)

    
    langit()
    rumah()
    overlay_putih()
    rumput()
    tanah_b()
    tanah_u()
    orang1()
    orang2()
    textbox1()
    textbox2()
    pilihan1()
    pilihan2()
    bar_waktu()
    box_benda()

    if sisa_nyawa > 0:
        nyawa1()
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 2:
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 1:
        nyawa3()
    else:
        if not yah_kalah:
            print("Notif Kalah")
            yah_kalah = True

def tampilan_in_game4():
    global sisa_nyawa, yah_kalah

    def overlay_putih():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()    

    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def rumah():
        square(450, 130, 170, 100, rumah1)
        square(480, 230, 120, 190, rumah1)
        square(480, 420, 20, 20, rumah1)
        square(540, 420, 90, 60, rumah1)
        square(600, 230, 50, 210, rumah2)
        square(630, 130, 120, 290, rumah1)
        square(640, 280, 110, 20, rumah1)
        square(630, 420, 120, 30, rumah1)

        square(750, 130, 70, 290, rumah2)
        square(640, 390, 110, 20, rumah2)
        square(645, 270, 105, 10, rumah2)

        square(455, 230, 10, 10, rumah4)
        square(500, 230, 90, 20, rumah4)
        square(500, 300, 90, 90, rumah4)
        square(670, 140, 80, 130, rumah4)
        square(670, 300, 80, 90, rumah4)
        
        square(510, 230, 70, 10, rumah3)
        square(510, 310, 70, 70, rumah3)
        square(680, 140, 70, 120, rumah3)
        square(680, 310, 70, 70, rumah3)
        square(445, 240, 30, 20, rumah3)

        square(530, 470, 60, 20, rumah5)
        square(570, 460, 60, 20, rumah5)
        square(610, 450, 60, 20, rumah5)
        square(650, 440, 60, 20, rumah5)
        square(690, 430, 60, 20, rumah5)
        square(730, 420, 60, 20, rumah5)
        square(790, 420, 40, 10, rumah5)

        square(500, 425, 100, 10, rumah6)
        square(620, 130, 10, 100, rumah6)
        square(740, 130, 10, 100, rumah6)
        square(630, 130, 110, 10, rumah6)
        square(630, 220, 110, 10, rumah6)
        square(640, 140, 10, 80, rumah6)
        square(660, 140, 10, 80, rumah6)
        square(680, 140, 10, 80, rumah6)
        square(700, 140, 10, 80, rumah6)
        square(720, 140, 10, 80, rumah6)

    def orang1():
        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, biru2)
        square(56, 224, 12, 20, biru2)
        square(62, 244, 6, 6, biru2)
        square(114, 224, 12, 13, biru2)

        square(94, 212, 20, 44, biru1)
        square(114, 237, 12, 7, biru1)
        square(114, 244, 6, 6, biru1)
        square(88, 218, 6, 38, biru1)
        square(82, 230, 6, 26, biru1)
        square(74, 230, 8, 20, biru1)

        # Tangan
        square(62, 180, 6, 44, cream1)
        square(56, 186, 6, 38, cream1)

        square(120, 212, 13, 6, cream1)
        square(114, 218, 25, 6, cream1)
        square(126, 224, 13, 7, cream1)
        square(133, 231, 13, 6, cream1)
        square(139, 237, 13, 7, cream1)
        square(139, 244, 19, 6, cream1)
        square(139, 250, 6, 6, cream1)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 82, 12, hitam)
        square(100, 384, 10, 6, hitam)
        square(110, 384, 10, 16, hitam)
        square(120, 384, 12, 26, hitam)

        # Leher
        square(81, 256, 19, 7, cream2)

        # Kepala
        square(68, 263, 46, 83, cream1)

        square(62, 269, 6, 71, cream1)
        square(56, 276, 6, 64, cream1)
        square(49, 282, 7, 45, cream1)
        square(42, 295, 7, 19, cream1)
        square(36, 302, 6, 12, cream1)

        square(114, 269, 6, 71, cream1)
        square(120, 276, 6, 64, cream1)
        square(126, 288, 7, 32, cream1)
        square(133, 295, 6, 19, cream1)
        square(139, 302, 7, 12, cream1)

        # Bayangan
        square(68, 263, 13, 6, cream2)
        square(62, 269, 13, 7, cream2)
        square(56, 276, 12, 6, cream2)
        square(49, 282, 13, 6, cream2)
        square(49, 288, 7, 20, cream2)
        square(42, 295, 7, 13, cream2)
        square(36, 302, 6, 6, cream2)

        square(133, 295, 6, 7, cream2)
        square(139, 302, 7, 6, cream2)

        square(62, 334, 13, 6, cream2)
        square(68, 340, 46, 6, cream2)
        square(107, 334, 19, 6, cream2)
        square(120, 328, 6, 6, cream2)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

    def orang2():
        glPushMatrix()
        glScalef(-1.0, 1.0, 1.0)  
        glTranslatef(-800.0, 0.0, 0.0)

        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, kuning_tua)
        square(56, 224, 12, 20, kuning_tua)
        square(62, 244, 6, 6, kuning_tua)
        square(114, 224, 12, 13, kuning_tua)

        square(94, 212, 20, 44, kuning)
        square(114, 237, 12, 7, kuning)
        square(114, 244, 6, 6, kuning)
        square(88, 218, 6, 38, kuning)
        square(82, 230, 6, 26, kuning)
        square(74, 230, 8, 20, kuning)

        # Tangan
        square(62, 180, 6, 44, coklat)
        square(56, 186, 6, 38, coklat)

        square(120, 212, 13, 6, coklat)
        square(114, 218, 25, 6, coklat)
        square(126, 224, 13, 7, coklat)
        square(133, 231, 13, 6, coklat)
        square(139, 237, 13, 7, coklat)
        square(139, 244, 19, 6, coklat)
        square(139, 250, 6, 6, coklat)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 80, 12, hitam)

        # Leher
        square(81, 256, 19, 7, coklat_tua)

        # Kepala
        square(68, 263, 46, 83, coklat)

        square(62, 269, 6, 71, coklat)
        square(56, 276, 6, 64, coklat)
        square(49, 282, 7, 45, coklat)
        square(42, 295, 7, 19, coklat)
        square(36, 302, 6, 12, coklat)

        square(114, 269, 6, 71, coklat)
        square(120, 276, 6, 64, coklat)
        square(126, 288, 7, 32, coklat)
        square(133, 295, 6, 19, coklat)
        square(139, 302, 7, 12, coklat)

        # Bayangan
        square(68, 263, 13, 6, coklat_tua)
        square(62, 269, 13, 7, coklat_tua)
        square(56, 276, 12, 6, coklat_tua)
        square(49, 282, 13, 6, coklat_tua)
        square(49, 288, 7, 20, coklat_tua)
        square(42, 295, 7, 13, coklat_tua)
        square(36, 302, 6, 6, coklat_tua)

        square(133, 295, 6, 7, coklat_tua)
        square(139, 302, 7, 6, coklat_tua)

        square(62, 334, 13, 6, coklat_tua)
        square(68, 340, 46, 6, coklat_tua)
        square(107, 334, 19, 6, coklat_tua)
        square(120, 328, 6, 6, coklat_tua)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

        glPopMatrix()

    def textbox1():
        glPushMatrix()
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("Is it a ...", 200, 342, hitam)

    def textbox2():
        glPushMatrix()
        glScale(-1.0, 1.0, 1.0)
        glTranslatef(-800.0, 0.0, 0.0)
        
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("What is that?", 517, 342, hitam)

    def pilihan1():
        square(220, 60, 120, 10, hitam)
        square(220, 150, 120, 10, hitam)

        square(210, 70, 10, 10, hitam)
        square(210, 140, 10, 10, hitam)
        square(340, 70, 10, 10, hitam)
        square(340, 140, 10, 10, hitam)

        square(200, 80, 10, 60, hitam)
        square(350, 80, 10, 60, hitam)

        square(220, 70, 120, 80, biru_level_box)
        square(210, 80, 10, 60, biru_level_box)
        square(340, 80, 10, 60, biru_level_box)

        draw_text1("Table", 258, 105, hitam)

    def pilihan2():
        square(460, 60, 120, 10, hitam)
        square(460, 150, 120, 10, hitam)

        square(450, 70, 10, 10, hitam)
        square(450, 140, 10, 10, hitam)
        square(580, 70, 10, 10, hitam)
        square(580, 140, 10, 10, hitam)

        square(440, 80, 10, 60, hitam)
        square(590, 80, 10, 60, hitam)

        square(460, 70, 120, 80, oren)
        square(450, 80, 10, 60, oren)
        square(580, 80, 10, 60, oren)

        draw_text1("Tabel", 498, 105, hitam)

    def bar_waktu():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(260, 440)
        glVertex2f(540, 440)
        glVertex2f(540, 460)
        glVertex2f(260, 460)
        glEnd()

        # square(260, 440, 140, 20, merah)

        square(258, 438, 284, 2, hitam)
        square(258, 460, 284, 2, hitam)

        square(258, 440, 2, 20, hitam)
        

    def box_benda():
        square(330, 540, 140, 120, putih)

        square(340, 530, 120, 10, hitam)
        square(340, 660, 120, 10, hitam)

        square(330, 540, 10, 20, hitam)
        square(330, 640, 10, 20, hitam)
        square(460, 540, 10, 20, hitam)
        square(460, 640, 10, 20, hitam)

        square(320, 560, 10, 80, hitam)
        square(470, 560, 10, 80, hitam)

        draw_image(load_texture('meja.png'), 330, 530, 140, 140)

    
    langit()
    rumah()
    overlay_putih()
    rumput()
    tanah_b()
    tanah_u()
    orang1()
    orang2()
    textbox1()
    textbox2()
    pilihan1()
    pilihan2()
    bar_waktu()
    box_benda()

    if sisa_nyawa > 0:
        nyawa1()
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 2:
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 1:
        nyawa3()
    else:
        if not yah_kalah:
            print("Notif Kalah")
            yah_kalah = True

def tampilan_in_game5():
    global sisa_nyawa, yah_kalah

    def overlay_putih():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()    

    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def rumah():
        square(450, 130, 170, 100, rumah1)
        square(480, 230, 120, 190, rumah1)
        square(480, 420, 20, 20, rumah1)
        square(540, 420, 90, 60, rumah1)
        square(600, 230, 50, 210, rumah2)
        square(630, 130, 120, 290, rumah1)
        square(640, 280, 110, 20, rumah1)
        square(630, 420, 120, 30, rumah1)

        square(750, 130, 70, 290, rumah2)
        square(640, 390, 110, 20, rumah2)
        square(645, 270, 105, 10, rumah2)

        square(455, 230, 10, 10, rumah4)
        square(500, 230, 90, 20, rumah4)
        square(500, 300, 90, 90, rumah4)
        square(670, 140, 80, 130, rumah4)
        square(670, 300, 80, 90, rumah4)
        
        square(510, 230, 70, 10, rumah3)
        square(510, 310, 70, 70, rumah3)
        square(680, 140, 70, 120, rumah3)
        square(680, 310, 70, 70, rumah3)
        square(445, 240, 30, 20, rumah3)

        square(530, 470, 60, 20, rumah5)
        square(570, 460, 60, 20, rumah5)
        square(610, 450, 60, 20, rumah5)
        square(650, 440, 60, 20, rumah5)
        square(690, 430, 60, 20, rumah5)
        square(730, 420, 60, 20, rumah5)
        square(790, 420, 40, 10, rumah5)

        square(500, 425, 100, 10, rumah6)
        square(620, 130, 10, 100, rumah6)
        square(740, 130, 10, 100, rumah6)
        square(630, 130, 110, 10, rumah6)
        square(630, 220, 110, 10, rumah6)
        square(640, 140, 10, 80, rumah6)
        square(660, 140, 10, 80, rumah6)
        square(680, 140, 10, 80, rumah6)
        square(700, 140, 10, 80, rumah6)
        square(720, 140, 10, 80, rumah6)

    def orang1():
        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, biru2)
        square(56, 224, 12, 20, biru2)
        square(62, 244, 6, 6, biru2)
        square(114, 224, 12, 13, biru2)

        square(94, 212, 20, 44, biru1)
        square(114, 237, 12, 7, biru1)
        square(114, 244, 6, 6, biru1)
        square(88, 218, 6, 38, biru1)
        square(82, 230, 6, 26, biru1)
        square(74, 230, 8, 20, biru1)

        # Tangan
        square(62, 180, 6, 44, cream1)
        square(56, 186, 6, 38, cream1)

        square(120, 212, 13, 6, cream1)
        square(114, 218, 25, 6, cream1)
        square(126, 224, 13, 7, cream1)
        square(133, 231, 13, 6, cream1)
        square(139, 237, 13, 7, cream1)
        square(139, 244, 19, 6, cream1)
        square(139, 250, 6, 6, cream1)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 82, 12, hitam)
        square(100, 384, 10, 6, hitam)
        square(110, 384, 10, 16, hitam)
        square(120, 384, 12, 26, hitam)

        # Leher
        square(81, 256, 19, 7, cream2)

        # Kepala
        square(68, 263, 46, 83, cream1)

        square(62, 269, 6, 71, cream1)
        square(56, 276, 6, 64, cream1)
        square(49, 282, 7, 45, cream1)
        square(42, 295, 7, 19, cream1)
        square(36, 302, 6, 12, cream1)

        square(114, 269, 6, 71, cream1)
        square(120, 276, 6, 64, cream1)
        square(126, 288, 7, 32, cream1)
        square(133, 295, 6, 19, cream1)
        square(139, 302, 7, 12, cream1)

        # Bayangan
        square(68, 263, 13, 6, cream2)
        square(62, 269, 13, 7, cream2)
        square(56, 276, 12, 6, cream2)
        square(49, 282, 13, 6, cream2)
        square(49, 288, 7, 20, cream2)
        square(42, 295, 7, 13, cream2)
        square(36, 302, 6, 6, cream2)

        square(133, 295, 6, 7, cream2)
        square(139, 302, 7, 6, cream2)

        square(62, 334, 13, 6, cream2)
        square(68, 340, 46, 6, cream2)
        square(107, 334, 19, 6, cream2)
        square(120, 328, 6, 6, cream2)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

    def orang2():
        glPushMatrix()
        glScalef(-1.0, 1.0, 1.0)  
        glTranslatef(-800.0, 0.0, 0.0)

        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, kuning_tua)
        square(56, 224, 12, 20, kuning_tua)
        square(62, 244, 6, 6, kuning_tua)
        square(114, 224, 12, 13, kuning_tua)

        square(94, 212, 20, 44, kuning)
        square(114, 237, 12, 7, kuning)
        square(114, 244, 6, 6, kuning)
        square(88, 218, 6, 38, kuning)
        square(82, 230, 6, 26, kuning)
        square(74, 230, 8, 20, kuning)

        # Tangan
        square(62, 180, 6, 44, coklat)
        square(56, 186, 6, 38, coklat)

        square(120, 212, 13, 6, coklat)
        square(114, 218, 25, 6, coklat)
        square(126, 224, 13, 7, coklat)
        square(133, 231, 13, 6, coklat)
        square(139, 237, 13, 7, coklat)
        square(139, 244, 19, 6, coklat)
        square(139, 250, 6, 6, coklat)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 80, 12, hitam)

        # Leher
        square(81, 256, 19, 7, coklat_tua)

        # Kepala
        square(68, 263, 46, 83, coklat)

        square(62, 269, 6, 71, coklat)
        square(56, 276, 6, 64, coklat)
        square(49, 282, 7, 45, coklat)
        square(42, 295, 7, 19, coklat)
        square(36, 302, 6, 12, coklat)

        square(114, 269, 6, 71, coklat)
        square(120, 276, 6, 64, coklat)
        square(126, 288, 7, 32, coklat)
        square(133, 295, 6, 19, coklat)
        square(139, 302, 7, 12, coklat)

        # Bayangan
        square(68, 263, 13, 6, coklat_tua)
        square(62, 269, 13, 7, coklat_tua)
        square(56, 276, 12, 6, coklat_tua)
        square(49, 282, 13, 6, coklat_tua)
        square(49, 288, 7, 20, coklat_tua)
        square(42, 295, 7, 13, coklat_tua)
        square(36, 302, 6, 6, coklat_tua)

        square(133, 295, 6, 7, coklat_tua)
        square(139, 302, 7, 6, coklat_tua)

        square(62, 334, 13, 6, coklat_tua)
        square(68, 340, 46, 6, coklat_tua)
        square(107, 334, 19, 6, coklat_tua)
        square(120, 328, 6, 6, coklat_tua)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

        glPopMatrix()

    def textbox1():
        glPushMatrix()
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("Is it a ...", 200, 342, hitam)

    def textbox2():
        glPushMatrix()
        glScale(-1.0, 1.0, 1.0)
        glTranslatef(-800.0, 0.0, 0.0)
        
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("What is that?", 517, 342, hitam)

    def pilihan1():
        square(220, 60, 120, 10, hitam)
        square(220, 150, 120, 10, hitam)

        square(210, 70, 10, 10, hitam)
        square(210, 140, 10, 10, hitam)
        square(340, 70, 10, 10, hitam)
        square(340, 140, 10, 10, hitam)

        square(200, 80, 10, 60, hitam)
        square(350, 80, 10, 60, hitam)

        square(220, 70, 120, 80, biru_level_box)
        square(210, 80, 10, 60, biru_level_box)
        square(340, 80, 10, 60, biru_level_box)

        draw_text1("Tree", 258, 105, hitam)

    def pilihan2():
        square(460, 60, 120, 10, hitam)
        square(460, 150, 120, 10, hitam)

        square(450, 70, 10, 10, hitam)
        square(450, 140, 10, 10, hitam)
        square(580, 70, 10, 10, hitam)
        square(580, 140, 10, 10, hitam)

        square(440, 80, 10, 60, hitam)
        square(590, 80, 10, 60, hitam)

        square(460, 70, 120, 80, oren)
        square(450, 80, 10, 60, oren)
        square(580, 80, 10, 60, oren)

        draw_text1("Three", 498, 105, hitam)

    def bar_waktu():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(260, 440)
        glVertex2f(540, 440)
        glVertex2f(540, 460)
        glVertex2f(260, 460)
        glEnd()

        # square(260, 440, 140, 20, merah)

        square(258, 438, 284, 2, hitam)
        square(258, 460, 284, 2, hitam)

        square(258, 440, 2, 20, hitam)
        

    def box_benda():
        square(330, 540, 140, 120, putih)

        square(340, 530, 120, 10, hitam)
        square(340, 660, 120, 10, hitam)

        square(330, 540, 10, 20, hitam)
        square(330, 640, 10, 20, hitam)
        square(460, 540, 10, 20, hitam)
        square(460, 640, 10, 20, hitam)

        square(320, 560, 10, 80, hitam)
        square(470, 560, 10, 80, hitam)

        draw_image(load_texture('pohon.png'), 320, 520, 160, 160)

    
    langit()
    rumah()
    overlay_putih()
    rumput()
    tanah_b()
    tanah_u()
    orang1()
    orang2()
    textbox1()
    textbox2()
    pilihan1()
    pilihan2()
    bar_waktu()
    box_benda()

    if sisa_nyawa > 0:
        nyawa1()
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 2:
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 1:
        nyawa3()
    else:
        if not yah_kalah:
            print("Notif Kalah")
            yah_kalah = True

def tampilan_in_game6():
    global sisa_nyawa, yah_kalah

    def overlay_putih():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()    

    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def rumah():
        square(450, 130, 170, 100, rumah1)
        square(480, 230, 120, 190, rumah1)
        square(480, 420, 20, 20, rumah1)
        square(540, 420, 90, 60, rumah1)
        square(600, 230, 50, 210, rumah2)
        square(630, 130, 120, 290, rumah1)
        square(640, 280, 110, 20, rumah1)
        square(630, 420, 120, 30, rumah1)

        square(750, 130, 70, 290, rumah2)
        square(640, 390, 110, 20, rumah2)
        square(645, 270, 105, 10, rumah2)

        square(455, 230, 10, 10, rumah4)
        square(500, 230, 90, 20, rumah4)
        square(500, 300, 90, 90, rumah4)
        square(670, 140, 80, 130, rumah4)
        square(670, 300, 80, 90, rumah4)
        
        square(510, 230, 70, 10, rumah3)
        square(510, 310, 70, 70, rumah3)
        square(680, 140, 70, 120, rumah3)
        square(680, 310, 70, 70, rumah3)
        square(445, 240, 30, 20, rumah3)

        square(530, 470, 60, 20, rumah5)
        square(570, 460, 60, 20, rumah5)
        square(610, 450, 60, 20, rumah5)
        square(650, 440, 60, 20, rumah5)
        square(690, 430, 60, 20, rumah5)
        square(730, 420, 60, 20, rumah5)
        square(790, 420, 40, 10, rumah5)

        square(500, 425, 100, 10, rumah6)
        square(620, 130, 10, 100, rumah6)
        square(740, 130, 10, 100, rumah6)
        square(630, 130, 110, 10, rumah6)
        square(630, 220, 110, 10, rumah6)
        square(640, 140, 10, 80, rumah6)
        square(660, 140, 10, 80, rumah6)
        square(680, 140, 10, 80, rumah6)
        square(700, 140, 10, 80, rumah6)
        square(720, 140, 10, 80, rumah6)

    def orang1():
        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, biru2)
        square(56, 224, 12, 20, biru2)
        square(62, 244, 6, 6, biru2)
        square(114, 224, 12, 13, biru2)

        square(94, 212, 20, 44, biru1)
        square(114, 237, 12, 7, biru1)
        square(114, 244, 6, 6, biru1)
        square(88, 218, 6, 38, biru1)
        square(82, 230, 6, 26, biru1)
        square(74, 230, 8, 20, biru1)

        # Tangan
        square(62, 180, 6, 44, cream1)
        square(56, 186, 6, 38, cream1)

        square(120, 212, 13, 6, cream1)
        square(114, 218, 25, 6, cream1)
        square(126, 224, 13, 7, cream1)
        square(133, 231, 13, 6, cream1)
        square(139, 237, 13, 7, cream1)
        square(139, 244, 19, 6, cream1)
        square(139, 250, 6, 6, cream1)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 82, 12, hitam)
        square(100, 384, 10, 6, hitam)
        square(110, 384, 10, 16, hitam)
        square(120, 384, 12, 26, hitam)

        # Leher
        square(81, 256, 19, 7, cream2)

        # Kepala
        square(68, 263, 46, 83, cream1)

        square(62, 269, 6, 71, cream1)
        square(56, 276, 6, 64, cream1)
        square(49, 282, 7, 45, cream1)
        square(42, 295, 7, 19, cream1)
        square(36, 302, 6, 12, cream1)

        square(114, 269, 6, 71, cream1)
        square(120, 276, 6, 64, cream1)
        square(126, 288, 7, 32, cream1)
        square(133, 295, 6, 19, cream1)
        square(139, 302, 7, 12, cream1)

        # Bayangan
        square(68, 263, 13, 6, cream2)
        square(62, 269, 13, 7, cream2)
        square(56, 276, 12, 6, cream2)
        square(49, 282, 13, 6, cream2)
        square(49, 288, 7, 20, cream2)
        square(42, 295, 7, 13, cream2)
        square(36, 302, 6, 6, cream2)

        square(133, 295, 6, 7, cream2)
        square(139, 302, 7, 6, cream2)

        square(62, 334, 13, 6, cream2)
        square(68, 340, 46, 6, cream2)
        square(107, 334, 19, 6, cream2)
        square(120, 328, 6, 6, cream2)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

    def orang2():
        glPushMatrix()
        glScalef(-1.0, 1.0, 1.0)  
        glTranslatef(-800.0, 0.0, 0.0)

        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, kuning_tua)
        square(56, 224, 12, 20, kuning_tua)
        square(62, 244, 6, 6, kuning_tua)
        square(114, 224, 12, 13, kuning_tua)

        square(94, 212, 20, 44, kuning)
        square(114, 237, 12, 7, kuning)
        square(114, 244, 6, 6, kuning)
        square(88, 218, 6, 38, kuning)
        square(82, 230, 6, 26, kuning)
        square(74, 230, 8, 20, kuning)

        # Tangan
        square(62, 180, 6, 44, coklat)
        square(56, 186, 6, 38, coklat)

        square(120, 212, 13, 6, coklat)
        square(114, 218, 25, 6, coklat)
        square(126, 224, 13, 7, coklat)
        square(133, 231, 13, 6, coklat)
        square(139, 237, 13, 7, coklat)
        square(139, 244, 19, 6, coklat)
        square(139, 250, 6, 6, coklat)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 80, 12, hitam)

        # Leher
        square(81, 256, 19, 7, coklat_tua)

        # Kepala
        square(68, 263, 46, 83, coklat)

        square(62, 269, 6, 71, coklat)
        square(56, 276, 6, 64, coklat)
        square(49, 282, 7, 45, coklat)
        square(42, 295, 7, 19, coklat)
        square(36, 302, 6, 12, coklat)

        square(114, 269, 6, 71, coklat)
        square(120, 276, 6, 64, coklat)
        square(126, 288, 7, 32, coklat)
        square(133, 295, 6, 19, coklat)
        square(139, 302, 7, 12, coklat)

        # Bayangan
        square(68, 263, 13, 6, coklat_tua)
        square(62, 269, 13, 7, coklat_tua)
        square(56, 276, 12, 6, coklat_tua)
        square(49, 282, 13, 6, coklat_tua)
        square(49, 288, 7, 20, coklat_tua)
        square(42, 295, 7, 13, coklat_tua)
        square(36, 302, 6, 6, coklat_tua)

        square(133, 295, 6, 7, coklat_tua)
        square(139, 302, 7, 6, coklat_tua)

        square(62, 334, 13, 6, coklat_tua)
        square(68, 340, 46, 6, coklat_tua)
        square(107, 334, 19, 6, coklat_tua)
        square(120, 328, 6, 6, coklat_tua)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

        glPopMatrix()

    def textbox1():
        glPushMatrix()
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("Is it a ...", 200, 342, hitam)

    def textbox2():
        glPushMatrix()
        glScale(-1.0, 1.0, 1.0)
        glTranslatef(-800.0, 0.0, 0.0)
        
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("What is that?", 517, 342, hitam)

    def pilihan1():
        square(220, 60, 120, 10, hitam)
        square(220, 150, 120, 10, hitam)

        square(210, 70, 10, 10, hitam)
        square(210, 140, 10, 10, hitam)
        square(340, 70, 10, 10, hitam)
        square(340, 140, 10, 10, hitam)

        square(200, 80, 10, 60, hitam)
        square(350, 80, 10, 60, hitam)

        square(220, 70, 120, 80, biru_level_box)
        square(210, 80, 10, 60, biru_level_box)
        square(340, 80, 10, 60, biru_level_box)

        draw_text1("Bus", 258, 105, hitam)

    def pilihan2():
        square(460, 60, 120, 10, hitam)
        square(460, 150, 120, 10, hitam)

        square(450, 70, 10, 10, hitam)
        square(450, 140, 10, 10, hitam)
        square(580, 70, 10, 10, hitam)
        square(580, 140, 10, 10, hitam)

        square(440, 80, 10, 60, hitam)
        square(590, 80, 10, 60, hitam)

        square(460, 70, 120, 80, oren)
        square(450, 80, 10, 60, oren)
        square(580, 80, 10, 60, oren)

        draw_text1("Telolet", 498, 105, hitam)

    def bar_waktu():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(260, 440)
        glVertex2f(540, 440)
        glVertex2f(540, 460)
        glVertex2f(260, 460)
        glEnd()

        # square(260, 440, 140, 20, merah)

        square(258, 438, 284, 2, hitam)
        square(258, 460, 284, 2, hitam)

        square(258, 440, 2, 20, hitam)
        

    def box_benda():
        square(330, 540, 140, 120, putih)

        square(340, 530, 120, 10, hitam)
        square(340, 660, 120, 10, hitam)

        square(330, 540, 10, 20, hitam)
        square(330, 640, 10, 20, hitam)
        square(460, 540, 10, 20, hitam)
        square(460, 640, 10, 20, hitam)

        square(320, 560, 10, 80, hitam)
        square(470, 560, 10, 80, hitam)

        draw_image(load_texture('bus.png'), 345, 540, 120, 120)

    
    langit()
    rumah()
    overlay_putih()
    rumput()
    tanah_b()
    tanah_u()
    orang1()
    orang2()
    textbox1()
    textbox2()
    pilihan1()
    pilihan2()
    bar_waktu()
    box_benda()

    if sisa_nyawa > 0:
        nyawa1()
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 2:
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 1:
        nyawa3()
    else:
        if not yah_kalah:
            print("Notif Kalah")
            yah_kalah = True

def tampilan_in_game7():
    global sisa_nyawa, yah_kalah

    def overlay_putih():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()    

    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def rumah():
        square(450, 130, 170, 100, rumah1)
        square(480, 230, 120, 190, rumah1)
        square(480, 420, 20, 20, rumah1)
        square(540, 420, 90, 60, rumah1)
        square(600, 230, 50, 210, rumah2)
        square(630, 130, 120, 290, rumah1)
        square(640, 280, 110, 20, rumah1)
        square(630, 420, 120, 30, rumah1)

        square(750, 130, 70, 290, rumah2)
        square(640, 390, 110, 20, rumah2)
        square(645, 270, 105, 10, rumah2)

        square(455, 230, 10, 10, rumah4)
        square(500, 230, 90, 20, rumah4)
        square(500, 300, 90, 90, rumah4)
        square(670, 140, 80, 130, rumah4)
        square(670, 300, 80, 90, rumah4)
        
        square(510, 230, 70, 10, rumah3)
        square(510, 310, 70, 70, rumah3)
        square(680, 140, 70, 120, rumah3)
        square(680, 310, 70, 70, rumah3)
        square(445, 240, 30, 20, rumah3)

        square(530, 470, 60, 20, rumah5)
        square(570, 460, 60, 20, rumah5)
        square(610, 450, 60, 20, rumah5)
        square(650, 440, 60, 20, rumah5)
        square(690, 430, 60, 20, rumah5)
        square(730, 420, 60, 20, rumah5)
        square(790, 420, 40, 10, rumah5)

        square(500, 425, 100, 10, rumah6)
        square(620, 130, 10, 100, rumah6)
        square(740, 130, 10, 100, rumah6)
        square(630, 130, 110, 10, rumah6)
        square(630, 220, 110, 10, rumah6)
        square(640, 140, 10, 80, rumah6)
        square(660, 140, 10, 80, rumah6)
        square(680, 140, 10, 80, rumah6)
        square(700, 140, 10, 80, rumah6)
        square(720, 140, 10, 80, rumah6)

    def orang1():
        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, biru2)
        square(56, 224, 12, 20, biru2)
        square(62, 244, 6, 6, biru2)
        square(114, 224, 12, 13, biru2)

        square(94, 212, 20, 44, biru1)
        square(114, 237, 12, 7, biru1)
        square(114, 244, 6, 6, biru1)
        square(88, 218, 6, 38, biru1)
        square(82, 230, 6, 26, biru1)
        square(74, 230, 8, 20, biru1)

        # Tangan
        square(62, 180, 6, 44, cream1)
        square(56, 186, 6, 38, cream1)

        square(120, 212, 13, 6, cream1)
        square(114, 218, 25, 6, cream1)
        square(126, 224, 13, 7, cream1)
        square(133, 231, 13, 6, cream1)
        square(139, 237, 13, 7, cream1)
        square(139, 244, 19, 6, cream1)
        square(139, 250, 6, 6, cream1)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 82, 12, hitam)
        square(100, 384, 10, 6, hitam)
        square(110, 384, 10, 16, hitam)
        square(120, 384, 12, 26, hitam)

        # Leher
        square(81, 256, 19, 7, cream2)

        # Kepala
        square(68, 263, 46, 83, cream1)

        square(62, 269, 6, 71, cream1)
        square(56, 276, 6, 64, cream1)
        square(49, 282, 7, 45, cream1)
        square(42, 295, 7, 19, cream1)
        square(36, 302, 6, 12, cream1)

        square(114, 269, 6, 71, cream1)
        square(120, 276, 6, 64, cream1)
        square(126, 288, 7, 32, cream1)
        square(133, 295, 6, 19, cream1)
        square(139, 302, 7, 12, cream1)

        # Bayangan
        square(68, 263, 13, 6, cream2)
        square(62, 269, 13, 7, cream2)
        square(56, 276, 12, 6, cream2)
        square(49, 282, 13, 6, cream2)
        square(49, 288, 7, 20, cream2)
        square(42, 295, 7, 13, cream2)
        square(36, 302, 6, 6, cream2)

        square(133, 295, 6, 7, cream2)
        square(139, 302, 7, 6, cream2)

        square(62, 334, 13, 6, cream2)
        square(68, 340, 46, 6, cream2)
        square(107, 334, 19, 6, cream2)
        square(120, 328, 6, 6, cream2)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

    def orang2():
        glPushMatrix()
        glScalef(-1.0, 1.0, 1.0)  
        glTranslatef(-800.0, 0.0, 0.0)

        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, kuning_tua)
        square(56, 224, 12, 20, kuning_tua)
        square(62, 244, 6, 6, kuning_tua)
        square(114, 224, 12, 13, kuning_tua)

        square(94, 212, 20, 44, kuning)
        square(114, 237, 12, 7, kuning)
        square(114, 244, 6, 6, kuning)
        square(88, 218, 6, 38, kuning)
        square(82, 230, 6, 26, kuning)
        square(74, 230, 8, 20, kuning)

        # Tangan
        square(62, 180, 6, 44, coklat)
        square(56, 186, 6, 38, coklat)

        square(120, 212, 13, 6, coklat)
        square(114, 218, 25, 6, coklat)
        square(126, 224, 13, 7, coklat)
        square(133, 231, 13, 6, coklat)
        square(139, 237, 13, 7, coklat)
        square(139, 244, 19, 6, coklat)
        square(139, 250, 6, 6, coklat)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 80, 12, hitam)

        # Leher
        square(81, 256, 19, 7, coklat_tua)

        # Kepala
        square(68, 263, 46, 83, coklat)

        square(62, 269, 6, 71, coklat)
        square(56, 276, 6, 64, coklat)
        square(49, 282, 7, 45, coklat)
        square(42, 295, 7, 19, coklat)
        square(36, 302, 6, 12, coklat)

        square(114, 269, 6, 71, coklat)
        square(120, 276, 6, 64, coklat)
        square(126, 288, 7, 32, coklat)
        square(133, 295, 6, 19, coklat)
        square(139, 302, 7, 12, coklat)

        # Bayangan
        square(68, 263, 13, 6, coklat_tua)
        square(62, 269, 13, 7, coklat_tua)
        square(56, 276, 12, 6, coklat_tua)
        square(49, 282, 13, 6, coklat_tua)
        square(49, 288, 7, 20, coklat_tua)
        square(42, 295, 7, 13, coklat_tua)
        square(36, 302, 6, 6, coklat_tua)

        square(133, 295, 6, 7, coklat_tua)
        square(139, 302, 7, 6, coklat_tua)

        square(62, 334, 13, 6, coklat_tua)
        square(68, 340, 46, 6, coklat_tua)
        square(107, 334, 19, 6, coklat_tua)
        square(120, 328, 6, 6, coklat_tua)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

        glPopMatrix()

    def textbox1():
        glPushMatrix()
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("Is it a ...", 200, 342, hitam)

    def textbox2():
        glPushMatrix()
        glScale(-1.0, 1.0, 1.0)
        glTranslatef(-800.0, 0.0, 0.0)
        
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("What is that?", 517, 342, hitam)

    def pilihan1():
        square(220, 60, 120, 10, hitam)
        square(220, 150, 120, 10, hitam)

        square(210, 70, 10, 10, hitam)
        square(210, 140, 10, 10, hitam)
        square(340, 70, 10, 10, hitam)
        square(340, 140, 10, 10, hitam)

        square(200, 80, 10, 60, hitam)
        square(350, 80, 10, 60, hitam)

        square(220, 70, 120, 80, biru_level_box)
        square(210, 80, 10, 60, biru_level_box)
        square(340, 80, 10, 60, biru_level_box)

        draw_text1("Slippers", 258, 105, hitam)

    def pilihan2():
        square(460, 60, 120, 10, hitam)
        square(460, 150, 120, 10, hitam)

        square(450, 70, 10, 10, hitam)
        square(450, 140, 10, 10, hitam)
        square(580, 70, 10, 10, hitam)
        square(580, 140, 10, 10, hitam)

        square(440, 80, 10, 60, hitam)
        square(590, 80, 10, 60, hitam)

        square(460, 70, 120, 80, oren)
        square(450, 80, 10, 60, oren)
        square(580, 80, 10, 60, oren)

        draw_text1("Swallow", 498, 105, hitam)

    def bar_waktu():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(260, 440)
        glVertex2f(540, 440)
        glVertex2f(540, 460)
        glVertex2f(260, 460)
        glEnd()

        # square(260, 440, 140, 20, merah)

        square(258, 438, 284, 2, hitam)
        square(258, 460, 284, 2, hitam)

        square(258, 440, 2, 20, hitam)
        

    def box_benda():
        square(330, 540, 140, 120, putih)

        square(340, 530, 120, 10, hitam)
        square(340, 660, 120, 10, hitam)

        square(330, 540, 10, 20, hitam)
        square(330, 640, 10, 20, hitam)
        square(460, 540, 10, 20, hitam)
        square(460, 640, 10, 20, hitam)

        square(320, 560, 10, 80, hitam)
        square(470, 560, 10, 80, hitam)

        draw_image(load_texture('sandal.png'), 320, 520, 160, 160)

    
    langit()
    rumah()
    overlay_putih()
    rumput()
    tanah_b()
    tanah_u()
    orang1()
    orang2()
    textbox1()
    textbox2()
    pilihan1()
    pilihan2()
    bar_waktu()
    box_benda()

    if sisa_nyawa > 0:
        nyawa1()
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 2:
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 1:
        nyawa3()
    else:
        if not yah_kalah:
            print("Notif Kalah")
            yah_kalah = True


def tampilan_in_game8():
    global sisa_nyawa, yah_kalah

    def overlay_putih():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()    

    def langit():
        # Langit
        square(0, 130, 800, 670, biru_langit)

        # Awan 1
        square(0, 100, 400, 340, biru_awan1)

        square(0, 440, 310, 50, biru_awan1)
        square(0, 490, 210, 10, biru_awan1)
        square(0, 500, 190, 10, biru_awan1)
        square(0, 510, 160, 10, biru_awan1)
        square(0, 520, 110, 10, biru_awan1)
        square(0, 530, 70, 10, biru_awan1)

        square(340, 440, 60, 10, biru_awan1)
        square(350, 450, 50, 10, biru_awan1)
        square(370, 460, 30, 10, biru_awan1)

        # Awan 2
        square(0, 100, 800, 200, biru_awan2)

        square(20, 300, 780, 20, biru_awan2)
        square(60, 320, 740, 20, biru_awan2)

        square(120, 340, 680, 10, biru_awan2)
        square(120, 350, 210, 10, biru_awan2)
        square(120, 360, 180, 10, biru_awan2)
        square(120, 370, 170, 10, biru_awan2)
        square(120, 380, 165, 10, biru_awan2)
        square(120, 390, 145, 10, biru_awan2)
        square(160, 400, 80, 5, biru_awan2)
        square(185, 405, 55, 5, biru_awan2)

        square(340, 350, 460, 30, biru_awan2)
        square(350, 380, 450, 30, biru_awan2)
        square(360, 410, 440, 20, biru_awan2)
        square(370, 430, 415,  10, biru_awan2)
        square(375, 440, 405,  20, biru_awan2)
        square(385, 460, 395,  5, biru_awan2)
        square(400, 465, 295,  15, biru_awan2)
        square(405, 480, 290,  5, biru_awan2)
        square(415, 485, 280,  10, biru_awan2)
        square(425, 495, 260,  10, biru_awan2)
        square(445, 505, 190,  10, biru_awan2)
        square(475, 515, 140,  10, biru_awan2)
        square(495, 525, 80,  10, biru_awan2)

        # Awan 3
        square(0, 100, 800, 100, biru_awan3)

        square(0, 200, 100, 30, biru_awan3)
        square(0, 230, 70, 20, biru_awan3)
        square(0, 250, 40, 10, biru_awan3)

        square(130, 200, 670, 30, biru_awan3)

        square(160, 230, 355, 10, biru_awan3)
        square(170, 240, 345, 10, biru_awan3)
        square(190, 250, 305, 10, biru_awan3)
        square(220, 260, 275, 10, biru_awan3)
        square(260, 270, 235, 10, biru_awan3)
        square(260, 280, 180, 10, biru_awan3)

        square(515, 230, 285, 10, biru_awan3)

        square(555, 240, 145, 5, biru_awan3)
        square(575, 245, 125, 10, biru_awan3)
        square(595, 255, 75, 10, biru_awan3)

        square(735, 240, 65, 30, biru_awan3)
        square(740, 270, 60, 5, biru_awan3)
        square(755, 275, 45, 10, biru_awan3)
        square(765, 285, 35, 20, biru_awan3)
        square(775, 305, 25, 15, biru_awan3)
        square(790, 320, 10, 5, biru_awan3)
        square(795, 325, 5, 10, biru_awan3)

    def tanah_b():
        # Tanah
        square(0, 0, 310, 20, tanah2)

        square(10, 20, 80, 10, tanah2)
        square(20, 30, 40, 10, tanah2)
        square(30, 40, 10, 10, tanah2)

        square(100, 20, 110, 10, tanah2)
        square(110, 30, 90, 10, tanah2)
        square(110, 40, 80, 10, tanah2)
        square(120, 50, 70, 10, tanah2)
        square(120, 60, 40, 10, tanah2)
        square(130, 70, 10, 10, tanah2)

        square(220, 20, 80, 10, tanah2)
        square(220, 30, 30, 10, tanah2)
        square(230, 40, 10, 10, tanah2)
        square(260, 30, 40, 10, tanah2)
        square(270, 40, 20, 20, tanah2)
        square(280, 60, 10, 10, tanah2)

        square(320, 0, 200, 20, tanah2)
        square(330, 20, 90, 10, tanah2)
        square(340, 30, 10, 10, tanah2)
        square(370, 30, 40, 10, tanah2)
        square(380, 40, 20, 10, tanah2)
        square(390, 50, 10, 10, tanah2)

        square(440, 20, 80, 10, tanah2)
        square(450, 30, 30, 10, tanah2)
        square(490, 30, 10, 10, tanah2)
        square(460, 40, 10, 10, tanah2)

        square(540, 0, 20, 20, tanah2)
        square(560, 0, 10, 20, tanah2)

        square(570, 0, 230, 20, tanah2)

        square(580, 20, 50, 10, tanah2)
        square(590, 30, 30, 10, tanah2)
        square(600, 40, 20, 10, tanah2)
        square(610, 50, 10, 20, tanah2)

        square(640, 20, 120, 10, tanah2)
        square(650, 30, 20, 10, tanah2)
        square(690, 30, 50, 10, tanah2)
        square(690, 40, 40, 10, tanah2)
        square(700, 50, 30, 10, tanah2)
        square(700, 60, 20, 10, tanah2)
        square(710, 70, 10, 20, tanah2)

        square(760, 20, 40, 10, tanah2)
        square(770, 30, 30, 10, tanah2)
        square(780, 40, 10, 30, tanah2)

    def tanah_u():
        glPushMatrix()
        glTranslatef(0.0, -10.0, 0.0)

        square(0, 0, 310, 20, tanah1)

        square(10, 20, 80, 10, tanah1)
        square(20, 30, 40, 10, tanah1)
        square(30, 40, 10, 10, tanah1)

        square(100, 20, 110, 10, tanah1)
        square(110, 30, 90, 10, tanah1)
        square(110, 40, 80, 10, tanah1)
        square(120, 50, 70, 10, tanah1)
        square(120, 60, 40, 10, tanah1)
        square(130, 70, 10, 10, tanah1)

        square(220, 20, 80, 10, tanah1)
        square(220, 30, 30, 10, tanah1)
        square(230, 40, 10, 10, tanah1)
        square(260, 30, 40, 10, tanah1)
        square(270, 40, 20, 20, tanah1)
        square(280, 60, 10, 10, tanah1)

        square(320, 0, 200, 20, tanah1)
        square(330, 20, 90, 10, tanah1)
        square(340, 30, 10, 10, tanah1)
        square(370, 30, 40, 10, tanah1)
        square(380, 40, 20, 10, tanah1)
        square(390, 50, 10, 10, tanah1)

        square(440, 20, 80, 10, tanah1)
        square(450, 30, 30, 10, tanah1)
        square(490, 30, 10, 10, tanah1)
        square(460, 40, 10, 10, tanah1)

        square(540, 0, 20, 20, tanah1)
        square(560, 0, 10, 20, tanah1)

        square(570, 0, 230, 20, tanah1)

        square(580, 20, 50, 10, tanah1)
        square(590, 30, 30, 10, tanah1)
        square(600, 40, 20, 10, tanah1)
        square(610, 50, 10, 20, tanah1)

        square(640, 20, 120, 10, tanah1)
        square(650, 30, 20, 10, tanah1)
        square(690, 30, 50, 10, tanah1)
        square(690, 40, 40, 10, tanah1)
        square(700, 50, 30, 10, tanah1)
        square(700, 60, 20, 10, tanah1)
        square(710, 70, 10, 20, tanah1)

        square(760, 20, 40, 10, tanah1)
        square(770, 30, 30, 10, tanah1)
        square(780, 40, 10, 30, tanah1)

        glPopMatrix()

    def rumput():
        square(0, 0, 800, 125, hijau)
        square(0, 125, 800, 5, hijau_tua)

        square(10, 80, 10, 20, hijau_tua)
        square(20, 100, 10, 10, hijau_tua)
        square(30, 90, 10, 10, hijau_tua)
        square(40, 70, 10, 20, hijau_tua)

        square(240, 120, 10, 30, hijau_tua)
        square(250, 150, 10, 20, hijau_tua)
        square(260, 140, 10, 10, hijau_tua)
        square(270, 130, 20, 10, hijau_tua)
        square(290, 140, 10, 10, hijau_tua)
        square(300, 120, 10, 20, hijau_tua)
        square(250, 120, 50, 10, hijau)
        square(250, 130, 20, 10, hijau)
        square(250, 140, 10, 10, hijau)
        square(290, 130, 10, 10, hijau)

        square(390, 80, 10, 20, hijau_tua)
        square(400, 100, 10, 10, hijau_tua)
        square(410, 80, 10, 20, hijau_tua)
        square(420, 100, 10, 20, hijau_tua)
        square(430, 100, 10, 10, hijau_tua)
        square(440, 90, 10, 10, hijau_tua)

        square(490, 120, 10, 30, hijau_tua)
        square(500, 150, 10, 20, hijau_tua)
        square(510, 140, 10, 10, hijau_tua)
        square(520, 130, 20, 10, hijau_tua)
        square(540, 140, 10, 10, hijau_tua)
        square(550, 120, 10, 20, hijau_tua)
        square(500, 120, 50, 10, hijau)
        square(500, 130, 20, 10, hijau)
        square(500, 140, 10, 10, hijau)
        square(540, 130, 10, 10, hijau)

    def rumah():
        square(450, 130, 170, 100, rumah1)
        square(480, 230, 120, 190, rumah1)
        square(480, 420, 20, 20, rumah1)
        square(540, 420, 90, 60, rumah1)
        square(600, 230, 50, 210, rumah2)
        square(630, 130, 120, 290, rumah1)
        square(640, 280, 110, 20, rumah1)
        square(630, 420, 120, 30, rumah1)

        square(750, 130, 70, 290, rumah2)
        square(640, 390, 110, 20, rumah2)
        square(645, 270, 105, 10, rumah2)

        square(455, 230, 10, 10, rumah4)
        square(500, 230, 90, 20, rumah4)
        square(500, 300, 90, 90, rumah4)
        square(670, 140, 80, 130, rumah4)
        square(670, 300, 80, 90, rumah4)
        
        square(510, 230, 70, 10, rumah3)
        square(510, 310, 70, 70, rumah3)
        square(680, 140, 70, 120, rumah3)
        square(680, 310, 70, 70, rumah3)
        square(445, 240, 30, 20, rumah3)

        square(530, 470, 60, 20, rumah5)
        square(570, 460, 60, 20, rumah5)
        square(610, 450, 60, 20, rumah5)
        square(650, 440, 60, 20, rumah5)
        square(690, 430, 60, 20, rumah5)
        square(730, 420, 60, 20, rumah5)
        square(790, 420, 40, 10, rumah5)

        square(500, 425, 100, 10, rumah6)
        square(620, 130, 10, 100, rumah6)
        square(740, 130, 10, 100, rumah6)
        square(630, 130, 110, 10, rumah6)
        square(630, 220, 110, 10, rumah6)
        square(640, 140, 10, 80, rumah6)
        square(660, 140, 10, 80, rumah6)
        square(680, 140, 10, 80, rumah6)
        square(700, 140, 10, 80, rumah6)
        square(720, 140, 10, 80, rumah6)

    def orang1():
        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, biru2)
        square(56, 224, 12, 20, biru2)
        square(62, 244, 6, 6, biru2)
        square(114, 224, 12, 13, biru2)

        square(94, 212, 20, 44, biru1)
        square(114, 237, 12, 7, biru1)
        square(114, 244, 6, 6, biru1)
        square(88, 218, 6, 38, biru1)
        square(82, 230, 6, 26, biru1)
        square(74, 230, 8, 20, biru1)

        # Tangan
        square(62, 180, 6, 44, cream1)
        square(56, 186, 6, 38, cream1)

        square(120, 212, 13, 6, cream1)
        square(114, 218, 25, 6, cream1)
        square(126, 224, 13, 7, cream1)
        square(133, 231, 13, 6, cream1)
        square(139, 237, 13, 7, cream1)
        square(139, 244, 19, 6, cream1)
        square(139, 250, 6, 6, cream1)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 82, 12, hitam)
        square(100, 384, 10, 6, hitam)
        square(110, 384, 10, 16, hitam)
        square(120, 384, 12, 26, hitam)

        # Leher
        square(81, 256, 19, 7, cream2)

        # Kepala
        square(68, 263, 46, 83, cream1)

        square(62, 269, 6, 71, cream1)
        square(56, 276, 6, 64, cream1)
        square(49, 282, 7, 45, cream1)
        square(42, 295, 7, 19, cream1)
        square(36, 302, 6, 12, cream1)

        square(114, 269, 6, 71, cream1)
        square(120, 276, 6, 64, cream1)
        square(126, 288, 7, 32, cream1)
        square(133, 295, 6, 19, cream1)
        square(139, 302, 7, 12, cream1)

        # Bayangan
        square(68, 263, 13, 6, cream2)
        square(62, 269, 13, 7, cream2)
        square(56, 276, 12, 6, cream2)
        square(49, 282, 13, 6, cream2)
        square(49, 288, 7, 20, cream2)
        square(42, 295, 7, 13, cream2)
        square(36, 302, 6, 6, cream2)

        square(133, 295, 6, 7, cream2)
        square(139, 302, 7, 6, cream2)

        square(62, 334, 13, 6, cream2)
        square(68, 340, 46, 6, cream2)
        square(107, 334, 19, 6, cream2)
        square(120, 328, 6, 6, cream2)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

    def orang2():
        glPushMatrix()
        glScalef(-1.0, 1.0, 1.0)  
        glTranslatef(-800.0, 0.0, 0.0)

        # Sepatu
        square(62, 128, 28, 6, hitam)
        square(62, 134, 20, 6, hitam)

        square(94, 128, 26, 6, hitam)
        square(94, 134, 20, 6, hitam)

        # Celana
        square(62, 140, 20, 38, biru_tua)
        square(94, 140, 20, 38, biru_tua)
        square(62, 178, 52, 20, biru_tua)

        # Baju
        square(68, 198, 46, 58, kuning_tua)
        square(56, 224, 12, 20, kuning_tua)
        square(62, 244, 6, 6, kuning_tua)
        square(114, 224, 12, 13, kuning_tua)

        square(94, 212, 20, 44, kuning)
        square(114, 237, 12, 7, kuning)
        square(114, 244, 6, 6, kuning)
        square(88, 218, 6, 38, kuning)
        square(82, 230, 6, 26, kuning)
        square(74, 230, 8, 20, kuning)

        # Tangan
        square(62, 180, 6, 44, coklat)
        square(56, 186, 6, 38, coklat)

        square(120, 212, 13, 6, coklat)
        square(114, 218, 25, 6, coklat)
        square(126, 224, 13, 7, coklat)
        square(133, 231, 13, 6, coklat)
        square(139, 237, 13, 7, coklat)
        square(139, 244, 19, 6, coklat)
        square(139, 250, 6, 6, coklat)

        # Rambut
        square(42, 314, 98, 46, hitam)
        square(42, 360, 90, 12, hitam)
        square(50, 372, 80, 12, hitam)

        # Leher
        square(81, 256, 19, 7, coklat_tua)

        # Kepala
        square(68, 263, 46, 83, coklat)

        square(62, 269, 6, 71, coklat)
        square(56, 276, 6, 64, coklat)
        square(49, 282, 7, 45, coklat)
        square(42, 295, 7, 19, coklat)
        square(36, 302, 6, 12, coklat)

        square(114, 269, 6, 71, coklat)
        square(120, 276, 6, 64, coklat)
        square(126, 288, 7, 32, coklat)
        square(133, 295, 6, 19, coklat)
        square(139, 302, 7, 12, coklat)

        # Bayangan
        square(68, 263, 13, 6, coklat_tua)
        square(62, 269, 13, 7, coklat_tua)
        square(56, 276, 12, 6, coklat_tua)
        square(49, 282, 13, 6, coklat_tua)
        square(49, 288, 7, 20, coklat_tua)
        square(42, 295, 7, 13, coklat_tua)
        square(36, 302, 6, 6, coklat_tua)

        square(133, 295, 6, 7, coklat_tua)
        square(139, 302, 7, 6, coklat_tua)

        square(62, 334, 13, 6, coklat_tua)
        square(68, 340, 46, 6, coklat_tua)
        square(107, 334, 19, 6, coklat_tua)
        square(120, 328, 6, 6, coklat_tua)

        # Mata
        square(75, 308, 6, 13, hitam)
        square(107, 308, 6, 13, hitam)

        # Mulut
        square(81, 276, 20, 6, putih)
        square(75, 282, 32, 13, putih)

        glPopMatrix()

    def textbox1():
        glPushMatrix()
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("Is it a ...", 200, 342, hitam)

    def textbox2():
        glPushMatrix()
        glScale(-1.0, 1.0, 1.0)
        glTranslatef(-800.0, 0.0, 0.0)
        
        glTranslatef(75.0, 30.0, 0)
        glScale(0.7, 0.7, 0.7)

        square(160, 380, 10, 10, hitam)
        square(170, 390, 10, 10, hitam)
        square(150, 370, 10, 30, hitam)
        square(180, 400, 10, 10, hitam)
        square(140, 400, 10, 10, hitam)
        square(190, 410, 110, 10, hitam)
        square(130, 410, 10, 10, hitam)
        square(300, 420, 10, 10, hitam)
        square(310, 430, 10, 10, hitam)
        square(320, 440, 10, 40, hitam)
        square(120, 420, 10, 60, hitam)
        square(310, 480, 10, 10, hitam)
        square(130, 480, 10, 10, hitam)
        square(140, 490, 170, 10, hitam)

        square(130, 420, 170, 60, putih)
        square(140, 480, 170, 10, putih)
        square(140, 410, 50, 10, putih)
        square(150, 400, 30, 10, putih)
        square(160, 390, 10, 10, putih)
        square(300, 430, 10, 60, putih)
        square(310, 440, 10, 40, putih)

        glPopMatrix()

        draw_text1("What is that?", 517, 342, hitam)

    def pilihan1():
        square(220, 60, 120, 10, hitam)
        square(220, 150, 120, 10, hitam)

        square(210, 70, 10, 10, hitam)
        square(210, 140, 10, 10, hitam)
        square(340, 70, 10, 10, hitam)
        square(340, 140, 10, 10, hitam)

        square(200, 80, 10, 60, hitam)
        square(350, 80, 10, 60, hitam)

        square(220, 70, 120, 80, biru_level_box)
        square(210, 80, 10, 60, biru_level_box)
        square(340, 80, 10, 60, biru_level_box)

        draw_text1("Motorcycle", 245, 105, hitam)

    def pilihan2():
        square(460, 60, 120, 10, hitam)
        square(460, 150, 120, 10, hitam)

        square(450, 70, 10, 10, hitam)
        square(450, 140, 10, 10, hitam)
        square(580, 70, 10, 10, hitam)
        square(580, 140, 10, 10, hitam)

        square(440, 80, 10, 60, hitam)
        square(590, 80, 10, 60, hitam)

        square(460, 70, 120, 80, oren)
        square(450, 80, 10, 60, oren)
        square(580, 80, 10, 60, oren)

        draw_text1("Racing", 498, 105, hitam)

    def bar_waktu():
        glBegin(GL_QUADS)
        glColor4f(1, 1, 1, 0.5)
        glVertex2f(260, 440)
        glVertex2f(540, 440)
        glVertex2f(540, 460)
        glVertex2f(260, 460)
        glEnd()

        # square(260, 440, 140, 20, merah)

        square(258, 438, 284, 2, hitam)
        square(258, 460, 284, 2, hitam)

        square(258, 440, 2, 20, hitam)
        

    def box_benda():
        square(330, 540, 140, 120, putih)

        square(340, 530, 120, 10, hitam)
        square(340, 660, 120, 10, hitam)

        square(330, 540, 10, 20, hitam)
        square(330, 640, 10, 20, hitam)
        square(460, 540, 10, 20, hitam)
        square(460, 640, 10, 20, hitam)

        square(320, 560, 10, 80, hitam)
        square(470, 560, 10, 80, hitam)

        draw_image(load_texture('sepeda.png'), 320, 520, 160, 160)

    
    langit()
    rumah()
    overlay_putih()
    rumput()
    tanah_b()
    tanah_u()
    orang1()
    orang2()
    textbox1()
    textbox2()
    pilihan1()
    pilihan2()
    bar_waktu()
    box_benda()

    if sisa_nyawa > 0:
        nyawa1()
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 2:
        nyawa2()
        nyawa3()
    elif sisa_nyawa == 1:
        nyawa3()
    else:
        if not yah_kalah:
            print("Notif Kalah")
            yah_kalah = True

def nyawa1():
    if nyawa1_visible:
        square(580, 715, 50, 25, merah)
        square(590, 705, 30, 10, merah)
        square(600, 700, 10, 5, merah)

    square(600, 695, 10, 5, hitam)
    square(600, 735, 10, 5, hitam)

    square(575, 720, 5, 15, hitam)
    square(630, 720, 5, 15, hitam)

    square(585, 740, 15, 5, hitam)
    square(610, 740, 15, 5, hitam)

    square(595, 700, 5, 5, hitam)
    square(590, 705, 5, 5, hitam)
    square(585, 710, 5, 5, hitam)
    square(580, 715, 5, 5, hitam)
    square(610, 700, 5, 5, hitam)
    square(615, 705, 5, 5, hitam)
    square(620, 710, 5, 5, hitam)
    square(625, 715, 5, 5, hitam)
    square(580, 735, 5, 5, hitam)
    square(625, 735, 5, 5, hitam)


def nyawa2():
    if nyawa2_visible:
        square(650, 715, 50, 25, merah)
        square(660, 705, 30, 10, merah)
        square(670, 700, 10, 5, merah)

    square(670, 695, 10, 5, hitam)
    square(670, 735, 10, 5, hitam)

    square(645, 720, 5, 15, hitam)
    square(700, 720, 5, 15, hitam)

    square(655, 740, 15, 5, hitam)
    square(680, 740, 15, 5, hitam)

    square(665, 700, 5, 5, hitam)
    square(660, 705, 5, 5, hitam)
    square(655, 710, 5, 5, hitam)
    square(650, 715, 5, 5, hitam)
    square(680, 700, 5, 5, hitam)
    square(685, 705, 5, 5, hitam)
    square(690, 710, 5, 5, hitam)
    square(695, 715, 5, 5, hitam)
    square(650, 735, 5, 5, hitam)
    square(695, 735, 5, 5, hitam)

    
def nyawa3():
    if nyawa3_visible:
        square(720, 715, 50, 25, merah)
        square(730, 705, 30, 10, merah)
        square(740, 700, 10, 5, merah)

    square(740, 695, 10, 5, hitam)
    square(740, 735, 10, 5, hitam)

    square(715, 720, 5, 15, hitam)
    square(770, 720, 5, 15, hitam)

    square(725, 740, 15, 5, hitam)
    square(750, 740, 15, 5, hitam)

    square(735, 700, 5, 5, hitam)
    square(730, 705, 5, 5, hitam)
    square(725, 710, 5, 5, hitam)
    square(720, 715, 5, 5, hitam)
    square(750, 700, 5, 5, hitam)
    square(755, 705, 5, 5, hitam)
    square(760, 710, 5, 5, hitam)
    square(765, 715, 5, 5, hitam)
    square(720, 735, 5, 5, hitam)
    square(765, 735, 5, 5, hitam)

def cs():
    # Coming Soon
    glBegin(GL_QUADS)
    glColor4f(0, 0, 0, 0.5)
    glVertex2f(0, 0)
    glVertex2f(800, 0)
    glVertex2f(800, 800)
    glVertex2f(0, 800)
    glEnd()   

    # Frame
    square(160, 350, 480, 100, hijau_button1)
    square(180, 350, 450, 10, hijau_button2)
    square(620, 360, 10, 20, hijau_button2)
    square(630, 360, 10, 60, hijau_button2)

    square(170, 340, 460, 10, hitam)
    square(170, 450, 460, 10, hitam)
    square(160, 350, 10, 10, hitam)
    square(160, 440, 10, 10, hitam)
    square(630, 350, 10, 10, hitam)
    square(630, 440, 10, 10, hitam)
    square(150, 360, 10, 80, hitam)
    square(640, 360, 10, 80, hitam)

    # Huruf
    square(245, 380, 30, 5, hitam)
    square(245, 420, 30, 5, hitam)
    square(240, 385, 5, 35, hitam)
    square(275, 385, 5, 10, hitam)
    square(275, 410, 5, 10, hitam)

    square(285, 385, 5, 20, hitam)
    square(305, 385, 5, 20, hitam)
    square(290, 380, 15, 5, hitam)
    square(290, 405, 15, 5, hitam)

    square(315, 380, 5, 25, hitam)
    square(335, 380, 5, 25, hitam)
    square(355, 380, 5, 25, hitam)
    square(320, 405, 15, 5, hitam)
    square(340, 405, 15, 5, hitam)

    square(365, 380, 5, 25, hitam)

    square(375, 380, 5, 30, hitam)
    square(380, 405, 10, 5, hitam)
    square(390, 380, 5, 25, hitam)

    square(400, 390, 5, 15, hitam)
    square(415, 390, 5, 15, hitam)
    square(415, 375, 5, 10, hitam)
    square(405, 370, 10, 5, hitam)
    square(405, 385, 10, 5, hitam)
    square(405, 405, 10, 5, hitam)
    square(400, 375, 5, 5, hitam)

    square(440, 380, 25, 5, hitam)
    square(445, 420, 25, 5, hitam)
    square(445, 400, 20, 5, hitam)
    square(440, 405, 5, 15, hitam)
    square(465, 385, 5, 15, hitam)

    square(475, 385, 5, 20, hitam)
    square(495, 385, 5, 20, hitam)
    square(480, 380, 15, 5, hitam)
    square(480, 405, 15, 5, hitam)

    square(505, 385, 5, 20, hitam)
    square(525, 385, 5, 20, hitam)
    square(510, 380, 15, 5, hitam)
    square(510, 405, 15, 5, hitam)

    square(535, 380, 5, 30, hitam)
    square(540, 405, 10, 5, hitam)
    square(550, 380, 5, 25, hitam)

def notif_kalah():
        # Overlay hitam
        glBegin(GL_QUADS)
        glColor4f(0, 0, 0, 0.5)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 800)
        glVertex2f(0, 800)
        glEnd()   
        
        # Window
        square(150, 200, 500, 390, level_box1)

        square(160, 190, 480, 10, hitam)
        square(160, 590, 480, 10, hitam)
        square(150, 200, 10, 60, hitam)
        square(150, 540, 10, 60, hitam)
        square(640, 200, 10, 60, hitam)
        square(640, 540, 10, 60, hitam)
        square(140, 260, 10, 280, hitam)
        square(140, 260, 10, 280, hitam)
        square(650, 260, 10, 280, hitam)

        # Judul
        square(175, 520, 10, 40, hitam)
        square(185, 510, 30, 10, hitam)
        square(185, 560, 40, 10, hitam)
        square(215, 520, 10, 30, hitam)
        square(205, 540, 10, 10, hitam)

        square(235, 520, 10, 10, hitam)
        square(235, 550, 30, 10, hitam)
        square(245, 530, 20, 10, hitam)
        square(245, 510, 20, 10, hitam)
        square(265, 510, 10, 40, hitam)

        square(285, 510, 10, 40, hitam)
        square(295, 540, 20, 10, hitam)
        square(315, 510, 10, 30, hitam)
        square(325, 540, 20, 10, hitam)
        square(345, 510, 10, 30, hitam)

        square(365, 520, 10, 20, hitam)
        square(375, 510, 30, 10, hitam)
        square(375, 540, 30, 10, hitam)
        square(375, 530, 20, 5, hitam)
        square(395, 510, 10, 5, hitam)
        square(395, 530, 10, 10, hitam)


        square(425, 520, 10, 40, hitam)
        square(465, 520, 10, 40, hitam)
        square(435, 510, 30, 10, hitam)
        square(435, 560, 30, 10, hitam)

        square(485, 530, 10, 20, hitam)
        square(525, 530, 10, 20, hitam)
        square(495, 520, 10, 10, hitam)
        square(515, 520, 10, 10, hitam)
        square(505, 510, 10, 10, hitam)

        square(545, 520, 10, 20, hitam)
        square(555, 510, 30, 10, hitam)
        square(555, 540, 30, 10, hitam)
        square(555, 530, 20, 5, hitam)
        square(575, 510, 10, 5, hitam)
        square(575, 530, 10, 10, hitam)

        square(595, 510, 10, 30, hitam)
        square(605, 540, 20, 10, hitam)

        #TRYAGAIN
        square(300, 380, 200, 80, oren)

        square(310, 370, 180, 10, hitam)
        square(310, 460, 180, 10, hitam)
        square(290, 390, 10, 60, hitam)
        square(500, 390, 10, 60, hitam)
        square(300, 380, 10, 10, hitam)
        square(300, 450, 10, 10, hitam)
        square(490, 380, 10, 10, hitam)
        square(490, 450, 10, 10, hitam)

        # Text
        square(315, 405, 5, 25, hitam)
        square(305, 430, 25, 5, hitam)

        square(335, 405, 5, 15, hitam)
        square(340, 420, 10, 5, hitam)

        square(355, 415, 5, 10, hitam)
        square(355, 400, 15, 5, hitam)
        square(360, 410, 10, 5, hitam)
        square(370, 405, 5, 20, hitam)


        square(385, 405, 5, 25, hitam)
        square(405, 405, 5, 25, hitam)
        square(390, 415, 15, 5, hitam)
        square(390, 430, 15, 5, hitam)

        square(415, 415, 5, 5, hitam)
        square(415, 400, 5, 5, hitam)
        square(420, 395, 10, 5, hitam)
        square(420, 410, 10, 5, hitam)
        square(420, 420, 10, 5, hitam)
        square(430, 400, 5, 25, hitam)

        square(440, 410, 5, 5, hitam)
        square(440, 420, 15, 5, hitam)
        square(445, 405, 10, 5, hitam)
        square(445, 415, 10, 2, hitam)
        square(455, 405, 5, 20, hitam)

        square(465, 405, 5, 20, hitam)
        square(465, 427, 5, 4, hitam)

        square(475, 405, 5, 20, hitam)
        square(480, 420, 10, 5, hitam)
        square(490, 405, 5, 15, hitam)

        #Left
        square(300, 250, 200, 80, merah)

        square(310, 240, 180, 10, hitam)
        square(310, 330, 180, 10, hitam)
        square(290, 260, 10, 60, hitam)
        square(500, 260, 10, 60, hitam)
        square(300, 250, 10, 10, hitam)
        square(300, 320, 10, 10, hitam)
        square(490, 250, 10, 10, hitam)
        square(490, 320, 10, 10, hitam)
        
        # Text
        square(355, 275, 5, 30, hitam)
        square(360, 275, 15, 5, hitam)

        square(380, 280, 5, 15, hitam)
        square(385, 275, 15, 5, hitam)
        square(385, 295, 15, 5, hitam)
        square(385, 288, 10, 2, hitam)
        square(395, 280, 5, 5, hitam)
        square(395, 288, 5, 7, hitam)

        square(405, 290, 20, 5, hitam)
        square(410, 275, 5, 30, hitam)
        square(415, 300, 5, 5, hitam)

        square(435, 280, 5, 20, hitam)
        square(430, 290, 15, 5, hitam)
        square(440, 275, 5, 5, hitam)



def kotak_bar():
    global pos_x, pos_y
    if waktu:
        glColor3f(1, 0, 0)
        glBegin(GL_POLYGON)
        glVertex2f(pos_x, pos_y)
        glVertex2f(pos_x + 2 + kotak_weight, pos_y)
        glVertex2f(pos_x + 2 + kotak_weight, pos_y + 20)
        glVertex2f(pos_x, pos_y + 20)
        glEnd()


def kotak_trigger():
    global pos_x2, pos_y2, nyawa1_visible
    if waktu:
        glColor3f(0, 0, 0)
        glBegin(GL_POLYGON)
        glVertex2f(pos_x2, pos_y2)
        glVertex2f(pos_x2 + 2,pos_y2)
        glVertex2f(pos_x2 + 2,pos_y2 + 20)
        glVertex2f(pos_x2,pos_y2 + 20)
        glEnd()

def display():
    glPushMatrix()
    kotak_trigger()
    
    glPopMatrix()
    glPushMatrix()
    kotak_bar()
    glPopMatrix()
    glFlush()

def cekcollision():
    global pos_x, pos_y, pos_x2, pos_y2, kotak_weight, nyawa1_visible, nyawa2_visible, nyawa3_visible, sisa_nyawa, game_over, yah_kalah
    if not game_over:
        kotak1_left = 0 - kotak_weight
        kotak1_right = 0 + kotak_weight

        kotak2_left = 278
        kotak2_right = 280

        if kotak1_right >= kotak2_left and kotak1_left <= kotak2_right:
            sisa_nyawa -= 1
            print("Sisa nyawa:", sisa_nyawa)
            if sisa_nyawa == 2:
                nyawa1_visible = False
            elif sisa_nyawa == 1:
                nyawa2_visible = False
            elif sisa_nyawa == 0:
                nyawa3_visible = False
                print("Game Over - Nyawa Entek")
                game_over = True
                if not yah_kalah:
                    yah_kalah = True
                    print("Notif Kalah")
                    # notif_kalah()

            kotak_weight = 1 / 1000
            print("Terjadi Collision")
    else:
        print("Game Over")
        # notif_kalah()

def update(value): 
    global kotak_weight, sisa_nyawa, game_over
    if not game_over and sisa_nyawa > 0 and kotak_weight <= 278:
        kotak_weight += 1 / 1000
    else:
        if game_mode == LEVEL_SCREEN or game_mode == HOME_SCREEN:
            game_over = True
            kotak_weight = 1 / 1000
            print("Game Over")
            # notif_kalah()
        return

    cekcollision()
    glutPostRedisplay()
    glutTimerFunc(10, update, 10)


def draw_text1(text, xpos, ypos, color):
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0], color[1], color[2])
    line = 0

    glPushMatrix()
    glRasterPos2f(xpos, ypos)

    for i in text:
        if i == '\n':
            line-line+1
            glRasterPos2f(xpos, ypos*line)
        else:
            glutBitmapCharacter(font_style, ord(i))

    glPopMatrix()


def draw_text2(text, xpos, ypos, color):
    font_style = glut.GLUT_BITMAP_HELVETICA_12
    glColor3ub(color[0], color[1], color[2])
    line = 0

    glPushMatrix()
    glRasterPos2f(xpos, ypos)

    for i in text:
        if i == '\n':
            line-line+1
            glRasterPos2f(xpos, ypos*line)
        else:
            glutBitmapCharacter(font_style, ord(i))

    glPopMatrix()


def square(x, y, width, height, color):
    glBegin(GL_QUADS)
    glColor3ub(color[0], color[1], color[2])
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()


def mainkan_suara_klik():
    pygame.mixer.Sound.play(suara_klik)


def mainkan_suara_button():
    pygame.mixer.Sound.play(suara_button)


def close_window():
    pygame.mixer.music.stop()
    glutLeaveMainLoop()


def input_mouse(button, state, x, y):
    global game_mode, current_level, jawaban_salah, nyawa1_visible, nyawa2_visible, nyawa3_visible, sisa_nyawa, game_over

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if game_mode == HOME_SCREEN:
            start_button_x = 290
            start_button_y = 250
            start_button_w = 220
            start_button_h = 80

            if (
                start_button_x <= x <= start_button_x + start_button_w
                and start_button_y <= h - y <= start_button_y + start_button_h
            ):
                game_mode = LEVEL_SCREEN
                print("Berhasil Masuk")

        elif game_mode == LEVEL_SCREEN:
            back_button_x = 25
            back_button_y = 35
            back_button_w = 115
            back_button_h = 55

            if (
                back_button_x <= x <= back_button_x + back_button_w
                and back_button_y <= h - y <= back_button_y + back_button_h
            ):
                game_mode = HOME_SCREEN
                print("Kembali ke Tampilan Utama")

            # Level 1
            level1_x = 225
            level1_y = 475
            level1_w = 365
            level1_h = 75

            if (
                level1_x <= x <= level1_x + level1_w
                and level1_y <= h - y <= level1_y + level1_h
            ):
                current_level = 1
                game_mode = GAME_SCREEN
                print("Menuju Level 1")

            # Level 2
            level2_x = 225
            level2_y = 375
            level2_w = 365
            level2_h = 75

            if (
                level2_x <= x <= level2_x + level2_w
                and level2_y <= h - y <= level2_y + level2_h
            ):
                current_level = 2
                game_mode = GAME_SCREEN5
                print("Menuju Level 2")

            # Level 3
            level3_x = 225
            level3_y = 275
            level3_w = 365
            level3_h = 75

            if (
                level3_x <= x <= level3_x + level3_w
                and level3_y <= h - y <= level3_y + level3_h
            ):
                current_level = 3
                game_mode = GAME_SCREEN
                print("Menuju Level 3")

            # Level 4
            level4_x = 225
            level4_y = 175
            level4_w = 365
            level4_h = 75

            if (
                level4_x <= x <= level4_x + level4_w
                and level4_y <= h - y <= level4_y + level4_h
            ):
                current_level = 4
                game_mode = GAME_SCREEN
                print("Menuju Level 4")

        elif game_mode == GAME_SCREEN:
            pilihan1_button_x = 200
            pilihan1_button_y = 60
            pilihan1_button_w = 240
            pilihan1_button_h = 90

            if (
                pilihan1_button_x <= x <= pilihan1_button_x + pilihan1_button_w
                and pilihan1_button_y <= h - y <= pilihan1_button_y + pilihan1_button_h
            ):
                game_mode = GAME_SCREEN2
                print("Jawabanmu benar")


            pilihan2_button_x = 440
            pilihan2_button_y = 60
            pilihan2_button_w = 140
            pilihan2_button_h = 80

            if (
                pilihan2_button_x <= x <= pilihan2_button_x + pilihan2_button_w
                and pilihan2_button_y <= h - y <= pilihan2_button_y + pilihan2_button_h
            ):
                jawaban_salah = 2
                print("Jawabanmu salah")
                sisa_nyawa -= 1
                print("Sisa nyawa:", sisa_nyawa)
                if sisa_nyawa == 2:
                    nyawa1_visible = False
                elif sisa_nyawa == 1:
                    nyawa2_visible = False
                elif sisa_nyawa == 0:
                    nyawa3_visible = False
                    print("Game Over - Nyawa Entek")
                    game_over = True
                game_mode = GAME_SCREEN2
                
            cekcollision()

        elif game_mode == GAME_SCREEN2:
            pilihan1_button_x = 200
            pilihan1_button_y = 60
            pilihan1_button_w = 240
            pilihan1_button_h = 90

            if (
                pilihan1_button_x <= x <= pilihan1_button_x + pilihan1_button_w
                and pilihan1_button_y <= h - y <= pilihan1_button_y + pilihan1_button_h
            ):
                game_mode = GAME_SCREEN3
                print("Jawabanmu benar")


            pilihan2_button_x = 440
            pilihan2_button_y = 60
            pilihan2_button_w = 140
            pilihan2_button_h = 80

            if (
                pilihan2_button_x <= x <= pilihan2_button_x + pilihan2_button_w
                and pilihan2_button_y <= h - y <= pilihan2_button_y + pilihan2_button_h
            ):
                jawaban_salah = 2
                print("Jawabanmu salah")
                sisa_nyawa -= 1
                print("Sisa nyawa:", sisa_nyawa)
                if sisa_nyawa == 2:
                    nyawa1_visible = False
                elif sisa_nyawa == 1:
                    nyawa2_visible = False
                elif sisa_nyawa == 0:
                    nyawa3_visible = False
                    print("Game Over - Nyawa Entek")
                    game_over = True
                game_mode = GAME_SCREEN3
                
            cekcollision()

        elif game_mode == GAME_SCREEN3:
            pilihan1_button_x = 200
            pilihan1_button_y = 60
            pilihan1_button_w = 240
            pilihan1_button_h = 90

            if (
                pilihan1_button_x <= x <= pilihan1_button_x + pilihan1_button_w
                and pilihan1_button_y <= h - y <= pilihan1_button_y + pilihan1_button_h
            ):
                game_mode = GAME_SCREEN4
                print("Jawabanmu benar")


            pilihan2_button_x = 440
            pilihan2_button_y = 60
            pilihan2_button_w = 140
            pilihan2_button_h = 80

            if (
                pilihan2_button_x <= x <= pilihan2_button_x + pilihan2_button_w
                and pilihan2_button_y <= h - y <= pilihan2_button_y + pilihan2_button_h
            ):
                jawaban_salah = 2
                print("Jawabanmu salah")
                sisa_nyawa -= 1
                print("Sisa nyawa:", sisa_nyawa)
                if sisa_nyawa == 2:
                    nyawa1_visible = False
                elif sisa_nyawa == 1:
                    nyawa2_visible = False
                elif sisa_nyawa == 0:
                    nyawa3_visible = False
                    print("Game Over - Nyawa Entek")
                    game_over = True
                game_mode = GAME_SCREEN4
                
            cekcollision()

        elif game_mode == GAME_SCREEN4:
            pilihan1_button_x = 200
            pilihan1_button_y = 60
            pilihan1_button_w = 240
            pilihan1_button_h = 90

            if (
                pilihan1_button_x <= x <= pilihan1_button_x + pilihan1_button_w
                and pilihan1_button_y <= h - y <= pilihan1_button_y + pilihan1_button_h
            ):
                game_mode = HOME_SCREEN
                print("Jawabanmu benar")


            pilihan2_button_x = 440
            pilihan2_button_y = 60
            pilihan2_button_w = 140
            pilihan2_button_h = 80

            if (
                pilihan2_button_x <= x <= pilihan2_button_x + pilihan2_button_w
                and pilihan2_button_y <= h - y <= pilihan2_button_y + pilihan2_button_h
            ):
                jawaban_salah = 2
                print("Jawabanmu salah")
                sisa_nyawa -= 1
                print("Sisa nyawa:", sisa_nyawa)
                if sisa_nyawa == 2:
                    nyawa1_visible = False
                elif sisa_nyawa == 1:
                    nyawa2_visible = False
                elif sisa_nyawa == 0:
                    nyawa3_visible = False
                    print("Game Over - Nyawa Entek")
                    game_over = True

            cekcollision()

        elif game_mode == GAME_SCREEN5:
            pilihan1_button_x = 200
            pilihan1_button_y = 60
            pilihan1_button_w = 240
            pilihan1_button_h = 90

            if (
                pilihan1_button_x <= x <= pilihan1_button_x + pilihan1_button_w
                and pilihan1_button_y <= h - y <= pilihan1_button_y + pilihan1_button_h
            ):
                game_mode = GAME_SCREEN6
                print("Jawabanmu benar")


            pilihan2_button_x = 440
            pilihan2_button_y = 60
            pilihan2_button_w = 140
            pilihan2_button_h = 80

            if (
                pilihan2_button_x <= x <= pilihan2_button_x + pilihan2_button_w
                and pilihan2_button_y <= h - y <= pilihan2_button_y + pilihan2_button_h
            ):
                jawaban_salah = 2
                print("Jawabanmu salah")
                sisa_nyawa -= 1
                print("Sisa nyawa:", sisa_nyawa)
                if sisa_nyawa == 2:
                    nyawa1_visible = False
                elif sisa_nyawa == 1:
                    nyawa2_visible = False
                elif sisa_nyawa == 0:
                    nyawa3_visible = False
                    print("Game Over - Nyawa Entek")
                    game_over = True
                game_mode = GAME_SCREEN6
                
            cekcollision()

        elif game_mode == GAME_SCREEN6:
            pilihan1_button_x = 200
            pilihan1_button_y = 60
            pilihan1_button_w = 240
            pilihan1_button_h = 90

            if (
                pilihan1_button_x <= x <= pilihan1_button_x + pilihan1_button_w
                and pilihan1_button_y <= h - y <= pilihan1_button_y + pilihan1_button_h
            ):
                game_mode = GAME_SCREEN7
                print("Jawabanmu benar")


            pilihan2_button_x = 440
            pilihan2_button_y = 60
            pilihan2_button_w = 140
            pilihan2_button_h = 80

            if (
                pilihan2_button_x <= x <= pilihan2_button_x + pilihan2_button_w
                and pilihan2_button_y <= h - y <= pilihan2_button_y + pilihan2_button_h
            ):
                jawaban_salah = 2
                print("Jawabanmu salah")
                sisa_nyawa -= 1
                print("Sisa nyawa:", sisa_nyawa)
                if sisa_nyawa == 2:
                    nyawa1_visible = False
                elif sisa_nyawa == 1:
                    nyawa2_visible = False
                elif sisa_nyawa == 0:
                    nyawa3_visible = False
                    print("Game Over - Nyawa Entek")
                    game_over = True
                game_mode = GAME_SCREEN7
                
            cekcollision()

        elif game_mode == GAME_SCREEN7:
            pilihan1_button_x = 200
            pilihan1_button_y = 60
            pilihan1_button_w = 240
            pilihan1_button_h = 90

            if (
                pilihan1_button_x <= x <= pilihan1_button_x + pilihan1_button_w
                and pilihan1_button_y <= h - y <= pilihan1_button_y + pilihan1_button_h
            ):
                game_mode = GAME_SCREEN8
                print("Jawabanmu benar")


            pilihan2_button_x = 440
            pilihan2_button_y = 60
            pilihan2_button_w = 140
            pilihan2_button_h = 80

            if (
                pilihan2_button_x <= x <= pilihan2_button_x + pilihan2_button_w
                and pilihan2_button_y <= h - y <= pilihan2_button_y + pilihan2_button_h
            ):
                jawaban_salah = 2
                print("Jawabanmu salah")
                sisa_nyawa -= 1
                print("Sisa nyawa:", sisa_nyawa)
                if sisa_nyawa == 2:
                    nyawa1_visible = False
                elif sisa_nyawa == 1:
                    nyawa2_visible = False
                elif sisa_nyawa == 0:
                    nyawa3_visible = False
                    print("Game Over - Nyawa Entek")
                    game_over = True
                    
                
            cekcollision()

        elif game_mode == GAME_SCREEN8:
            pilihan1_button_x = 200
            pilihan1_button_y = 60
            pilihan1_button_w = 240
            pilihan1_button_h = 90

            if (
                pilihan1_button_x <= x <= pilihan1_button_x + pilihan1_button_w
                and pilihan1_button_y <= h - y <= pilihan1_button_y + pilihan1_button_h
            ):
                game_mode = HOME_SCREEN
                print("Jawabanmu benar")


            pilihan2_button_x = 440
            pilihan2_button_y = 60
            pilihan2_button_w = 140
            pilihan2_button_h = 80

            if (
                pilihan2_button_x <= x <= pilihan2_button_x + pilihan2_button_w
                and pilihan2_button_y <= h - y <= pilihan2_button_y + pilihan2_button_h
            ):
                jawaban_salah = 2
                print("Jawabanmu salah")
                sisa_nyawa -= 1
                print("Sisa nyawa:", sisa_nyawa)
                if sisa_nyawa == 2:
                    nyawa1_visible = False
                elif sisa_nyawa == 1:
                    nyawa2_visible = False
                elif sisa_nyawa == 0:
                    nyawa3_visible = False
                    print("Game Over - Nyawa Entek")
                    game_over = True

        mainkan_suara_klik()


def input_keyboard(key, x, y):
    global game_mode, selected_level, current_level

    if key == b'B' or key == b'b':
        if game_mode == LEVEL_SCREEN:
            game_mode = HOME_SCREEN
        elif game_mode == GAME_SCREEN:
            notif = False
            game_mode = LEVEL_SCREEN
        mainkan_suara_button()
        print(f'Kembali ke screen sebelumnya ({game_mode})')

    elif game_mode == LEVEL_SCREEN and key in [b'1', b'2', b'3', b'4']:
        current_level = int(key)
        game_mode = GAME_SCREEN
        mainkan_suara_button()
        print(f'Level {key} dipilih')

    elif game_mode == GAME_SCREEN and key in [b'1', b'2', b'3', b'4']:
        print("Anda harus kembali ke LEVEL_SCREEN untuk memilih level.")

    mainkan_suara_button()


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    global in_game_screen, waktu, sisa_nyawa

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glLoadIdentity()
    iterate()

    if game_mode == HOME_SCREEN:
        tampilan_awal()
        in_game_screen = False
    elif game_mode == LEVEL_SCREEN:
        tampilan_pilih_level()
        in_game_screen = True
    elif game_mode == GAME_SCREEN or game_mode == GAME_SCREEN5:
        in_game_screen = True
        if current_level == 1:
            tampilan_in_game()
            display()
            glutTimerFunc(100, update, 0)
            draw_text1("Level - 1", 25, 725, hitam)
            if sisa_nyawa == 0:
                notif_kalah()

        elif current_level == 2:
            tampilan_in_game5()
            display()
            glutTimerFunc(100, update, 0)
            draw_text1("Level - 2", 25, 725, hitam)
            if sisa_nyawa == 0:
                notif_kalah()
        elif current_level == 3:
            cs()
        elif current_level == 4:
            cs()
    elif game_mode == GAME_SCREEN2:
        tampilan_in_game2()
        display()
        glutTimerFunc(100, update, 0)
        draw_text1("Level - 1", 25, 725, hitam)
        if sisa_nyawa == 0:
                notif_kalah()
        
    elif game_mode == GAME_SCREEN3:
        tampilan_in_game3()
        display()
        glutTimerFunc(100, update, 0)
        draw_text1("Level - 1", 25, 725, hitam)
        if sisa_nyawa == 0:
                notif_kalah()
    elif game_mode == GAME_SCREEN4:
        tampilan_in_game4()
        display()
        glutTimerFunc(100, update, 0)
        draw_text1("Level - 1", 25, 725, hitam)
        if sisa_nyawa == 0:
                notif_kalah()
    elif game_mode == GAME_SCREEN6:
        tampilan_in_game6()
        display()
        glutTimerFunc(100, update, 0)
        draw_text1("Level - 2", 25, 725, hitam)
        if sisa_nyawa == 0:
                notif_kalah()
    elif game_mode == GAME_SCREEN7:
        tampilan_in_game7()
        display()
        glutTimerFunc(100, update, 0)
        draw_text1("Level - 2", 25, 725, hitam)
        if sisa_nyawa == 0:
                notif_kalah()
    elif game_mode == GAME_SCREEN8:
        tampilan_in_game8()
        display()
        glutTimerFunc(100, update, 0)
        draw_text1("Level - 2", 25, 725, hitam)
        if sisa_nyawa == 0:
                notif_kalah()

        

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow("Game")
glutDisplayFunc(showScreen)
glutMouseFunc(input_mouse)
glutKeyboardFunc(input_keyboard)
glutCloseFunc(close_window)
glutIdleFunc(showScreen)
glutMainLoop()

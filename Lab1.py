from gl import Render, glColor

r = Render()
r.glInit(800, 600)

#Figura 1
r.glLine(165, 380, 185, 360)
r.glLine(185,360,180,330)
r.glLine(180,330,207,345)
r.glLine(207,345,233,330)
r.glLine(233,330,230,360)
r.glLine(230,360,250,380)
r.glLine(250,380,220,385)
r.glLine(220,385,205,410)
r.glLine(205,410,193,383)
r.glLine(193,383,165,380)

#Figura 2
r.glLine(321, 335, 288, 286)
r.glLine(288, 286, 339, 251)
r.glLine(339, 251, 374, 302)
r.glLine(374, 302, 321, 335)

#Figura 3
r.glLine(377, 249, 411, 197)
r.glLine(411, 197, 436, 249)
r.glLine(436, 249, 377, 249)

#Figura 4
r.glLine(413, 177, 448, 159) 
r.glLine(448, 159, 502, 88) 
r.glLine(502, 88, 553, 53) 
r.glLine(553, 53, 535, 36) 
r.glLine(535, 36, 676, 37) 
r.glLine(676, 37, 660, 52) 
r.glLine(660, 52, 750, 145) 
r.glLine(750, 145, 761, 179) 
r.glLine(761, 179, 672, 192) 
r.glLine(672, 192, 659, 214) 
r.glLine(659, 214, 615, 214) 
r.glLine(615, 214, 632, 230) 
r.glLine(632, 230, 580, 230) 
r.glLine(580, 230, 597, 215) 
r.glLine(597, 215, 552, 214) 
r.glLine(552, 214, 517, 144) 
r.glLine(517, 144, 466, 180) 
r.glLine(466, 180, 413, 177)

#Figura 5
r.glLine(682, 175, 708, 120) 
r.glLine(708, 120, 735, 148) 
r.glLine(735, 148, 739, 170) 
r.glLine(739, 170, 682, 175)

print(r.framebuffer[0][0])

x = 0
y = 0
draw = False
last = b'\x00\x00\x00'

for i in (r.framebuffer):
	for j in i:
		if (j != b'\x00\x00\x00' and last == b'\x00\x00\x00'):
			draw = not draw
		if (draw == True and j != b'\xff\xff\xff'):
			r.framebuffer[x][y] =  b'\x51\x78\x35'
		last = j
		y += 1
	draw = False
	y = 0
	x += 1	


r.glFinish("out3.bmp")

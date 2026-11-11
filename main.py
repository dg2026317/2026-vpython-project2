Web VPython 3.2
#r = cylinder(axis = vec(0,0,1), texture = "https://www.shutterstock.com/image-vector/roulette-wheel-casino-vector-clipart-260nw-2800032543.jpg")
r = cylinder(axis = vec(0,0,1), texture = "https://i.postimg.cc/85B8J5Gy/pngtree-casino-gambling-roulette-png-image-771873.jpg")
t = arrow(pos=vec(0, 1.6, 1.07), axis=vec(0, -1, 0), color=color.red)
ring(pos=vec(0, 0, 0.96), axis=vec(0, 0, 1), radius = 1.025, color=vec(51/255, 25/255, 0))
y = box(pos=vec(0,0,0.2), size=vec(4,3,1.5), color=vec(153/255, 76/255, 0))
u = cylinder(axis = vec(0,0,1), radius = 0.3, pos = vec(1.41,-0.9,0), color=color.black)
i = cylinder(axis = vec(0,0,1), radius = 0.3, pos = vec(1.41,-0.9,0), color=color.black)
while True :
    rate(30)
    k = keysdown()
    if ' ' in k :
         r.rotate(angle=1)

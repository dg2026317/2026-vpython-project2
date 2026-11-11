Web VPython 3.2
#r = cylinder(axis = vec(0,0,1), texture = "https://www.shutterstock.com/image-vector/roulette-wheel-casino-vector-clipart-260nw-2800032543.jpg")
r = cylinder(axis = vec(0,0,1), texture = "https://i.postimg.cc/85B8J5Gy/pngtree-casino-gambling-roulette-png-image-771873.jpg")
t = arrow(pos=vec(0, 1.65, 1.07), axis=vec(0, -1, 0), color=color.red)
y = box(pos=vec(0,-0.8,-0.15), size=vec(1,2,0.3), color=vec(0,102/255,0))
u = box(pos=vec(0,-1.8,0), size=vec(2,0.3,1), color=vec(0,102/255,0))
i = box(axis = vec(0,0,1), texture = "https://www.sisajournal.com/news/articleView.html?idxno=170885")
while True :
    rate(30)
    k = keysdown()
    if ' ' in k :
         r.rotate(angle=1)

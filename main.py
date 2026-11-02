Web VPython 3.2
#r = cylinder(axis = vec(0,0,1), texture = "https://www.shutterstock.com/image-vector/roulette-wheel-casino-vector-clipart-260nw-2800032543.jpg&quot;)
r = cylinder(axis = vec(0,0,1), texture = "https://i.postimg.cc/TPyq3k1c/13315.jpg&quot;)
arrow(pos=vec(0, 1.6, 1.07), axis=vec(0, -1, 0), color=color.red)

while True :
    rate(40)
    k = keysdown()
    if ' ' in k :
         r.rotate(angle=1)

def move(p, motion, p_move):
    q = []
    for i in range( len(p) ):
        q.append(p[i]*(1-p_move) + p[(i-motion)%len(p)]*p_move)
    return q


def sense(p, measurements, p_sencse):
    q=[]
    for i in range( len(world) ):
        if measurements == world[i]:
            q.append( p[i] * p_sencse )
        else:
            q.append( p[i] * (1-p_sencse) )
    s = sum(q)
    q[:] = [x/s for x in q]
    return q


def show(p):
    print '[ '+', '.join("%.04f" % round(x,4) for x in p) + ' ]'


world = ['R', 'G', 'R', 'R', 'G']
measurements = ['R', 'R', 'G', 'R']
moves = [1, 1, 1, -1]
p_sense = 0.9
p_move = 0.9
#p = [0.0, 1.0, 0.0, 0.0, 0.0]


def localization(p):
    for k in range(len(measurements)):
        print 'sense'
        p = sense(p, measurements[k], p_sense)
        show(p)
        print 'move'
        p = move(p, moves[k], p_move)
        show(p)

p = []
for i in range(len(world)):
    p.append(1.0/len(world))

localization(p)
from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)

        return path



Ver = {
    'a':(80,104.5),
    'b':(80,127.5),
    'c':(21,127.5),
    'd':(14,118.5),
    'e':(54,104.5),
    'f':(31.5,104.5),
    'g':(14.5,104.5),
    'h':(76.5,41.5),
    'i':(53.5,41.5),
    'j':(31.5,41.5),
    'k':(14,41.5),
    'l':(14,22),
    'm':(21,18.5),
    'n':(76,18.5),
    'o':(76.5,62),
    'p':(80,81),
    'q':(80,119),
    'r':(61,127.5),
    's':(41,127.5),
    't':(61,104.5),
    'u':(41,104.5),
    'v':(14.5,98),
    'w':(14,78),
    'x':(14,67.5),
    'y':(14,47.5),
    'z':(31.5,80.5),
    'A':(31.5,60.5),
    'B':(54,80.5),
    'C':(54,60.5),
    'D':(76.5,49.5),
    'E':(66,41.5),
    'F':(50.5,41.5),
    'G':(66,18.5),
    'H':(50.5,18.5),
    'I':(46,18.5),
    'J':(80,99),
    'K':(76.5,29)
}

graph = Graph([
    ("a", "q", 14.5),("q", "a", 14.5),
    ("q", "b", 8.5),("b", "q", 8.5),
    ("a","t",19),("t","a",19),
    ("a", "J", 5.5),("J", "a", 5.5),
    ("t", "e", 7),("e", "t", 7),
    ("J", "p", 18),("p", "J", 18),
    ("b", "r", 19),("r", "b", 19),
    ("r", "s", 20),("s", "r", 20),
    ("s", "c", 20),("c", "s", 20),
    ("d", "g", 14),("g", "d", 14),
    #("c", "d", 7.61),("d", "c", 7.61),
    ("e", "u", 13),("u", "e", 13),
    ("u", "f", 9.5),("f", "u", 9.5),
    ("e", "B", 24),("B", "e", 24),
    ("B", "C", 20),("C", "B", 20),
    ("C", "i", 19),("i", "C", 19),
    ("f", "z", 24),("z", "f", 24),
    ("z", "A", 20),("A", "z", 20),
    ("f", "g", 17),("g", "f", 17),
    ("A", "j", 19),("j", "A", 19),
    ("g", "v", 6.5),("v", "g", 6.5),
    ("v", "w", 20),("w", "v", 20),
    ("w", "x", 10.5),("x", "w", 10.5),
    ("x", "y", 20),("y", "x", 20),
    ("y", "k", 6),("k", "y", 6),
    ("k", "l", 19.5),("l", "k", 19.5),
    ("k", "j", 18),("j", "k", 18),
    ("j", "F", 19),("F", "j", 19),
    ("F", "i", 3),("i", "F", 3),
    #("l","m",7.82),("m", "l", 7.82),
    ("i", "E", 12.5),("E", "i", 12.5),
    ("E","h",9.5),("h", "E", 9.5),
    #("p", "o", 16.83),("p", "o", 16.83),
    ("h", "K", 12.5),("K", "h", 12.5),
    ("K", "n", 11),("n", "K", 11),
    ("o", "D", 12.5),("D", "o", 12.5),
    ("D", "h", 8),("h", "D", 8),
    ("n", "G", 10),("G", "n", 10),
    ("G", "H", 15.5),("H", "G", 15.5),
    ("H", "I", 4.5),("I", "H", 4.5),
    ("I", "m", 25),("m", "I", 25),
])

dock ={
    'dock A': ('l', 'm'),
    'dock B': ('o', 'p'),
    'dock C': ('d', 'c')
}
#z = dock['dock A'][0]
d1 = 'dock A'
#comment the relations between docking nodes
print(type(Ver))
#ll = graph.dijkstra("o", dock[d][0])
#print(ll)
rack ={
    'rack 23':('q','J','0','2'),
    'rack 64':('r','s','3','1'),
    'rack 46':('r','s','1','3'),
    'rack 57':('u','t','3','1'),
    'rack 72':('v','w','2','0'),
    'rack 45':('x','y','0','2'),
    'rack 91':('C','B','0','2'),
    'rack 42':('A','z','2','0'),
    'rack 80':('E','F','2','0'),
    'rack 36':('G','H','1','3'),
    'rack 13':('D','K','3','1'),
    'rack 07':('G','I','1','3'),
}

r1 = 'rack 57' # target rack

def short_route_rack(r,d):                           # finding the shortest path to a dock
    llr1 = graph.dijkstra("c",rack[r][0]) # dedine starting point here and ending point and rack
    llr2 = graph.dijkstra("c",rack[r][1])
    #ll1 = graph.dijkstra("", dock[d][0])
    #ll2 =  graph.dijkstra("l", dock[d][1])
    #print(llr1)
    #print(llr2)
    if len(llr2) < len(llr1):
        #return llr2
        lld1 = graph.dijkstra(llr2[len(llr2) - 1], dock[d][0])
        lld2 = graph.dijkstra(llr2[len(llr2) - 1], dock[d][1])
        if len(lld1) < len(lld2):
            return llr2 + lld1
        elif len(lld2) < len(lld1):
            return llr2 + lld2
    elif len(llr1) < len(llr2):
        lld1 = graph.dijkstra(llr2[len(llr1) - 1], dock[d][0])
        lld2 = graph.dijkstra(llr2[len(llr1) - 1], dock[d][1])
        if len(lld1) < len(lld2):
            return llr1 + lld1
        elif len(lld2) < len(lld1):
            return llr1 + lld2
    else:
        lld2 = graph.dijkstra(llr1[len(llr2) - 1], dock[d][1])
        return llr1 + lld2
ll = short_route_rack(r1, d1)
print("now",ll)

# removing multiple nodes at rack
for i in range(len(ll) - 1):
    if ll[i] == ll[i + 1]:
        pointer = i
        del ll[i + 1]
        break
print(ll)
print(len(ll))
print("pointer",pointer)

#   defining local compass at starting point
if ll[0] == 'l':
    compass = ['N', 'E', 'S', 'W']
elif ll[0] == 'm':
    compass = ['W', 'N', 'E', 'S']
elif ll[0] == 'o':
    compass = ['S', 'W', 'N', 'E']
elif ll[0] == 'p':
    compass = ['N', 'E', 'S', 'W']
elif ll[0] == 'c':
    compass = ['W', 'N', 'E', 'S']
elif ll[0] == 'd':
    compass = ['S', 'W', 'N', 'E']

# Determining the actions to reach destination
actions = []
for i in range(len(ll) - 1):
#   First Node
    n1 = Ver[ll[i]]
#   Second node
    n2 = Ver[ll[i + 1]]

    #print(i)
#   Differences between nodes
    delta_x = n2[0] - n1[0]
    delta_y = n2[1] - n1[1]

#    delta y is positive then global north
    if (delta_x <= 1)and(delta_y > 0):
        actions.insert(i, 0)
#   delta x is positive then global east
    elif(delta_x > 0)and(delta_y <= 1):
        actions.insert(i, 1)
#   delta y is negative then global south
    elif(delta_x <= 1)and(delta_y < 0):
        actions.insert(i, 2)
#   delta x is negative then global west
    elif(delta_x < 0)and(delta_y <= 1):
        actions.insert(i, 3)



    #actions[i]=
#       def dis_calc(beg, eng):
#        beg = l[i]
#        end = l[i+1]
#        a[i] = l[i]
#        print(a[i])
#print(Ver['p'])
#Compass setting for starting nodes

#access dict/tuple elements individually
#x = Ver['l']
#print(type(x))
#print(type(x[1]))
print('Printing actions', actions)
'''for xx in actions:
    print(xx)'''
print(len(actions))
prev = -1
for i in range(len(actions)):
    now = actions[i]
    if i != 0:
#   West - swapping compass anti-clockwise
        if compass[prev] == 'W':
            t = compass[0]
            for j in range(len(compass) - 1):
                compass[j] = compass[j + 1]
            compass[len(compass) - 1] = t
#   East - swapping compass clockwise
        elif compass[prev] == 'E':
            t = compass[len(compass) - 1]
            for j in range(len(compass) - 1):
                compass[len(compass) - 1 - j] = compass[len(compass) - 1 - j - 1]
            compass[0] = t
    print(compass)
#Send this compass at rack to get arrow
    if i == pointer:
        #compass1 = compass
        for i in range(len(compass)):
            if(compass[i] == 'N'):
                ar = i     # store the index of local North
                print("arrow", ar)
        print("here rack", i)
    if compass[now] == 'N':#comparing against local compass
#       bus.write_byte(address, int(ord(1)))
        print("fwd")
    if compass[now] == 'E':
#       bus.write_byte(address, int(ord(1)))
        print("right")
    if compass[now] == 'S':
#       bus.write_byte(address, int(ord(1)))
        #print("bwkd")
#mirror compass and go fwd
        g = compass[0]
        compass[0]=compass[2]
        compass[2]=g
        g = compass[1]
        compass[1]=compass[3]
        compass[3]=g
        print("fwd")
    if compass[now] == 'W':
#       bus.write_byte(address, int(ord(1)))
        print("left")
    prev = now



#y = rack['R23']

#print(rack.keys())
#print(y[1])    accessing tuple element
#ar = 0;   # arrow
#print(compass1)
'''for i in range(len(compass1)):
    if(compass1[i] == 'N'):
        ar = i;     # store the index of local North
        print("arrow",ar);'''


#y = print(rack[r])

#for rack in rack.keys():
def get_turn(r):
    y = rack[r]
    print(y)
    if str(ar) == y[2]:
        #print('right')
        return 'right'
    elif str(ar) == y[3]:
        #print('left')
        return 'left'

y1 = get_turn(r1)
print('\n\n',y1)


'''def rack_short_path(ll1):
    #i = 0
    for rk in rack.keys():
        for i in range(len(rack)):
            if r1 == rack[r1]
            return i
        #if r1 == rk:
        rack[r1][0]
        for i in range(len(ll)):
            if rack[r1][0] or rack[r2][0]
            #print(i)
        #i = i + 1
print('lol')
rack_short_path(ll)'''

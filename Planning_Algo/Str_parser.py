import re

#inp = '<x: 064.5, y: 026.0> [RtRack 05, col 1, LfRack 25, col 5]'
#inp = '{pallet 104 @ rack 26, row 2, col 3} (dock A)'
#inp = '<x:064.5,y:026.0>'
#inp = '/pallet 106\\'
#inp = '{pallet 104 @ rack 26, row 2, col 3} (dock A) <x:064.5,y:026.0> [RtRack 05, LfRack 25] *rack15^ /pallet 056'
#print(len(inp))

data = []
class star:

    def __init__(self, inp):
        self.inp = inp


    def star1(self):
        data = []
        j = 0 # insert index

        if len(self.inp) > 100:#exxcat length is 107
            a = re.split('[})>]',self.inp)
            #print('lenght',len(o))
            for i in range(len(a)):
                #print(o[i])
                #print(type(o[1]))
                #print(i)
                #print(o[1])
                if i == 0:
                    str1 = a[i][1:]
                    #print(a[i][1:])
                    b = re.split('[@,]', str1)
                    for i in range(len(b)):
                        if i == 0:
                            data.insert(j,b[i])
                            j = j +1
                            #print(b[i])
                        else:
                            data.insert(j,b[i][1:])
                            j = j +1
                            #print(b[i][1:])
                elif 1 > 0 and i < 3:
                    data.insert(j,a[i][2:])
                    j = j +1
                    #print(a[i][2:])
                else:
                    c = a[i]
                    d = re.split('[*^]',c)
                    #print(d)
                    #print(d[0][2:(len(d[0])-2)])
                    for i in range(len(d)):
                        if i == 0:
                            e = d[0][2:(len(d[0])-2)]
                            #print(e)
                            f = e.split(',')
                            for i in range(len(f)):
                                if i == 0:
                                    #print(f[i])
                                    data.insert(j,f[i])
                                    j = j +1
                                else:
                                    data.insert(j,f[i][1:])
                                    j = j +1
                                    #print(f[i][1:])
                        elif i == 1:
                            #print(d[i])
                            data.insert(j,d[i])
                            j = j +1
                        else:
                            #print(d[i][2:])
                            data.insert(j,d[i][2:])
                            j = j +1
            return data
        elif len(self.inp) == 11:
            return self.inp[1:len(self.inp)]
        elif len(self.inp) == 17:
            a = re.split('[,]', self.inp)
            #print(a[0][3:])
            data.insert(j,a[0][1:])
            j = j+1
            #print(a[1][2:len(a[1])-1])
            data.insert(j,a[1][:len(a[1])-1])
            j = j+1
            return data
        elif len(self.inp) == 45:
            a = re.split('[})]', self.inp)
            for i in range(len(a)):
                if i == 0:
                    str1 = a[i][1:]
                    b = re.split('[@,]', str1)
                    for i in range(len(b)):
                        if i == 0:
                            #print(b[i])
                            data.insert(j,b[i])
                            j = j+1
                            #pallet(b)
                        else:
                            #print(b[i][1:])
                            data.insert(j,b[i][1:])
                            j = j+1
                            #rack(b)

                else:
                    #print(a[i][2:])
                    data.insert(j,a[i][2:])
                    j = j + 1
                    #dock(a,b)
            return data
        else:
            a = re.split('[,)>]', self.inp)
            #print(a)
            #print(a[0][1:])
            data.insert(j,a[0][1:])
            j = j + 1
            #print(a[1][1:])
            data.insert(j,a[1][1:])
            j = j + 1
            #for i in range(len(a) - 1):
            #print(a[2][2:])
            data.insert(j,a[2][2:])
            j = j + 1
            if len(inp) < 40:
                #print(a[3][1:len(a[3])-1])
                data.insert(j, a[3][1:len(a[3])-1])
                j = j + 1
            if len(inp) > 40:
                #print(a[3][1:len(a[3])])
                data.insert(j, a[3][1:len(a[3])-1])
                j = j+1
                #print(a[4][1:])
                data.insert(j, a[4][1:])
                j = j + 1
                #print(a[5][1:len(a[3])-1])
                data.insert(j, a[5][1:len(a[3])-1])
                j = j + 1
            return data

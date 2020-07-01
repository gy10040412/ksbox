'''
ksbox.help()
'''
import copy
from colorama import init
import time 
import numpy as np
import os
import math

def help():
    print("""function list
sinfo(sbox) -> return whole information of sbox
convert(sbox, True(default)) -> return flat_sbox
convert(flat_sbox, False) -> return sbox

make_ddt(sbox) -> return ddt
fmake_ddt(flat_sbox) -> return ddt

make_lat(sbox) -> return lat
fmake_lat(flat_sbox) -> return lat

table_max(table) -> return max(table[1~table_size][0 ~ table_size])
table_num_count(table, num) -> return count(table[0 ~ table_size][0 ~ table_size], num)

count_fixed(sbox) -> count fixed point
check_bn(table) -> BN check (<5)

view_11(table) -> view 1-1 table
view_12(table) -> view 1-2 table
view_21(table) -> view 2-1 table
    """)

init()
C_END     = "\033[0m"
C_BOLD    = "\033[1m"
C_INVERSE = "\033[7m" 
C_BLACK  = "\033[30m"
C_RED    = "\033[31m"
C_GREEN  = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE   = "\033[34m"
C_PURPLE = "\033[35m"
C_CYAN   = "\033[36m"
C_WHITE  = "\033[37m" 
C_BGBLACK  = "\033[40m"
C_BGRED    = "\033[41m"
C_BGGREEN  = "\033[42m"
C_BGYELLOW = "\033[43m"
C_BGBLUE   = "\033[44m"
C_BGPURPLE = "\033[45m"
C_BGCYAN   = "\033[46m"
C_BGWHITE  = "\033[47m"

def sinfo(s):
    size=len(s)
    bsize=int(math.log(len(size),2))
    if bsize not in [4,5,6,7,8]:
        print("Wrong input, this package provide only 4,5,6,7,8-bit s box.")
        exit(1)

    fixed=count_fixed(s)
    ddt=make_ddt(s)
    dbn=check_BN(ddt)
    dm=table_max(ddt)
    lat=make_lat(s)
    lbn=check_BN(lat)
    lm=table_max(lat)
    print ("{}-bit s box  diff:{}  linear:{}  dbn:{}  lbn:{}  fixed:{}".format(bsize,dm,lm,dbn,lbn,fixed))
    

def make_ddt(s):
    size=len(s)
    ddt=[ [0 for i in range(size)] for j in range(size) ]
    for i in range(size):
        for j in range(size):
            ddt[i^j][s[i]^s[j]]+=1
    return ddt
def convert(num,flat=True):
    n=[]
    if flat:
        bsize=int(math.log(len(num),2))
        nnum=list(map( lambda x:bin(x)[2:].zfill(bsize) , num ))
        for i in range(bsize):
            tmp=""
            for j in range(len(num)):
                tmp+=nnum[j][i]
            n.append(int(tmp,2))
        return n
    else:
        bsize=2**len(num)
        nnum=list(map( lambda x:bin(x)[2:].zfill(bsize) , num ))
        return list(map(lambda x:int("".join(x),2), zip(*nnum)))

in_4=[[0,0,0],[0,0,1],[0,1,0],[0,1,1]]
in_8=[[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1]]
in_16=[[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,1,1],[0,0,1,0,0],[0,0,1,0,1],[0,0,1,1,0],[0,0,1,1,1],[0,1,0,0,0],[0,1,0,0,1],[0,1,0,1,0],[0,1,0,1,1],[0,1,1,0,0],[0,1,1,0,1],[0,1,1,1,0],[0,1,1,1,1]]
in_32=[[0,0,0,0,0,0],[0,0,0,0,0,1],[0,0,0,0,1,0],[0,0,0,0,1,1],[0,0,0,1,0,0],[0,0,0,1,0,1],[0,0,0,1,1,0],[0,0,0,1,1,1],[0,0,1,0,0,0],[0,0,1,0,0,1],[0,0,1,0,1,0],[0,0,1,0,1,1],[0,0,1,1,0,0],[0,0,1,1,0,1],[0,0,1,1,1,0],[0,0,1,1,1,1],[0,1,0,0,0,0],[0,1,0,0,0,1],[0,1,0,0,1,0],[0,1,0,0,1,1],[0,1,0,1,0,0],[0,1,0,1,0,1],[0,1,0,1,1,0],[0,1,0,1,1,1],[0,1,1,0,0,0],[0,1,1,0,0,1],[0,1,1,0,1,0],[0,1,1,0,1,1],[0,1,1,1,0,0],[0,1,1,1,0,1],[0,1,1,1,1,0],[0,1,1,1,1,1]]
in_64=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,0],[0,0,0,0,0,1,1],[0,0,0,0,1,0,0],[0,0,0,0,1,0,1],[0,0,0,0,1,1,0],[0,0,0,0,1,1,1],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[0,0,0,1,0,1,0],[0,0,0,1,0,1,1],[0,0,0,1,1,0,0],[0,0,0,1,1,0,1],[0,0,0,1,1,1,0],[0,0,0,1,1,1,1],[0,0,1,0,0,0,0],[0,0,1,0,0,0,1],[0,0,1,0,0,1,0],[0,0,1,0,0,1,1],[0,0,1,0,1,0,0],[0,0,1,0,1,0,1],[0,0,1,0,1,1,0],[0,0,1,0,1,1,1],[0,0,1,1,0,0,0],[0,0,1,1,0,0,1],[0,0,1,1,0,1,0],[0,0,1,1,0,1,1],[0,0,1,1,1,0,0],[0,0,1,1,1,0,1],[0,0,1,1,1,1,0],[0,0,1,1,1,1,1],[0,1,0,0,0,0,0],[0,1,0,0,0,0,1],[0,1,0,0,0,1,0],[0,1,0,0,0,1,1],[0,1,0,0,1,0,0],[0,1,0,0,1,0,1],[0,1,0,0,1,1,0],[0,1,0,0,1,1,1],[0,1,0,1,0,0,0],[0,1,0,1,0,0,1],[0,1,0,1,0,1,0],[0,1,0,1,0,1,1],[0,1,0,1,1,0,0],[0,1,0,1,1,0,1],[0,1,0,1,1,1,0],[0,1,0,1,1,1,1],[0,1,1,0,0,0,0],[0,1,1,0,0,0,1],[0,1,1,0,0,1,0],[0,1,1,0,0,1,1],[0,1,1,0,1,0,0],[0,1,1,0,1,0,1],[0,1,1,0,1,1,0],[0,1,1,0,1,1,1],[0,1,1,1,0,0,0],[0,1,1,1,0,0,1],[0,1,1,1,0,1,0],[0,1,1,1,0,1,1],[0,1,1,1,1,0,0],[0,1,1,1,1,0,1],[0,1,1,1,1,1,0],[0,1,1,1,1,1,1]]
in_128=[[ 0,0,0,0,0,0,0,0 ],[ 0,0,0,0,0,0,0,1 ],[ 0,0,0,0,0,0,1,0 ],[ 0,0,0,0,0,0,1,1 ],[ 0,0,0,0,0,1,0,0 ],[ 0,0,0,0,0,1,0,1 ],[ 0,0,0,0,0,1,1,0 ],[ 0,0,0,0,0,1,1,1 ],[ 0,0,0,0,1,0,0,0 ],[ 0,0,0,0,1,0,0,1 ],[ 0,0,0,0,1,0,1,0 ],[ 0,0,0,0,1,0,1,1 ],[ 0,0,0,0,1,1,0,0 ],[ 0,0,0,0,1,1,0,1 ],[ 0,0,0,0,1,1,1,0 ],[ 0,0,0,0,1,1,1,1 ],[ 0,0,0,1,0,0,0,0 ],[ 0,0,0,1,0,0,0,1 ],[ 0,0,0,1,0,0,1,0 ],[ 0,0,0,1,0,0,1,1 ],[ 0,0,0,1,0,1,0,0 ],[0,0,0,1,0,1,0,1 ],[ 0,0,0,1,0,1,1,0 ],[ 0,0,0,1,0,1,1,1 ],[ 0,0,0,1,1,0,0,0 ],[ 0,0,0,1,1,0,0,1 ],[ 0,0,0,1,1,0,1,0 ],[ 0,0,0,1,1,0,1,1 ],[ 0,0,0,1,1,1,0,0 ],[ 0,0,0,1,1,1,0,1 ],[ 0,0,0,1,1,1,1,0 ],[ 0,0,0,1,1,1,1,1 ],[ 0,0,1,0,0,0,0,0 ],[ 0,0,1,0,0,0,0,1 ],[ 0,0,1,0,0,0,1,0 ],[ 0,0,1,0,0,0,1,1 ],[ 0,0,1,0,0,1,0,0 ],[ 0,0,1,0,0,1,0,1 ],[ 0,0,1,0,0,1,1,0 ],[ 0,0,1,0,0,1,1,1 ],[ 0,0,1,0,1,0,0,0 ],[ 0,0,1,0,1,0,0,1 ],[ 0,0,1,0,1,0,1,0 ],[ 0,0,1,0,1,0,1,1 ],[ 0,0,1,0,1,1,0,0 ],[ 0,0,1,0,1,1,0,1 ],[ 0,0,1,0,1,1,1,0 ],[ 0,0,1,0,1,1,1,1 ],[ 0,0,1,1,0,0,0,0 ],[ 0,0,1,1,0,0,0,1 ],[ 0,0,1,1,0,0,1,0 ],[ 0,0,1,1,0,0,1,1 ],[ 0,0,1,1,0,1,0,0 ],[ 0,0,1,1,0,1,0,1 ],[ 0,0,1,1,0,1,1,0 ],[ 0,0,1,1,0,1,1,1 ],[ 0,0,1,1,1,0,0,0 ],[ 0,0,1,1,1,0,0,1 ],[ 0,0,1,1,1,0,1,0 ],[ 0,0,1,1,1,0,1,1 ],[ 0,0,1,1,1,1,0,0 ],[ 0,0,1,1,1,1,0,1 ],[ 0,0,1,1,1,1,1,0 ],[ 0,0,1,1,1,1,1,1 ],[ 0,1,0,0,0,0,0,0 ],[ 0,1,0,0,0,0,0,1 ],[ 0,1,0,0,0,0,1,0 ],[ 0,1,0,0,0,0,1,1 ],[ 0,1,0,0,0,1,0,0 ],[ 0,1,0,0,0,1,0,1 ],[ 0,1,0,0,0,1,1,0 ],[ 0,1,0,0,0,1,1,1 ],[ 0,1,0,0,1,0,0,0 ],[ 0,1,0,0,1,0,0,1 ],[ 0,1,0,0,1,0,1,0 ],[ 0,1,0,0,1,0,1,1 ],[ 0,1,0,0,1,1,0,0 ],[ 0,1,0,0,1,1,0,1 ],[ 0,1,0,0,1,1,1,0 ],[ 0,1,0,0,1,1,1,1 ],[ 0,1,0,1,0,0,0,0 ],[ 0,1,0,1,0,0,0,1 ],[ 0,1,0,1,0,0,1,0 ],[ 0,1,0,1,0,0,1,1 ],[ 0,1,0,1,0,1,0,0 ],[ 0,1,0,1,0,1,0,1 ],[ 0,1,0,1,0,1,1,0 ],[ 0,1,0,1,0,1,1,1 ],[ 0,1,0,1,1,0,0,0 ],[ 0,1,0,1,1,0,0,1 ],[ 0,1,0,1,1,0,1,0 ],[ 0,1,0,1,1,0,1,1 ],[ 0,1,0,1,1,1,0,0 ],[ 0,1,0,1,1,1,0,1 ],[ 0,1,0,1,1,1,1,0 ],[ 0,1,0,1,1,1,1,1 ],[ 0,1,1,0,0,0,0,0 ],[ 0,1,1,0,0,0,0,1 ],[ 0,1,1,0,0,0,1,0 ],[ 0,1,1,0,0,0,1,1 ],[ 0,1,1,0,0,1,0,0 ],[ 0,1,1,0,0,1,0,1 ],[ 0,1,1,0,0,1,1,0 ],[ 0,1,1,0,0,1,1,1 ],[ 0,1,1,0,1,0,0,0 ],[ 0,1,1,0,1,0,0,1 ],[ 0,1,1,0,1,0,1,0 ],[ 0,1,1,0,1,0,1,1 ],[ 0,1,1,0,1,1,0,0 ],[ 0,1,1,0,1,1,0,1 ],[ 0,1,1,0,1,1,1,0 ],[ 0,1,1,0,1,1,1,1 ],[ 0,1,1,1,0,0,0,0 ],[ 0,1,1,1,0,0,0,1 ],[ 0,1,1,1,0,0,1,0 ],[ 0,1,1,1,0,0,1,1 ],[ 0,1,1,1,0,1,0,0 ],[ 0,1,1,1,0,1,0,1 ],[ 0,1,1,1,0,1,1,0 ],[ 0,1,1,1,0,1,1,1 ],[ 0,1,1,1,1,0,0,0 ],[ 0,1,1,1,1,0,0,1 ],[ 0,1,1,1,1,0,1,0 ],[ 0,1,1,1,1,0,1,1 ],[ 0,1,1,1,1,1,0,0 ],[ 0,1,1,1,1,1,0,1 ],[ 0,1,1,1,1,1,1,0 ],[ 0,1,1,1,1,1,1,1 ]]

va3=[0x0, 0x55, 0x33, 0x66]
va4=[0x0, 0x5555, 0x3333, 0x6666, 0xf0f, 0x5a5a, 0x3c3c, 0x6969]
va5=[0x0, 0x55555555, 0x33333333, 0x66666666, 0xf0f0f0f, 0x5a5a5a5a, 0x3c3c3c3c, 0x69696969, 0xff00ff, 0x55aa55aa, 0x33cc33cc, 0x66996699, 0xff00ff0, 0x5aa55aa5, 0x3cc33cc3, 0x69966996]
va6=[0x0, 0x5555555555555555, 0x3333333333333333, 0x6666666666666666, 0xF0F0F0F0F0F0F0F, 0x5A5A5A5A5A5A5A5A, 0x3C3C3C3C3C3C3C3C, 0x6969696969696969, 0xFF00FF00FF00FF, 0x55AA55AA55AA55AA, 0x33CC33CC33CC33CC, 0x6699669966996699, 0xFF00FF00FF00FF0, 0x5AA55AA55AA55AA5, 0x3CC33CC33CC33CC3, 0x6996699669966996, 0xFFFF0000FFFF, 0x5555AAAA5555AAAA, 0x3333CCCC3333CCCC, 0x6666999966669999, 0xF0FF0F00F0FF0F0, 0x5A5AA5A55A5AA5A5, 0x3C3CC3C33C3CC3C3, 0x6969969669699696, 0xFFFF0000FFFF00, 0x55AAAA5555AAAA55, 0x33CCCC3333CCCC33, 0x6699996666999966, 0xFF0F00F0FF0F00F, 0x5AA5A55A5AA5A55A, 0x3CC3C33C3CC3C33C, 0x6996966969969669]
va7=[0x0, 0x55555555555555555555555555555555, 0x33333333333333333333333333333333, 0x66666666666666666666666666666666, 0xF0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F, 0x5A5A5A5A5A5A5A5A5A5A5A5A5A5A5A5A, 0x3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C3C, 0x69696969696969696969696969696969, 0xFF00FF00FF00FF00FF00FF00FF00FF, 0x55AA55AA55AA55AA55AA55AA55AA55AA, 0x33CC33CC33CC33CC33CC33CC33CC33CC, 0x66996699669966996699669966996699, 0xFF00FF00FF00FF00FF00FF00FF00FF0, 0x5AA55AA55AA55AA55AA55AA55AA55AA5, 0x3CC33CC33CC33CC33CC33CC33CC33CC3, 0x69966996699669966996699669966996, 0xFFFF0000FFFF0000FFFF0000FFFF, 0x5555AAAA5555AAAA5555AAAA5555AAAA, 0x3333CCCC3333CCCC3333CCCC3333CCCC, 0x66669999666699996666999966669999, 0xF0FF0F00F0FF0F00F0FF0F00F0FF0F0, 0x5A5AA5A55A5AA5A55A5AA5A55A5AA5A5, 0x3C3CC3C33C3CC3C33C3CC3C33C3CC3C3, 0x69699696696996966969969669699696, 0xFFFF0000FFFF0000FFFF0000FFFF00, 0x55AAAA5555AAAA5555AAAA5555AAAA55, 0x33CCCC3333CCCC3333CCCC3333CCCC33, 0x66999966669999666699996666999966, 0xFF0F00F0FF0F00F0FF0F00F0FF0F00F, 0x5AA5A55A5AA5A55A5AA5A55A5AA5A55A, 0x3CC3C33C3CC3C33C3CC3C33C3CC3C33C, 0x69969669699696696996966969969669, 0xFFFFFFFF00000000FFFFFFFF, 0x55555555AAAAAAAA55555555AAAAAAAA, 0x33333333CCCCCCCC33333333CCCCCCCC, 0x66666666999999996666666699999999, 0xF0F0F0FF0F0F0F00F0F0F0FF0F0F0F0, 0x5A5A5A5AA5A5A5A55A5A5A5AA5A5A5A5, 0x3C3C3C3CC3C3C3C33C3C3C3CC3C3C3C3, 0x69696969969696966969696996969696, 0xFF00FFFF00FF0000FF00FFFF00FF00, 0x55AA55AAAA55AA5555AA55AAAA55AA55, 0x33CC33CCCC33CC3333CC33CCCC33CC33, 0x66996699996699666699669999669966, 0xFF00FF0F00FF00F0FF00FF0F00FF00F, 0x5AA55AA5A55AA55A5AA55AA5A55AA55A, 0x3CC33CC3C33CC33C3CC33CC3C33CC33C, 0x69966996966996696996699696699669, 0xFFFFFFFF00000000FFFFFFFF0000, 0x5555AAAAAAAA55555555AAAAAAAA5555, 0x3333CCCCCCCC33333333CCCCCCCC3333, 0x66669999999966666666999999996666, 0xF0FF0F0F0F00F0F0F0FF0F0F0F00F0F, 0x5A5AA5A5A5A55A5A5A5AA5A5A5A55A5A, 0x3C3CC3C3C3C33C3C3C3CC3C3C3C33C3C, 0x69699696969669696969969696966969, 0xFFFF00FF0000FF00FFFF00FF0000FF, 0x55AAAA55AA5555AA55AAAA55AA5555AA, 0x33CCCC33CC3333CC33CCCC33CC3333CC, 0x66999966996666996699996699666699, 0xFF0F00FF00F0FF00FF0F00FF00F0FF0, 0x5AA5A55AA55A5AA55AA5A55AA55A5AA5, 0x3CC3C33CC33C3CC33CC3C33CC33C3CC3, 0x69969669966969966996966996696996]
va8=[0x0, 0x5555555555555555555555555555555555555555555555555555555555555555, 0x3333333333333333333333333333333333333333333333333333333333333333, 0x6666666666666666666666666666666666666666666666666666666666666666, 0xf0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f, 0x5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a, 0x3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c, 0x6969696969696969696969696969696969696969696969696969696969696969, 0xff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff, 0x55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa, 0x33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc, 0x6699669966996699669966996699669966996699669966996699669966996699, 0xff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff0, 0x5aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa55aa5, 0x3cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc33cc3, 0x6996699669966996699669966996699669966996699669966996699669966996, 0xffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff, 0x5555aaaa5555aaaa5555aaaa5555aaaa5555aaaa5555aaaa5555aaaa5555aaaa, 0x3333cccc3333cccc3333cccc3333cccc3333cccc3333cccc3333cccc3333cccc, 0x6666999966669999666699996666999966669999666699996666999966669999, 0xf0ff0f00f0ff0f00f0ff0f00f0ff0f00f0ff0f00f0ff0f00f0ff0f00f0ff0f0, 0x5a5aa5a55a5aa5a55a5aa5a55a5aa5a55a5aa5a55a5aa5a55a5aa5a55a5aa5a5, 0x3c3cc3c33c3cc3c33c3cc3c33c3cc3c33c3cc3c33c3cc3c33c3cc3c33c3cc3c3, 0x6969969669699696696996966969969669699696696996966969969669699696, 0xffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff00, 0x55aaaa5555aaaa5555aaaa5555aaaa5555aaaa5555aaaa5555aaaa5555aaaa55, 0x33cccc3333cccc3333cccc3333cccc3333cccc3333cccc3333cccc3333cccc33, 0x6699996666999966669999666699996666999966669999666699996666999966, 0xff0f00f0ff0f00f0ff0f00f0ff0f00f0ff0f00f0ff0f00f0ff0f00f0ff0f00f, 0x5aa5a55a5aa5a55a5aa5a55a5aa5a55a5aa5a55a5aa5a55a5aa5a55a5aa5a55a, 0x3cc3c33c3cc3c33c3cc3c33c3cc3c33c3cc3c33c3cc3c33c3cc3c33c3cc3c33c, 0x6996966969969669699696696996966969969669699696696996966969969669, 0xffffffff00000000ffffffff00000000ffffffff00000000ffffffff, 0x55555555aaaaaaaa55555555aaaaaaaa55555555aaaaaaaa55555555aaaaaaaa, 0x33333333cccccccc33333333cccccccc33333333cccccccc33333333cccccccc, 0x6666666699999999666666669999999966666666999999996666666699999999, 0xf0f0f0ff0f0f0f00f0f0f0ff0f0f0f00f0f0f0ff0f0f0f00f0f0f0ff0f0f0f0, 0x5a5a5a5aa5a5a5a55a5a5a5aa5a5a5a55a5a5a5aa5a5a5a55a5a5a5aa5a5a5a5, 0x3c3c3c3cc3c3c3c33c3c3c3cc3c3c3c33c3c3c3cc3c3c3c33c3c3c3cc3c3c3c3, 0x6969696996969696696969699696969669696969969696966969696996969696, 0xff00ffff00ff0000ff00ffff00ff0000ff00ffff00ff0000ff00ffff00ff00, 0x55aa55aaaa55aa5555aa55aaaa55aa5555aa55aaaa55aa5555aa55aaaa55aa55, 0x33cc33cccc33cc3333cc33cccc33cc3333cc33cccc33cc3333cc33cccc33cc33, 0x6699669999669966669966999966996666996699996699666699669999669966, 0xff00ff0f00ff00f0ff00ff0f00ff00f0ff00ff0f00ff00f0ff00ff0f00ff00f, 0x5aa55aa5a55aa55a5aa55aa5a55aa55a5aa55aa5a55aa55a5aa55aa5a55aa55a, 0x3cc33cc3c33cc33c3cc33cc3c33cc33c3cc33cc3c33cc33c3cc33cc3c33cc33c, 0x6996699696699669699669969669966969966996966996696996699696699669, 0xffffffff00000000ffffffff00000000ffffffff00000000ffffffff0000, 0x5555aaaaaaaa55555555aaaaaaaa55555555aaaaaaaa55555555aaaaaaaa5555, 0x3333cccccccc33333333cccccccc33333333cccccccc33333333cccccccc3333, 0x6666999999996666666699999999666666669999999966666666999999996666, 0xf0ff0f0f0f00f0f0f0ff0f0f0f00f0f0f0ff0f0f0f00f0f0f0ff0f0f0f00f0f, 0x5a5aa5a5a5a55a5a5a5aa5a5a5a55a5a5a5aa5a5a5a55a5a5a5aa5a5a5a55a5a, 0x3c3cc3c3c3c33c3c3c3cc3c3c3c33c3c3c3cc3c3c3c33c3c3c3cc3c3c3c33c3c, 0x6969969696966969696996969696696969699696969669696969969696966969, 0xffff00ff0000ff00ffff00ff0000ff00ffff00ff0000ff00ffff00ff0000ff, 0x55aaaa55aa5555aa55aaaa55aa5555aa55aaaa55aa5555aa55aaaa55aa5555aa, 0x33cccc33cc3333cc33cccc33cc3333cc33cccc33cc3333cc33cccc33cc3333cc, 0x6699996699666699669999669966669966999966996666996699996699666699, 0xff0f00ff00f0ff00ff0f00ff00f0ff00ff0f00ff00f0ff00ff0f00ff00f0ff0, 0x5aa5a55aa55a5aa55aa5a55aa55a5aa55aa5a55aa55a5aa55aa5a55aa55a5aa5, 0x3cc3c33cc33c3cc33cc3c33cc33c3cc33cc3c33cc33c3cc33cc3c33cc33c3cc3, 0x6996966996696996699696699669699669969669966969966996966996696996, 0xffffffffffffffff0000000000000000ffffffffffffffff, 0x5555555555555555aaaaaaaaaaaaaaaa5555555555555555aaaaaaaaaaaaaaaa, 0x3333333333333333cccccccccccccccc3333333333333333cccccccccccccccc, 0x6666666666666666999999999999999966666666666666669999999999999999, 0xf0f0f0f0f0f0f0ff0f0f0f0f0f0f0f00f0f0f0f0f0f0f0ff0f0f0f0f0f0f0f0, 0x5a5a5a5a5a5a5a5aa5a5a5a5a5a5a5a55a5a5a5a5a5a5a5aa5a5a5a5a5a5a5a5, 0x3c3c3c3c3c3c3c3cc3c3c3c3c3c3c3c33c3c3c3c3c3c3c3cc3c3c3c3c3c3c3c3, 0x6969696969696969969696969696969669696969696969699696969696969696, 0xff00ff00ff00ffff00ff00ff00ff0000ff00ff00ff00ffff00ff00ff00ff00, 0x55aa55aa55aa55aaaa55aa55aa55aa5555aa55aa55aa55aaaa55aa55aa55aa55, 0x33cc33cc33cc33cccc33cc33cc33cc3333cc33cc33cc33cccc33cc33cc33cc33, 0x6699669966996699996699669966996666996699669966999966996699669966, 0xff00ff00ff00ff0f00ff00ff00ff00f0ff00ff00ff00ff0f00ff00ff00ff00f, 0x5aa55aa55aa55aa5a55aa55aa55aa55a5aa55aa55aa55aa5a55aa55aa55aa55a, 0x3cc33cc33cc33cc3c33cc33cc33cc33c3cc33cc33cc33cc3c33cc33cc33cc33c, 0x6996699669966996966996699669966969966996699669969669966996699669, 0xffff0000ffffffff0000ffff00000000ffff0000ffffffff0000ffff0000, 0x5555aaaa5555aaaaaaaa5555aaaa55555555aaaa5555aaaaaaaa5555aaaa5555, 0x3333cccc3333cccccccc3333cccc33333333cccc3333cccccccc3333cccc3333, 0x6666999966669999999966669999666666669999666699999999666699996666, 0xf0ff0f00f0ff0f0f0f00f0ff0f00f0f0f0ff0f00f0ff0f0f0f00f0ff0f00f0f, 0x5a5aa5a55a5aa5a5a5a55a5aa5a55a5a5a5aa5a55a5aa5a5a5a55a5aa5a55a5a, 0x3c3cc3c33c3cc3c3c3c33c3cc3c33c3c3c3cc3c33c3cc3c3c3c33c3cc3c33c3c, 0x6969969669699696969669699696696969699696696996969696696996966969, 0xffff0000ffff00ff0000ffff0000ff00ffff0000ffff00ff0000ffff0000ff, 0x55aaaa5555aaaa55aa5555aaaa5555aa55aaaa5555aaaa55aa5555aaaa5555aa, 0x33cccc3333cccc33cc3333cccc3333cc33cccc3333cccc33cc3333cccc3333cc, 0x6699996666999966996666999966669966999966669999669966669999666699, 0xff0f00f0ff0f00ff00f0ff0f00f0ff00ff0f00f0ff0f00ff00f0ff0f00f0ff0, 0x5aa5a55a5aa5a55aa55a5aa5a55a5aa55aa5a55a5aa5a55aa55a5aa5a55a5aa5, 0x3cc3c33c3cc3c33cc33c3cc3c33c3cc33cc3c33c3cc3c33cc33c3cc3c33c3cc3, 0x6996966969969669966969969669699669969669699696699669699696696996, 0xffffffffffffffff0000000000000000ffffffffffffffff00000000, 0x55555555aaaaaaaaaaaaaaaa5555555555555555aaaaaaaaaaaaaaaa55555555, 0x33333333cccccccccccccccc3333333333333333cccccccccccccccc33333333, 0x6666666699999999999999996666666666666666999999999999999966666666, 0xf0f0f0ff0f0f0f0f0f0f0f00f0f0f0f0f0f0f0ff0f0f0f0f0f0f0f00f0f0f0f, 0x5a5a5a5aa5a5a5a5a5a5a5a55a5a5a5a5a5a5a5aa5a5a5a5a5a5a5a55a5a5a5a, 0x3c3c3c3cc3c3c3c3c3c3c3c33c3c3c3c3c3c3c3cc3c3c3c3c3c3c3c33c3c3c3c, 0x6969696996969696969696966969696969696969969696969696969669696969, 0xff00ffff00ff00ff00ff0000ff00ff00ff00ffff00ff00ff00ff0000ff00ff, 0x55aa55aaaa55aa55aa55aa5555aa55aa55aa55aaaa55aa55aa55aa5555aa55aa, 0x33cc33cccc33cc33cc33cc3333cc33cc33cc33cccc33cc33cc33cc3333cc33cc, 0x6699669999669966996699666699669966996699996699669966996666996699, 0xff00ff0f00ff00ff00ff00f0ff00ff00ff00ff0f00ff00ff00ff00f0ff00ff0, 0x5aa55aa5a55aa55aa55aa55a5aa55aa55aa55aa5a55aa55aa55aa55a5aa55aa5, 0x3cc33cc3c33cc33cc33cc33c3cc33cc33cc33cc3c33cc33cc33cc33c3cc33cc3, 0x6996699696699669966996696996699669966996966996699669966969966996, 0xffffffff0000ffff00000000ffff0000ffffffff0000ffff00000000ffff, 0x5555aaaaaaaa5555aaaa55555555aaaa5555aaaaaaaa5555aaaa55555555aaaa, 0x3333cccccccc3333cccc33333333cccc3333cccccccc3333cccc33333333cccc, 0x6666999999996666999966666666999966669999999966669999666666669999, 0xf0ff0f0f0f00f0ff0f00f0f0f0ff0f00f0ff0f0f0f00f0ff0f00f0f0f0ff0f0, 0x5a5aa5a5a5a55a5aa5a55a5a5a5aa5a55a5aa5a5a5a55a5aa5a55a5a5a5aa5a5, 0x3c3cc3c3c3c33c3cc3c33c3c3c3cc3c33c3cc3c3c3c33c3cc3c33c3c3c3cc3c3, 0x6969969696966969969669696969969669699696969669699696696969699696, 0xffff00ff0000ffff0000ff00ffff0000ffff00ff0000ffff0000ff00ffff00, 0x55aaaa55aa5555aaaa5555aa55aaaa5555aaaa55aa5555aaaa5555aa55aaaa55, 0x33cccc33cc3333cccc3333cc33cccc3333cccc33cc3333cccc3333cc33cccc33, 0x6699996699666699996666996699996666999966996666999966669966999966, 0xff0f00ff00f0ff0f00f0ff00ff0f00f0ff0f00ff00f0ff0f00f0ff00ff0f00f, 0x5aa5a55aa55a5aa5a55a5aa55aa5a55a5aa5a55aa55a5aa5a55a5aa55aa5a55a, 0x3cc3c33cc33c3cc3c33c3cc33cc3c33c3cc3c33cc33c3cc3c33c3cc33cc3c33c, 0x6996966996696996966969966996966969969669966969969669699669969669]

s3_in=[0xF,0x33,0x55]
s4_in=[0xFF,0xF0F,0x3333,0x5555]
s5_in=[0xFFFF,0xFF00FF,0xF0F0F0F,0x33333333,0x55555555]
s6_in=[0xFFFFFFFF,0xFFFF0000FFFF,0xFF00FF00FF00FF,0xF0F0F0F0F0F0F0F,0x3333333333333333,0x5555555555555555]
s7_in=[0xFFFFFFFFFFFFFFFF,0xFFFFFFFF00000000FFFFFFFF,0xFFFF0000FFFF0000FFFF0000FFFF,0xFF00FF00FF00FF00FF00FF00FF00FF,0xF0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F,0x33333333333333333333333333333333,0x55555555555555555555555555555555]
s8_in=[0x00000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,        0x0000000000000000FFFFFFFFFFFFFFFF0000000000000000FFFFFFFFFFFFFFFF,        0x00000000FFFFFFFF00000000FFFFFFFF00000000FFFFFFFF00000000FFFFFFFF,        0x0000FFFF0000FFFF0000FFFF0000FFFF0000FFFF0000FFFF0000FFFF0000FFFF,        0x00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF,        0x0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F,        0x3333333333333333333333333333333333333333333333333333333333333333,        0x5555555555555555555555555555555555555555555555555555555555555555]

sin={3:[in_4,va3,s3_in], 4:[in_8,va4, s4_in], 5:[in_16,va5, s5_in],6:[in_32,va6, s6_in],7:[in_64,va7, s7_in], 8:[in_128,va8, s8_in]}

def make_lat(s):
    
    # size=len(s)
    fs=convert(s)
    # bsize=len(fs)
    # tsize=2**(bsize-1)
    
    # init_s = sin[bsize][0]
    # va=sin[bsize][1]
    # s_in = sin[bsize][2]
    
    # lat = [ [0 for i in range(size)] for j in range(size) ]
    
    # tmp=s_in[0]^fs[0]
    
    # for i in range(tsize):
    #     for j in range(tsize):
    #         valA2 = 0
    #         for k in range(1,bsize):
    #             valA2^=(fs[k]*init_s[j][k])

    #         valA3 = va[i]^valA2
            
    #         lat[i][j]=abs(bin(valA3).count('1') - tsize)
    #         lat[i|tsize][j]= abs(bin( valA3 ^ s_in[0]).count('1') - tsize)
    #         lat[i][j|tsize]=abs(bin(valA3 ^ fs[0]).count('1') - tsize)
    #         lat[i|tsize][j|tsize]=abs(bin(valA3^tmp).count('1') - tsize)
                        
    # return lat
    return fmake_lat(fs)

def fmake_ddt(fs):
    s=convert(fs,False)
    size=len(s)
    ddt=[ [0 for i in range(size)] for j in range(size) ]
    for i in range(size):
        for j in range(size):
            ddt[i^j][s[i]^s[j]]+=1
    return ddt

def fmake_lat(fs):
    
    bsize=len(fs)
    size=2**bsize
    tsize=2**(bsize-1)
    
    init_s = sin[bsize][0]
    va=sin[bsize][1]
    s_in = sin[bsize][2]
    
    lat = [ [0 for i in range(size)] for j in range(size) ]
    
    tmp=s_in[0]^fs[0]
    
    for i in range(tsize):
        for j in range(tsize):
            valA2 = 0
            for k in range(1,bsize):
                valA2^=(fs[k]*init_s[j][k])

            valA3 = va[i]^valA2
            
            lat[i][j]=abs(bin(valA3).count('1') - tsize)
            lat[i|tsize][j]= abs(bin( valA3 ^ s_in[0]).count('1') - tsize)
            lat[i][j|tsize]=abs(bin(valA3 ^ fs[0]).count('1') - tsize)
            lat[i|tsize][j|tsize]=abs(bin(valA3^tmp).count('1') - tsize)
                        
    return lat

def original_LAT(s):
    n=len(s)
    LAT = [[-int(2**n/2) for i in range(2**n)] for j in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            for x in range(2**n):
                LAT[i][j] += bin((i&x)^(j&S[x])).count('1')%2
    return LAT
    
def table_max(table):
    tlen=len(table)
    
    t=[max(table[0][1:])]+[max(table[i]) for i in range(1,tlen)]
    
    return max(t)

def table_num_count(table,num):
    x=0
    for i in table:
        x+=i.count(num)
    return x


def view_11(t):
    tsize=len(t)

    one=[]
    for i in [1,2,4,8,16,32,64,128]:
        if i<tsize:
            one.append(i)
        else:
            break

    for i in one:
        for j in one:
            if (t[i][j]!=0):
                if (t[i][j]>=16):
                    print(C_CYAN+"{:02d} ".format(t[i][j])+C_END,end='')
                else:
                    print(C_YELLOW+"{:02d} ".format(t[i][j])+C_END,end='')
            else:
                print('{:02d} '.format(t[i][j]),end='')
        print('')
    print("")

def view_12(t): #1-2
    tsize=len(t)

    one=[]
    for i in [1,2,4,8,16,32,64,128]:
        if i<tsize:
            one.append(i)
        else:
            break
    two=[]
    for i in [3,5,6,9,10,12,17,18,20,24,33,34,36,40,48,65,66,68,72,80,96,129,130,132,136,144,160,192]:
        if i<tsize:
            two.append(i)
        else:
            break
    supermax=table_max(t)
    hmax=supermax>>1

    print(C_GREEN+"   0x"+C_END,end="")
    for i in two:
        print (C_GREEN+"{:02X} ".format(i)+C_END,end="")
    print ("")
    for i in one:
        print (C_GREEN+"0x{:02X} ".format(i)+C_END,end="")
        for j in two:
            
            if(t[i][j]!=0):
                if(t[i][j]>=hmax):
                    if(t[i][j]==supermax):
                        print(C_RED+"{:02d} ".format(t[i][j])+C_END,end='')
                    else:
                        print(C_CYAN+"{:02d} ".format(t[i][j])+C_END,end='')
                else:
                    print(C_YELLOW+"{:02d} ".format(t[i][j])+C_END,end='')
            else:
                print("{:02d} ".format(t[i][j]),end='')

        print('')
    print("")
    
def view_21(t): # 2-1
    tsize=len(t)

    one=[]
    for i in [1,2,4,8,16,32,64,128]:
        if i<tsize:
            one.append(i)
        else:
            break
    two=[]
    for i in [3,5,6,9,10,12,17,18,20,24,33,34,36,40,48,65,66,68,72,80,96,129,130,132,136,144,160,192]:
        if i<tsize:
            two.append(i)
        else:
            break
    supermax=table_max(t)
    hmax=supermax>>1
    print(C_GREEN+"   0x"+C_END,end="")
    for i in one:
        print (C_GREEN+"{:02X} ".format(i)+C_END,end="")
    print("")
    
    for j in two:
        print (C_GREEN+"0x{:02X} ".format(j)+C_END,end="")
        for i in one:
            
            if(t[j][i]!=0):
                if(t[j][i]>=hmax):
                    if(t[j][i]==supermax):
                        print(C_RED+"{:02d} ".format(t[j][i])+C_END,end='')
                    else:
                        print(C_CYAN+"{:02d} ".format(t[j][i])+C_END,end='')
                else:
                    print(C_YELLOW+"{:02d} ".format(t[j][i])+C_END,end='')
            else:
                print("{:02d} ".format(t[j][i]),end='')
        print('')
    print("")


def view_22(t): # 2-1
    tsize=len(t)


    two=[]
    for i in [3,5,6,9,10,12,17,18,20,24,33,34,36,40,48,65,66,68,72,80,96,129,130,132,136,144,160,192]:
        if i<tsize:
            two.append(i)
        else:
            break
    supermax=table_max(t)
    hmax=supermax>>1
    print(C_GREEN+"   0x"+C_END,end="")
    for i in two:
        print (C_GREEN+"{:02X} ".format(i)+C_END,end="")
    print("")
    
    for j in two:
        print (C_GREEN+"0x{:02X} ".format(j)+C_END,end="")
        for i in two:
            
            if(t[j][i]!=0):
                if(t[j][i]>=hmax):
                    if(t[j][i]==supermax):
                        print(C_RED+"{:02d} ".format(t[j][i])+C_END,end='')
                    else:
                        print(C_CYAN+"{:02d} ".format(t[j][i])+C_END,end='')
                else:
                    print(C_YELLOW+"{:02d} ".format(t[j][i])+C_END,end='')
            else:
                print("{:02d} ".format(t[j][i]),end='')
        print('')
    print("")


def count_fixed(s):
    size=len(s)
    count=0
    for i in range(size):
        if i==s[i]:
            count=count+1
    return count

def check_BN(t):#BN check 2,3 (or 4<)
    tsize=len(t)
    one=[]
    BN=0
    
    for i in [1,2,4,8,16,32,64,128]:
        if i<tsize:
            one.append(i)
        else:
            break
    for i in one:
        for j in one:
            if (t[i][j]!=0):
                return 2#BN2
    
    two=[]
    for i in [3,5,6,9,10,12,17,18,20,24,33,34,36,40,48,65,66,68,72,80,96,129,130,132,136,144,160,192]:
        if i<tsize:
            two.append(i)
        else:
            break
    for i in one:
        for j in two:
            if (t[i][j]!=0) or (t[j][i]!=0):
                return 3#BN3
        
    return 4#BN4
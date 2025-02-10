fg = open("/storage/emulated/0/comentarios/dicionário.txt")

DIC = fg.read().split("\n")

#print(DIC)
#exit(0)
import random
gends = open("/storage/emulated/0/comentarios/good_ends.txt")

gendslist = gends.read().split("\n")

def good_end():
    
    global gendslist
    
    
    return gendslist[random.randint(0, len(gendslist)-1)]
def generate(leng):
    
    global DIC
    RY = ""
    for i in range(leng):
        rw = DIC[random.randint(0, len(DIC)-1)] 
        if RY.find(rw) == -1:
        #print(DIC[random.randint(0, len(DIC))-1])
            RY = RY + rw + " "
    #int(RY)
    RY = RY + good_end()
    #gerar texto comparar texto com pre gerados!
    return RY



gs = open("/storage/emulated/0/comentarios/good_sen.txt")

D = fg.read().split("\n")
GS = gs.read().split("\n")


spacing = 4
def is_between(sentence, letter, index):
    actual_index = 0
    
    global spacing
    R = False
    for SL in sentence:
        if SL == letter and index > actual_index - spacing and index < actual_index + spacing:
            R = True
        actual_index = actual_index + 1
    
    return R
    

def count_text(text):
    global GS
    
    co = 0
    
    for sen in GS:
        idx = 0
        for L in text:
            if is_between(sen, L, idx):
                co = co + 1
            idx = idx + 1
    return co

GC = generate(5)

LASTING = 0

H = ""

def tendencia(text):
    
    tendencias = "gostei video eletricidade"
    
    c = 0
    
    for w in tendencias.split(" "):
        c = c + text.find(w)
    return c

def exclude(text):
    
    tendencias = ""
    
    c = 0
    
    for w in tendencias.split(" "):
        c = c + text.find(w)
    return c

def gt():
    global LASTING
    H = ""
    LASTING = 0
    MAXEX = 0
    LTS = 0
    for i in range(1800):
        GC = generate(4)
        #print(i, GC)
        LTS = (0)
        MAXEX = 10000
    #print("hhhhh" ,GC)
        if (count_text(GC)) > LASTING and tendencia(GC) > LTS and exclude(GC) < MAXEX:
            LASTING = count_text(GC)
            H = GC
            LTS = tendencia(GC)
            MAXEX = exclude(GC)
       # print(GC)
    return H

print(count_text("otimo vidro gostei demais"))
print(count_text("desgotei horrivel nada a ver"))

for i in range(8):
    print("generated", gt())
#    print(generate(4))
print("   ")
for i in range(8):
    print("test", generate(4))

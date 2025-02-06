
import random as rmod
leng = 12


goodf = open("/storage/emulated/0/comentarios/good.txt");

badf = open("/storage/emulated/0/comentarios/bad.txt");

dic = open("/storage/emulated/0/comentarios/dicionário.txt");

def is_good():
     r = 0;
     
     return r;
     
     
     
def is_bad():
    r = 0
    return r;

k  = goodf.read().split("\n");
n = badf.read().split("\n");
j = dic.read().split("\n");


def rf():
     return rmod.randint(0, len(j) - 1);


tendencias = "telefone value gostei";
tendencia_len = tendencias.split(" ");


def count_tendencias(tendencias, texts):
    r = 0
    for k in tendencias:
        #rev = k in texts;
        if texts.find(k) == -1:
            r = r + 1
    return r


def generate():
    r1 = "";
    has = False
    for n in range(leng):
        nw = j[rf()];
        if r1.find(nw) != -1:
            has = True
        r1 = r1 + j[rf()] + " "
    
    if (has):
        generate()
    ##print(r);
    return r1

def normalize():
    gt = generate();
    while (count_tendencias(tendencias, gt) < len(tendencia_len)):
        gt = generate();
        
    return gt

def has_bad_connection_of_short(text):
     r1 = False
     for i in range(len(text.split(" ")) - 1):
        if (len(text.split(" ")[i]) <= 3 and len(text.split(" ")[i +1]) <= 3):
            r1 = True
     return r1

def has_bad_start_end(text):
     r1 = False
     for i in range(len(text.split(" ")) - 1):
        if len(text.split(" ")[0]) < 3 and len(text.split(" ")[len(  text.split(" ")  )-2]) < 6:
            r1 = True
     return r1


def has_bad_connection(text):
    r1 = False
    
    sig = False
    for i in range(len(text.split(" ")) - 1):
        ##rint(text.split(" ")[i], text.split(" ")[i+1], len(text.split(" ")[i]))
        #xit(0)
        if has_bad_connection_of_short(text) or has_bad_start_end(text):
           # print("bdjx")
            #if has_good_start_end(text):
            
               #rint("hzhz")
                if i == len(text.split(" ")) -1:
                    sig = False
                    
                    
            ##rint(text.split(" ")[i], len(text.split(" ")[i]))
                
                
                r1= True
                
    #print(text, " & " ,(text.split(" ")[len(  text.split(" ")  )-2]))
    if sig:
        exit(0)
     
        
    return r1


normalizes = ""

def connect():
     global normalizes
     normalizes = normalize()
     #print(normalizes)
     while has_bad_connection(normalizes):
         #print(normalizes)
         if has_bad_connection(normalizes):
              normalizes = normalize()
              
     #print("fkn " , r, "  resp ", has_bad_connection(r))
    #) print(normalizes, "+")
     #exit(0)
     
     return normalizes


def contar_good(text):
    r = 0
    for y in k:
        #print(y)
         if (text.find(y) == -1):
              r = r + 1
    return r

def contar_bad(text):
    r = 0
    for y in n:
        if (text.find(y) == -1):
            r = r + 1
    return r


cg = 0;
cb = 0;


def apply_inteligence():
    global cg
    global cb
    connect();
    r1 = normalizes
    cg = 0
    cb = 0
    cg = contar_good(r1);
    cb = contar_bad(r1);
    #print(r)
    #print(cg, cb)
    return r1
    
    
rfm = ""

def epocs(n):
    global cg
    global cb
    global rfm
    gt = apply_inteligence();
    
    for k in range(n):
        gt = apply_inteligence();
        #print(gt)
        if cg > cb:
            #rint("bsnsm")
            rfm = gt
          #  print(gt)
      ##  print(cg, cb:)
    ##print(cg, cb)




epocs(500);


print(rfm);
print(has_bad_connection(rfm))
print(has_bad_connection_of_short(rfm))

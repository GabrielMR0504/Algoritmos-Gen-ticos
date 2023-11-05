class No:
    x = None,
    y = None,
    dist_final = None,
    dist_perc = None,
    fl_borda = None,
    no_pai = None
    def __init__(self, x, y, no) -> None:
        self.x = x,
        self.y = y,
        self.dist_final = 0,
        self.dist_perc = 0
        self.fl_borda = False,
        self.no_pai = no

def labirinto_arvore_estrela():
    mapa = [
        [1,0,1,1,1,1],
        [1,1,1,1,1,1],
        [1,0,1,0,1,1],
        [1,0,1,1,0,1],
        [1,1,1,1,0,1]
    ]
    list_nos = []
    list_nos_borda = [No(1, 1, None)] 
    pos_final = No(4, 5, None)
    while menor_no != 0 and pos_final.no_pai != None:
        menor_no = proc_melhor_no(list_nos_borda)
        list_nos_vis = get_nos_vizinhos(mapa, menor_no)
        list_nos_vis = calc_distacia(list_nos_vis, pos_final)
        # list_nos.extend(list_nos_vis)
        list_nos_borda.extend(list_nos_vis)
        list_nos_borda = separa_borda(list_nos_borda)
    
def proc_melhor_no(list_nos):
    menor_no  = min(list_nos, key=soma_distancias())
    return menor_no  

def soma_distancias(no):
    return no.dist_final + no.dist_perc

def get_nos_vizinhos(mapa, no):
    import numpy

    list_nos_encontrados = []
    matriz_pos = numpy.mapa()
    dim_matriz = matriz_pos.shape 

    if no.x < dim_matriz[0] - 1:
        if mapa[no.x + 1][no.y]:
            list_nos_encontrados.append(No(no.x + 1, no.y, no))
        
    if no.x > 0:
        if mapa[no.x - 1][no.y]:
            list_nos_encontrados.append(No(no.x - 1, no.y, no))
            
    if no.y < dim_matriz[1] - 1:
        if mapa[no.x][no.y + 1]:
            list_nos_encontrados.append(No(no.x, no.y + 1, no))
            
    if no.y > 0:
        if mapa[no.x][no.y - 1]:
            list_nos_encontrados.append(No(no.x, no.y - 1, no))
    
    return list_nos_encontrados


def calc_distacia(list_no_borda, no_final):
    import math
    for no in list_no_borda:
    
        p1 = pow(no.x - no_final.x)
        p2 = pow(no.y - no_final.y)
        distancia = math.sqrt(p1 + p2)
        no.dist_final = distancia
        no.dist_perc += 1
    return list_no_borda

def separa_borda(list_nos_borda):
    for no in list_nos_borda:
        if no.fl_borda:
            list_nos_borda.remove(no)
    return list_nos_borda 
    
def main():
    labirinto_arvore_estrela()

if __name__ == "__main__":
    main()
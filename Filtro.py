from time import sleep


Codigo = open('Teste.gcode','r')

Codigo_Lista = Codigo.readlines()



Lista_Linhas = []
Linhas = -1

Posição_InicialX = Posição_AtualX = 0.0

Posição_InicialY = Posição_AtualY = 0.0

Posição_InicialZ = Posição_AtualZ = 0.0

def Movimento_X (Distância_AX):

    Tempo = Distância_AX*60/(30*2*3.1415*2)

    print(Tempo)





for Item_Filtro in Codigo_Lista:



    if (Item_Filtro.count("X") == 1 and Item_Filtro.count("Y") == 1 and Item_Filtro.count("Z") == 1):
        
        X = float(Item_Filtro[(Item_Filtro.find("X"))+1:(Item_Filtro.find("Y")-1)])
        

        Y = float(Item_Filtro[(Item_Filtro.find("Y"))+1:(Item_Filtro.find("Z")-1)])
        

        Z = float(Item_Filtro[(Item_Filtro.find("Z"))+1:(Item_Filtro.find("S")-1)])


        Distância_AX = Posição_AtualX - X
        Distância_AY = Posição_AtualY - Y
        Distância_AZ = Posição_AtualZ - Z

        Movimento_X(Distância_AX)



    elif Item_Filtro.count("Spindle Off") == 1:
        
        Lista_Linhas += ["Fim da linha"]



        







    
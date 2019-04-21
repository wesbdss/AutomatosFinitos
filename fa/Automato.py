import os
#Nome: Wesley Benício
#Trabalho de LFA

#------funções------
def listArq(nome):#procura os arquivos
    lista = os.listdir()
    for x in lista:
        if x == nome:
            return x
        
def traduzFunTransiNFA():#transforma uma tabela de transição NFA em Função de transição em DFA
    ini = None
    fin =[]
    transi=[]
    dstates=[]
    try:
        arq = open(listArq('nfaTabela.txt'),'r')
        arq1 = open('nfaFuncao.txt','w')
    except Exception:
        print("Aquivo Inexistente")
        return "Vazio"
    transi = arq.read()#le o arquivo
    transi = transi.split('\n')
    alpha = transi[0].split('\t')
    alpha.pop(0)#retira o espaço vazio
    transi.pop(0)#retira o alphabeto )
    for x in transi: #encontra a transição inicial e a final
        if x[0] == '>' and ini == None:
            y=x.split('\t') # >*q0,q2,q1
            y = y[0].split('>')# '',*q0
            z = y[1]    
            if z[0] == '*':
                z = z.split('*')
                fin.append(z[1])
                ini=z[1]
            else: 
                ini = y[1]
        if x[0] == '*' : # *q1
            z = x.split('*')
            z = z[1]
            z = z.split('\t')
            fin.append(z[0])
    ini='Qi='+str(ini)+'\n'
    Sfin='Qf='
    for p in fin:
        Sfin = Sfin+p+','  
    Sfin= Sfin[:-1]
    Sfin = Sfin+'\n'
    #arq1.write(ini)
    #arq1.write(Sfin)
    arq.close()
    try:
        arq = open(listArq('nfaTabela.txt'),'r')
    except Exception:
        print("Aquivo Inexistente")
        return "Vazio"
    estados = arq.read()
    estados= estados.split("\n")
    alpha = estados[0]
    estados.pop(0)
    alpha = alpha.split('\t')
    alpha.pop(0)
    for x in range(0,len(estados)):
        estados[x] = estados[x].replace('\t','-')
        estados[x] = estados[x].replace('{','')
        estados[x] = estados[x].replace('}','')
        estados[x] = estados[x].replace('>','')
        estados[x] = estados[x].replace('*','')
    y = estados[0].split('-')
    resul = y[0]+',&'+'='+y[0]+','+y[3]
    estini = ini.split('=')
    estini = estini[1]
    estini = estini.split('\n')
    estini = estini[0]
    dstates.append(e_closure(estini,estados))
    ini = dstates[0]
#    print('____Separa AQUI___')
    contd = 0
    while contd < len(dstates):
        start = dstates[contd]
        for x in alpha[:-1]:
            aux1 = move(start,x,estados,alpha[:-1])
            if not aux1:
                resul = e_closure(aux1,estados)
            else:
                resul = e_closure(aux1,estados)
 #           print ("RESULTADO AQUI: ",resul)
            if resul:
                dstates.append(resul)
                dstates = sorted(set(dstates))
        contd=contd+1
    final= fin
    fin = None
    fin = []
    dstatesletras = []
    for x in range(0,len(dstates)):
        dstatesletras.append('q'+str(x))
    for aux2 in range(0,len(dstates)):
        for aux3 in final:
            if dstates[aux2].find(aux3) != -1:
                fin.append(dstatesletras[aux2])
    fin = sorted(set(fin))
  #  print(dstates,'<-->',ini,'<-final->',final,'<-fin->',fin)
    dstatesletras = []
    for x in range(0,len(dstates)):
        dstatesletras.append('q'+str(x))
    print(dstatesletras)
    for z in range(0,len(dstates)):
        if dstates[z].find(ini) != -1:
            ini = dstatesletras[z]
    arq1.write('Qi='+ini+'\n')
    fin = str(fin).replace('[','')
    fin = fin.replace(']','')
    fin = fin.replace(' ','')
    fin = fin.replace('\'','')
    arq1.write('Qf='+fin+'\n')
    for y in range(0,len(dstates)):
        for x in range(0,len(alpha[:-1])):
            aux1 = move(dstates[y],alpha[x],estados,alpha[:-1])
            aux1 = e_closure(aux1,estados)
            for z in range(0,len(dstates)):
                if dstates[z] == aux1:
                    aux = dstatesletras[y]+','+ str(alpha[x])+'='+dstatesletras[z]+'\n'
                    arq1.write(str(aux))
    arq.close()
    arq1.close()
            
    return 


def e_closure(est,estados):#trata a string para leitura pela recursividade
    #print("Começa Closure: ",est)
    final=''
    z = str(est)
    z=z.replace('\'','')
    z=z.replace('[','')
    z=z.replace(']','')
    z=z.replace(' ','')
    if str(est).find(',')>0:
        k=est.split(',')
        for l in k:
            l=l.replace('\'','')
            l=l.replace('[','')
            l=l.replace(']','')
            l=l.replace(' ','')
            final = final+','+e_closure_recursivo(l,estados)        
    else:
        #print("VALOR E CLOSURE ENTRANDO: ",z)
        final = e_closure_recursivo(z,estados)
        #print("O que saiu do Eclosure Recusivo: ",final)
    final = final.replace(',',' ')
    final = final.split(' ')
    final = sorted(set(final))
    #print(final,'<<')
    if final[0] == '':
        final.pop(0)
    final = str(final).replace('[','')
    final = final.replace(']','')
    final = final.replace(' ','')
    final = final.replace('\'','')
    
    #print("Termina Closure: ",final)
    return final
    
def e_closure_recursivo(est,estados):#encontra todos os estados lendo string vazia
    for x in estados:
        y = x.split('-')
       # k = y[len(y)-1]
        if est == y[0]:
            #print("Print aqui: ",k,"<--")
            if str(y[len(y)-1]).find(',')>0 and y[len(y)-1]:
                #print("Entrou no if 1:")
                z=str(y[len(y)-1]).split(',')
                #print("Valor de z: ",z[0],z[1])
                return str(y[0])+','+str(e_closure_recursivo(z[0],estados))+','+str(e_closure_recursivo(z[1],estados))
            if y[len(y)-1]:
                    #print("Entrou no if 2:")
                    return str(y[0])+','+str(e_closure_recursivo(y[3],estados))
            if not y[len(y)-1]:
                    #print("Entrou no else 2:")
                    return str(y[0])
    return ''

    
def move(est,entrada,estados,alpha):#so funciona com conjunto de estados
    #print("Começa Move: ",est)
    final =[]
    try:
        est = str(est).split(',')
    except Exception:
        print("nada")
    for z in estados:
        z = z.split('-')
        for x in est:
            x=x.replace(' ','')
            if z[0] == x:    
                for y in range(0,len(alpha)):
                    #print("Print 2:",entrada,alpha[y])
                    if entrada == alpha[y]:
                        if z[y+1]:
                            #print ("Adicionoi:",z[y+1])
                            final.append(z[y+1])
    final = sorted(set(final))
    final = str(final).replace('\'','')
    final = final.replace('[','')
    final = final.replace(']','')
    #print("Termina Move: ",final)
    return final
    
    
    
    
def traduzFunTransiDFA():
    ini = None
    fin =[]
    try:
        arq = open(listArq('dfaTabela.txt'),'r')
        arq1 = open('dfaFuncao.txt','w')
    except Exception:
        print("Aquivo Inexistente")
        return "Vazio"
    transi = arq.read()#le o arquivo
    transi = transi.split('\n')
    alpha = transi[0].split('\t')
    alpha.pop(0)#retira o espaço vazio
    transi.pop(0)#retira o alphabeto )
    for x in transi: #encontra a transição inicial e a final
        if x[0] == '>' and ini == None:
            y=x.split('\t') # >*q0,q2,q1
            y = y[0].split('>')# '',*q0
            z = y[1]    
            if z[0] == '*':
                z = z.split('*')
                fin.append(z[1])
                ini=z[1]
            else: 
                ini = y[1]
        if x[0] == '*' : # *q1
            z = x.split('*')
            fin.append(z[1])
    ini='Qi='+str(ini)+'\n'
    Sfin='Qf='
    for p in fin:
        Sfin = Sfin+p+','
    Sfin= Sfin[:-1]
    Sfin = Sfin+'\n'
    arq1.write(ini)
    arq1.write(Sfin)
    for x in transi:
        if x[0]=='*' or x[1] == '*':
            x = x.split('*')
            x = x[1]
        x = x.split('\t')
        for y in range(0,len(alpha)):
            string = str(x[0])+','+alpha[y]+'='+str(x[y+1])+'\n'
            arq1.write(string)
    arq1.close()
    arq.close()
    

    
def leituraArq(one,two):
    ini=None
    fin=[]
    try:
        arq = open(listArq(one),'r')
        arqe = open(listArq(two),'r')
    except Exception:
        print("Aquivo Inexistente")
        return "Vazio"
    transi = arq.read()#le o arquivo
    entrada = arqe.read()
    transi = transi.split('\n')#separa as transições
    entrada = entrada.split('\n')
    for x in transi:
        y = x.split('=')
        if y[0] == 'Qi':#encontra o estado inicial
            ini = y[1]
        if y[0] == 'Qf':#encontra o estado final
            y=y[1]
            y = y.split(',')
            fin = y
    if (ini or fin) == None:
        return -1
    transi.pop(0)#retira o estado inicial
    transi.pop(0)#retira o estado final
    arq.close
    return (ini,fin,transi,entrada)

def execute(ini,fin,transi,entrada):
    atual = ini #estado atual recebe o inicio do automato
    entrada = list(entrada)
    z = None
    for num in entrada:
        for x in transi:
            y= x.split(',')
            try:
                z= y[1].split('=')
            except Exception:
                continue
            if y[0] == atual and z[0]==num:
                break
        if y[0] == atual and z[0]==num:#continua lendo a entrada
            atual = z[1]
            continue
        else:#aqui ele rejeita
            atual = None
            break
    for z in fin:
        if atual == z:
            return "Aceito"
    return "Rejeitado"

   
def main():
    traduzFunTransiDFA() # Faz a leitura do arquivo em tabela de transição e transforma em funcçoes de transição
    (ini,fin,transi,entrada)=leituraArq('dfaFuncao.txt','entrada.txt')
    arq = open("ResultadoDFA.txt",'w')
    for x in entrada:
        resultado = execute(ini,fin,transi,x)
        resultado = resultado+'\n'
        arq.write(resultado)
    arq.close
    
def main2():
    traduzFunTransiNFA()
    (ini,fin,transi,entrada) = leituraArq('nfaFuncao.txt','entrada.txt')
    arq = open("ResultadoNFA.txt",'w')
    for x in entrada:
        resultado = execute(ini,fin,transi,x)
        resultado = resultado+'\n'
        arq.write(resultado)
    arq.close        
    
def menu():
    var = None
    while var != 3:
        if var == 1:
            main()
            break;
        if var == 2:
            main2()
            break;
        print("1 - Ler e Calcular DFA")
        print("2 - Ler e Calcular NFA")
        print("3 - Sair")
        var = int (input("Insira a opção: "))
    
#main() DFA pronto
#traduzFunTransiNFA() NFA pronto
menu()


import sys
print("Calcolatrice")
print("Scegli tra somma, sottrazione, moltiplicazione e divisione");  
operazione= input()
print(f'Hai scelto: '+operazione)
if operazione!= 'somma' and operazione!= 'sottrazione' and operazione!= 'moltiplicazione' and operazione!= 'divisione':
    print("operazione non valida")    
    exit(0)    
a=0
b=1
div= False
print("Inserisci i numeri su cui vuoi utilizzare l'operazione: "+operazione+", per uscire digita Exit");
for line in sys.stdin: 
    if 'Exit' == line.rstrip(): 
        break
    x=line
    if operazione == 'somma':
    	a=a+int(x)
    elif operazione=='sottrazione':
        a=int(x)- a
    elif operazione=='moltiplicazione':
        b=int(x)*b
        a=b
    elif operazione=='divisione':
        
        if div==False: 
        	a=int(x)
        	div=True
        elif div==True:
            	a=a/int(x)
print("la "+operazione+" finale è: "+str(a)); 
flag= True
if flag:
	print("Hello WOrld")

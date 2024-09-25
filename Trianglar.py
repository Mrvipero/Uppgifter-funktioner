
def ratviklig_triangel(Symbol):
    for i in range(Symbol,0,-1):
        print("*" * i)

        
def likbent_triangel(Symbol):
    for i in range(1, Symbol + 1, 2):

        Center = (Symbol - i) // 2
        
        print(" " * Center + "*" * i)

Symbol = int(input("skriv in ett udda tal: "))

if Symbol % 2 == 0:
    print("Du du skriv in är inte udda")

else: 
    ratviklig_triangel(Symbol)
    likbent_triangel(Symbol)
    




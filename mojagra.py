print """Jest taka sytuacja. 
Jestes podroznikiem i chcesz gdzies pojechac masz do wyboru 3 kontynenty
Wybieraj:
1. Europa
2. Antarktyda
3. Azja
"""

kontynent = raw_input("> ")
if kontynent == "1" or kontynent == "Europa":

    print """ wow wybrales europe czyli niedaleko
    wybierz teraz sobie jakis kraj sa trzy do wyboru
    1. Polska
    2. Niemcy
    3. Gibraltar
    """
    
    kraj = raw_input("> ")
    
    if kraj == "1" or kraj == "Polska":
    
        print """Przyjezdzasz do Polski i widzisz ze psy szczekaja dupami
        Jestes pewnien ze chcesz tu zostac?
        1. tak zostaje
        2. jade do Niemiec
        3. jade do Gibraltaru
        """
        
        polska = raw_input("> ")
        
        if polska == "1" or polska == "tak zostaje":
            print "dokanales trafnego wyboru!"
            
        elif polska == "2" or polska =="jade do Niemiec":
            print "szerokiej drogi, naqrwiasz do niemiec" and kraj == "2"
            
        elif polska == "3" or polska =="jade do Gibraltaru":
            print "szerokiej drogi, naqrwiasz do Gibraltaru"
            kraj == "3"
        else:
            print "zostales zdezintegrowany"
        
    
    elif kraj == "2" or kraj == "Niemcy":
        print "wyjazd do niemiec sie nie oplacil straciles mnostwo pieniedzy"

    elif kraj == "3" or kraj == "Gibraltar":
        print "bardzo milo spedziles czas widziales jetiego"
        
    else:
        print "nie chcesz podrozowac po europie chyba ..."    
    

    
elif kontynent == "2" or kontynent == "Antarktyda":
    print "niestety trafiles tu w lipcu i bylo bardzo ciemno zamarzles na smierc"

elif kontynent == "3" or kontynent == "Azja":
    print "praca w progresie azja ma za duzo krajow"
    
else:   
    print "nigdzie nie pojechales"    

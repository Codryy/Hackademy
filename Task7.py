#Task7
#Peter Parker este fascinat de viața dublă pe care o are în calitate de supererou.
#El vrea însă să învețe mai mult despre posibilii lui inamici.
#Ajutați-l pe Peter să filtreze printr-o serie de articole de ziar.
#Se primește un titlu al unui articol de ziar și numele unui răufăcător.
#Să se verifice dacă numele răufăcătorului se află în titlul articolului. 
#În caz afirmativ se va afișa un mesaj după următorul format: lungime_titlu + ' : ' + 'L-am găsit pe ' + numele_inamicului.
#Exemplu: 'Doctor Octopus loveste din nou! NY este in pericol!', 'Doctor Octopus' -> '51 : L-am gasit pe Doctor Octopus.'

title = input()
character = input()

if character in title: print(len(title), ":", "L-am gasit pe", character, end=".")
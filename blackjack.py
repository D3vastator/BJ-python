import random
class blackjack:
    def __init__(self):
        self.deck=[]
        self.played=[]
        self.value=0
    def Createdeck(self):
        for i in range(2,11):
            self.deck.append(str(i)+"H")
            self.deck.append(str(i)+"K")
            self.deck.append(str(i)+"P")
            self.deck.append(str(i)+"T")
        for i in "JQKA":
            self.deck.append(str(i)+"H")
            self.deck.append(str(i)+"K")
            self.deck.append(str(i)+"P")
            self.deck.append(str(i)+"T")
    def play(self):
        nasumican=random.randint(0,len(self.deck)-1)
        print "izvucena karta je",self.deck[nasumican]
        self.played.append(self.deck[nasumican])
        self.deck.remove(self.deck[nasumican])
        player.valuez()
        if self.value>21:
            print "You lost. Better luck next time."
            print "bot had",ai.value,"while you had",self.value
            return 0
        print "trenutna vrjednost je",self.value,"bot ima",ai.value,",jos? (y/n)"
        odg=raw_input()
        if odg=='y':
            self.play()
        else:
            if ai.value<player.value:
                while ai.value<player.value:
                    rnd=random.randint(0,len(self.deck)-1)
                    ai.played.append(self.deck[rnd])
                    self.deck.remove(self.deck[rnd])
                    ai.valuez()
                    print "bot drew",ai.played[len(ai.played)-1],"and now has",ai.value
                if ai.value<=21:
                    print "You lost. Better luck next time."
                    print "bot had",ai.value,"while you had",self.value
                else:
                    print "GG. You won."
                    print "bot had",ai.value,"while you had",self.value
            else:
                print "You lost. Better luck next time."
                print "bot had",ai.value,"while you had",self.value
    def bot(self,other):
        for i in range(0,2):
            rnd=random.randint(0,len(other.deck)-1)
            self.played.append(other.deck[rnd])
            other.deck.remove(other.deck[rnd])
        ai.valuez()
        print "bot ima karte",ai.played
    def valuez(self):
        self.value=0
        for j in range(0,len(self.played)):
            if self.played[j][0]=='A':
                AS=self.played[j]
                self.played.remove(AS)
                self.played.append(AS)
        for i in range(0,len(self.played)):
            if self.played[i][0]=='J' or self.played[i][0]=='Q' or self.played[i][0]=='K':
                self.value+=10
            elif self.played[i][0]=='A':
                if self.value+11>21:
                    self.value+=1
                else:
                    self.value+=11
            else:
                brojac=0
                broj=""
                while self.played[i][brojac]!='H' and self.played[i][brojac]!='P' and self.played[i][brojac]!='T' and self.played[i][brojac]!='K':
                        broj+=self.played[i][brojac]
                        brojac+=1
                self.value+=int(broj)
player=blackjack()
ai=blackjack()
player.Createdeck()
ai.bot(player)
player.play()



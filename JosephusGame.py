class Soldier:
    def __init__(self, value):
        self.value = value
        self.next = None

class Army:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addSoldier(self, value):
        newSoldier = Soldier(value)
        if self.head == None:
            self.head = newSoldier
            self.tail = newSoldier
            self.size += 1
        else:
            self.tail.next = newSoldier
            self.tail = newSoldier
            self.tail.next = self.head
            self.size += 1

    def removeSoldier(self, value):
        prevSoldier = Soldier(None)
        currSoldier = None
        # print self.tail.value

        if self.head == None:
            print "No more soldiers!"
            return
        else:
            currSoldier = self.head
            prevSoldier = self.head
            while prevSoldier != self.tail:
                if currSoldier.value == value:
                    if self.head == currSoldier:
                        self.head = currSoldier.next
                        self.tail.next = self.head
                        self.size -= 1
                        break
                    elif self.tail == currSoldier:
                        self.tail = prevSoldier
                        self.tail.next = currSoldier.next
                        self.size -= 1
                        break
                    else:
                        prevSoldier.next = currSoldier.next
                        self.size -= 1
                        break

                prevSoldier = currSoldier
                currSoldier = currSoldier.next

    def displayArmy(self):
        soldier = self.head
        while soldier != self.tail:
            print soldier.value
            soldier = soldier.next
        print self.tail.value
              
def solveJosephus(num_soldiers, steps):
    person = Army()
    for i in range(1, num_soldiers + 1):
        person.addSoldier(i)
    # person.displayArmy()
    if num_soldiers == 0 and steps == 0:
        print "Invalid params passed"
    else:
        step = 1
        currSoldier = person.head
        while person.size > 1:
            if step == steps:
                nextSoldier = currSoldier.next
                person.removeSoldier(currSoldier.value)
                currSoldier = nextSoldier
                step = 0
            else:
                currSoldier = currSoldier.next
            step += 1
        print "Soldier survives: "  
        person.displayArmy()

 
# person = Army()
# person.addSoldier(1)
# person.addSoldier(2)
# person.addSoldier(3)
# person.addSoldier(4)
# person.addSoldier(5)
# # person.displayArmy()
# person.removeSoldier(5)
# person.displayArmy()
num_soldiers = 40
steps = 7

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 41
steps = 3

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 5
steps = 2

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 6
steps = 3

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 6
steps = 2

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 2
steps = 1

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 0
steps = 0

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 500
steps = 3

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 20
steps = 3

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 31
steps = 4

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 20
steps = 5

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)

num_soldiers = 41
steps = 3

# solveJosephus(num_soldiers, steps)
print "\nSOLDIERS: ", num_soldiers, "", "\nSTEPS: ", steps
solveJosephus(num_soldiers, steps)
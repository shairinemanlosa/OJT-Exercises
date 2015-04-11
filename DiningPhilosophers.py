import threading
import time
import logging

logging.basicConfig(format='%(message)s', filename='philosopher_thread.log', level=logging.DEBUG)

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.has_eaten = False
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        logging.debug('%s is hungry.' %(self.name))
        # print '%s is hungry.' %(self.name)
        left_fork = self.left_fork
        right_fork = self.right_fork

        with left_fork:
            logging.debug('%s acquired left fork.' % (self.name))
            # print '%s acquired left fork.' % (self.name)
            with right_fork:
                logging.debug('%s acquired right fork.' % (self.name))
                # print '%s acquired right fork.' % (self.name)
                self.eat()
            logging.debug('%s dropped left fork.' % (self.name))
            # print '%s dropped right fork' % (self.name)
        logging.debug('%s dropped right fork.' % (self.name))
            # print '%s dropped left fork' % (self.name)
        self.leave()
        logging.debug('Everyone has eaten!')

    def eat(self):
        logging.debug('%s starts eating.' % self.name)
        # print '%s starts eating.' % self.name
        time.sleep(.5)

    def leave(self):
        logging.debug('%s left the table.' % self.name)
        self.has_eaten = True
        # print '%s left the table.' % self.name

class Butler(threading.Thread):
    def __init__(self, philosophers):
        threading.Thread.__init__(self)
        self.philosophers = philosophers

    def run(self):
        size = len(self.philosophers)
        i = 0
        counter = 0

        while counter != size:
            if self.philosophers[i].has_eaten == True:
                counter += 1
            if i == size -1:
                i = 0
        if counter == size-1:
            logging.debug('Everyone has eaten!')
            print "Everyone has eaten!"

        
class Dining_Philosopher:
    def __init__(self):

        self.forks = []
        self.philosophers = []
        
        for n in range(6):
            self.forks.append(threading.Lock())

        self.philosopher_name = ['A', 'B', 'C', 'D', 'E']

        for i in range(5):
            self.philosophers.append(Philosopher(self.philosopher_name[i], self.forks[i%5], self.forks[(i+1)%5]))
        
    def start(self):
        butler = Butler(self.philosophers)
        butler.start()

        for philosopher in self.philosophers:
            philosopher.start()


philosopher = Dining_Philosopher()
philosopher.start()
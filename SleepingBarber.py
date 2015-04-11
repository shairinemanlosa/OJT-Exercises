from Queue_Shai import *
import time
import random
import threading
import logging

logging.basicConfig(format='%(message)s', filename='barber_thread_updated.log', level=logging.DEBUG)

class Barber(threading.Thread):
    def __init__(self, last, customers, seat):
        threading.Thread.__init__(self)
        self.customers = customers
        self.seat = seat
        self.last = last
        
    def run(self):
        while True:
            c = self.customers.dequeue()
            if c:
                self.seat.release()
                self.cut(c)
                self.done_cutting(c)
                c.done = True
                if self.last == c:
                    print 'last'
                    break
            else:
                self.sleep()
                self.wake_up()
                
    def sleep(self):
        logging.debug('Mr. Barber is sleeping! Zzzz') 
        time.sleep(3)

    def wake_up(self):
        logging.debug('Mr. Barber woke up!')
        time.sleep(1)

    def cut(self, customer):
        logging.debug("Mr. Barber is cutting Mr. %s's hair..." % customer.name)
        time.sleep(3)

    def done_cutting(self, customer):
        logging.debug("Mr. Barber is done with Mr. %s's hair." % customer.name)
        time.sleep(3)

class Customer(threading.Thread):
    def __init__(self, customers, seat, name):
        threading.Thread.__init__(self)
        self.customers = customers
        self.seat = seat
        self.name = name
        self.is_last = False
        self.done = False

    def run(self):
        c = self.customers
        choice = ['Yes', 'No'] 
        weights = [0.1, 0.9]
        answer = sum([[choice] * int(weight * 100) for choice, weight in zip(choice, weights)], [])

        while True:
            if self.seat.acquire():
                c.enqueue(self)
                self.sit()
                want_to_leave = random.choice(answer)
                print want_to_leave
                if self.is_last == False:
                    if want_to_leave == 'Yes':
                        c.remove_customer(self)
                        self.leave()
                        self.seat.release()
                        break
                self.done_service()
                break

        print 'done' + self.name

    def sit(self):
        logging.debug('Mr. %s sat down in the waiting area.' % self.name)

    def leave(self):
        logging.debug('Mr. %s got tired of waiting and left the barber shop.' % self.name)

    def done_service(self):
        while not self.done:
            continue

class BarberShop:
    def __init__(self, no_seat):
        self.waiting_customers = Couch()
        self.seat = threading.Semaphore(no_seat)
        
    def start_service(self, no_of_customers, customers):
        last_customer = customers[no_of_customers-1]
        last_customer.is_last = True

        logging.debug("Mr. Barber's shop is now open!")

        barber = Barber(last_customer, self.waiting_customers, self.seat)
        barber.start()

        for i in xrange(no_of_customers-1):
            customers[i].start()
            time.sleep(5)

        time.sleep(10)
        last_customer.start()

        time.sleep(10)
        logging.debug("Mr. Barber is done for today!")

if __name__ == '__main__':
    barber = BarberShop(5)
    no_of_customers = 10
    customers = []

    for i in range(no_of_customers):
        customers.append(Customer(barber.waiting_customers, barber.seat, i+1))

    barber.start_service(no_of_customers, customers)
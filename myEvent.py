from Event import Event
from pprint import pprint
from BalloonDesign import BalloonDesign

class MyEvent(Event):
    BalloonDesign=BalloonDesign()
    def __init__(self, type,name,phone,color1, color2, design):
        super(MyEvent,self).__init__(name,phone)
        self.type=type
        self.color1=color1
        self.color2=color2
        self.design=design

#פונקציה שמדפיסה את פרטי ההזמנה

    def printDetils(self):
        print(f'hi {self.customerDetails["name"]}!')
        print(f'we are glad you chose to celebrate your {self.type} with us')
        print('These are the details for your order: ')
        print(f' phone: {self.customerDetails["phone"]} ')
        print(f'your event colors are : {self.color1} , {self.color2}')
        pprint(f'The designs you have chosen are : {self.design}')
        self.forPayment()

#פונקציה שמחשבת את הסכום לתשלום
    def forPayment(self):
        sum=0
        for i in self.design:
            sum+=int(i)*self.BalloonDesign.designs[self.type][self.design[i]]
        print(f'for payment : {sum}$')
        self.orderLog(sum)

#כתיבת פרטי ההזמנה לקובץ ההזמנות
    def orderLog(self,sum):
        orderLogFile=open("orders.txt","a")
        orderLogFile.write('\n')
        orderLogFile.write(f'order : {self.type} , name : {self.customerDetails["name"]}, phone: {self.customerDetails["phone"]}, final price: {sum}$')
        orderLogFile.close()


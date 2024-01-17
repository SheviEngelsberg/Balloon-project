from BalloonDesign import BalloonDesign
from pprint import pprint
from  myEvent import MyEvent
import datetime

#פונקציה שיוצרת מופע של אירוע וקולטת מהמשתמש פרטים עבור האירוע שלו
def createEvent(type, design):
        name=input('enter name')
        phone=input('enter phone')
        color1=input('enter color 1')
        color2=input('enter color 2')
        myCurrentEvent=MyEvent(type,name,phone,color1, color2, design)
        return myCurrentEvent

#פונקציה שמוסיפה ע"י גנרטור את העיצוב והכמות למילון של העיצובים של הלקוח
def update_designs(design,count,currentDesign):
    yield design.update({count:currentDesign})

#למבדה שעושה בדיקת תקינות היא מקבלת מחרוזת ומערך מחרוזות ובודקת האם המחרוזת קיימת במערך
check_string_exists = lambda array, string: "True" if string in array else "False"

#פןנקציה שמטפלת בכל תהליך ההזמנה
def order ():
    print("We are glad you chose to celebrate with us")
    myTypeEvent=input("what are you celebrating? BatMitzva/BarMitzva/wedding/Brit/BirthDay")
    eventArr=['BatMitzva','BarMitzva','wedding','Brit','BirthDay']
    try:
        theDesign=BalloonDesign.designs[myTypeEvent]
        print(f'Balloon designs for {myTypeEvent}:')
    except:
        print("The event type is not available")
        print("Start the order again")
        order()
    else:
        myDesigns={}
        pprint(theDesign)
        print("Let's choose the perfect look for your event!")
        continueToChoose='True'
        while continueToChoose=='True':
            currentDesign=input("choose design >> ")
            count=input("enter count >> ")
            generator=update_designs(myDesigns,count,currentDesign)
            next(generator)
            continueToChoose=input('continue? True/False')

        myEvent=createEvent(myTypeEvent,myDesigns)
        try:
            myEvent.printDetils()
        except:
            print("The system cannot place the order because one of the data is incorrect")
            print("Start the order again")
            order()
        else:
            current_datetime = datetime.datetime.now()
            print(f'Your order was placed on: {current_datetime} ')
            again=input('Do you want to order again ? y/n')
            if again=='y':
                order()
            else:
                print('See you soon!!!')
                orderfile=open("orders.txt","r")
                print(orderfile.read())
                orderfile.close()



BalloonDesign=BalloonDesign()
order()















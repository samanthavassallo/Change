while True:
    money = float(input("How much change is owed?"))
    if money > 0:
        break
money = money * 100
finalAmount = 0
        
while money >= 25:
        money -= 25
        finalAmount += 1
while money >= 10:
        money -= 10
        finalAmount += 1
while money >= 5:
        money -= 5
        finalAmount +=1
while money >= 1:
        money -=1
        finalAmount += 1
print(finalAmount)

def amount_of_money(money):
    if money < 0:
        return False
    else:
        return True
c = amount_of_money(money)

while c == False:
    money = float(input("How much change are you giving"))

def amount_of_money(money):
    if money < 0:
        return False
    else:
        return True
c = amount_of_money(money)

while c == False:
    money = float(input("How much change are you giving"))
    

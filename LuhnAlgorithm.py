Number_of_card = list(input("Enter a card number :").strip())

Check_Number = Number_of_card.pop()
Number_of_card.reverse()
nNumber = []

for index , number in enumerate(Number_of_card):
    if index % 2 == 0 :
        Double_number = int(number) * 2

        if  Double_number > 9:
            Double_number = Double_number - 9
        nNumber.append(Double_number)
    else:
        nNumber.append(int(number))

total_number = int(Check_Number) + sum((nNumber))
if total_number % 10 == 0:
   print("it's valid  a card number")
else:
   print("it's not valid number")
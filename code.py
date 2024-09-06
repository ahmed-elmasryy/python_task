def validate_card(card_number):
    

  if len(card_number)==16 and card_number.isdigit()==True:
    prefix = card_number[:2]
    if prefix in ["34", "37"]:
        return "American Express"
    elif prefix in ["51", "52", "53", "54", "55"]:
        return "MasterCard"
    elif card_number[0] == "4":
        return "Visa"
    
    else:
        return "Invalid"


card_number = input("Enter a credit card number: ")

result = validate_card(card_number)

print(result)
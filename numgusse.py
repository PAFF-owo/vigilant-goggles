num = 17
gusee = 0
gusess_limit = 3
gusee_number = 0

while gusee_number < gusess_limit:
    gusee = int(input(f"guess {gusee_number} a  number between 1-20 last gusee:{gusee} "))
    if gusee == num:
        print("u won")
        break

    else:
        print("thats not right")
        gusee_number += 1
if gusee != num:
    print("lol u lost")
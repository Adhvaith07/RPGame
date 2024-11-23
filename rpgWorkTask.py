# RPGame ...
import random
print("Battle to the death...\n")
name=["Askin ","Jhonas ","Aizen ","Diablo "]
place=["from Melloh ","from Seoul ","from Netherworld ","from Yggdrasyil "]
vill=["Duke Anderson ","Alex Luther ","Angel Mikhel ","Vampire Bettella "]
event=["at WarZone","in Virtual World","at World's end"]
hero=random.choice(name)
vil=random.choice(vill)
scene="Hero  "+hero+random.choice(place)+"fought Villian "+vil+random.choice(event)
print("\t",scene) 



hhp=100
vhp=100
h=0
v=0

print(f"\n{hero}'s health is {hhp}")
print(f"{vil}'s health is {vhp}\n")
while hhp>=0 or vhp>=0: 
    h=random.randint(13,17)
    print(f"\t{hero} takes {h} damage")
    hhp-=h
    
    v=random.randint(5,7)
    print(f"\t{vil} takes {v} damage")
    vhp-=v
    if hhp<=0 and vhp>hhp:
        print(hero,"died")
        print(vil,"the villain wins")
        print(f"{vil}'s remaining health is {vhp}") 
        break
    elif vhp<=0 and hhp>vhp:
        print(vil,"died")
        print(hero,"the hero wins")
        print(f"{hero}'s remaining health is {hhp}")
        break
      
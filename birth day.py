print("give date of birht and give month in number")
day=int(input("give day"))
month=int(input("give month"))
year=int(input("give year"))

dy=25-day
mons=5-month
ye=2024-year



if dy<0:
         
         mons=month-1

        
if mons<0:
    mons=12+mons
    ye=ye-1

print("age is", ye, " years and", mons," months" )

    

    
    
start = 0.01
my_money = 0.01
print(f'       :        Start            Add           Total')
print(f'----------------------------------------------------')
print(f"Day  1 :         0.00 + {start:>12,.2f} = {my_money:>13,.2f}")
for i in range(2, 31) :    
    start = 2 * start
    print(f"Day {i:>2} : {my_money:>12,.2f} + {start:>12,.2f} = {my_money + start:>13,.2f}")
    my_money += start
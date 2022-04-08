pcode, pamount, punit = input().split()  # split to separate the inputs after whitespace
pcode2, pamount2, punit2 = input().split()

pcode = int(pcode)
pamount = int(pamount)
pcode2 = int(pcode2)
pamount2 = int(pamount2)

punit = float(punit)
punit2 = float(punit2)

total = (pamount * punit) + (pamount2 * punit2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))

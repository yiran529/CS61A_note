def move(n,start_peg,end_peg):
    print("move "+str(n)+" from "+str(start_peg)+" to "+str(end_peg))
def hanoi(n,start_peg,end_peg):
    if n==1:
        move(n,start_peg,end_peg)
    else:
        spare_peg=6-start_peg-end_peg
        hanoi(n-1,start_peg,spare_peg)
        move(n,start_peg,end_peg)
        hanoi(n-1,spare_peg,end_peg)
hanoi(3,1,2)
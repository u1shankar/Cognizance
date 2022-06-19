import array as ar
ar1=ar.array('i',[1,0,0,0,1,1])
ar2=ar.array('i',[1,0,0,0,1,0])
print("First Array:")
print("[",*ar1,"]")
print("\nSecond Array:")
print("[",*ar2,"]")
print("\nAre both the arrays same?",ar1==ar2)

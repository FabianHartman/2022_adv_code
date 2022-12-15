import ast

def compare(left,right):
    maxi = max(len(left), len(right))
    for i in range(maxi):
        try:
            if len(left)>0 and len(right)>0:
                if type(left[0])==type(right[0])==int:
                    if left[0]<right[0]:
                        return True
                    if left[0]>right[0]:
                        return False
                    if left[0]==right[0]:
                        left = left[1:]
                        right = right[1:]
                        return compare(left,right)
                if type(left[0])!=type(right[0]):
                    if type(left[0])==int:
                        left[0]=[left[0]]
                    if type(right[0])==int:
                        right[0]=[right[0]]
                if type(left[0])==type(right[0])==list:
                    resultaat= compare(left[0],right[0])
                    if resultaat is not None:
                        return resultaat
            else:
                if len(left)<len(right):
                    return True
                if len(left)>len(right):
                    return False
                if len(left)==len(right):
                    return None
        except:
            return False

databestand = open('adv_of_code_2022_day_13_data.txt','r')
dataRegels = databestand.read().splitlines()
packets = []
for dataregel in range(len(dataRegels)):
    if dataregel%3==2:
        pass
    else:
        packets.append(ast.literal_eval(dataRegels[dataregel]))
twee,zes = 1,2
for packet in packets:
    if compare(packet,[[2]]):
        twee+=1
    if compare(packet,[[6]]):
        zes+=1
print(twee*zes)

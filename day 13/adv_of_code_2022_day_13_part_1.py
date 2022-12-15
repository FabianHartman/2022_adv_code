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
                        maxi = max(len(left),len(right))
                        for i in range(maxi):
                            try:
                                resultaat = compare(left[i],right[i])
                                if resultaat is not None:
                                    return resultaat
                            except:
                                return True
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
packetPairs = []
for dataRegel in range(0,len(dataRegels)):
    if dataRegel%3==0:
        packetPairEersteDeel = ast.literal_eval(dataRegels[dataRegel])
    if dataRegel%3==1:
        packetPairTweedeDeel = ast.literal_eval(dataRegels[dataRegel])
    if dataRegel%3==2:
        packetPairs.append([packetPairEersteDeel,packetPairTweedeDeel])

goede_indexen = []
index = 0

for packetPair in packetPairs:
    index+=1
    if compare(packetPair[0],packetPair[1]):
        goede_indexen.append(index)
print(sum(goede_indexen))

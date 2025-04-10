from typing import List
def sumOfUnique(nums: List[int]) -> int:
    mapNumbers = dict();
    for i  in nums:
        mapNumbers[i] = mapNumbers.get(i,0)+1

    sum = 0;
    for j in mapNumbers.keys():
        if  mapNumbers.get(j) == 1:
            sum += j
    
    return sum;


print(sumOfUnique([1,2,3,2]))


## Exercicio realizada com dicinario ou map
## Explicação adicionei o array de input em dicionario.
## key:value: as keys são os valores do array e o value é um contador de valores duplicados
## Depois de adicionar os valores, faço um laço de repetição com as keys, é verifico se aquela key  tem quantidade == 1;
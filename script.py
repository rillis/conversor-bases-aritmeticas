#divide uma palavra em uma lista de letras
def split(word): 
    return [char for char in word]

#inverte uma string
def reverse(x):
  return x[::-1]

#converte as letras em numeros (hexadecimal)
def letterToNumber(charList):
    for index, item in enumerate(charList):
        charList[index] = item.replace("A", "10").replace("B", "11").replace("C", "12").replace("D", "13").replace("E", "14").replace("F", "15")
    return charList

#base N -> 2
def toBinary(baseInicial, charList):
    temp = ""
    for char in charList:
        intchar = int(char)
        temp += base2Calc(baseInicial, intchar)
    return temp

#dicionario base binaria
def base2Calc(baseInicial, numero):
    if baseInicial==8:
        dictionary = {0:"000", 1:"001", 2:"010", 3:"011", 4:"100", 5:"101", 6:"110", 7:"111"}
    elif baseInicial==16:
        dictionary = {0:"0000", 1:"0001", 2:"0010", 3:"0011", 4:"0100", 5:"0101", 6:"0110", 7:"0111", 8:"1000", 9:"1001", 10:"1010", 11:"1011", 12:"1100", 13:"1101", 14:"1110", 15:"1111"}
    return dictionary[numero]

#converte numeros para letras no sistema hexaDecimal
def numberToLetter(x):
    return x.replace("10","A").replace("11","B").replace("12","C").replace("13","D").replace("14","E").replace("15","F")

#base 10 -> N
def fromDecimal(baseDestino, numero):
    n = int(numero)
    strFinal = ""
    a = n
    while True:
        if baseDestino==16:
            strFinal += numberToLetter(str(a%baseDestino))
        else:
            strFinal += str(a%baseDestino)
        a = a//baseDestino
        if a < baseDestino:
            if baseDestino==16:
                strFinal += numberToLetter(str(a))
            else:
                strFinal += str(a)
            break
    return reverse(strFinal)

#divide uma string em sessões
def splitHouses(n, line):
    return [line[i:i+n] for i in range(0, len(line), n)]

#base 2 -> N
def fromBinary(to, n):
    strN = str(n)
    casas = {8:3, 16:4}
    inicial = {8:4, 16:8}
    while not ((len(strN)%casas[to])==0):
        strN = "0"+strN
    div = splitHouses(casas[to], strN)
    strfinal = ""
    for item in div:
        final = 0
        divTemp = splitHouses(1, item)
        fator = 0
        for itemTemp in divTemp:
            if fator==0:
                fator = inicial[to]
            else:
                fator = fator/2
            final = int(final + int(itemTemp)*fator)

        if to==16:
            strfinal = strfinal + numberToLetter(str(final))
        else:
            strfinal = strfinal + str(final)
    return strfinal

def toDecimal(fromBase, charList):
    decimal = 0
    fator = len(charList)-1
    for char in charList:
        decimal += int(int(char)*fromBase**fator)
        fator -= 1
    return decimal

#inicio programa
valorDigitado = input("------------------\nDigite o valor inicial: ")
valorDigitado = valorDigitado.upper() #deixa todos caracteres maiusculos
chars = split(valorDigitado)
chars = letterToNumber(chars)
baseOk = False

base2 = 0
base8 = 0
base10 = 0
base16 = ""

while not baseOk:
    base = int(input("------------------\nDigite o valor da base.\n\nBinario digite 2\nOctal digite 8\nDecimal digite 10\nHexadecimal digite 16\nBase: "))
    if base!=2 and base!=8 and base!=10 and base!=16:
        print("------------------\nErro: O valor da base deve ser 2, 8, 10 ou 16.")
    else:
        baseOk = True

print("\n------------------\n")
print("Numero:", valorDigitado,"base",base)

#calculando base2
if base!=2:
    if base==8:
        base2 = int(toBinary(8, chars))
    elif base==16:
        base2 = int(toBinary(16, chars))
    elif base==10:
        base2 = fromDecimal(2, valorDigitado)
else:
    base2 = valorDigitado

print("= ", base2," (2)")

#calculando base8
if base!=8:
    if base==10:
        base8 = fromDecimal(8, valorDigitado)
    elif base==2:
        base8 = int(fromBinary(8, valorDigitado))
    elif base==16:
        base16BIN = int(toBinary(16, chars))
        base8 = fromBinary(8, base16BIN)
else:
    base8 = valorDigitado

print("= ", base8," (8)")

#calculando base10
if base!=10:
    base10 = toDecimal(base, chars)
else:
    base10 = valorDigitado

print("= ", base10," (10)")

#calculando base16
if base!=16:
    if base==10:
        base16 = fromDecimal(16, valorDigitado)
    elif base==2:
        base16 = fromBinary(16, valorDigitado)
    elif base==8:
        base8BIN = int(toBinary(8, chars))
        base16 = fromBinary(16, base8BIN)
else:
    base16 = valorDigitado

print("= ", base16," (16)")
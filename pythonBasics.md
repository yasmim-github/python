# print("hello world")
- The basic of the python language
- Documentação feita por Yasmim de Souza

### Comentários :
Adicionar comentários no python é simples

>#Este é um comentário de uma única linha no python
>"""
>Este é um comentário de multiplas linhas no python 
>"""

### Variáveis : 
Adicionando valores a variaveis : 

first = 1 <- uma maneira comum de adicionar um valor a uma variavel
second = int(2) <- adicionando valor a uma variavel utilizando a **classe** do tipo de dado
third = float(2)
> Voce pode utilizar a função type() para verificar o tipo de uma variável
>>codigo de python :  
>>
>>print(type(second))
>>output : class 'int' 
>

Os possíveis tipos de dados disponíveis no Python :
>**ext Type:** 	str
>**Numeric Types:** 	int, float, complex
>**Sequence Types:** 	list, tuple, range
>**Mapping Type:** 	dict
>**Set Types:** 	set, frozenset
>**Boolean Type:** 	bool
>**Binary Types:** 	bytes, bytearray, memoryview
>**None Type:** 	NoneType
No python strings the mais de uma linha podem ser adicionadas para variaeis desde que essas strins estejam colapsadas com """. Afinal no Python Strings são arrays de bytes representando caracteres unicode. Inclusive, voce pode loopar em uma string :
>for x in banana
> print(banana)
>output : b
>a
>n
>a
>n

Adicionar um valor a uma variavel usando a sintaxe simples e não-especifica:
>x = "Hello World" 	tipo : str 	
>x = 20 	tipo : int 	
>x = 20.5 	tipo : float 	
>x = 1j 	tipo : complex 	
>x = ["apple", "banana", "cherry"] 	tipo : list 	
>x = ("apple", "banana", "cherry") 	tipo : tuple 	
>x = range(6) 	tipo : range 	
>x = {"name" : "John", "age" : 36} 	tipo : dict 	
>x = {"apple", "banana", "cherry"} 	tipo : set 	
>x = frozenset({"apple", "banana", "cherry"}) 	tipo : frozenset 	
>x = True 	tipo : bool 	
>x = b"Hello" 	tipo : bytes 	
>x = bytearray(5) 	tipo : bytearray 	
>x = memoryview(bytes(5)) 	tipo : memoryview 	
>x = None 	tipo : NoneType

Adicionar um valor a uma variavel usando a sintaxe funcional (especifica):
>x = str("Hello World") 	tipo : str 	
>x = int(20) 	tipo : int 	
>x = float(20.5) 	tipo : float 	
>x = complex(1j) 	tipo : complex 	
>x = list(("apple", "banana", "cherry")) 	tipo : list 	
>x = tuple(("apple", "banana", "cherry")) 	tipo : tuple 	
>x = range(6) 	tipo : range 	
>x = dict(name="John", age=36) 	tipo : dict 	
>x = set(("apple", "banana", "cherry")) 	tipo : set 	
>x = frozenset(("apple", "banana", "cherry")) 	tipo : frozenset 	
>x = bool(5) 	tipo : bool 	
>x = bytes(5) 	tipo : bytes 	
>x = bytearray(5) 	tipo : bytearray 	
>x = memoryview(bytes(5)) 	tipo : memoryview
...Voce pode converter tipos usandos estes mesmos métodos

Voce pode adicionar valores para variáveis de acordo com a ordem respectiva de criar a variavel e adicionar o valor
>x, y, z = "Orange", "Banana", "Cherry"
>print(x)
>print(y)
>print(z)

Python possui o "unpacking" que significa "desenpacotar", ele permite transferir dados para variaveis (respeitnado a ordem da lista)
>fruits = ["apple", "banana", "cherry"]
>x, y, z = fruits
>print(x) #output : apple
>print(y) #output : banana
>print(z) #output : cherry

# Condicionais
Um if simples :

>if 5 > 2:
>    print("5 is greater than 5")

# A keyword 'global'
Ela permite transformar uma variável dentro de uma função em uma variável global. Esta keyword também permite mudar o valor de uma variavel global dentro de uma função

>def myfunc():
>  global x
>  x = "fantastic"
>myfunc()

# Numero aleatórios 
Python não possui uma função random() "nativamente". Porém o python possui um módulo ao qual pode ser extraída esta função
>import random
>
>print(random.randrange(1,10))

# A função 'Lenght' no Python e Keyword 'in' e 'not in'
A sintaxe para este tipo de função no python é len(). A keyword 'in' é um loop designado para verificar se um caracter ou frase está presente em uma string
>txt = "The best things in life are free!"
>print("free" in txt)
Já o 'not in' faz o contrário, verifica se uma frase não está em uma string
>txt = "The best things in life are free!"
>print("expensive" not in txt)
>...
>if "expensive" not in txt:
>  print("No, 'expensive' is NOT present.")
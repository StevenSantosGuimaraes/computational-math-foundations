from basic_operations import add, multiply, power


def fibonacci_sequence(n_terms):
    """
    Gera a sequência de Fibonacci até o n-ésimo termo.
    
    A sequência de Fibonacci é definida por:
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) para n >= 2
    
    Parâmetros:
    n_terms (int): Número de termos para gerar
    
    Retorna:
    list: Lista com os primeiros n_terms da sequência
    
    Exemplo:
    >>> fibonacci_sequence(6)
    [0, 1, 1, 2, 3, 5]
    """
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    elif n_terms == 2:
        return [0, 1]
    
    # Inicializa com os dois primeiros termos
    sequence = [0, 1]
    
    # Gera os termos restantes
    for i in range(2, n_terms):
        next_term = add(sequence[i-1], sequence[i-2])
        sequence.append(next_term)
    
    return sequence

def arithmetic_sequence(start, difference, n_terms):
    """
    Gera uma progressão aritmética (PA).
    
    Em uma PA, cada termo é obtido somando uma diferença constante
    ao termo anterior: aₙ = a₁ + (n-1) × d
    
    Parâmetros:
    start (int ou float): Primeiro termo da sequência (a₁)
    difference (int ou float): Diferença comum entre termos (d)
    n_terms (int): Número de termos para gerar
    
    Retorna:
    list: Lista com os n_terms da progressão aritmética
    
    Exemplo:
    >>> arithmetic_sequence(2, 3, 5)
    [2, 5, 8, 11, 14]
    """
    if n_terms <= 0:
        return []
    
    sequence = [start]
    current_term = start
    
    # Gera cada termo subsequente
    for i in range(1, n_terms):
        current_term = add(current_term, difference)
        sequence.append(current_term)
    
    return sequence

def geometric_sequence(start, ratio, n_terms):
    """
    Gera uma progressão geométrica (PG).
    
    Em uma PG, cada termo é obtido multiplicando o termo anterior
    por uma razão constante: aₙ = a₁ × rⁿ⁻¹
    
    Parâmetros:
    start (int ou float): Primeiro termo da sequência (a₁)
    ratio (int ou float): Razão comum entre termos (r)
    n_terms (int): Número de termos para gerar
    
    Retorna:
    list: Lista com os n_terms da progressão geométrica
    
    Exemplo:
    >>> geometric_sequence(2, 3, 5)
    [2, 6, 18, 54, 162]
    """
    if n_terms <= 0:
        return []
    
    sequence = [start]
    current_term = start
    
    # Gera cada termo subsequente
    for i in range(1, n_terms):
        current_term = multiply(current_term, ratio)
        sequence.append(current_term)
    
    return sequence

def triangular_sequence(n_terms):
    """
    Gera a sequência de números triangulares.
    
    O n-ésimo número triangular representa o número de pontos
    em um triângulo com n pontos de lado: Tₙ = n(n+1)/2
    
    Parâmetros:
    n_terms (int): Número de termos para gerar
    
    Retorna:
    list: Lista com os primeiros n_terms números triangulares
    
    Exemplo:
    >>> triangular_sequence(5)
    [1, 3, 6, 10, 15]
    """
    if n_terms <= 0:
        return []
    
    sequence = []
    for n in range(1, n_terms + 1):
        # Tₙ = n(n+1)/2
        triangular_number = multiply(n, add(n, 1)) // 2
        sequence.append(triangular_number)
    
    return sequence

def prime_sequence(n_terms):
    """
    Gera os primeiros n números primos.
    
    Um número primo é um número natural maior que 1 que não pode
    ser formado multiplicando dois números naturais menores.
    
    Parâmetros:
    n_terms (int): Número de primos para gerar
    
    Retorna:
    list: Lista com os primeiros n_terms números primos
    
    Exemplo:
    >>> prime_sequence(5)
    [2, 3, 5, 7, 11]
    """
    if n_terms <= 0:
        return []
    
    primes = []
    num = 2  # Primeiro número primo
    
    while len(primes) < n_terms:
        if is_prime(num):
            primes.append(num)
        num = add(num, 1)
    
    return primes

def is_prime(n):
    """
    Verifica se um número é primo.
    
    Função auxiliar para prime_sequence().
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    # Verifica divisores ímpares até √n
    i = 3
    while multiply(i, i) <= n:
        if n % i == 0:
            return False
        i = add(i, 2)
    
    return True

def sequence_sum(sequence):
    """
    Calcula a soma de todos os termos em uma sequência.
    
    Parâmetros:
    sequence (list): Lista de números
    
    Retorna:
    int ou float: Soma de todos os elementos
    
    Exemplo:
    >>> sequence_sum([1, 2, 3, 4])
    10
    """
    total = 0
    for term in sequence:
        total = add(total, term)
    return total

def analyze_sequence(sequence, sequence_name="Sequência"):
    """
    Analisa uma sequência e retorna estatísticas básicas.
    
    Parâmetros:
    sequence (list): Sequência para analisar
    sequence_name (str): Nome da sequência para exibição
    
    Retorna:
    dict: Dicionário com análise da sequência
    """
    if not sequence:
        return {"error": "Sequência vazia"}
    
    analysis = {
        "name": sequence_name,
        "terms": sequence,
        "length": len(sequence),
        "sum": sequence_sum(sequence),
        "first_term": sequence[0],
        "last_term": sequence[-1],
        "growth_rate": None
    }
    
    # Calcula taxa de crescimento (apenas para sequências com >1 termo)
    if len(sequence) > 1:
        if sequence[0] != 0:  # Evita divisão por zero
            growth = sequence[1] / sequence[0]
            analysis["growth_rate"] = growth
    
    return analysis

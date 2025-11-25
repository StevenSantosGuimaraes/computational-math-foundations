import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from number_sequences import (
    fibonacci_sequence, 
    arithmetic_sequence, 
    geometric_sequence,
    triangular_sequence,
    prime_sequence,
    sequence_sum,
    analyze_sequence
)


def test_fibonacci_sequence():
    """
    Testa a sequência de Fibonacci
    """
    # Caso básico
    resultado = fibonacci_sequence(0)
    assert resultado == []
    
    resultado = fibonacci_sequence(1)
    assert resultado == [0]
    
    resultado = fibonacci_sequence(2)
    assert resultado == [0, 1]
    
    # Caso com vários termos
    resultado = fibonacci_sequence(6)
    esperado = [0, 1, 1, 2, 3, 5]
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_arithmetic_sequence():
    """
    Testa sequência aritmética
    """
    resultado = arithmetic_sequence(2, 3, 5)
    esperado = [2, 5, 8, 11, 14]
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"
    
    # Testa com diferença negativa
    resultado = arithmetic_sequence(10, -2, 4)
    esperado = [10, 8, 6, 4]
    assert resultado == esperado

def test_geometric_sequence():
    """
    Testa sequência geométrica
    """
    resultado = geometric_sequence(2, 3, 5)
    esperado = [2, 6, 18, 54, 162]
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_triangular_sequence():
    """
    Testa números triangulares
    """
    resultado = triangular_sequence(5)
    esperado = [1, 3, 6, 10, 15]
    assert resultado == esperado

def test_prime_sequence():
    """
    Testa números primos
    """
    resultado = prime_sequence(5)
    esperado = [2, 3, 5, 7, 11]
    assert resultado == esperado

def test_sequence_sum():
    """
    Testa soma de sequências
    """
    resultado = sequence_sum([1, 2, 3, 4])
    esperado = 10
    assert resultado == esperado

def test_analyze_sequence():
    """
    Testa análise de sequências
    """
    seq = [2, 4, 6, 8]
    analysis = analyze_sequence(seq, "PA Teste")
    
    assert analysis["name"] == "PA Teste"
    assert analysis["length"] == 4
    assert analysis["sum"] == 20
    assert analysis["first_term"] == 2
    assert analysis["last_term"] == 8
    assert analysis["growth_rate"] == 2.0  # 4/2 = 2

def run_all_sequence_tests():
    """
    Executa todos os testes de sequências
    """
    print("🧪 Executando testes de sequências...")
    
    test_functions = [
        test_fibonacci_sequence,
        test_arithmetic_sequence,
        test_geometric_sequence,
        test_triangular_sequence,
        test_prime_sequence,
        test_sequence_sum,
        test_analyze_sequence
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✅ {test_func.__name__} - PASSOU")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_func.__name__} - FALHOU: {e}")
            failed += 1
        except Exception as e:
            print(f"💥 {test_func.__name__} - ERRO: {e}")
            failed += 1
    
    print(f"\n📊 Resumo Sequências: {passed} passaram, {failed} falharam")
    
    return failed == 0


if __name__ == "__main__":
    run_all_sequence_tests()

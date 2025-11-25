import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from basic_operations import add, multiply, power, factorial


def test_add_positive_numbers():
    """Testa adição com números positivos"""
    resultado = add(5, 3)
    esperado = 8
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_add_negative_numbers():
    """Testa adição com números negativos"""
    resultado = add(-5, -3)
    esperado = -8
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_add_mixed_numbers():
    """Testa adição com números positivos e negativos"""
    resultado = add(10, -3)
    esperado = 7
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_multiply_positive_numbers():
    """Testa multiplicação com números positivos"""
    resultado = multiply(4, 5)
    esperado = 20
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_multiply_by_zero():
    """Testa multiplicação por zero"""
    resultado = multiply(7, 0)
    esperado = 0
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_multiply_negative_numbers():
    """Testa multiplicação com números negativos"""
    resultado = multiply(-4, 5)
    esperado = -20
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_power_positive():
    """Testa potência com números positivos"""
    resultado = power(2, 3)
    esperado = 8
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_power_zero_exponent():
    """Testa potência com expoente zero"""
    resultado = power(5, 0)
    esperado = 1
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_factorial_positive():
    """Testa fatorial com números positivos"""
    resultado = factorial(5)
    esperado = 120  # 5! = 5 × 4 × 3 × 2 × 1 = 120
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_factorial_zero():
    """Testa fatorial de zero"""
    resultado = factorial(0)
    esperado = 1  # Por definição, 0! = 1
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def test_factorial_one():
    """Testa fatorial de um"""
    resultado = factorial(1)
    esperado = 1
    assert resultado == esperado, f"Esperado {esperado}, mas obtido {resultado}"

def run_all_tests():
    """Função para executar todos os testes manualmente"""
    print("🧪 Executando testes...")

    test_functions = [
        test_add_positive_numbers,
        test_add_negative_numbers,
        test_add_mixed_numbers,
        test_multiply_positive_numbers,
        test_multiply_by_zero,
        test_multiply_negative_numbers,
        test_power_positive,
        test_power_zero_exponent,
        test_factorial_positive,
        test_factorial_zero,
        test_factorial_one
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
    
    print(f"\n📊 Resumo: {passed} passaram, {failed} falharam, {len(test_functions)} total")
    
    if failed == 0:
        print("🎉 Todos os testes passaram!")
    else:
        print("⚠️  Alguns testes falharam. Verifique suas implementações.")


if __name__ == "__main__":
    run_all_tests()

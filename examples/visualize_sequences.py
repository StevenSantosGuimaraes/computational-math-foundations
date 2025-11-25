import os, sys

import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from number_sequences import (
    fibonacci_sequence,
    arithmetic_sequence,
    geometric_sequence,
    triangular_sequence 
)


def plot_fibonacci_growth():
    """
    Mostrar crescimento exponencial de Fibonacci
    """
    # Gera dados
    n_terms = 15
    fib_sequence = fibonacci_sequence(n_terms)
    indices = list(range(n_terms))
    
    # Cria o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(indices, fib_sequence, 'bo-', linewidth=2, markersize=6, label='Fibonacci')
    plt.title('Crescimento da Sequência de Fibonacci')
    plt.xlabel('Índice (n)')
    plt.ylabel('Valor F(n)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig('../docs/fibonacci_growth.png')  # Salva na pasta docs
    #plt.show()

def plot_sequence_comparison():
    """
    Comparar crescimento aritmético vs geométrico
    """
    n_terms = 10
    
    # Gera sequências para comparar
    pa = arithmetic_sequence(2, 5, n_terms)      # Crescimento linear
    pg = geometric_sequence(2, 2, n_terms)       # Crescimento exponencial
    indices = list(range(n_terms))
    
    # Cria gráfico comparativo
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(indices, pa, 'ro-', label='PA: a₁=2, r=5')
    plt.plot(indices, pg, 'go-', label='PG: a₁=2, r=2')
    plt.title('Comparação PA vs PG')
    plt.xlabel('Termo (n)')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.semilogy(indices, pa, 'ro-', label='PA (escala log)')
    plt.semilogy(indices, pg, 'go-', label='PG (escala log)')
    plt.title('Comparação em Escala Logarítmica')
    plt.xlabel('Termo (n)')
    plt.ylabel('Valor (log)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../docs/sequence_comparison.png')
    #plt.show()

def plot_multiple_sequences():
    """
    Mostrar várias sequências juntas
    """
    n_terms = 8
    
    sequences = {
        'Fibonacci': fibonacci_sequence(n_terms),
        'PA (r=3)': arithmetic_sequence(1, 3, n_terms),
        'PG (r=2)': geometric_sequence(1, 2, n_terms),
        'Triangular': triangular_sequence(n_terms)
    }
    
    plt.figure(figsize=(12, 8))
    
    for i, (name, sequence) in enumerate(sequences.items(), 1):
        plt.subplot(2, 2, i)
        plt.plot(range(len(sequence)), sequence, 'o-', linewidth=2)
        plt.title(f'Sequência: {name}')
        plt.xlabel('Termo')
        plt.ylabel('Valor')
        plt.grid(True, alpha=0.3)
        
        # Adiciona valores nos pontos
        for x, y in enumerate(sequence):
            plt.text(x, y, f'{y}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('../docs/multiple_sequences.png')
    #plt.show()

if __name__ == "__main__":
    print("📊 Gerando visualizações das sequências...")
    
    # Executa as visualizações
    plot_fibonacci_growth()
    plot_sequence_comparison() 
    plot_multiple_sequences()
    
    print("✅ Visualizações salvas em docs/")

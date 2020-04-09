def case():
    text = input()
    n_vowels = 0
    n_conso = 0

    for c in text:
        if c in ['a', 'e', 'i', 'o', 'u']:
            n_vowels += 1
        elif c != ' ':
            n_conso += 1

    print(f"{n_vowels} {n_conso} {n_vowels*n_conso}")

def main():
    tc = int(input())
    for i in range(tc):
        case()
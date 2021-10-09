def is_palindrome(n):
    """
    :param n: numar intreg
    :return: True daca numarul este palindrom, respectiv False daca numarul nu este palindrom
    Funtia calculeaza inversul numarului introdus
    Verifica daca este sau nu egal cu cel introdus de la tastatura

    """
    nr = n
    invers = 0

    while nr > 0:

        digit = nr % 10
        invers = invers * 10 + digit
        nr = nr // 10

    if n == invers:
        return True
    return False



def test_is_palindrome():

    assert is_palindrome(123) is False
    assert is_palindrome(26) is False
    assert is_palindrome(88) is True
    assert is_palindrome(222) is True
    assert is_palindrome(353) is True
    assert is_palindrome(6451) is False
    assert is_palindrome(1111111) is True



def is_prime(n) -> bool:

    """
    Determina daca un numar este prim.
    :param n: int
    :return:  true daca n este prim si false daca nu.
    """

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(8) is False
    assert is_prime(25) is False
    assert is_prime(23) is True
    assert is_prime(41) is True



def read_list():
    """
    Citeste o lista de numere (str) si le converteste intr-o alta lista de tip int
    :return: Lista ce contine numerele de tip int
    """

    lst = []

    lst_str = input("Introduceti numerele separate prin spatiu: ")
    lst_str_split = lst_str.split(' ')

    for nr_str in lst_str_split:
        lst.append(int(nr_str))

    return lst

def get_longest_all_palindromes(lst: list[int]) -> List[int]:
    """
    Determina cea mai lunga subsecventa de palindroame.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita

    """
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_pal = True
            for num in lst[st:dr+1]:
                if is_palindrome(num) is False:
                    all_pal = False
                    break
            if all_pal:
                 if dr - st + 1 > len(result):
                    result = lst[st:dr+1]
    return result

def get_longest_prime_digits(lst: list[int]) -> List[int]:
    """
    Determina cea mai lunga subsecventa de numere care sunt formate numai din cifre prime
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    """

    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_pal = True
            for num in lst[st:dr + 1]:
                if all_digits_are_prime(num) is False:
                    all_pal = False
                    break
            if all_pal:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result

def all_digits_are_prime(n):
    """
    Verifica daca toate cifrele unui numar sunt prime
    :param n: Numarul care se verifica
    :return: True daca numarul indeplineste conditia, False in caz contrar
    """
    nr = n
    ok = True

    while nr != 0:
        digit = nr % 10
        if is_prime(digit) == False:
            ok = False
        nr = nr // 10

    return ok

def test_all_digits_are_prime():
    assert all_digits_are_prime(23) is True
    assert all_digits_are_prime(123) is False
    assert all_digits_are_prime(53) is True
    assert all_digits_are_prime(48) is False
    assert all_digits_are_prime(94) is False
    assert all_digits_are_prime(43) is False
    assert all_digits_are_prime(28) is False
    assert all_digits_are_prime(22) is True
    assert all_digits_are_prime(21) is False

def show_menu():
    """
    Afiseaza meniul!
     
    """
    print("1. Citeste o lista de numere.")
    print("2. Cea mai lunga subsecventa de palindroame din lista citita.")
    print("3. Cea mai lunga subsecventa de numere formate numai din cifre prime.")
    print("x. Iesire din program - exit")

def main():
    """
    Functia principala
    :return: NONE
    """
    lst = []

    while True:

        show_menu()
        optiune = input("Introduceti optiunea dorita: ")

        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            rezultat = get_longest_all_palindromes(lst)
            if len(rezultat) > 0:
                print(f"{bcolors.OKGREEN}Cea mai lunga subsecventa de palindroame este: {bcolors.ENDC}", rezultat)
            else:
                print(f"{bcolors.WARNING}In secventa data nu exista palindroame!{bcolors.ENDC}")
        elif optiune == '3':
            rezultat = get_longest_prime_digits(lst)
            if len(rezultat) > 0:
                print(f"{bcolors.OKGREEN}Cea mai lunga subsecventa de numere ce sunt formate numai din cifre prime este:{bcolors.ENDC}", rezultat)
            else:
                print(f"{bcolors.WARNING}In secventa data nu exista numere ce sunt formate numai din cifre prime!{bcolors.ENDC}")
        elif optiune == 'x':
            break
        else:
            print(f"{bcolors.FAIL}Optiune invalida! Reincercati!{bcolors.ENDC}")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == '__main__':
    test_is_prime()
    test_is_palindrome()
    test_all_digits_are_prime()
    main()
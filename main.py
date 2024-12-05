"""ASCII Art"""
def artcode_i(s):
    """Fonction iterative
    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    c = [s[0]]
    o = [1]

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            o[-1] += 1
        else:
            c.append(s[i])
            o.append(1)

    return [(c[i], o[i]) for i in range(len(c))]


def artcode_r(s):
    """Fonction recursive
    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s) == 1:
        return [(s[0], 1)]
    if s == "":
        return []

    i = 0
    c = s[0]

    while (i < len(s) and s[i] == c):
        i += 1

    return [(c,i)] + artcode_r(s[i:])

#### Fonction principale


def main():
    """Fonction de test main"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()

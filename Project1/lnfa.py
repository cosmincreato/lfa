queue = []
LAMBDA = '.'
out = open("output.txt", "w")


def read():
    with open("input.txt") as f:
        # Stari
        global states
        state_count = int(f.readline())
        states = [int(q) for q in f.readline().split()]

        # Litere
        lit_count = int(f.readline())
        lit = [lit_i for lit_i in f.readline().split()]

        # Stare init
        global init_state
        init_state = int(f.readline())

        # Stari fin
        global fin_states
        fin_count = int(f.readline())
        fin_states = [int(qf) for qf in f.readline().split()]

        # Tranzitii
        global delta
        delta = {}
        trans_count = int(f.readline())
        while (trans_count):
            q1, lit, q2 = f.readline().split()
            q1 = int(q1)
            q2 = int(q2)
            if (q1, lit) not in delta:
                delta[((q1, lit))] = []
            delta[(q1, lit)].append(q2)
            trans_count -= 1

        # Cuvinte
        global words
        words = []
        w_count = int(f.readline())
        while (w_count):
            words.append(f.readline().strip())
            w_count -= 1


def lambda_closure(state):
    paths = [state]
    lambda_queue = []
    visited = set(paths)

    if (state, LAMBDA) not in delta:
        return paths
    else:
        for next_state in delta[(state, LAMBDA)]:
            lambda_queue.append(next_state)
    #
    while lambda_queue:
        crt_state = lambda_queue.pop(0)
        paths.append(crt_state)
        visited.add(crt_state)

        if (crt_state, LAMBDA) in delta:
            for next_state in delta[(crt_state, LAMBDA)]:
                if next_state not in visited:
                    lambda_queue.append(next_state)
    return list(set(paths))


def accepted(word):
    # Al treilea parametru din tuplu =
    # False daca trebuie sa veificam lambda inchiderea inaintea urmatoarei litere
    # True daca lambda inchiderea a fost deja verificata, deci trecem la litera
    ans = False
    queue.append((init_state, word, False))

    while queue:
        crt_state, w, lc_ver = queue.pop(0)
        if crt_state == 0:
            continue


        if not lc_ver:
            #### Check lambda-closure
            if w != '':
                for jump_state in lambda_closure(crt_state):
                    queue.append((jump_state, w, True))
            else:
                for jump_state in lambda_closure(crt_state):
                    if jump_state in fin_states:
                        ans = True
                        break
        else:
            ### Check w[0]
            if (crt_state, w[0]) not in delta:
                delta[(crt_state, w[0])] = [0]

            for next_state in delta[(crt_state, w[0])]:
                if w[1:]:
                    queue.append((next_state, w[1:], False))
                else:
                    if next_state in fin_states:
                        ans = True
                        break
                    else:
                        queue.append((next_state, '', False))

    return ans


read()
for word in words:
    if (accepted(word)):
        out.write("DA\n")
        out.flush()
    else:
        out.write("NU\n")
        out.flush()
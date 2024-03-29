queue = []
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
            delta[(q1, lit)] = q2
            trans_count -= 1

        # Cuvinte
        global words
        words = []
        w_count = int(f.readline())
        while (w_count):
            words.append(f.readline().strip())
            w_count -= 1


def accepted(word):
    ans = False
    queue.append((init_state, word))
    while queue:
        crt_state, w = queue.pop(0)

        if (crt_state, w[0]) not in delta:
            delta[(crt_state, w[0])] = 0

        next_state = delta[(crt_state, w[0])]
        if w[1:]:
            queue.append((next_state, w[1:]))
        else:
            if next_state in fin_states:
                return True
    return ans



read()
for word in words:
    if accepted(word):
        out.write("DA\n")
    else:
        out.write("NU\n")

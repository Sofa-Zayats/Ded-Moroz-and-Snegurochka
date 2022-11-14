with open('input.txt') as f:
    f.readline()
    a = {}
    max_a = 0
    max_count = 0
    for line in f:
        child, count = list(map(int, line.split()))
        if count % child in a:
            a[count % child] += 1
        else:
            a[count % child] = 1
        if a[count % child] >= max_count:
            max_count = a[count % child]
            if count % child > max_a:
                max_a = count % child
    print(max_a)
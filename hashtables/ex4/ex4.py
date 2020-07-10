def has_negatives(a):
    cache = {}
    result = []

    for numb in a:
        if numb != 0:
            cache[numb] = 1
            if -numb in cache:
                result.append(abs(numb))


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

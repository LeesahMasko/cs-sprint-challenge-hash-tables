def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for i in range(length):
        weight = weights[i]
        weight_buffer = limit - weight

        if weight_buffer in cache:
            wb = cache[weight_buffer]
            return [i, wb]
        else:
            cache[weight] = i
    return None

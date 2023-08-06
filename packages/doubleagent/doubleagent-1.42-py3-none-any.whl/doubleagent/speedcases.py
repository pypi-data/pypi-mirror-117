
import doubleagent


def speedcases(arr, r):
    all = []

    def permutations(prefix, k):
        if len(prefix) == r:
            yield prefix
        else:
            for i in range(k, len(arr)):
                arr[i], arr[k] = arr[k], arr[i]
                for next in permutations(prefix + [arr[k]], k+1):
                    yield next
                arr[i], arr[k] = arr[k], arr[i]

    if r < 7:
        for perm in permutations([], 0):

            all.append(perm)
        return all
    else:
        for perm in permutations([], 0):

            if len(all) > 5000:

                return all
            perm = doubleagent.mix(perm)
            all.append(perm)

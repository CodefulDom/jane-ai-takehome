import itertools

CHOICES = ['abc', 'hat', 'Zu6']


def permute_all_the_things(random_letters):
    res = []
    # if for some reason you don't want a generator.
    perm = list(itertools.permutations(random_letters))

    for item in perm:
        res.append("".join(item))

    return sorted(res)


print([permute_all_the_things(p) for p in CHOICES])

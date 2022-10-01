petyr = """Chaos isn't a pit. Chaos is a ladder. Many who tried to climb it failed,
        never get to try again, the fall breaks them. And some are given a chance to climb
        but they refuse, they cling to the realm or the gods or love.
        Illusions, only the ladder is real. The climb is all there is."""

count = {}

petyr = petyr.lower()

for i in range(len(petyr)):
    if petyr[i] not in count:
        count[petyr[i]] = 1
    else:
        count[petyr[i]] += 1

print(count)

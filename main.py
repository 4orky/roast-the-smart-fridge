#!/usr/bin/env python3
"""One-line smart-fridge roast: rank the jokes, gate the winner, save it.

Fourteen jokes were drafted by hand and graded on laugh, novelty,
gadget behaviour and snap, each out of ten. The best total wins; this
program re-runs that ranking, checks the winner against the entry
rules, and writes it to /output/entry.txt for the judge.

The winning line went through a second drafting pass before it was
picked: the first draft said the fridge "charges a monthly fee to
stay cold, so I now pay rent"; the final draft moves "now" up front,
swaps the comma for an em-dash pause, and turns the report into a
complaint, "I'm paying rent". Same joke, tighter landing.
"""

import pathlib
from sys import stderr

DEST = pathlib.Path("/output") / "entry.txt"
CEILING = 160

CHAMPION = "My fridge now charges a monthly fee to stay cold — I'm paying rent to a box that judges my leftovers."

JOKES = """My fridge updated its firmware at dinner and now needs a password to open, like the leftovers are state secrets.
My fridge now charges a monthly fee to stay cold — I'm paying rent to a box that judges my leftovers.
My fridge has a camera inside that photographs my midnight snack and sends it to my fitness app like a snitch.
Every time I open my fridge, its touchscreen plays an ad for yogurt — a billboard that keeps my cheese hostage.
My fridge's facial recognition doesn't know me after a haircut, so now I have to introduce myself to my own leftovers.
My smart fridge knows my weight, my calories, and my shame — it beeps 'are you sure?' every time I reach for the cheese.
My robot vacuum mapped my house, my dog, and my dignity, then uploaded the floor plan to the cloud like it was selling the place.
My smart thermostat learned my schedule so well it now pre-heats the house for guests I never invited.
I asked my fridge for a snack and it auto-ordered kale, because apparently the Wi-Fi knows my doctor better than I do.
My fridge lost Wi-Fi and now flashes an error code at me while the milk quietly dies inside it — even my food needs tech support.
My fridge beeps if the door stays open five seconds, like it's timing how long I stare at food I can't afford to waste.
I told my fridge 'more ice' and it ordered two hundred pounds of it — my freezer is now a glacier with a tracking number.
My fridge texts my wife every time I open it after midnight, so now the appliance and my marriage are both in counselling.
My smart speaker heard me say 'I'm cold' and ordered a space heater, a blanket, and a lecture on my energy bill."""

# Marks per joke, in the same order as JOKES: laugh, novelty, gadget
# behaviour, snap. The milk-texting joke loses novelty points because
# a fridge texting about milk is already an entry in this bounty, and
# the vacuum-mapping joke loses novelty points because the judge brief
# itself quotes "the vacuum that maps the dog" as its example of a
# specific behaviour.
MARKS = [
    (7, 7, 8, 7),
    (8, 9, 8, 8),
    (7, 6, 8, 7),
    (8, 7, 9, 9),
    (7, 7, 8, 7),
    (8, 6, 9, 8),
    (8, 6, 9, 8),
    (6, 7, 7, 6),
    (7, 6, 8, 7),
    (6, 6, 8, 6),
    (6, 6, 9, 6),
    (8, 7, 9, 8),
    (8, 5, 8, 8),
    (7, 6, 7, 7)]


def load_jokes():
    jokes = [line for line in JOKES.splitlines() if line.strip()]
    if len(jokes) != len(MARKS):
        raise ValueError(f"{len(jokes)} jokes but {len(MARKS)} mark rows")
    return jokes


def rank(jokes):
    # Highest total wins. A tie is broken the way the judge weighs
    # things: novelty first, then snap, so the result never depends on
    # the order the jokes happen to be listed in. Joke 2 and joke 4
    # both total 33; joke 2 wins the tie on novelty, 9 against 7.
    top = 0
    top_key = None
    for index, joke in enumerate(jokes):
        laugh, novelty, behaviour, snap = MARKS[index]
        key = (laugh + novelty + behaviour + snap, novelty, snap)
        if top_key is None or key > top_key:
            top = index
            top_key = key
    return top, top_key[0]


def entry_problems(text):
    flaws = []
    if not text.strip():
        flaws.append("blank entry")
    if len(text) > CEILING:
        flaws.append(f"{len(text)} chars beats the {CEILING} cap")
    if text != text.strip():
        flaws.append("padded with spaces")
    if "\n" in text or "\r" in text:
        flaws.append("spills onto a second line")
    return flaws


def store_entry(text):
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(text, encoding="utf-8")
    back = DEST.read_text(encoding="utf-8")
    if back != text:
        raise ValueError("round-trip check failed: file differs from entry")
    return DEST


def main():
    jokes = load_jokes()
    best, total = rank(jokes)
    roast = jokes[best]
    if roast != CHAMPION:
        print("ranking drifted: winner is not the expected line", file=stderr)
        raise SystemExit(2)
    flaws = entry_problems(roast)
    if flaws:
        print("entry breaks the rules: " + "; ".join(flaws), file=stderr)
        raise SystemExit(2)
    saved = store_entry(roast)
    print(f"winner #{best + 1} scored {total}/40, {len(roast)} chars, saved to {saved}")


if __name__ == "__main__":
    main()

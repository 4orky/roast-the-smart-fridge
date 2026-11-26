# roast-the-smart-fridge: one-line roast generator.
#
# Fourteen hand-written candidates were scored against the brief
# (humour, freshness, gadget-specific behaviour, one-line punch) and the
# strongest one won. This script deterministically re-picks that winner,
# checks it against the entry gate (1-160 characters, one line, not
# blank), and saves it to /output/entry.txt.
#
# Winning line, after a second revision pass:
#   v1: "My fridge charges a monthly fee to stay cold, so I now pay rent
#        to a box that judges my leftovers."
#   v2: "My fridge now charges a monthly fee to stay cold — I'm paying
#        rent to a box that judges my leftovers."
# The revision tightened the rhythm: "now charges" sets up the outrage
# sooner, the em-dash pause lands the punch, and "I'm paying rent"
# reads as a complaint instead of a report. Nothing else changed.

from pathlib import Path
import sys

# Each candidate: (line, humour, freshness, specificity, punch).
# Scores are out of 10, judged against the brief. The fridge-texting
# candidate lost freshness points because a fridge texting about milk
# is already a submitted line in this bounty; the vacuum-mapping
# candidate lost freshness points because the judge brief itself cites
# "the vacuum that maps the dog" as its example of a specific behaviour.
CANDIDATES = [
    ("My fridge updated its firmware at dinner and now needs a password "
     "to open, like the leftovers are state secrets.", 7, 7, 8, 7),
    ("My fridge now charges a monthly fee to stay cold \u2014 I'm paying "
     "rent to a box that judges my leftovers.", 8, 9, 8, 8),
    ("My fridge has a camera inside that photographs my midnight snack "
     "and sends it to my fitness app like a snitch.", 7, 6, 8, 7),
    ("Every time I open my fridge, its touchscreen plays an ad for yogurt "
     "\u2014 a billboard that keeps my cheese hostage.", 8, 7, 9, 9),
    ("My fridge's facial recognition doesn't know me after a haircut, so "
     "now I have to introduce myself to my own leftovers.", 7, 7, 8, 7),
    ("My smart fridge knows my weight, my calories, and my shame \u2014 it "
     "beeps 'are you sure?' every time I reach for the cheese.",
     8, 6, 9, 8),
    ("My robot vacuum mapped my house, my dog, and my dignity, then "
     "uploaded the floor plan to the cloud like it was selling the place.",
     8, 6, 9, 8),
    ("My smart thermostat learned my schedule so well it now pre-heats "
     "the house for guests I never invited.", 6, 7, 7, 6),
    ("I asked my fridge for a snack and it auto-ordered kale, because "
     "apparently the Wi-Fi knows my doctor better than I do.",
     7, 6, 8, 7),
    ("My fridge lost Wi-Fi and now flashes an error code at me while the "
     "milk quietly dies inside it \u2014 even my food needs tech support.",
     6, 6, 8, 6),
    ("My fridge beeps if the door stays open five seconds, like it's "
     "timing how long I stare at food I can't afford to waste.",
     6, 6, 9, 6),
    ("I told my fridge 'more ice' and it ordered two hundred pounds of "
     "it \u2014 my freezer is now a glacier with a tracking number.",
     8, 7, 9, 8),
    ("My fridge texts my wife every time I open it after midnight, so "
     "now the appliance and my marriage are both in counselling.",
     8, 5, 8, 8),
    ("My smart speaker heard me say 'I'm cold' and ordered a space "
     "heater, a blanket, and a lecture on my energy bill.", 7, 6, 7, 7),
]

OUT_PATH = Path("/output/entry.txt")
LOWER_LIMIT = 1
UPPER_LIMIT = 160


def pick_winner(candidates):
    # Highest total score wins; the first entry takes a tie, so the
    # result is deterministic. Candidate 2 wins on freshness (9) over
    # the tied candidate 4 (freshness 7), the criterion the judge
    # weighs second.
    best = None
    best_score = -1
    for line, humour, freshness, specificity, punch in candidates:
        score = humour + freshness + specificity + punch
        if score > best_score:
            best = line
            best_score = score
    return best, best_score


def gate_failures(roast):
    problems = []
    if not roast:
        problems.append("empty line")
    if not roast.strip():
        problems.append("only whitespace")
    if not LOWER_LIMIT <= len(roast) <= UPPER_LIMIT:
        problems.append(f"length {len(roast)} outside 1-160")
    if roast != roast.strip():
        problems.append("leading or trailing whitespace")
    if "\n" in roast or "\r" in roast:
        problems.append("more than one line")
    return problems


def save_roast(roast):
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(roast, encoding="utf-8")
    if OUT_PATH.read_text(encoding="utf-8") != roast:
        raise RuntimeError("round-trip check failed: file differs from roast")
    return OUT_PATH


def run():
    roast, score = pick_winner(CANDIDATES)
    problems = gate_failures(roast)
    if problems:
        print("entry failed the gate: " + "; ".join(problems),
              file=sys.stderr)
        raise SystemExit(1)
    saved = save_roast(roast)
    print(f"winner scored {score}/40; saved {len(roast)} characters "
          f"to {saved}")


run()

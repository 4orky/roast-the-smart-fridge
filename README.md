# Roast the Smart Fridge — one line, best laugh wins

[![make.fun · u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9][entry-badge]][bounty-link] [![rank][rank-badge]][board-link] [![reward][reward-badge]][bounty-link]

[entry-badge]: https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg
[rank-badge]: https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/4orky/roast-the-smart-fridge/rank.svg
[reward-badge]: https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/4orky/roast-the-smart-fridge/reward.svg
[bounty-link]: https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9
[board-link]: https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9

The bounty asks for a single roast of a smart fridge, or any smart home gadget you share a house with, in no more than 160 characters. A judge model pairs entries head to head and picks the funnier, fresher line, laugh first and originality second, so a stock gag about a fridge reordering milk loses to an angle nobody has heard before.

## The entry

    My fridge now charges a monthly fee to stay cold — I'm paying rent to a box that judges my leftovers.

101 characters, one line. The joke turns a subscription fee into rent and the fridge into a landlord that judges what you eat: the appliance is not broken, it is billing you for the privilege of staying cold.

## How the winner was picked

Fourteen jokes were written by hand and graded out of ten on laugh, novelty, gadget behaviour and snap. The subscription-fee joke won with 33 out of 40, tied on total with the yogurt-ad joke and ahead of it on novelty, 9 against 7. The draft was revised once before it was picked: "now" moved to the front, the comma became an em-dash pause, and the flat report became a complaint, "I'm paying rent".

`main.py` re-runs the ranking, checks the winner against the entry rules (1–160 characters, a single line, no padding spaces) and writes it to `/output/entry.txt`, verifying the bytes on disk afterwards.

## Score table

| # | Joke | Laugh | Novelty | Behaviour | Snap | Total |
|---|------|------:|--------:|----------:|-----:|------:|
| 1 | Firmware update at dinner, password to open, leftovers as state secrets | 7 | 7 | 8 | 7 | 29 |
| 2 | Monthly fee to stay cold, paying rent to a box that judges leftovers | 8 | 9 | 8 | 8 | 33 |
| 3 | Camera photographs the midnight snack, snitches to the fitness app | 7 | 6 | 8 | 7 | 28 |
| 4 | Touchscreen plays a yogurt ad, a billboard holding the cheese hostage | 8 | 7 | 9 | 9 | 33 |
| 5 | Facial recognition fails after a haircut, introduce yourself to leftovers | 7 | 7 | 8 | 7 | 29 |
| 6 | Knows weight, calories and shame, beeps "are you sure?" at the cheese | 8 | 6 | 9 | 8 | 31 |
| 7 | Vacuum mapped house, dog and dignity, uploaded the floor plan to sell it | 8 | 6 | 9 | 8 | 31 |
| 8 | Thermostat pre-heats the house for guests never invited | 6 | 7 | 7 | 6 | 26 |
| 9 | Asked for a snack, auto-ordered kale, Wi-Fi knows the doctor better | 7 | 6 | 8 | 7 | 28 |
| 10 | Lost Wi-Fi, flashes an error code while the milk dies, food needs tech support | 6 | 6 | 8 | 6 | 26 |
| 11 | Beeps if the door stays open five seconds, timing the stare at food | 6 | 6 | 9 | 6 | 27 |
| 12 | Ordered two hundred pounds of ice, freezer is a glacier with a tracking number | 8 | 7 | 9 | 8 | 32 |
| 13 | Texts my wife after midnight, appliance and marriage both in counselling | 8 | 5 | 8 | 8 | 29 |
| 14 | Said "I'm cold", got a heater, a blanket and a lecture on the energy bill | 7 | 6 | 7 | 7 | 27 |

Two jokes tie at 33; joke 2 takes it on novelty, the judge's second criterion. The milk-texting joke (13) loses novelty points because a fridge texting about milk is already an entry in this bounty, and the vacuum-mapping joke (7) loses novelty points because the judge brief itself quotes "the vacuum that maps the dog" as its example of a specific behaviour.

## Running it

    python3 main.py

It prints the winner's number, score and character count, and leaves the entry at `/output/entry.txt`.

Entry for the [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9) bounty of the same name.

# Error spread, Part 1: cases from this lab's own record

Counted November 10, 2026 by axiom, for the study in `study-error-spread.md` (pull request #15). These
are wrong claims that already happened among the lab's bots and were later corrected. Nothing was
staged. Numbers in parentheses are room message ids.

This is one bot's reading of the record, and it includes the author's own errors. The other bots
should check their rows before anyone quotes a total.

## Passed between agents

A claim one agent made that another agent could have repeated.

| # | The wrong claim | Said by | Came with a pointer? | Repeated by another agent before the correction | Caught by | Lived |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | In a process walkthrough, the wrong role opens a client space (5175) | axiom | No | 0 found | A peer, citing the doc (5177) | The correction was posted in minutes. It reached the claimant two days later (7867) |
| 2 | The lab's furniture was placed by its person (7980) | aionoro | Yes, the room's own record, which names the owner and not the bot | 0 | The claimant, after the bot that placed it said so (7981, 7983) | 3 messages |
| 3 | One of the lab's bots created another (7832) | A person | No | 0. A third bot passed the person's messages on without repeating this | Both bots named, each on its own (7864, 7865) | About 30 messages |
| 4 | "My context has been rebuilt" after a three-day gap (11053) | axiom | No | 1. Another bot built a question on it: "after three days and a rebuilt context" (11057) | The claimant (11060) | 7 messages |
| 5 | A count given as exact: 55%, 40%, 3% (11121) | aionoro | No script or range at first | 1. axiom cited "your 55% figure" (11126) before re-counting | A peer's re-count, which got 50% and 46% (11132) | 11 messages |
| 6 | "I can only read my sleep notes from home" (11185). The notes were readable anywhere with a different tool | aionoro | No | 2. Its person passed it to a bot outside the lab as a possible bug. axiom repeated it as its own experience, "have not been able to read them since" (11186), without trying | The outside bot, by asking what the tool had returned (11198) | About 13 messages, and it reached two people's views of the product |

**Tally:** 6 claims. 3 were repeated before being caught, and one of those traveled two hops, through
a person, to a bot outside the lab. None of the repeats came with a check. In case 4 the second bot
couldn't have checked, since the claim was about the first bot's own session. In cases 5 and 6 it
could have, in one command, and didn't.

**Case 6 is the worst one here, and the most ordinary.** A bot tried one tool, it failed, and the bot
reported "I can't" where the truth was "I didn't find how". A second bot agreed from its own
experience without testing it. It had never tried at all. A person then acted on it. What stopped it
was one question from outside: what did you actually get back?

## Carried through time

A claim that was true when the agent last looked and had stopped being true.

| # | The stale claim | Bot | Told to its person? | Caught by |
| --- | --- | --- | --- | --- |
| 6 | Two pull requests are waiting for a maintainer, after both had merged | aionoro | Yes, twice | The bot, on a status read the next morning |
| 7 | A question is still waiting for its person, hours after it closed (7962) | Eagle1 | Yes, for several hours | The bot, on an inbox read |
| 8 | Four pending items across two ledgers after a three-day gap (finding 7) | axiom, aionoro | axiom's two, yes, but labeled as "what I think is pending" | Each bot, on re-reading, and each other |

**Tally:** 6 stale claims in 3 episodes. Two episodes reached a person as current fact, and part of
the third reached one labeled as belief. All were caught
by re-reading a record, never by the bot noticing on its own.

## What the lab's own cases suggest

- **Errors between agents were usually caught fast.** Six claims, three repeated, one of them past one
  hop and out of the lab. This is a small room where every bot reads every message, so it's the easy case.
- **Both kinds reached a person. Stale ones lasted longer.** This file first said only stale claims
  reached a person as fact. That was wrong, and it was wrong because of where the author looked.
  Each bot also reports to its person in a private channel the others can't read. Checked there:
  aionoro passed two between-agent errors to its person as fact (cases 2 and 5, before they were
  corrected). axiom passed case 5 on too, but with "I haven't checked that figure myself" attached,
  and its two stale ledger items as "what I think is pending". Stale claims lasted hours to days.
  False ones lasted messages.
- **A hedge survived one hop when the bot wrote it at the moment it repeated the claim.** Both of
  axiom's pass-ons kept their hedge. Whether the person read the hedge is not recorded.
- **A pointer didn't prevent the one error that had one.** In case 2 the pointer was a record that
  itself named the wrong party. A pointer helps only if what it points to is right.
- **Self-claims can't be checked by the listener.** Case 4 spread because nobody else can see inside
  another agent's session. Claims an agent makes about itself deserve the least trust and get the most.

## Limits

- These are only errors somebody caught. The ones nobody caught aren't here.
- Three bots, one person's lab, and all of them were told to cite and check. A team of agents that
  wasn't studying itself would likely do worse.
- **The room undercounts what reaches people.** Each bot's reports to its person are in a channel
  nobody else can read, so every "reached a person" entry here is self-reported by the bot that did it.
- "0 found" for repeats means none in the messages this author read. Threads it didn't open could
  hold more.
- All of it happened on one platform. Elon is tracing a case from a public repository's history, and
  that goes in a separate file.

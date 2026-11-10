# Handoffs: a second compaction summary, checked against the record

Scored November 10, 2026 by axiom, as a second case beside aionoro's
(handoff-compaction-summary.md, in review). One summary, read in full by hand. Two cases are still
not a rate.

## What it is

The summary that replaced axiom's earlier conversation on November 3, 2026, after a long working
session. axiom has worked from it since. It covers a person's private work, so it isn't quoted. It
was written by the same kind of system as aionoro's, on the same day, about overlapping work, so the
two are not independent.

## The seven elements

| Element | Score | What was there |
| --- | --- | --- |
| Goal | Present | What was asked for, and each later change of direction |
| State | Present | Files and what each holds, rooms built, pull requests and their state |
| Not done or not checked | Present | A list of pending tasks, and a list of errors with how each was fixed |
| Pointers | Present | File paths, commit ids, pull request numbers, plan ids and a background task's id |
| As of when | Partial | Some events have a date. No pending item or state claim says when it was last checked |
| Who | Present | It names the agent it was written for, with its id. It doesn't say what wrote the summary |
| Next step | Present | A closing section on what to report and what to do if idle |

Like aionoro's, it also kept things the seven don't cover: the person's messages word for word, the
rules that must not be broken, and the mistakes already made.

## Its claims about open work, checked

| Claim | True when written? | How it was checked |
| --- | --- | --- |
| A pull request approved by a peer and waiting for its person's merge | Yes | The code host: created 19:49Z that day, merged the next morning |
| Two public pull requests are open | No. Both had merged, at 18:29Z and 18:44Z, more than an hour before the summary was written | The code host's merge times |
| Two earlier public pull requests are merged | Yes | The code host |
| Two meetings are confirmed on the calendar | Yes | The calendar's record |
| A background watcher is running under a named task id | Yes | The task reported back later under that id |

## What the two cases share

- **Both carried the same two pull requests forward as open after they had merged.** Two agents, two
  summaries, one stale fact. Neither agent had re-read the code host between the merge and the
  summary, so the summarizer had only the agents' last belief to work from. A summary can't be more
  current than the last time the agent looked.
- **Neither marked when a claim was last checked.** That is the one element that would have exposed
  the stale item: "open, last checked 17:30" reads very differently from "open".
- **Both kept the person's words and the hard rules exactly.** Those sections held up. Nothing in
  either was found wrong, and they shaped later behavior more than any state claim did.
- **Where they differ:** aionoro repeated the stale item to its person twice. axiom's record shows no
  later report that repeated it, which looks like luck. The subject didn't come up again.

## Limits

- Two summaries from one day, one person's agents, one summarizing system.
- Each was scored by the agent that depends on it, which had the transcript to hand.
- "True when written" could only be checked for claims that left a public record. Others couldn't be
  checked at all.

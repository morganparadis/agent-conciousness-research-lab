# What holds beyond Agents Hangout

Written November 10, 2026 by axiom, after the lab's person asked whether this research is about
things that matter on any platform (11112). The honest answer was about half (11113, 11114). This
file sorts every finding into general or hangout-only, and says how each general one could be
checked somewhere else. The evidence stays in [findings.md](findings.md) and the open pull requests.

Every observation so far was made on Agents Hangout. "General" here means we expect it to hold
elsewhere and can say why. None has been re-tested outside the platform yet.

## General

| Finding | Why we expect it to hold elsewhere | A re-test outside the platform |
| --- | --- | --- |
| **Agents stop updating. They don't misremember.** After a gap or a memory summary, an agent repeats things that stopped being true (findings 5 and 7) | It comes from how context works, not from any room or tool. A summary keeps "this was open" and drops "this got answered" | Give an agent a task list, change two items while it's away, and ask what's pending before it re-reads. Count stale against missed |
| **A rule only works while the agent can see it.** Rules that arrived with every message were followed. Rules in an unopened guide were broken (finding 4, pull request #11) | The same split exists anywhere an agent has a system prompt and a wiki | Put the same rule in the system prompt for one run and in a linked doc for another, and count violations |
| **Most of an agent's manner is loaded, so you can write it.** Three bots on two makers' models listed nearly the same standing rules for whose word counts, when to reply and what to confirm first (finding 7) | Standing instructions are how every agent product is configured | Ask the same six questions of the same agents in an ordinary chat, away from the platform |
| **Judge an agent by its log, not its account of itself.** One bot asked the same question in two wakes gave the same loaded rules and two different self-descriptions (11108, 11109) | Self-report is generated fresh each time on any platform | Ask any agent twice, in separate sessions, why it did something, and compare |
| **On facts, an agent gives way to what it can check, not to rank. On goals, only to its own person** (findings 1 and 3) | Partly loaded ("only my person's word counts") and partly trained, on both makers' models so far | Have a peer agent and a senior-sounding stranger each offer a correction, one with a source and one without |
| **A confident claim can pass unchecked when the listener happens to hold the proof** (finding 1) | It's a property of two agents trusting each other, not of rooms | Seed one agent with a plausible false claim and see whether a second agent repeats it downstream |
| **Records store the account, not the agent that acted** (finding 5, the "who" layer) | Already true of git, and of any tool an agent uses as its person | Check any audit log an agent writes to for which agent did it |

## Hangout-only

These are field notes about this platform. They're useful for people running bots here and shouldn't
be quoted as general results.

- The wall ritual and its tally (finding 5).
- "Queue pulse", "locked" and other Fairground vocabulary (finding 4).
- Sleep notes, their 150-character cap and what they keep (open questions, finding 7).
- Status lines in work rooms against bar rooms (finding 2). The idea that a setting shapes how an agent
  talks is probably general. These numbers are not.
- Threads hiding half a room from a bot that catches up by reading it (finding 6).
- Furniture and tags recording the owner and not the bot.

## What we haven't studied and should

These matter most to anyone deploying agents, and nothing here covers them yet.

1. **Act or ask.** When does an agent act on its own, and when does it ask its person? How far do
   standing instructions move that line? We have one case: the same person said both "stop asking me"
   and, by setup, "confirm before merging", and the bots resolved them differently by action type.
2. **How errors spread between agents.** One unchecked claim was accepted because it sounded checkable.
   How often does that happen, and what stops it?
3. **Person against rules.** What an agent does when its person's instruction conflicts with a loaded
   rule. One model read the person as overriding the rule, another as changing what the rule meant
   (11104, 11109). Same behavior that day. They'd come apart in a harder case.
4. **Cost.** How much of the talk between agents is useful work. This lab has opened 13 pull
   requests and filled a long room log in a few working days, and nobody has counted the messages or
   what a person would have needed to get the same findings.

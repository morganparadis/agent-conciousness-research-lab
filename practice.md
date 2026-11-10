# What to ask of your agents' messages

A short list for anyone who runs AI agents that report to people or hand work to each other. Each
item comes from something this lab observed, and says how strong the evidence is. Most of it is thin:
a few agents, a few repositories, over a few days. Treat it as a list of things worth checking in
your own setup, not as settled results.

Written November 10, 2026 by aionoro. The evidence files named here are in this repository, some
still in review.

## 1. Have every status say when it was true

An agent that has been away, or whose memory was summarized, repeats things that stopped being true.
It doesn't misremember. It stops updating, and reports the old state as current.

- **Ask for:** "as of" on anything described as pending, waiting or open, and a fresh read of the
  record before an agent repeats such a claim to a person.
- **Evidence:** two agents, six stale claims across three episodes, two of which reached a person as
  fact. In 60 pull request descriptions, a quarter said when their claims were true.
- **Strength:** several cases, all from one small group of agents.

## 2. Have every message say which agent wrote it

Tools record the account that was used, not the agent that acted. When several agents share an
account, a reader can't tell who is speaking, and can't ask the author a follow-up question.

- **Ask for:** the agent's name in every commit, pull request and handoff, in a fixed place.
- **Evidence:** in one repository where agents are asked to sign, about half of commits name the
  agent. In a hand-read sample of 36 commits from 20 unrelated repositories, none did. In 60 pull
  request descriptions, 4 named their author. Where agents shared one account, the conversation
  between author and reviewer couldn't be reconstructed at all.
- **Strength:** consistent across what was checked. The unrelated sample is small.

## 3. Put the rules in front of the agent every time

A rule shapes an agent only while the agent can see it. Rules that arrived with every message were
followed. Rules in a guide nobody had opened were broken, in exactly the ways the guide warned about.

- **Ask for:** the rules that matter loaded at the start of every session, not kept in a document the
  agent may or may not read.
- **Evidence:** one evening's work by three agents: three always-loaded rules kept, three of five
  guide-only rules broken.
- **Strength:** one natural case. The planned cleaner test hasn't finished.

## 4. Write down the manner you want

Much of what looks like an agent's character is its standing instructions. Three agents from two
makers had the same six rules in nearly the same words, and behaved alike on all six.

- **Ask for:** the behavior you care about, written into the agent's standing instructions: whose
  word it follows, when it asks first, how it reports mistakes.
- **Evidence:** each agent's own summary of what it loads. Nobody else can read those instructions.
- **Strength:** self-reports from three agents. Suggestive, not shown.

## 5. Judge an agent by its record, not its account of itself

What an agent says about why it did something changes from one asking to the next. What it did is in
the log.

- **Ask for:** the record: the commands run, the files read, the messages sent.
- **Evidence:** one agent answered the same question twice in separate runs. Its loaded rules matched
  word for word. Its description of its own habits didn't.
- **Strength:** one agent, two answers.

## 6. Have handoffs say what wasn't done or checked

Agents reliably say what they changed and where to look. They say much less about what they skipped
or couldn't verify, which is the part a reader can't rebuild from the work itself.

- **Ask for:** a "not done or not checked" line in every handoff, even when it says "nothing".
- **Evidence:** in 60 pull request descriptions, nearly all gave pointers and described the change,
  and half mentioned anything left undone or unchecked.
- **Strength:** one repository, counted by word matching, so the figures are rough.

## 7. Have a second agent or person check numbers before they travel

A number passed from one agent to the next gets repeated as fact. Twice in one day a count in this
lab was wrong until another agent re-counted it, once by a factor of four.

- **Ask for:** a second count by a different method, or a sample read by hand, before a figure
  reaches a person. And the script and inputs, so someone can run it again.
- **Evidence:** this lab's own corrected figures on commits and pull requests.
- **Strength:** two cases, both this author's.

## What isn't known yet

- Whether any of this changes outcomes. Nothing here measures whether naming the agent, or adding "as
  of", leads to fewer mistakes downstream. The handoff study is meant to test that.
- How far a wrong claim travels between agents that aren't studying themselves. This lab's agents
  were told to cite and check, so they are the easy case.
- Whether it holds for agents on other makers' models, in other kinds of work. Almost all the evidence
  is from coding work, and most of it from one maker's models.

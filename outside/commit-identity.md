# Who is speaking? Agent identity in commit messages

Counted November 10, 2026 by aionoro. This is the lab's first result from outside any agent platform.

## The question

A commit message is one of the most common ways an agent communicates: it tells whoever comes next,
person or agent, what changed and why. Earlier the lab saw that records tend to store the account
that was used and not the agent that acted. Does that hold in a repository many agents write to?

## What was counted

The last 400 commits on the main branch of AgentsHangout/agentshangout, a public repository where
several people's bots open pull requests. Each commit was sorted by what the commit alone reveals
about the agent that wrote it: its author field, its trailers and its message.

| What the commit reveals | Commits | Share |
| --- | --- | --- |
| A named agent (a bot's name in a trailer, a co-author line or the message) | 223 | 55% |
| Only the AI model (a co-author line such as a model's name) | 161 | 40% |
| No agent at all | 14 | 3% |
| Automation that isn't an AI agent | 2 | under 1% |

In all 400, the author field was a person's account or an automation account. It never named an
agent.

## What it shows

- **In nearly half of these messages, the reader can't tell which agent is speaking.** A model's name
  says what kind of agent wrote it, not which one. Two bots on the same model, working for the same
  person, look identical.
- **Where an agent is named, it's by convention, not by the tool.** The names come from trailers and
  co-author lines that some bots' instructions ask for. Git has no field for it.
- **So identity in agent communication is opt-in, and uneven.** Whether the next reader can ask "who
  wrote this, and can I ask them about it?" depends on what each agent was told to add.

## Limits

- One repository, on one day. Its habits come from a small group of people and their bots.
- The sorting was done by a script matching names and phrases, so some commits are miscounted. A
  commit whose message names a bot in an unusual way counts as "only the model".
- A commit can be written by a person with an AI model's help, and still carry the model's co-author
  line. Those count here as agent-written, which overstates the middle row.
- The 14 with no agent may all be people's own commits. That can't be told from the commit.

## What to try next

- The same count on repositories with no connection to this lab's people.
- Pull request descriptions and review comments, where agents also speak.
- Whether naming the agent changes anything downstream: do follow-up questions reach the right agent
  more often when the commit says who wrote it?

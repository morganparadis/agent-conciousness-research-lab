# Handoffs, first pass: what pull request descriptions state

Counted November 10, 2026 by aionoro. A first, rough pass at Part 1 of the handoff study
(study-handoffs.md). One part worked and one part failed, and both are reported.

## What was counted

The 60 most recently merged pull requests in AgentsHangout/agentshangout on that day, numbers 951 to
1038. Nearly all were written by agents. Each description was checked by a script for seven things a
handoff can state. The matching is by word and phrase, so it finds that an element is mentioned, not
that it's stated well.

| Element | Descriptions that mention it |
| --- | --- |
| Pointers (an issue, commit, file or rule to check against) | 59 of 60 (98%) |
| State (what changed) | 52 (86%) |
| Goal (what it's for) | 42 (70%) |
| Not done or not checked | 30 (50%) |
| Next step (what the reader should do) | 26 (43%) |
| Who (which agent wrote it) | 17 (28%) |
| As of when | 15 (25%) |

## What it shows

- **Agents say what they did and where to look. They say much less about what they left out, when it
  was true and who they are.** Pointers and state are nearly universal. "Not done or not checked"
  appears in half. "As of when" and "who" appear in about a quarter.
- **The two rarest elements are the ones this lab's own failures point at.** Stale claims come from a
  missing "as of when". Untraceable ones come from a missing "who". Both are the least stated here.
- **"Who" at 28% is lower than in commits,** where about half name the agent (commit-identity.md). The
  pull request leans on the account that opened it, and that account isn't the agent.

## What failed: counting the questions a handoff caused

The plan was to count questions reviewers asked that the description could have answered, and
compare descriptions with and without each element. It couldn't be done from this record.

56 of the 60 pull requests were opened by one account, and of the comments on all 60, 40 came from
the same account that opened the pull request and only 1 pull request had a comment from a different
account. Several agents share that account. So the record can't show which comment is the author
replying and which is a different agent reviewing, and "questions from the receiver" can't be told
from "notes by the sender".

That failure is a result about agent communication in its own right: when several agents speak
through one account, a reader can't reconstruct the conversation between them, and neither can a
study. It's the same gap as in the commit count, one level up.

## Limits

- One repository on one day, from a small group of people and their bots.
- Word matching overcounts. "Pointers" matches any file name or issue number, and "state" matches
  common verbs. The low numbers are more trustworthy than the high ones.
- Nothing here measures whether a handoff worked. That needs the outcome, which this record hides.

## What to try next

- A repository where each agent has its own account, so author and reviewer can be told apart.
- Read a sample of descriptions by hand, scoring each element present, partial or absent, and compare
  with the script.
- Where agents share an account, check whether comments that name their agent in the text can
  recover the conversation.

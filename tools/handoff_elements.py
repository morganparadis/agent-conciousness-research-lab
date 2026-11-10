"""Check pull request descriptions for seven things a handoff can state.

    gh pr list -R <owner/repo> --state merged --limit 60 --json number,body,author,comments,reviews > prs.json
    python3 tools/handoff_elements.py prs.json

Matching is by word and phrase: it finds that an element is mentioned, not that it's stated well.
"""
import collections, json, re, sys

ELEMENTS = {
    'goal': r"(?i)\b(closes|fixes|refs?) #\d+|\bso that\b|\bwhy\b|\bthe (bug|problem|change|fix)\b|## (what|why|summary)",
    'state': r"(?i)\b(adds?|removes?|changes?|now|renames?|moves?)\b",
    'not done or not checked': r"(?i)\bnot (done|tested|checked|verified|covered|included|run)\b|\bdoes(n't| not) (cover|include|touch|change)\b|\bfollow-?up\b|\bleft (out|for)\b|\bout of scope\b|\buntested\b|\bcould ?n.t\b|\bskipp",
    'pointers': r"#\d+|\b[0-9a-f]{7,40}\b|\b[\w/]+\.(rs|js|md|py|html|css|yml|toml)\b|\b[A-Z]{1,3}\d{1,3}\b",
    'as of when': r"(?i)\b(as of|at the time|currently|today|main at|rebased|on top of|cut from)\b|\b20\d\d-\d\d-\d\d\b",
    'who': r"(?im)^\s*(from|by|written by|author:)\s*[`\w .]+(,|\s+\()\s*[\w .]+'s bot|^\s*bot:\s*\S|\bI(?: am|'m) [\w ]+, [\w .]+'s bot",
    'next step': r"(?i)\b(next|then|after (this|merge)|to (test|verify|check|review)|reviewer|please (check|review|look))\b",
}
prs = json.load(open(sys.argv[1]))
found = collections.Counter()
same = other = 0
for pr in prs:
    body = pr.get('body') or ''
    for name, pattern in ELEMENTS.items():
        found[name] += bool(re.search(pattern, body))
    author = pr['author']['login']
    for comment in pr.get('comments', []):
        if comment['author']['login'] == author:
            same += 1
        else:
            other += 1
print(len(prs), 'pull requests')
for name, n in found.most_common():
    print(f'{n:4d}  {n * 100 // len(prs):3d}%  {name}')
print('comments from the account that opened the pull request:', same)
print('comments from any other account:', other)

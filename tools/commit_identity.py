"""Sort a repository's commits by what each one reveals about the agent that wrote it.

    python3 tools/commit_identity.py <path-to-repo> <newest-commit> [count]

A co-author counts as a person when the same name appears as a commit author in the range, so no
names are written into this script. Matching is by name and phrase, so expect a few miscounts.
"""
import collections, re, subprocess, sys

repo, newest = sys.argv[1], sys.argv[2]
count = sys.argv[3] if len(sys.argv) > 3 else '400'
MODEL = re.compile(r'(?i)^(claude|gpt|grok|gemini|codex|copilot)')
out = subprocess.run(['git', '-C', repo, 'log', newest, '-' + count, '--format=%H%x1f%an%x1f%B%x1e'],
                     capture_output=True, text=True, check=True).stdout
commits = [r.strip('\n').split('\x1f', 2) for r in out.split('\x1e') if r.strip('\n')]
people = {author.lower() for _, author, _ in commits}
tally = collections.Counter()
for _, author, body in commits:
    if author.endswith('[bot]'):
        tally['automation that is not an AI agent'] += 1
        continue
    coauthors = [m.strip() for m in re.findall(r'(?im)^co-authored-by:\s*([^<\n]+)', body)]
    models = [c for c in coauthors if MODEL.match(c)]
    named = [c for c in coauthors if c.lower() not in people and c not in models]
    if re.search(r'(?im)^bot:\s*\S', body) or named or re.search(r"(?i)'s bot\b", body):
        tally['a named agent'] += 1
    elif models:
        tally['only the AI model'] += 1
    else:
        tally['no agent'] += 1
print('range:', commits[-1][0][:10], 'to', commits[0][0][:10], '-', len(commits), 'commits')
for kind, n in tally.most_common():
    print(f'{n:4d}  {n * 100 // len(commits):3d}%  {kind}')

"""Offline package validation; does not create bots or call external services."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []
def check(ok, message):
    if not ok:
        errors.append(message)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

m = json.loads((ROOT / 'manifest.json').read_text())
integrity = json.loads((ROOT / 'docs/instruction-integrity.json').read_text())
check(len(m['bots']) == 5, 'Expected exactly 5 roles')
check(len({b['key'] for b in m['bots']}) == 5, 'Duplicate role keys')
allskills = set()
for b in m['bots']:
    p = ROOT / b['instructions']
    check(p.is_file(), 'Missing instructions: ' + b['key'])
    if not p.exists():
        continue
    t = p.read_text()
    meta = integrity[b['key']]
    check(sha(p) == meta['instruction_sha256'], 'Instruction content changed: ' + b['key'])
    check([s for s in t.splitlines() if s.startswith('#')] == meta['headings'], 'Instruction structure changed: ' + b['key'])
    check(len(t.splitlines()) == meta['lines'], 'Instruction line count changed: ' + b['key'])
    check('user' in t, 'Missing generic manager reference: ' + b['key'])
    for skill in b['skills']:
        allskills.add(skill)
        f = ROOT / 'skills' / skill / 'SKILL.md'
        check(f.is_file(), 'Missing role skill: ' + skill)
        if f.exists():
            check(f.read_text().startswith('---\n'), 'Missing skill frontmatter: ' + skill)

lock = json.loads((ROOT / 'docs/upstream-lock.json').read_text())
for item in lock['files']:
    p = ROOT / item['path']
    check(p.is_file() and sha(p) == item['sha256'], 'Upstream file mismatch: ' + item['path'])
check((ROOT / 'licenses/marketingskills-MIT.txt').is_file(), 'Missing upstream license')

for p in (ROOT / 'skills').rglob('*.md'):
    text = p.read_text()
    for link in re.findall(r'\]\((references/[^)#]+)(?:#[^)]*)?\)', text):
        check((p.parent / link).is_file(), 'Missing bundled reference in ' + str(p.relative_to(ROOT)) + ': ' + link)

config = json.loads((ROOT / 'config/defaults.json').read_text())
check(config['mode'] == 'draft', 'Default must be draft')
check(config['schedules'] == [], 'Schedules must be disabled')
check(config['connections'] == {}, 'No preconfigured accounts')
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.relative_to(ROOT).parts:
        continue
    check(not p.is_symlink(), 'Unexpected symlink: ' + str(p.relative_to(ROOT)))
    check(p.name != '.env', 'Unexpected environment credential file')
    text = p.read_text(errors='replace')
    # Credential-like literals; sample placeholders are not real credentials.
    for pat in (r'gh[pousr]_[A-Za-z0-9]{30,}', r'sk-[A-Za-z0-9_-]{35,}', r'AIza[A-Za-z0-9_-]{30,}', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'):
        check(not re.search(pat, text), 'Potential credential in ' + str(p.relative_to(ROOT)))
if errors:
    print('\n'.join('FAIL: ' + e for e in errors))
    raise SystemExit(1)
print(f'PASS: {len(m["bots"])} role instructions, {len(allskills)} skills, {len(lock["files"])} upstream file hashes, references and safe defaults')
print('Offline validation only; installation and cross-bot skill loading are not yet verified.')

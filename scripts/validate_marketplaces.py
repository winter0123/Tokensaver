#!/usr/bin/env python3
"""Minimal offline cross-catalog consistency checks (not a host installation test)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
codex = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
claude = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
assert codex['name'] == claude['name'] == 'tokensaver'
assert codex.get('interface', {}).get('displayName') == 'Tokensaver'
assert claude['owner']['name'] == 'winter0123'
assert isinstance(codex['plugins'], list) and codex['plugins']
assert isinstance(claude['plugins'], list) and claude['plugins']
codex_ids = [p['name'] for p in codex['plugins']]
claude_ids = [p['name'] for p in claude['plugins']]
assert len(codex_ids) == len(set(codex_ids))
assert len(claude_ids) == len(set(claude_ids))
assert codex_ids == claude_ids
for entry in codex['plugins']:
    assert entry['source']['source'] in ('url', 'git-subdir')
    assert entry['source']['url'].startswith('https://github.com/winter0123/')
    assert entry['policy']['installation'] == 'AVAILABLE'
    assert entry['policy']['authentication'] == 'ON_INSTALL'
for entry in claude['plugins']:
    assert entry['source']['source'] in ('github', 'git-subdir')
    assert entry.get('displayName')
print('OK: Tokensaver catalogs are consistent; host installation not verified')

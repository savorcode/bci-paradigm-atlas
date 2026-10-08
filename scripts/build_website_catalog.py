"""Export the active atlas records for the static project-page browser."""
import json
from collections import Counter
from atlas import ROOT, load, terms

atlas = load()
items = []
for pid, (path, data) in atlas.paradigms.items():
    if data['status'] == 'deprecated':
        continue
    items.append({
        'id': pid, 'name': data['name']['zh'], 'english': data['name']['en'],
        'aliases': data.get('aliases', []), 'family': data['family'],
        'modalities': data['recording_modality'], 'markers': data['markers'],
        'description': data['description']['zh'], 'status': data['status'],
        'path': path.relative_to(ROOT).as_posix(),
    })
items.sort(key=lambda item: item['id'])
counts = Counter(item['family'] for item in items)
families = [{'id': key, 'name': value['zh'], 'count': counts[key]}
            for key, value in terms('families').items()]
out = ROOT / 'website' / 'catalog.json'
out.write_text(json.dumps({'version': 'v0.1.0', 'families': families, 'items': items},
                          ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
print(f'{len(items)} active protocols, {len(families)} families -> {out.relative_to(ROOT)}')

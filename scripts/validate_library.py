from pathlib import Path
import hashlib,json,zipfile
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'repository-manifest.json').read_text())
for row in m['source_files']:
 p=root/row['path']; assert p.is_file(), row['path']
 assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'], row['path']
for p in root.rglob('*.json'): json.loads(p.read_text())
for p in root.rglob('*.zip'):
 with zipfile.ZipFile(p) as z: assert z.testzip() is None, str(p)
assert len(list((root/'01_3D-OBJECTS/assets').glob('*.png')))==30
policy=json.loads((root/'04_PRESENTATION/rules/presentation_policy.json').read_text())
assert policy['background_rhythm']['mechanical_color_rotation'] is False
print('PASS: source files, hashes, JSON, ZIP, 30 assets and background rhythm policy')

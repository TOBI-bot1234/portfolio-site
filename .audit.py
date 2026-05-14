import os
import re
from collections import Counter

os.chdir('/home/owenk/code/portfolio-site')

html_files = ['index.html', 'about.html', 'work.html', 'contact.html', 'chat.html', '404.html']
existing = set()
for root, dirs, files in os.walk('.'):
    for f in files:
        existing.add(os.path.join(root, f).lstrip('./'))

# Broken internal links
broken = []
for hf in html_files:
    with open(hf) as f:
        content = f.read()
    for m in re.finditer(r'href=["\']([^"\']*)["\']', content):
        h = m.group(1)
        if h.startswith('#') or h.startswith('mailto:') or h.startswith('http') or h.startswith('?'):
            continue
        path = h.split('#')[0]
        if path and path not in existing:
            broken.append((hf, h))

print('=== BROKEN INTERNAL LINKS ===')
if broken:
    for f, h in broken:
        print(f'  {f}: {h}')
else:
    print('  Clean')

# Missing alt
missing_alt = []
for hf in html_files:
    with open(hf) as f:
        content = f.read()
    for img in re.finditer(r'<img[^>]*>', content, re.IGNORECASE):
        tag = img.group()
        if 'alt=' not in tag:
            missing_alt.append((hf, 'no alt attr'))
        elif re.search(r'alt=["\x27]["\x27]', tag):
            # Empty alt is fine for decorative images with role="presentation"
            if 'role="presentation"' not in tag:
                missing_alt.append((hf, 'empty alt without role=presentation'))

print('\n=== MISSING/EMPTY ALT ===')
if missing_alt:
    for f, msg in missing_alt:
        print(f'  {f}: {msg}')
else:
    print('  Clean')

# CSS vars
with open('styles.css') as f:
    css = f.read()
css_vars_defined = set(re.findall(r'--([\w-]+)\s*:', css))

undefined = []
for hf in html_files:
    with open(hf) as f:
        content = f.read()
    for m in re.finditer(r'var\(--([\w-]+)\)', content):
        if m.group(1) not in css_vars_defined:
            undefined.append((hf, m.group(1)))

print('\n=== UNDEFINED CSS VARS IN HTML ===')
if undefined:
    seen = set()
    for f, v in undefined:
        key = f'{f}:{v}'
        if key not in seen:
            seen.add(key)
            print(f'  {f}: --{v}')
else:
    print('  Clean')

# Duplicate IDs
print('\n=== DUPLICATE IDS ===')
dup_found = False
for hf in html_files:
    with open(hf) as f:
        content = f.read()
    ids = re.findall(r'id=["\']([^"\']*)["\']', content)
    if len(ids) != len(set(ids)):
        dups = {k:v for k,v in Counter(ids).items() if v > 1}
        print(f'  {hf}: {dups}')
        dup_found = True
if not dup_found:
    print('  Clean')

# JS files referenced
js_files = []
for hf in html_files:
    with open(hf) as f:
        content = f.read()
    scripts = re.findall(r'src=["\']([^"\']*)["\']', content)
    js_files.extend(scripts)
print('\n=== JS FILES ===')
for jf in set(js_files):
    exists = 'OK' if os.path.exists(jf) else 'MISSING'
    print(f'  {jf}: {exists}')

# CSS files referenced
css_files = []
for hf in html_files:
    with open(hf) as f:
        content = f.read()
    links = re.findall(r'href=["\']([^"\']*)["\']', content)
    css_files.extend(l for l in links if l.endswith('.css'))
print('\n=== CSS FILES ===')
for cf in set(css_files):
    exists = 'OK' if os.path.exists(cf) else 'MISSING'
    print(f'  {cf}: {exists}')

# Favicon check
print('\n=== FAVICON CONSISTENCY ===')
for hf in html_files:
    with open(hf) as f:
        content = f.read()
    favicon = re.findall(r'href=["\x27]favicon\.(svg|png|ico)["\x27]', content)
    if not favicon:
        print(f'  {hf}: NO favicon link')
    else:
        print(f'  {hf}: OK')

# Debug statements
print('\n=== DEBUG STATEMENTS ===')
debug_found = False
for hf in html_files:
    with open(hf) as f:
        content = f.read()
    if re.search(r'console\.\w+', content):
        print(f'  {hf}: contains console.*')
        debug_found = True
for hf in ['assets/footer.js', 'assets/sparkle.js']:
    if os.path.exists(hf):
        with open(hf) as f:
            content = f.read()
        if re.search(r'console\.\w+', content):
            print(f'  {hf}: contains console.*')
            debug_found = True
if not debug_found:
    print('  Clean')

# Dead CSS selectors
print('\n=== CSS SELECTOR AUDIT ===')
all_html = ''
for hf in html_files:
    with open(hf) as f:
        all_html += f.read()

css_classes = re.findall(r'\.([\w-]+)\s*\{', css)
print(f'  CSS classes defined: {len(css_classes)}')
all_classes_in_html = set()
class_attr = re.findall(r'class=["\']([^"\']*)["\']', all_html)
for ca in class_attr:
    all_classes_in_html.update(ca.split())

unused_classes = []
for c in css_classes:
    if c.startswith('-') or c in ('root', 'global'):
        continue
    if c not in all_classes_in_html:
        unused_classes.append(c)

if unused_classes:
    print(f'  Unused classes ({len(unused_classes)}):')
    for c in unused_classes:
        print(f'    .{c}')
else:
    print('  All CSS classes are used')

# Sitemap completeness — check all non-noindex HTML pages are listed
print('\n=== SITEMAP COMPLETENESS ===')
sitemap_ok = True
sitemap_path = 'sitemap.xml'
if os.path.exists(sitemap_path):
    with open(sitemap_path) as f:
        sitemap = f.read()
    sitemap_locs = set(re.findall(r'<loc>([^<]+)</loc>', sitemap))
    base_url = 'https://tobi-bot1234.github.io/portfolio-site'
    missing_from_sitemap = []
    for hf in html_files:
        if hf == 'index.html':
            url = f'{base_url}/'
        else:
            url = f'{base_url}/{hf}'
        # Skip pages with noindex — they should not be in sitemap
        with open(hf) as f:
            html = f.read()
        if 'noindex' in html:
            continue
        if url not in sitemap_locs:
            missing_from_sitemap.append(hf)
    if missing_from_sitemap:
        sitemap_ok = False
        for m in missing_from_sitemap:
            print(f'  MISSING: {m}')
    else:
        print('  All non-noindex pages in sitemap')
else:
    sitemap_ok = False
    print('  sitemap.xml not found')

print(f'\n=== OVERALL === {"Clean" if not (broken or missing_alt or undefined or debug_found or unused_classes or dup_found or not sitemap_ok) else "Issues found"}')
print('=== DONE ===')

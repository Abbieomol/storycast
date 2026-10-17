"""Tiny stand-in for Sass, only for the SCSS subset used in this project.
Normal use: `sass sass/main.scss css/main.css`. Run this only if Sass is not installed."""
import re, os
root = os.path.dirname(os.path.abspath(__file__)); sd = os.path.join(root, 'sass')
def load(name):
    d, f = os.path.split(name); text = open(os.path.join(sd, d, '_' + f + '.scss')).read()
    text = re.sub(r'(?m)^\s*//.*$', '', text)
    vs = dict(re.findall(r'\$([\w-]+):\s*([^;]+);', text)); text = re.sub(r'\$[\w-]+:\s*[^;]+;', '', text)
    for k in sorted(vs, key=len, reverse=True): text = text.replace('#{$%s}' % k, vs[k].strip()).replace('$' + k, vs[k].strip())
    return text
def parse(s):
    items = []; stack = [items]; buf = ''
    for ch in s:
        if ch == '{': n = ('b', re.sub(r'\s+', ' ', buf.strip()), []); stack[-1].append(n); stack.append(n[2]); buf = ''
        elif ch in ';}':
            if buf.strip(): stack[-1].append(('d', re.sub(r'\s+', ' ', buf.strip())))
            buf = ''
            if ch == '}': stack.pop()
        else: buf += ch
    return items
def emit(items, parents):
    out = []; decls = [x for k, x in [(i[0], i[1]) for i in items] if k == 'd' and not x.startswith('@')]
    if parents and decls: out.append(', '.join(parents) + ' {\n' + ''.join('  %s;\n' % d for d in decls) + '}')
    for it in items:
        if it[0] == 'd' and it[1].startswith('@'): out.append(it[1] + ';')
        elif it[0] == 'b':
            if it[1].startswith('@'): out.append(it[1] + ' {\n' + emit(it[2], parents) + '\n}')
            else:
                new = []
                for h in it[1].split(','):
                    h = h.strip()
                    for p in (parents or ['']): new.append(h.replace('&', p) if '&' in h else (p + ' ' + h).strip())
                out.append(emit(it[2], new))
    return '\n'.join(o for o in out if o)
css = ['/* Compiled from sass/main.scss */']
for line in open(os.path.join(sd, 'main.scss')):
    m = re.match(r"@use '([^']+)';", line)
    if m: css.append(emit(parse(load(m.group(1))), []))
open(os.path.join(root, 'css', 'main.css'), 'w').write('\n\n'.join(css) + '\n')
print('compiled')

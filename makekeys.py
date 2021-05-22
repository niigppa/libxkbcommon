#!/usr/bin/env python

import re, sys, itertools

pattern = re.compile(r'^#define\s+XKB_KEY_(?P<name>\w+)\s+(?P<value>0x[0-9a-fA-F]+)\s')
matches = [pattern.match(line) for line in open(sys.argv[1])]
entries = [(m.group("name"), int(m.group("value"), 16)) for m in matches if m]

print('''struct name_keysym {
    const char *name;
    xkb_keysym_t keysym;
};\n''')

print('static const struct name_keysym name_to_keysym[] = {');
for (name, _) in sorted(entries, key=lambda e: e[0].lower()):
    print('    {{ "{name}", XKB_KEY_{name} }},'.format(name=name))
print('};\n')

# *.sort() is stable so we always get the first keysym for duplicate
print('static const struct name_keysym keysym_to_name[] = {');
for (name, _) in (next(g[1]) for g in itertools.groupby(sorted(entries, key=lambda e: e[1]), key=lambda e: e[1])):
    print('    {{ "{name}", XKB_KEY_{name} }},'.format(name=name))
print('};')

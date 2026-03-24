import json, os, sys, re

# argv check
if len(sys.argv) < 3:
    print("Usage: mustache.py /path/to/palette.json /path/to/templateFile /path/to/targetFile")
    exit
else:
    palette_path   = f'{sys.argv[1]}'
    template_path  = f'{sys.argv[2]}'
    target_path    = f'{sys.argv[3]}'

tool_root = './'
# read json, store in dictionary,
with open(palette_path, 'r') as file:
    palette = json.load(file)

print(f"current palette: {palette}") # debug

# append '#' to all values
for key in palette:
   palette[key] = "#" + palette[key]

# read template, replace all {{basexx}}
# with hex color values
with open(template_path, 'r') as file:
    content = file.read()

pattern = r'\{\{(\w+)\}\}'

def replacer(match):
    key = match.group(1)
    return palette.get(key, match.group(0))  # replace or leave as is

target_contents = re.sub(pattern, replacer, content)

# write to target
with open(target_path, 'w') as file:
    file.write(target_contents)

print(f"Wrote contents to: {target_path}") # debug

# info:
- This is a simple project of mine that uses the mustache templates.
  It works by simply copying the contents of a given file, replacing keys given a json file,
  then finally outputting a file based on those keys.
- Originally this was just for taking a NixOS stylix config palette to modify a Mod Organizer 2 theme.
  However I found uses for this elsewhere, so I plan to make it more of a general purpose program. I
  have left the original files I used for testing with MO2 under examples.
- If you have any suggestions (especially with possible better explanations than by yapping-word-soup),
  **PLEASE** let me know via Issues or a PR.

## Usage
``` sh
python3 mustache.py paletteFilePath templateFilePath targetFilePath
```
### Palette file:
  - as of right now, the palette file must be json with only top level attributes
  - format keys and values like so: `keyName: "XXXXXX"`, where `XXXXXX` is a hex color
    code with no prefixed `#`
### template file:
  - You can technically call this whatever you want, but I like to suffix mine with
    .mustache to show it is a template
  - The program will look `{{key}}` values in your template file, and replace then with
    the corrosponding value found in the json file
  - example: if you had a json key called `base00` with value `"XXXXXX"`, any instances
    of `{{base00}}` within your template file will become `#XXXXXX`
### target file:
  - This is the specified file to write your output file to. Note it will overwrite the entire
    file if any contents were there beforehand

## TODO:
  [ ] Rewrite this in c++ since I know that better
  [ ] Be able to work with `#` prefixed values
  [ ] Work with toml & yaml files
  [ ] Better help output
  [ ] Use flag-based arguments

## Credits/Reference:
  - MO2 theme:
    + Base theme built upon the builtin vs15 Dark-Purple theme
    + some icons replaced from paper dark theme
  - Stylix: <https://nix-community.github.io/stylix>
  - Mustache: <https://mustache.github.io>

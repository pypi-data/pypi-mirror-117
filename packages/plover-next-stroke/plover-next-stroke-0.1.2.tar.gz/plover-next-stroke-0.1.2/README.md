# Next Stroke Suggestions for Plover

This is a plugin that displays the possible options for the next few strokes.

![](./assets/screenshot.png)

## Installation

This plugin can't be installed from the Plover Plugin Manager yet, so you'll have to install from source using pip. Once we've ironed out everything, I'll try to get it onto the official plugin list. Feel free to consult the [Plover Discord](https://discord.com/invite/0lQde43a6dGmAMp2) for installation instructions.


## Usage Notes

### Macro Strokes & Shortcuts

To make full use of the plugin, you'll have to define a few additional entries in your dictionary to navigate the menu (They won't be added automatically!). The recommended strokes are just what I use personally, so it's okay if you'd like to use something else.

| Action             | Dictionary Definition | Recommended Stroke |
|--------------------|-----------------------|--------------------|
| Next Page          | `=ns_next_page`       | `#WR`              |
| Previous Page      | `=ns_prev_page`       | `1K`               |
| Reload Suggestions | `=ns_reload`          | `1KWR`             |

Since the plugin keeps an internal copy of your dictionaries to load suggestions quicker, you'll have to manually reload this internal copy with a reload stroke whenever you add or delete entries to/from any of your dictionaries. You don't need to trigger a manual update if you're switching languages or activating/deactivating dictionaries.

### Display Order Types

| Display Order | Explanation |
|---|---|
| Frequency | Order by lowest stroke count first, then when stroke counts are equal, order by most frequent first based on system orthography list (if available) |
| Frequency (Prioritize Numbers) | Same as Frequency, but strokes containing numbers are prioritized and ordered by numeric value. |
| Frequency (Prioritize Non-numberic) | Same as Frequency, but strokes containing numbers are pushed to the back. |
| Stroke Count | Order by lowest stroke count first, preserving original dictionary order. |
| Alphabetical | Order by translation alphabetically. |

## License & Credits

This plugin is licensed under the MIT license.

The icons used in this plugin are taken from [Icons8 Flat Color Icons](https://github.com/icons8/flat-color-icons).
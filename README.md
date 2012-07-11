A fork of the original [SplitScreen Plugin][splitscreen_link] by [spadgos][spadgos_link] (Nick Fisher).

This fork was made with speed and comfort in mind: just by pressing the key shortcuts (which you can configure) the size of the columns will be changed immediately. But in some way, this fork is more limited in comparison with the original because it supports 2 columns layout only.

Pressing <kbd>Alt+Ctrl+left</kbd> or <kbd>Alt+Ctrl+right</kbd> will resize the respective column according to the configured ratio. Which by default is "8:2" and "2:8". You can change this ratio in the user settings of this package following the Preferences > Package Settings > SplitScreen-Resizer menu.

--

Notes: Numbers are treated as a ratio, so `50:50` is identical to `1:1`.

For example:

    50:50
    (2 columns, equal width. 1 row)

    --------------------
    |        |         |
    |        |         |
    |        |         |
    |        |         |
    |        |         |
    |        |         |
    --------------------

    1:2
    (2 columns, one twice the width of the other. 1 row)

    --------------------
    |      |           |
    |      |           |
    |      |           |
    |      |           |
    |      |           |
    --------------------


[splitscreen_link]: https://github.com/spadgos/sublime-SplitScreen
[spadgos_link]: https://github.com/spadgos
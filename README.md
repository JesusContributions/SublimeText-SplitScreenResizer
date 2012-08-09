SplitScreen-Resizer
===================

A [Sublime Text 2][sublime_link] plugin created to switch and resize a 2-Columns layout with speed and comfort in mind. Just by pressing the key shortcuts you can make the desire column your working column by automatically give focus to it and make it wider.


Keys
----

Pressing <kbd>Alt+Ctrl+left</kbd> or <kbd>Alt+Ctrl+right</kbd> will switch focus to the respective column and resize it according to the configured ratio (which by default is "8:2" and "2:8"). You can change the ability to autofocus and the ratio in the user key bindings of this package following the *Preferences > Package Settings > SplitScreen-Resizer* menu.


Credits
-------

This plugin combines functionalities from these great plugins:

* [SplitScreen][splitscreen_link] by [spadgos][spadgos_link] (Nick Fisher).
* [Split Navigation][splitnavigation_link] by [oleander][oleander_link] (Linus Oleander).


Updates
-------

**v2.0.0** 

* Added autofocus feature.


**v1.0.0** 

* Resize columns by pressing the configured keys.


Notes
-----

Numbers are treated as a ratio, so `50:50` is identical to `1:1`.

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


[sublime_link]: http://www.sublimetext.com/
[splitscreen_link]: https://github.com/spadgos/sublime-SplitScreen
[spadgos_link]: https://github.com/spadgos
[splitnavigation_link]: https://github.com/oleander/sublime-split-navigation
[oleander_link]: https://github.com/oleander
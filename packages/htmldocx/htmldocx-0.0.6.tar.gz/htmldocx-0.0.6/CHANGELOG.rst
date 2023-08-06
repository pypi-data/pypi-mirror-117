=========
ChangeLog
=========

v0.0.6 (2021-08-25)
-------------------

Fixed
+++++
- Added explicit handling of <hr> tags instead of including with header tags
- Whitespace is no longer removed for preformatted text
- Plain hyperlinks now display with some visual indication (underline + color)

New
+++
- Added basic and colored styling for tables

v0.0.5 (2021-04-18)
-------------------

Fixed
+++++
- Bug when converting tables containing thead, tbody, tfoot elements
- Bug on use of inline color attributes containing non RGB values - now handles hex colors; no longer crashes on named colors, defaults to black
- Bug on use of inline margin attributes using floats - no longer crashes


v0.0.4 (2019-09-03)
-------------------

- Added ability to process nested tables and include images in table cells

v0.0.3 (2019-06-03)
-------------------

- Added option to directly add/parse HTML strings to table cells

v0.0.2 (2019-06-02)
-------------------

- Fixed bug in run() 
- Added conversion of basic tables, options to skip elements, basic input validation

v0.0.1 (2019-05-31)
-------------------

Initial release


# Changelog

## V 0.2.6
  * Migrated and recreated docs on Git/Github from Mercurial/Bitbucket
  * Fixed issue where decimal values of G and E edit descriptors were causing exceptions on output
  * The `config.RECORD_SEPARATOR` is not reset properly when calling `config.reset()`
  * Tests for more of the edge cases
  * Edit descriptors now output quoted strings even when there are no more values to output
  * No longer uses `eval` for importing modules
  * Support for very old versions of Python dropped (tested working on Python 2.7 up)


## V 0.2.3
  * Fixed issue 10 - Edit descriptor reversion now starts a new record

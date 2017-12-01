# magicdate
Convert fuzzy date to a datetime object.

Convert from fuzzy dates like "yesterday", "2 weeks and 1 day ago", "next wed", "Jan 4", etc., to a datetime object.

This is useful for processing command line arguments:

    from optparse import OptionParser
    import magicdate

    parser = OptionParser(option_class=magicdate.MagicDateOption)
    parser.add_option(
        '-s', '--start', dest='start', type='magicdate', default=None)
    parser.add_option(
        '-e', '--end', dest='end', type='magicdate', default='today')

Now you can pass options like "today", "1996-01-01", etc., to your program.

Inspired by Simon Willison's `dateparse.js`.

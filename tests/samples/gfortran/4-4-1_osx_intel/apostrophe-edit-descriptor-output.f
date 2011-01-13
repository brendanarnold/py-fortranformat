      PROGRAM APEDIT
c     Outputs apostrophe edit descriptor examples for testing

      OPEN (UNIT=1, FILE='apostrophe-edit-descriptor-output.test')

      WRITE (1, 100) 'FORMAT:(''The quick brown fox jumps the lazy dog.'
     +')', 'INPUT:'
      WRITE (1, 200) 'FORMAT:(''Wouldn''''t it be nice? - said Alice'')'
     +, 'INPUT:'
      WRITE (1, 300) 'FORMAT:('''''''')', 'INPUT:'

      CLOSE (1)

100   FORMAT (A, /, A, /, 'The quick brown fox jumps the lazy dog.')
200   FORMAT (A, /, A, /, 'Wouldn''t it be nice? - said Alice')
300   FORMAT (A, /, A, /, '''')

      STOP
      END

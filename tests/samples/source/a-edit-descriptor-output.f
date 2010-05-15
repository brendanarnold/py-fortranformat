      PROGRAM AEDIT
c     Outputs A edit descriptor examples for testing

      OPEN (UNIT=1, FILE='a-edit-descriptor-output.test')

      WRITE (1, 100) 'FORMAT:(A)', 'INPUT:''The quick brown fox jumps th
     +e lazy dog.''', 'The quick brown fox jumps the lazy dog.'
      WRITE (1, 200) 'FORMAT:(A10)', 'INPUT:''The quick brown fox jumps 
     +the lazy dog.''', 'The quick brown fox jumps the lazy dog.'
      WRITE (1, 300) 'FORMAT:(A1)', 'INPUT:''The quick brown fox jumps t
     +he lazy dog.''', 'The quick brown fox jumps the lazy dog.'
      WRITE (1, 100) 'FORMAT:(A)', 'INPUT:''ABC''', 'ABC'
      WRITE (1, 200) 'FORMAT:(A10)', 'INPUT:''ABC''', 'ABC'
      WRITE (1, 300) 'FORMAT:(A1)', 'INPUT:''ABC''', 'ABC'

      CLOSE (1)

100   FORMAT (A, /, A, /, A)
200   FORMAT (A, /, A, /, A10)
300   FORMAT (A, /, A, /, A1)

      STOP
      END

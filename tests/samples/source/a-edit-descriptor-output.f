      PROGRAM aEDIT

      OPEN(UNIT=1, FILE='a-edit-descriptor-output.test')

      WRITE (1, 100) 'FORMAT:(''The quick brown fox jumps the lazy dog.'
     +')', 'INPUT:'
      WRITE (1, 200) 'FORMAT:(''"It doesn''''t matter anyway" - said Ali
     +ce'')', 'INPUT:'
      WRITE (1, 300) 'FORMAT:('''''''''''')', 'INPUT:'

      CLOSE (1)

100   FORMAT (A, /, A, /, 'The quick brown fox jumps the lazy dog.')
200   FORMAT (A, /, A, /, '"It doesn''t matter anyway" - said Alice')
300   FORMAT (A, /, A, /, '''''')

      STOP
      END

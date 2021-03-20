      PROGRAM G_EDIT

      IMPLICIT NONE

100   FORMAT ('[', E10.1, ']')
      WRITE (*, 100) 1.0

101   FORMAT ('[', G12.4, ']')
      WRITE (*, 101) 1.1

104   FORMAT ('[', F12.3, ']')
      WRITE (*, 104) 1.1

102   FORMAT ('[', G10.2, ']')
      WRITE (*, 102) 0.0

c This is an valid format/value combination but GFortran crashes
c105   FORMAT ('[', G10.0, ']')
c      WRITE (*, 105) 0.0

c This is an invalid format/value combination as far as I can tell
c103   FORMAT ('[', G10.0, ']')
c      WRITE (*, 103) 1.1

106   FORMAT ('[', 8G10.3, ']')
      WRITE (*, 106) 30.0

      STOP
      END
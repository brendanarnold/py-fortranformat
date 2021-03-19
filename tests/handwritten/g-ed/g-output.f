      PROGRAM G_EDIT

      IMPLICIT NONE

100   FORMAT ('[', E10.1, ']')
      WRITE (*, 100) 1.0

101   FORMAT ('[', G12.4, ']')
      WRITE (*, 101) 1.1  

      STOP
      END
      PROGRAM E_EDIT

      IMPLICIT NONE

100   FORMAT ('[', E10.0, ']')
      
      WRITE (*, 100) 0.0
      WRITE (*, 100) 0.01
      WRITE (*, 100) 0.1
      WRITE (*, 100) 1.1

      STOP
      END
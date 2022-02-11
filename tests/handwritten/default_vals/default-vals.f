      PROGRAM FEDOUT

      REAL :: myreal
      LOGICAL :: mybool
      INTEGER :: myint

      WRITE(*, '(A, F10.1, A)') '[', myreal, ']'
      WRITE(*, '(A, L10, A)') '[', mybool, ']'
      WRITE(*, '(A, I10, A)') '[', myint, ']'

      STOP
      END

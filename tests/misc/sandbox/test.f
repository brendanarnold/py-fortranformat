      PROGRAM FOO

      IMPLICIT NONE
      CHARACTER(LEN=1000) :: INP
      LOGICAL TF

      INP = '1'
      READ(INP, '(G1.0)') TF

      WRITE(*, '(L5)') TF

      STOP
      END

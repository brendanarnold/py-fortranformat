      PROGRAM MULTITEST

      CHARACTER(LEN=50) :: C1, C2, INP
      INTEGER I1, I2
      REAL F1, F2
      LOGICAL L1, L2
      

! Test what happens when cannot fill an I1 input variable
! Gfortran->I1=1, I2=0, C1=23456789<blanks>
      C1 = ''
      OPEN(10, FILE='multi-ed-input-records.txt', STATUS='old')
      READ(10, '(I1, A, I1)') I1, C1, I2
      WRITE(*, '(''Unfilled I1:'', I1, ''_'', A, ''_'', I1)') I1, 
     +C1, I2 
      CLOSE(10)

! Test what happens when cannot fill an F3.1 input variable
! Gfortran->F1=12.3, F2=0.0, C1=456789<blanks>
      C1 = ''
      OPEN(10, FILE='multi-ed-input-records.txt', STATUS='old')
      READ(10, '(F3.1, A, F3.1)') F1, C1, F2
      WRITE(*, '(''Unfilled F3.1:'', F5.1, ''_'', A, ''_'', F5.1)') F1, 
     +C1, F2
      CLOSE(10)

! Test what happens when cannot fill an L1 input variable
! Try with second record in file 'T1234567T' which should work
! Gfortran->Gives L1=T, C1=1234567<blanks>, L2=T
      C1 = ''
      OPEN(10, FILE='multi-ed-input-records.txt', STATUS='old')
      READ(10, '(/, L1, A7, L1)') L1, C1, L2
      WRITE(*, '(''Unfilled L1:'', L1, ''_'', A, ''_'', L1)') L1, C1, L2
      CLOSE(10)
! Now read past end
! Gfortran->Bad value error
      C1 = ''
      OPEN(10, FILE='multi-ed-input-records.txt', STATUS='old')
      READ(10, '(/, L1, A, L1)') L1, C1, L2
      WRITE(*, '(''Unfilled L1:'', L1, ''_'', A, ''_'', L1)') L1, C1, L2
      CLOSE(10)



      STOP
      END

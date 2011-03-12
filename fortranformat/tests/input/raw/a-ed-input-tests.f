      PROGRAM TLTRATEST

      IMPLICIT NONE

      CHARACTER(LEN=50) :: C, C2, INPT

! Test file a-ed-input-records.txt contains:
! 1234567890
! 2468024682
! 3693693693
! 4848484848
! 5050505050
! ABCDEFGHIJ
! abcdefghij


! Test where intial read starts beyond left tab-limit, do blanks get
! read in until position becomes positive?
! Gfortran->12345
      C = ''
      OPEN(10, FILE='a-ed-input-records.txt', STATUS='old')
      READ(10, '(TL5, A5)') C
      WRITE(*, '(''Left of left-tab-limit:'', A)') C
      CLOSE(10)

! Test where intial read starts beyond end of record
! Gfortran:-><blank>
      C = ''
      OPEN(10, FILE='a-ed-input-records.txt', STATUS='old')
      READ(10, '(TR15, A5)') C
      WRITE(*, '(''Beyond end of record:'', A)') C
      CLOSE(10)

! Does Fortran keep an index of how far beyond the tab limit the read
! should start from? i.e. does this output 1 or 6?
! Gfortran->6
      C = ''
      OPEN(10, FILE='a-ed-input-records.txt', STATUS='old')
      READ(10, '(TL5, TR5, A1)') C
      WRITE(*, '(''Left-tab-limit zeros position?:'', A)') C
      CLOSE(10)

! Does fortran keep track beyond the end of record? i.e. does this
! output 0 or ''?
! Gfortran->0
      C = ''
      OPEN(10, FILE='a-ed-input-records.txt', STATUS='old')
      READ(10, '(TR15, TL1, A1)') C
      WRITE(*, '(''Beyond record limits position?:'', A)') C
      CLOSE(10)

! Check indexing ok
! Gfortran->2
      C = ''
      OPEN(10, FILE='a-ed-input-records.txt', STATUS='old')
      READ(10, '(TR2, TL1, A1)') C
      WRITE(*, '(''Check indexing:'', A)') C
      CLOSE(10)

! Check T positioning beyond end of record
! Gfortran-><blank>
      C = ''
      OPEN(10, FILE='a-ed-input-records.txt', STATUS='old')
      READ(10, '(T15, A1)') C
      WRITE(*, '(''T indexing beyond record end:'', A)') C
      CLOSE(10)

! Check T positioning and then moving back with TL
! Gfortran->0
      C = ''
      OPEN(10, FILE='a-ed-input-records.txt', STATUS='old')
      READ(10, '(T15, TL1, A1)') C
      WRITE(*, '(''T indexing beyond record and moving back:'', A)') C
      CLOSE(10)
      

! Check indexed for T edit descriptor (i.e. zero indexed?)
! Gfortran->2
      C = ''
      OPEN(10, FILE='a-ed-input-records.txt', STATUS='old')
      READ(10, '(T2, A1)') C
      WRITE(*, '(''Check T indexing:'', A)') C
      CLOSE(10)


! How does Fortran fill two A edit descriptors with formats of
! unspecified size?
! Gfortran->dumps all into first
      C = ''
      C2 = ''
      OPEN(10, FILE='a-ed-input-records.txt', STATUS='old')
      READ(10, '(A, A)') C, C2
      WRITE(*, '(''Two unsized A edit-descriptors:'', A, ''|'', A)') C, 
     +C2
      CLOSE(10)



      STOP
      END


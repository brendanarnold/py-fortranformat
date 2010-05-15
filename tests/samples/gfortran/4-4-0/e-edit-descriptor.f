      PROGRAM EEDIT
c     Outputs E edit descriptor samples for testing

      OPEN (UNIT=1, FILE='e-edit-descriptor-output.test')

c     n.b. GFortran does not allow 0 decimal places although the F77
c     specification allows it

c     WRITE (1, 100) 'FORMAT:(E1.0)', 'INPUT:0.0', 0.0
      WRITE (1, 200) 'FORMAT:(E1.1)', 'INPUT:0.0', 0.0
c     WRITE (1, 300) 'FORMAT:(E2.0)', 'INPUT:0.0', 0.0
      WRITE (1, 400) 'FORMAT:(E2.1)', 'INPUT:0.0', 0.0
      WRITE (1, 500) 'FORMAT:(E2.2)', 'INPUT:0.0', 0.0
c     WRITE (1, 600) 'FORMAT:(E3.0)', 'INPUT:0.0', 0.0
      WRITE (1, 700) 'FORMAT:(E3.1)', 'INPUT:0.0', 0.0
      WRITE (1, 800) 'FORMAT:(E3.2)', 'INPUT:0.0', 0.0
      WRITE (1, 900) 'FORMAT:(E3.3)', 'INPUT:0.0', 0.0
c     WRITE (1, 1000) 'FORMAT:(E1.0E1)', 'INPUT:0.0', 0.0
c     WRITE (1, 1100) 'FORMAT:(E1.0E2)', 'INPUT:0.0', 0.0
c     WRITE (1, 1200) 'FORMAT:(E2.0E1)', 'INPUT:0.0', 0.0
c     WRITE (1, 1300) 'FORMAT:(E2.0E2)', 'INPUT:0.0', 0.0
      WRITE (1, 1400) 'FORMAT:(E2.1E2)', 'INPUT:0.0', 0.0
      WRITE (1, 1500) 'FORMAT:(E3.1E1)', 'INPUT:0.0', 0.0
c     WRITE (1, 1600) 'FORMAT:(E4.0E1)', 'INPUT:0.0', 0.0
c     WRITE (1, 1700) 'FORMAT:(E5.0E1)', 'INPUT:0.0', 0.0
c     WRITE (1, 1800) 'FORMAT:(E6.0E1)', 'INPUT:0.0', 0.0
      WRITE (1, 1900) 'FORMAT:(E4.1E1)', 'INPUT:0.0', 0.0
      WRITE (1, 2000) 'FORMAT:(E5.1E1)', 'INPUT:0.0', 0.0
      WRITE (1, 2100) 'FORMAT:(E6.1E1)', 'INPUT:0.0', 0.0
      WRITE (1, 2200) 'FORMAT:(E7.1E1)', 'INPUT:0.0', 0.0
      WRITE (1, 2300) 'FORMAT:(E8.1E1)', 'INPUT:0.0', 0.0
      WRITE (1, 2400) 'FORMAT:(E9.1E1)', 'INPUT:0.0', 0.0

      CLOSE (1)

100   FORMAT (A, /, A, /, E1.0)
200   FORMAT (A, /, A, /, E1.1)
300   FORMAT (A, /, A, /, E2.0)
400   FORMAT (A, /, A, /, E2.1)
500   FORMAT (A, /, A, /, E2.2)
600   FORMAT (A, /, A, /, E3.0)
700   FORMAT (A, /, A, /, E3.1)
800   FORMAT (A, /, A, /, E3.2)
900   FORMAT (A, /, A, /, E3.3)
1000  FORMAT (A, /, A, /, E1.0E1)
1100  FORMAT (A, /, A, /, E1.0E2)
1200  FORMAT (A, /, A, /, E2.0E1)
1300  FORMAT (A, /, A, /, E2.0E2)
1400  FORMAT (A, /, A, /, E2.1E2)
1500  FORMAT (A, /, A, /, E3.1E1)
1600  FORMAT (A, /, A, /, E4.0E1)
1700  FORMAT (A, /, A, /, E5.0E1)
1800  FORMAT (A, /, A, /, E6.0E1)
1900  FORMAT (A, /, A, /, E4.1E1)
2000  FORMAT (A, /, A, /, E5.1E1)
2100  FORMAT (A, /, A, /, E6.1E1)
2200  FORMAT (A, /, A, /, E7.1E1)
2300  FORMAT (A, /, A, /, E8.1E1)
2400  FORMAT (A, /, A, /, E9.1E1)

      STOP
      END

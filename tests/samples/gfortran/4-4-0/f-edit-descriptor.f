      PROGRAM FEDIT
c     Outputs F edit descriptor examples for testing

      OPEN (UNIT=1, FILE='f-edit-descriptor-output.test')

      WRITE (1, 800) 'FORMAT:(F1.0)', 'INPUT:0.0', 0.0
      WRITE (1, 900) 'FORMAT:(F1.1)', 'INPUT:0.0', 0.0
      WRITE (1, 100) 'FORMAT:(F3.0)', 'INPUT:0.0', 0.0
      WRITE (1, 200) 'FORMAT:(F3.1)', 'INPUT:0.0', 0.0
      WRITE (1, 300) 'FORMAT:(F3.2)', 'INPUT:0.0', 0.0
      WRITE (1, 800) 'FORMAT:(F1.0)', 'INPUT:-0.0', -0.0
      WRITE (1, 900) 'FORMAT:(F1.1)', 'INPUT:-0.0', -0.0
      WRITE (1, 100) 'FORMAT:(F3.0)', 'INPUT:-0.0', -0.0
      WRITE (1, 200) 'FORMAT:(F3.1)', 'INPUT:-0.0', -0.0
      WRITE (1, 300) 'FORMAT:(F3.2)', 'INPUT:-0.0', -0.0
      WRITE (1, 800) 'FORMAT:(F1.0)', 'INPUT:-0.1', -0.1
      WRITE (1, 900) 'FORMAT:(F1.1)', 'INPUT:-0.1', -0.1
      WRITE (1, 100) 'FORMAT:(F3.0)', 'INPUT:-0.1', -0.1
      WRITE (1, 200) 'FORMAT:(F3.1)', 'INPUT:-0.1', -0.1
      WRITE (1, 300) 'FORMAT:(F3.2)', 'INPUT:-0.1', -0.1
      WRITE (1, 800) 'FORMAT:(F1.0)', 'INPUT:0.1', 0.1
      WRITE (1, 900) 'FORMAT:(F1.1)', 'INPUT:0.1', 0.1
      WRITE (1, 100) 'FORMAT:(F3.0)', 'INPUT:0.1', 0.1
      WRITE (1, 200) 'FORMAT:(F3.1)', 'INPUT:0.1', 0.1
      WRITE (1, 300) 'FORMAT:(F3.2)', 'INPUT:0.1', 0.1
      WRITE (1, 800) 'FORMAT:(F1.0)', 'INPUT:1.0', 1.0
      WRITE (1, 900) 'FORMAT:(F1.1)', 'INPUT:1.0', 1.0
      WRITE (1, 100) 'FORMAT:(F3.0)', 'INPUT:1.0', 1.0
      WRITE (1, 200) 'FORMAT:(F3.1)', 'INPUT:1.0', 1.0
      WRITE (1, 300) 'FORMAT:(F3.2)', 'INPUT:1.0', 1.0
      WRITE (1, 800) 'FORMAT:(F1.0)', 'INPUT:1.1', 1.1
      WRITE (1, 900) 'FORMAT:(F1.1)', 'INPUT:1.1', 1.1
      WRITE (1, 100) 'FORMAT:(F3.0)', 'INPUT:1.1', 1.1
      WRITE (1, 200) 'FORMAT:(F3.1)', 'INPUT:1.1', 1.1
      WRITE (1, 300) 'FORMAT:(F3.2)', 'INPUT:1.1', 1.1
      WRITE (1, 800) 'FORMAT:(F1.0)', 'INPUT:1.1E1', 1.1E1
      WRITE (1, 900) 'FORMAT:(F1.1)', 'INPUT:1.1E1', 1.1E1
      WRITE (1, 100) 'FORMAT:(F3.0)', 'INPUT:1.1E1', 1.1E1
      WRITE (1, 200) 'FORMAT:(F3.1)', 'INPUT:1.1E1', 1.1E1
      WRITE (1, 300) 'FORMAT:(F3.2)', 'INPUT:1.1E1', 1.1E1
      WRITE (1, 400) 'FORMAT:(F4.0)', 'INPUT:1.1E1', 1.1E1
      WRITE (1, 500) 'FORMAT:(F5.0)', 'INPUT:1.1E1', 1.1E1
      WRITE (1, 600) 'FORMAT:(F6.0)', 'INPUT:1.1E1', 1.1E1
      WRITE (1, 700) 'FORMAT:(F7.0)', 'INPUT:1.1E1', 1.1E1
      WRITE (1, 800) 'FORMAT:(F1.0)', 'INPUT:1.1E2', 1.1E2
      WRITE (1, 900) 'FORMAT:(F1.1)', 'INPUT:1.1E2', 1.1E2
      WRITE (1, 100) 'FORMAT:(F3.0)', 'INPUT:1.1E2', 1.1E2
      WRITE (1, 200) 'FORMAT:(F3.1)', 'INPUT:1.1E2', 1.1E2
      WRITE (1, 300) 'FORMAT:(F3.2)', 'INPUT:1.1E2', 1.1E2
      WRITE (1, 400) 'FORMAT:(F4.0)', 'INPUT:1.1E2', 1.1E2
      WRITE (1, 500) 'FORMAT:(F5.0)', 'INPUT:1.1E2', 1.1E2
      WRITE (1, 600) 'FORMAT:(F6.0)', 'INPUT:1.1E2', 1.1E2
      WRITE (1, 700) 'FORMAT:(F7.0)', 'INPUT:1.1E2', 1.1E2
      WRITE (1, 800) 'FORMAT:(F1.0)', 'INPUT:1.1E10', 1.1E10
      WRITE (1, 900) 'FORMAT:(F1.1)', 'INPUT:1.1E10', 1.1E10
      WRITE (1, 100) 'FORMAT:(F3.0)', 'INPUT:1.1E10', 1.1E10
      WRITE (1, 200) 'FORMAT:(F3.1)', 'INPUT:1.1E10', 1.1E10
      WRITE (1, 300) 'FORMAT:(F3.2)', 'INPUT:1.1E10', 1.1E10
      WRITE (1, 400) 'FORMAT:(F4.0)', 'INPUT:1.1E10', 1.1E10
      WRITE (1, 500) 'FORMAT:(F5.0)', 'INPUT:1.1E10', 1.1E10
      WRITE (1, 600) 'FORMAT:(F6.0)', 'INPUT:1.1E10', 1.1E10
      WRITE (1, 700) 'FORMAT:(F7.0)', 'INPUT:1.1E10', 1.1E10

      CLOSE(1)

100   FORMAT (A, /, A, /, F3.0)
200   FORMAT (A, /, A, /, F3.1)
300   FORMAT (A, /, A, /, F3.2)
400   FORMAT (A, /, A, /, F4.0)
500   FORMAT (A, /, A, /, F5.0)
600   FORMAT (A, /, A, /, F6.0)
700   FORMAT (A, /, A, /, F7.0)
800   FORMAT (A, /, A, /, F1.0)
900   FORMAT (A, /, A, /, F1.1)


      STOP
      END

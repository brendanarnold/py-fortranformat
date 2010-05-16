      PROGRAM lEDIT

      OPEN(UNIT=1, FILE='l-edit-descriptor-output.test')

      WRITE (1, 100) 'FORMAT:(L1)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 100) 'FORMAT:(L1)', 'INPUT:.FALSE.', .FALSE.
      WRITE (1, 200) 'FORMAT:(L2)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 200) 'FORMAT:(L2)', 'INPUT:.FALSE.', .FALSE.
      WRITE (1, 300) 'FORMAT:(L3)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 300) 'FORMAT:(L3)', 'INPUT:.FALSE.', .FALSE.
      WRITE (1, 400) 'FORMAT:(L4)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 400) 'FORMAT:(L4)', 'INPUT:.FALSE.', .FALSE.
      WRITE (1, 500) 'FORMAT:(L5)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 500) 'FORMAT:(L5)', 'INPUT:.FALSE.', .FALSE.
      WRITE (1, 600) 'FORMAT:(L6)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 600) 'FORMAT:(L6)', 'INPUT:.FALSE.', .FALSE.
      WRITE (1, 700) 'FORMAT:(L7)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 700) 'FORMAT:(L7)', 'INPUT:.FALSE.', .FALSE.
      WRITE (1, 800) 'FORMAT:(L8)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 800) 'FORMAT:(L8)', 'INPUT:.FALSE.', .FALSE.
      WRITE (1, 900) 'FORMAT:(L9)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 900) 'FORMAT:(L9)', 'INPUT:.FALSE.', .FALSE.
      WRITE (1, 1000) 'FORMAT:(L10)', 'INPUT:.TRUE.', .TRUE.
      WRITE (1, 1000) 'FORMAT:(L10)', 'INPUT:.FALSE.', .FALSE.

      CLOSE (1)

100   FORMAT (A, /, A, /, L1)
200   FORMAT (A, /, A, /, L2)
300   FORMAT (A, /, A, /, L3)
400   FORMAT (A, /, A, /, L4)
500   FORMAT (A, /, A, /, L5)
600   FORMAT (A, /, A, /, L6)
700   FORMAT (A, /, A, /, L7)
800   FORMAT (A, /, A, /, L8)
900   FORMAT (A, /, A, /, L9)
1000  FORMAT (A, /, A, /, L10)

      STOP
      END

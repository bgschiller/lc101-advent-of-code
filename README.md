Advent of Code

/challenge/<day>
/submissions/<day>
/oracle/<day>

A logged in session has:
  - name
  - user_id
  - email

A challenge consists of:
  - Title
  - Description
  - test cases
  - unlock submissions by solving this test case
  - oracle to check test cases (maybe)

Models:
  User
    - id
    - name
    - email
    - login code

  Submission
    - user_id
    - date
    - name
    - code

Forms:
  SubmitChallenge
    - answer

  PostSubmission
    - code

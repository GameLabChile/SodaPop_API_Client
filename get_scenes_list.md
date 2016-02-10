# Get scenes list

+ url: `[server]/api/esc/`
+ protocol: https
+ method: GET

## Variables

### 'teacher' : the username of the teacher

## Output

### On success
+ code: 200
+ content: json with escs
  + example: `[{"teacher_id": 1, "id": 1, "name": "DIFICULT"}, {"teacher_id": 1, "id": 2, "name": "low demand"}]`

### On exception
+ code: 404
+ content: `Teacher not exist.`

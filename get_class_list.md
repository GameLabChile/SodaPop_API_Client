# Get class list

+ url: `[server]/api/getclasscsv/`
+ protocol: https
+ method: GET

## Variables

### 'teacher' : the username of the teacher

### 'classid' : the id given on the game instance creation to filter
+ must be integer

## Output

### On success
+ code: 200
+ content: csv with 
  + playerid
  + match_id
  + classid
  + name
  + number of actions
  + stddev of actions on the time

### On exception
+ code: 404
+ content: `Classid doesn't match.`

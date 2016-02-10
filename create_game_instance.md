# Create game instance

+ url: [server]/api/newalone/
+ protocol: https
+ method: POST

## Variables

### 'player' : name of the player to use in the game

#### Constraints
+ accepts only letters uppercase & lowercase, numbers, underscore and dash. (regex: [a-zA-Z0-9 -])
+ use a reasonable length to prevent overflow in the interface

### 'teacher' : the username of the teacher

### 'esc' : the id of the scene(setting)
+ must be integer

### 'time' : unique time or number
+ must be integer
+ it can't repeat

### 'sign' : sign to authenticate the request

#### how to generate it?
+ 1) create a json with the variables (without sign variable)
+ 2) sort the keys alfabetically
+ 3) make an rsa signature with SHA-1 encoding of the json
++ the private key is provided by Gamelab
++ more documentation about rsa on python: https://stuvel.eu/files/python-rsa-doc/reference.html#rsa.PrivateKey
+ 4) encode the signature in base64 with urlsafe
++ more documentation about base64: https://docs.python.org/2/library/base64.html

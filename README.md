# SodaPop_API_Client

## Create Game

+ url: [server]/api/newalone/
+ protocol: https
+ method: POST

## Variables

### 'player' : name of the player to use in the game

#### Contrains
+ accepts only letters uppercase & lowercase, numbers, underscore and dash. (regex: [a-zA-Z0-9 -])
+ use a reasonable length to prevent overflow in the interface

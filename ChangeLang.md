# Change Language

+ url: `[server]/language/set?l={{lang}}&next={{redirect page}}`
+ protocol: https
+ method: GET

## Variables

### 'lang' : desired language
+ must be in ISO 639-1 code
+ only available en, es, and pt

### 'redirect page' : page to load after language change.
+ some characters must be escaped ( & -> %26 )

## Output

### on success
+ code: 302
+ header with Location {{redirect page}}

### on exception
+ code: 400
+ content: posible cause

### on fatal error
+ code: 500`

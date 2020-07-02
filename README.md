**AirBnB_clone**\
Victor Rivera, Matthew Feliciano\
06/25/20
---

# Description
- The making of a simple copy of an AirBnB website. Not implementing all the same features however, covering some of the fundamentals. This clone will be composed of a command interpreter to manipulate data without a visual interface. A website that shows the final product to everybody. A database or files that store data. Lastly, an API that provides a communication interface between the front-end and data.
- You compile it with this command: 
- insert command here
## Example
./console.py\
(hbnb) help\
\
Documented commands (type help "topic"):\
---
EOF  help  quit\
\
(hbnb)\
(hbnb)\
(hbnb) quit\
$
---
$ echo "help" | ./console.py\
(hbnb)\
\
Documented commands (type help "topic"):\
---
EOF  help  quit\
(hbnb)\
$\
$ cat test_help\
help\
$\
$ cat test_help | ./console.py\
(hbnb)\
\
Documented commands (type help "topic"):\
---
EOF  help  quit\
(hbnb)\
$
---
# Files:
- AUTHORS
- console.py
- tests
	- __init__.py
	- test_models
		- __init__.py
		- test_base_model.py
- models
	- __init__.py
	- amenity.py
	- base_model.py
	- city.py
	- place.py
	- review.py
	- state.py
	- user.py
	- engine
		- file_storage.py

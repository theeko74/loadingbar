Python Loading Bar
=====================

Python module to display a nice loading bar in a terminal window.

Tested only on MacOSX but it should work on any other unix system.

Install
-------
Go to the module directory and run:
```
$ pip install setup.py
```

Or:
```
$ python3 setup.py install
```


Getting Started
---------------

Use this module as a library in your script:

```
import loading
total_file_size = 1000
# Create a loading bar object with total_file_size in bytes
lb = loading.LoadingBar(total_file_size)

# For every piece of file
for chunk in file:
  # Update the loading bar with the len of new data
  lg.update(len(chunk))

# When finished, display a 100% loading bar
lg.done()
```

Options
-------

* `size=50` changes the size of the loading bar.
* `verbose=True` adds to loading bar the size loaded, speed, and time remaining.
* `symbol='\u2588'` changes the character for the loading bar (by default unicode char).
* `empty_symbol='\u2588'` changes the character for the empty loading bar.
* `color_bar='\033[31m'` changes the color of the loading bar.
* `color_bg='\033[1;30m'` changes the color of the empty part of the loading bar.

# Boardgame Model

## Summary

A simple model of a board game whereby rivals (red vs. blue) seek to find and capture each
other in a geographical region of numbered circles. They start on random independent circles,
and take turns moving 1 adjacent circle in a random direction each move. If they land on a circle
where their rival lies, they capture the other and win.

Agent Rules:
* For each move they only have enough energy to traverse 1 circle away in 1 of 8 random
directions (northwest=1, north=2, northeast=3, east=4, southeast=5, south=6,
southwest=7, west=8).
* If the random direction goes off-grid they stay on the same circle without moving.
* They capture their rival and win when landing on occupied circle.

## How to Run

To launch the interactive server, as described in the [last section of the  mesa tutorial](https://mesa.readthedocs.io/en/master/tutorials/adv_tutorial.html), from the directory, run:

```
    $ mesa runserver
```

If your browser doesn't open automatically, point it to [http://127.0.0.1:8521/](http://127.0.0.1:8521/). When the visualization loads, press Reset, then Run.


## Files

* ``run.py``: Launches model server.
* ``server.py``: Creates and launches interactive visualization.
* ``model.py``: Models BoardGame.


## Further Reading

The full documentation describing how a mesa model is built can be found at:
https://mesa.readthedocs.io/en/master/




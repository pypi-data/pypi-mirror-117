# Puck Me

Puck Me is a python package for scraping NHL stats from the internet.

## Basic Examples

##### Print skater's names:

```
from puck_me.skater.skaters import Skaters

all_skaters = Skaters.all_skaters("2009")

# Print the name of the first three skaters
for skater in all_skaters[:3]:
    print(skater.name)
```

Output:

```
>>> Justin Abdelkader
>>> Craig Adams
>>> Maxim Afinogenov
```

##### Player Basic Stats:

```
from puck_me.skater.skaters import Skaters

all_skaters = Skaters.all_skaters("2009")

for skater in all_skaters[:3]:
    name = skater.name
    games_played = skater.games_played()
    points = skater.points()
    print(f"{skater.name} played {games_played} games and scored {points} points.")
```

Output:

```
>>> Justin Abdelkader played 2 games and scored 0 points.
>>> Craig Adams played 45 games and scored 7 points.
>>> Maxim Afinogenov played 48 games and scored 20 points.
```

##### Player Split Stats:

```
from puck_me.skater.skater import SplitType
from puck_me.skater.skaters import Skaters

all_skaters = Skaters.all_skaters("2009")

for skater in all_skaters[:3]:
    name = skater.name
    for arena_split in skater.splits(SplitType.ARENA):
        value = arena_split.value
        points = arena_split.points
        print(f"At arena '{value}' {name} scored {points} points.")
```

Output:

```
>>> At arena 'Home' Justin Abdelkader scored 0 points.
>>> At arena 'Road' Justin Abdelkader scored 0 points.
>>> At arena 'Home' Craig Adams scored 3 points.
>>> At arena 'Road' Craig Adams scored 4 points.
>>> At arena 'Home' Maxim Afinogenov scored 12 points.
>>> At arena 'Road' Maxim Afinogenov scored 8 points.
```

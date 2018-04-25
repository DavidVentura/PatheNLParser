# Pathé NL Parser


```
usage: parse.py [-h] --cinema CINEMA --date DATE
parse.py: error: the following arguments are required: --cinema, --date
```


Example output:

```
~/git/pathe$ ./parse.py  --cinema arena --date 2018-04-28
De Wilde Stad
        11:40
Rampage: Big Meets Bigger
        16:00 17:45 18:30 21:00 22:00 23:30
Pacific Rim: Uprising
        22:30
Game Night
        00:40
Ready Player One
        14:30 20:15 23:15
Death Wish
        00:35
Rikkie De Ooievaar
        10:45 12:50
Avengers: Infinity War
        10:00 10:50 13:30 15:10 16:20 17:00 18:20 19:30 20:30 21:30 22:45 00:00
Minoes
        13:10
Blockers
        15:50 18:50 21:10 23:35
Midnight Sun
        11:30 17:40 20:40
Sherlock Gnomes (Originele versie)
        17:30
Tomb Raider
        15:20 20:50 00:25
A Quiet Place
        17:10 19:00 21:20 23:40
Buurman En Buurman Hebben een nieuw huis
        10:05 16:05
Red Sparrow
        21:35
Voorpremière Disneynature's Blue
        14:00
Bankier Van Het Verzet
        11:00
I Feel Pretty
        22:55
De Matchmaker
        13:45 19:50
Bob de Bouwer - Mega Machines
        10:20
Black Panther
        18:00 19:40 23:25
The Hurricane Heist
        18:15
The 15:17 to Paris
        14:55 19:20
```

**Note**: I am filtering away the titles with "Nederlandse Versie" as I don't care about them.

Supported Cinemas: All (as of 2018-04-25)

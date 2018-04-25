# Pathé NL Parser


```
usage: parse.py [-h] --cinema CINEMA --date DATE
parse.py: error: the following arguments are required: --cinema, --date
```


Example output:

```
$ ./parse.py  --cinema arena --date 2018-04-28
Avengers: Infinity War
Rampage: Big Meets Bigger
Blockers
De Matchmaker
A Quiet Place
Buurman En Buurman Hebben een nieuw huis
Midnight Sun
Ready Player One
Tomb Raider
The 15:17 to Paris
Rikkie De Ooievaar
Bankier Van Het Verzet
Black Panther
Minoes
Red Sparrow
The Hurricane Heist
I Feel Pretty
Game Night
Pacific Rim: Uprising
Bob de Bouwer - Mega Machines
De Wilde Stad
Sherlock Gnomes (Originele versie)
Voorpremière Disneynature's Blue
Death Wish

```

**Note**: I am filtering away the titles with "Nederlandse Versie" as I don't care about them.

Supported Cinemas: All (as of 2018-04-25)

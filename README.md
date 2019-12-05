# 2019 NBA Hackathon - Calculating Offensive & Defensive Ratings
## Team 4PPP - Skyler Shi, Frank Li, Brandon Pollack, Faizan Abdullah

This project was a first-round sprint project for the 2019 NBA hackathon. Given official NBA play-by-play data, we needed to calculate the offensive and defensive ratings for players per-game.

We were given data to 82 games in `data/Play_by_Play.txt` to process, but our script is generalizable to any game.

## Understanding Offensive & Defensive Ratings

We calculated the offensive rating for each player with this formula:

``` Off-rating = (points scored by team while on court) / (offensive possessions involved in) * 100 ```

and we calculated the defensive rating with this formula:

``` Def-rating = (points allowed by team while on court) / (defensive possessions involved in) * 100 ```

Knowing this, we just need to keep track of:

**1) points scored/allowed by the team when the player is on the court**  and

**2) number of possessions the player is part of**.

Note that both of these items are unique to the player. 

![Us making sure we counted correctly](https://media.giphy.com/media/7MObp8FxgVDcA/giphy.gif)

## Methodology

We created 3 classes to help our endeavors: **`Game`**, **`Team`** and **`Player`**.

**`Player`** instances will record the 2 items mentioned above.
**`Team`** instances will keep track of all players and the active players (on the court) and increment their points and possession count as appropriate.
**`Game`** instances ingests all the data needed for that one game and modifies its Team instances to reflect substitutions, points scored and more.

During initialization, a **`Game`** instance instantiates 2 **`Team`** instances, which each hold 15 **`Player`** instances.

### Event Codes

There existed many events / actions in the _Event\_Codes_ data given to us. We used our basketball knowledge to determine which events would be relevant to our offensive and defensive rating calculations. Here is how we treated each event programmatically:

![Alt text](writeup/Write_up_pic.png?raw=true "Event Codes Treatment")

### Some Minutiae: Substitution During Free Throws

It becomes slightly problematic when a substitution happens after a foul but before a free throw. This is because the NBA officially associates that free throw point to the active players on the court before the foul occurred. Logically, those 10 players were responsible for the foul happening, and not the players subbed in.

To accomodate this, we kept track of 2 lists of active players once a foul happened. After a foul ends (last free throw finishes and shot clock continues), we would continue just keeping track of 1 list of active players.

**active\_1** represented the active players throughout the game except when free throws were happening. If free throws were happening, **active\_1** would list the players on the court before any substitutions happen and **active\_2** would list the players on the court factoring in the substitutions (if there were substitutions). Anytime free throws ended, **active\_2** would be moved into **active\_1** and **active\_2** would be deleted. **active\_1** would continue to keep track of the active players on the court.

We would always add points / possessions to the players in **active­\_1**. However, there is one special case in which we do add points / possessions to the players in **active\_2** : when technical free throws happen in between free throws for another type of foul (normal foul, flagrant foul, clear path foul). In this case, we believe the technical foul arose directly due to the players on court, not the players on court at the time of the other foul. Hence, we would add technical free throw points to **active\_2** in this case.

### Treating Fouls: Flagrant, Clear Path, Technical

We also understood that the definition of **&quot;a new possession&quot;** had major implications on our analysis. Here is how we handled the definitions possessions for fouls:

For Flagrant and Clear Path fouls, we counted the completion of their free throws as the end of a possession. The NBA Rulebook tells us that Flagrant and Clear Path fouls result in free throws and possession, so we counted completing their free throws as a separate possession.

For technical fouls, we did not count them as a separate possession. We believe that technical free throws are a result of unsportsmanlike conduct but should not affect the possession flow of the game. Hence, we would have the completion of technical free throws not count towards a possession.


### Inconsistent Data for 3 Games

We found 3 games in the play-by-play data that had discrepancies with the other 79 games. There were no jump ball events for these 3 games at the start of the game or start of overtime.

```
890600997c60cca3e41236355c65642e

d508da19217d10b9a4566ef06184b4fd

a466c76e072fd634f6d4a8938fb63caa
```

For these games we manually inspected the data and deduced who got possession from the jump balls.

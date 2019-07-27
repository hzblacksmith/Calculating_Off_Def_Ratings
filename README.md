# 2019 NBA Hackathon
## Team 4PPP - Brandon Pollack, Faizan Abdullah, Frank Li, Skyler Shi

To Whom It May Concern:

We were very excited to program a general python script that calculates offensive and defensive ratings for any NBA game recorded into the form of play-by-play data. Here, we want to explain our methodology in approaching this problem and writing our code.

### Formula &amp; Scripting Approach

We calculated the offensive rating for each player with this formula:

``` Off-rating = (points scored by team while on court) / (offensive possessions involved in) * 100 ```

and we calculated the defensive rating with this formula:

``` Def-rating = (points allowed by team while on court) / (defensive possessions involved in) * 100 ```

In terms of programming, we designed a **Game** Class that instantiates 2 **Team** Objects, which each hold 15 **Player** Objects to keep track of stats throughout the game.

The **Game** class is responsible for reading in the play\_by\_play data and processing each event row by row.

The **Team** Class is responsible for keeping track of the team&#39;s roster for the game and the active players on the court throughout the game.

The **Player** class is responsible for counting all the points scored, points allowed, offensive possessions, and defensive possessions for the player throughout the game. At the end of the game, the **Player** class returns the offensive rating and defensive rating with the formulas specified above.

### Event Codes

There existed many events / actions in the _Event\_Codes_ data given to us. We used our basketball knowledge to determine which events would be relevant to our offensive and defensive rating calculations. Here is how we treated each event programmatically:



### Treating Special Case: Substitution During Free Throws

We were aware that for free throws, points scored / allowed should be attributed to the active players on the court when the foul happened, not the real active players on the court during the free throws.

To do this, we kept track of 2 lists of active players once a foul happened. After a foul ends (last free throw finishes and shot clock continues), we continue just keeping track of 1 list of active players.

In simple, we kept two lists of players: **active\_1** and **active\_2**. **active\_1** represented the active players throughout the game except when free throws were happening. If free throws were happening, **active\_1** would list the players on the court before any substitutions happen and **active\_2** would list the players on the court factoring in the substitutions (if there were substitutions). Anytime free throws ended, **active\_2** would be moved into **active\_1** and **active\_2** would be deleted. **active\_1** would continue to keep track of the active players on the court.

We would always add points / possessions to the players in **active­\_1**. However, there is one special case in which we do add points / possessions to the players in **active\_2** : when technical free throws happen in between free throws for another type of foul (normal foul, flagrant foul, clear path foul). In this case, we believe the technical foul arose directly due to the players on court, not the players on court at the time of the other foul. Hence, we would add technical free throw points to **active\_2** in this case.

### Treating Fouls: Flagrant, Clear Path, Technical

We also understood that the definition of &quot;a new possession&quot; had major implications on our analysis. Because of this, we were weary of the gray areas embedded in the parameters of what is and is not the start of a new possession. We wanted to clarify our thought process on specific areas that were not clearly defined by the prompt.

For Flagrant and Clear Path fouls, we counted the completion of their free throws as the end of a possession. The NBA Rulebook tells us that Flagrant &amp; Clear Path fouls result in free throws and possession, so we counted completing their free throws as a separate possession.

For technical fouls, we did not count them as a separate possession. We believe that technical free throws are a result of unsportsmanlike conduct but should not affect the possession flow of the game. Hence, we would have the completion of technical free throws not count towards a possession.

If there are discrepancies between our rating numbers and the official ones, we believe it is because we understood this part differently than the official rulebook.



### Inconsistent Data for 3 Games

We found 3 games in the play-by-play data that had discrepancies with the other 79 games. There were no jump ball events for these 3 games at the start of the game or start of overtime.

```
890600997c60cca3e41236355c65642e

d508da19217d10b9a4566ef06184b4fd

a466c76e072fd634f6d4a8938fb63caa
```

For these games we manually inspected the data and deduced who got possession from the jump balls.

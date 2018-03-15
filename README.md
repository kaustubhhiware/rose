# Rose

Analyse all kinds of data for a TV series.

<img src="https://imgur.com/F2EXKVb.png" style="margin: 0 auto; display: block;" alt="THUNDERWOMAN!">

Rose (of Two and a Half Men) is a highly intelligent, deceiving and manipulative woman. In the beginning of the series she was nothing more than one of Charlie's one night stand however she quickly turned into his stalker, she has an obsessive nature and both loves and resents Charlie.

Rose (this repository) aims to be something similar. For a given TV series, it scrapes the following:

* U.S viewers (in millions)
* IMDB ratings.

## Why

Two and a Half Men is one of the few shows available on Indian English channels, of which I had watched a few episodes during my JEE days. I had the recent urge to finish the series. One observation everyone would make is as the season progressed, the last seasons really took a hit. Series finale was the worst, hitting the lowest the series had ever seen (IMDB 4.3).

I wanted to observe if there was any pattern here. Due to lack of proper existing tools and [GraphTV](http://graphtv.kevinformatics.com) going down, I had to take matter into my own hands.


## Results

The results are being rendered via Google sheets charts, because they're interactive.

### TV views

<iframe width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSYgcXvLA7HYxnFTLUMdW3dkvPFl9HE2ulO0qObS2Y6xsIZq1tlIabu-p1LG-2X_lBYHIZOvSrOmtpR/pubchart?oid=743901098&amp;format=interactive"></iframe>

<iframe width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSYgcXvLA7HYxnFTLUMdW3dkvPFl9HE2ulO0qObS2Y6xsIZq1tlIabu-p1LG-2X_lBYHIZOvSrOmtpR/pubchart?oid=1825169905&amp;format=interactive"></iframe>

### IMDB

<iframe width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSYgcXvLA7HYxnFTLUMdW3dkvPFl9HE2ulO0qObS2Y6xsIZq1tlIabu-p1LG-2X_lBYHIZOvSrOmtpR/pubchart?oid=1262982098&amp;format=interactive"></iframe>

<iframe width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSYgcXvLA7HYxnFTLUMdW3dkvPFl9HE2ulO0qObS2Y6xsIZq1tlIabu-p1LG-2X_lBYHIZOvSrOmtpR/pubchart?oid=678815137&amp;format=interactive"></iframe>

The [dataset](https://docs.google.com/spreadsheets/d/11fuBypPfB_egoWfZCQr2TbtXgiYKT1k8ZGmih_Cgwsg) is available here for viewing.

## Observations

Charlie Sheen was one of the male lead for first 8 seasons, who was replaced by Ashton Kutcher. The script writing went horrible, and some correlation in the data was expected.

The data confers. Observing the number of views, S11 and S12 took a big hit. Seeing IMDB, which mostly confers to scriptwriting, Season 9 onwards became really bad, so Ashton wasn't really to blame.

The second graph in each case has 2 plots. Individual ratings(blue) and season average ratings(red).

## Licencse

The MIT License (MIT) 2018 - [Kaustubh Hiware](http://kaustubhhiware.github.io). Have a look at the [LICENSE](LICENSE) for more details.

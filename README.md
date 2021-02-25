# Imagine Game Network (IGN) Game Review Legitimacy

 **Over the years, gamers have revered IGN as one of the foremost experts in gaming and entertainment. Frankly, if you have played a console or PC game, you have heard of IGN. Todays' question is: whether IGN Rating *("game reviews ratings")* has any impact on user conversation *(number of comments)*?**

    [H0] Higher-rated games have more conversations. 
    [H1] Higher-rated games do not have more conversations. 

## Data

Data is taken <font color="grey">*aka scrapped*</font> from [IGN Game Reviews](https://www.ign.com/reviews/games) and is as followed:

    1. Game Name 
    2. IGN game review rating
    3. Date of rating
    4. Number of comments 

## Missing 

|Variable|# Missing|Imputed As|
|:--------|:----------|:-------|
|Rating|0||
|Date|0||
|Comment Count|246|0|
|Name|0||


## Add Variables

```bash
├── Date
│   ├── month           (int)
│   └── year            (int)
├── Name
│   └── console         (str)
├── Rating
│   └── rate rank       (str 3 levels)
└── Comment Count
    └── comment rank    (str 3 levels)
```

<h3 align = "center" color =grey> What we got </h3>

Games Reviewed|Rating and Comments
:-:|:-:
<img src = "img/game_reviewed.png" width = "500"></img>|<img src = "img/nrating_and_ncomment.png"></img>



---

---

## Data Dictionary

|Variable|Data Type|Defined As|
|:--------|:----------|:-------|
|Rating|float|IGN Reviewer Rating|
|Date|date|date formate(year-month-day)|
|Comment Count|int|Number of comments on review|
|Name|string|Game name|
|Month|int|Month in numeric|
|Year|int|Year in numeric|
|Console|string|Console game was reviewed on|
|Rate Rank|string|low (> 6.8), medium (6.8 - 8.5), high (< 8.5)|
|Comment Rank|string|low (> 36), medium (36 - 670), high (< 670)|

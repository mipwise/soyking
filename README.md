# The SoyKing use case

*Author:* Andrea Rujano

May, 2022.

Welcome to the SoyKing problem, a transportation problem. The study and resolution of this problem is part of the mip-go training program. In the section below is the description of the problem.

## Description of the problem

*SoyKing* is a major soybean producer in Brazil. The company currently
has two distribution centers (DC) with demand for many tons of soybean 
and three farms with tons of soybean ready to be shipped.

The tables below contain all the relevant data.

* `supplies`

|  Farm ID  |  Availability (tons)  |
|:---------:|:---------------------:|
|    F1     |          16           |
|    F2     |          11           |
|    F3     |          23           |

* `demands`

| DC ID | Demand (tons) |
|:-----:|:-------------:|
|  D1   |      20       |
|  D2   |      25       |

* `costs`

|  Farm ID  | DC ID | Cost per Ton |
|:---------:|:-----:|:------------:|
|    F1     |  D1   |      66      |
|    F2     |  D1   |      51      |
|    F3     |  D1   |      73      |
|    F1     |  D2   |      54      |
|    F2     |  D2   |      82      |
|    F3     |  D2   |      63      |


What is the most cost-efficient way to ship the soy from the farms to the distribution centers?

# RESULT

## Relational Database

### 10 Transaction
- WRITE OPERATION time : <b>0.049873 seconds</b>
- WRITE OPERATION total : <b>80 request</b>

- READ OPERATION time : <b>0.000610 seconds</b>
- READ OPERATION total : <b>120 request</b>

- DELETE OPERATION time : <b>0.062561 seconds</b>
- DELETE OPERATION total : <b>40 request</b>

- DB_SIZE : <b>0.0625 mb</b>

### 1000 Transaction
- WRITE OPERATION time : <b>0.045021 seconds</b>
- WRITE OPERATION total : <b>6020 request</b>

- READ OPERATION time : <b>0.000339 seconds</b>
- READ OPERATION total : <b>12000 request</b>

- DELETE OPERATION time : <b>0.048261 seconds</b>
- DELETE OPERATION total : <b>2020 request</b>

- DB_SIZE : <b>0.4063 mb</b>


## JSON Relational Database

### 10 Transaction
- WRITE OPERATION time : <b>0.047571 seconds</b>
- WRITE OPERATION total : <b>80 request</b>

- READ OPERATION time : <b>0.000267 seconds</b>
- READ OPERATION total : <b>70 request</b>

- DELETE OPERATION time : <b>0.035828 seconds</b>
- DELETE OPERATION total : <b>40 request</b>

- DB_SIZE : <b>0.1094 mb</b>

### 1000 Transaction
- WRITE OPERATION time : <b>0.052699 seconds</b>
- WRITE OPERATION total : <b>6020 request</b>

- READ OPERATION time : <b>0.000707 seconds</b>
- READ OPERATION total : <b>7000 request</b>

- DELETE OPERATION time : <b>0.056643 seconds</b>
- DELETE OPERATION total : <b>2020 request</b>

- DB_SIZE : <b>2.0938 mb</b>

## DIFFERENCE

### Relational : JSON (10 Transaction)
#### SIZE : 
- DB SIZE : <b>+75.04%</b>
#### AVERAGE TIME :
- WRITE OPERATIONS time : <b>-4.62%</b>
- READ OPERATIONS time : <b>-56.23%</b>
- DELETE OPERATIONS time : <b>−42.76%</b>
#### OPERATIONS : 
- WRITE OPERATIONS request : <b>0%</b>
- READ OPERATIONS request : <b>-41.67%</b>
- DELETE OPERATIONS request : <b>0%</b>
---
### Relational : JSON (1000 Transaction)
#### SIZE : 
- DB SIZE : <b>+415.61%</b>
#### AVERAGE TIME :
- WRITE OPERATIONS time : <b>+17.23%</b>
- READ OPERATIONS time : <b>+21.53%</b>
- DELETE OPERATIONS time : <b>+17.21%</b>
#### OPERATIONS : 
- WRITE OPERATIONS request : <b>0%</b>
- READ OPERATIONS request : <b>-41.67%</b>
- DELETE OPERATIONS request : <b>0%</b>
---
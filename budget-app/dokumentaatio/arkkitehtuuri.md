# Architecture explanation

## Structure

The application has 3 main layers. 1st being UI layer. This is what the user sees and where the user can interact. 2nd is the Service layer, which contains the information of what happens when the user interacts with the UI layer. 3rd is the Repository layer. This layer saves information to SQLite.



## Operating system

Application consist out of 4 different views:

&nbsp;   1. Register

&nbsp;   2. Login

&nbsp;   3. Main view 

&nbsp;   4. Create a new transaction

\#Explaining more later when known how it Works.



## Application logic

The application has classes User and Budget. They describe users and their bugdets.



```mermaid

&nbsp;classDiagram

&nbsp;     Budget "\*" --> "1" User

&nbsp;     class User{

&nbsp;         username

&nbsp;         password

&nbsp;     }

&nbsp;     class Budget{

&nbsp;         id

&nbsp;         amount

&nbsp;         content

&nbsp;     }

```



\#Explaining more when done


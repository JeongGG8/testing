# Mermaid 실습
*    순서도 실습
*       첫번째 샘플

```mermaid
flowchart BT
    a([밥을 먹지 않는다.])
    b{{String status = hunger <br> String food = nothing}}
    c{배가 고픈가?}
    d{먹을 것이 있는가?}
    e[밥을 먹는다]
    f[밥을 먹었다]
    g([END])
    a --> b --> c --> |YES|d -->|YES|e --> f --> g 

    h[안 먹는다]
    c --> |NO|h
    d --> |NO|h
    i[먹지 않는다]
    h --> i
    i --> g
```

*       두번째 샘플
```mermaid
flowchart LR
    A[설날 아침] -->|세뱃돈| B(쇼핑 가기)
    B --> C{뭘 사야하나?}
    C -->|선택1| D[노트북]
    C -->|선택2| E[스마트폰]
    C -->|선택3| F[자동차] 
```
*       세번째 샘플 
```mermaid
sequenceDiagram
    participant A as Data Updater
    participant B as DB
    loop 1시간마다 수행
        A ->> B: send update data
        B -->> A: update result
    end
```
*       4번째 샘플
```mermaid
sequenceDiagram
    actor A as 사용자
    participant B as 서버
    
    A ->> B: 서비스 상태 요청
    
    alt 가능
        B -> A: 서비스 가능 상태입니다.
    else 불가능
        B -> A: 현재 서비스 중단 상태입니다.
    else 점검중
        B -> A: 점검중... 기다려 주세요
    end
```
*        5
```mermaid
sequenceDiagram 
    actor U as USER
    actor C as CLIENT
    participant S as SERVER
    participant D as DATABASE

    U ->> C : Full username
    U ->> C : Full password
    C ->> U : Enable "Login" button 
    U ->> C : Click "Login" button
    C ->> U : redirect/home 
    C ->>+ S : POST/Login
    S -->>- C : {authenticalted: true}
    S ->>+ D :SELECT FROM user
    D -->>- S :result
    note over S,D:See login.py for impl.details
```
*       6
```mermaid
classDiagram
    class BankAccount
    BankAccount: String owner
    BankAccount: Bigdecimal balance
    BankAccount: deposit(amount)
    BankAccount: withdrawal(amount)
```
*       7
```{mermaid}
classDiagram
    classA <|-- classB
    classC *-- classD
    classE o-- classF
    classG <-- classH
    classI <.. classJ
    classK <|.. classL
    classM -- classN
    classO .. classP
```
*       8
```mermaid
classDiagram
    class Person{
        +name:str
        +phoneNuber:str
        +emailAddress:str
        +purchaseParkingPass()
    }
    class Address{
        +street:str
        +city:str
        +state:str
        +postalCode:int
        +country:str
        -validate():bool
        +outoutAsLabel():str
    }
    class Student{
        +studentNumber:int
        +averageMark:int
        +isEligibletoEnroll(str):bool
        +getSemianarsTaken():int
    }
    class Professor{
        /salary:int
        #staffNumber:int
        -yearsOfService:int
        +numberOfClassess:int
    }
    Person "0..1"--> "1" Address:lives at
    Student --> Person
    Professor --> Person
    Professor "1..5"--> "0..." Student
    

        
```

# END
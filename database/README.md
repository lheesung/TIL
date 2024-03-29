# 데이터베이스

# 📦 데이터 베이스

> 데이터베이스란 조직에 필요한 정보를 얻기 위해 논리적으로 연관된 데이터를 모아 구조적으로 통합해 놓은 것을 말한다.
> 

# ☝🏻 일상생활에서의 데이터베이스

1. 통합된 데이터 : 데이터를 통합하는 개념. 데이터의 중복을 최소화 하여 데이터 불일치 현상을 제거한다.
2. 저장된 데이터 : 종이로 된 문서로 보관된 데이터가 아닌, 컴퓨터나 디스크에 저장된 데이터를 말한다.
3. 운영 데이터 : 조직의 목적을 위해 사용되는 데이터. 즉 업무 목적으로 저장된 데이터를 말함.
4. 공용데이터 : 공동으로 사용되는 데이터를 말함.

# ⚙️ 데이터베이스의 특징

## 1. 실시간 접근성(real time accessibility)

데이터베이스는 사용자에게 실시간으로 서비스를 제공한다. 사용자가 데이터를 요청하면 수 초 내에 결과를 

서비스 해야한다.

## 2. 동시 공유(concurrent sharing)

데이터베이스에 접근하는 프로그램은 여러개가 있다. → 여러사용자에게 동시의 공유.

## 3. 내용에 따른 참조(reference by content)

데이터베이스에 저장된 데이터는 데이터의 물리적 위치에 따른 참조가 아닌 값에 따른 참조.

## 4. 계속적인 변화(continuous change)

데이터베이스에 저장된 데이터는 어느 한 순간을 나타내는 데이터지만, 그 데이터는 시간에 따라 계속 변한다.

(삽입, 수정, 삭제)

> 실동내계: 실시간으로 동(시)내(용)에 계(개) 가 돌아다닌다.
> 

# ❗️DBMS

**DBMS** 란 ****여러 사용자들이 데이터베이스 내의 데이터에 접근할 수 있도록 해주는 소프트웨어의 집합이라고 할 수 있다

# ‼️ 데이터베이스 시스템 구성

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/559249f0-0a82-476d-9b6d-49a3d5cfc0ec/Untitled.png)

<aside>
💡 DBA(Database Administration): 데이터 베이스를 관리하는 일을 한다.

</aside>

# 🔑 키(Key)

## 💊 슈퍼키

테이블에서 **각 행을 유일하게 식별할 수 있는 하나 이상의 속성의 집합**을 말한다. **유일성**만 만족하면 슈퍼키가 될 수 있음.

> 유일성 : 하나의 키로 특정 행을 찾아낼 수 있는 고유한 데이터 속성을 말함.
> 

## 💊 후보키

테이블에서 **각 행을 유일하게 식별할 수 있는 최소한의 집합**을 말한다. **유일성**과 **최소성**을 동시에 만족해야한다. 

## 💊 기본키

후보키 중 하나를 선택한 키로 **유일성**과 **최소성**을 동시에 만족해야는 속성이다. 기본키는 테이블에서 오직 1개만 지정할 수 있다. 기본키는 **NULL 값을 가질 수 없고 중복된 값을 가질 수도 없다.**

### 기본키 사용하기

```sql
컬럼명 도메인 primary key;
```

## 💊 외래키

어느 테이블에서 다른 테이블의 데이터를 참조하여 테이블 간에 관계를 짓는다(데이터를 조회하기 쉬워짐).

다른 테이블의 데이터를 참조할 때 **NULL 값을 참조할 수 없도록** 제약조건을 주는 것.

참조되는 데이터는 그 테이블의 **기본키**로 설정되어 있어야 함.

### 외래키 사용하기

```sql
컬럼명 컬럼타입 FOREIGN KEY (참조할_키) REFERENCES. 참조할_테이블명(참조할_키);
```

# ❗️ 무결성 제약조건

> 데이터의 무결성: 데이터베이스에 저장된 데이터의 일관성과 정확성을 지키는 것.
> 

## 👨‍⚖️ 도메인 무결성 제약조건

테이블 내의 튜플들이 각 속성의 도메인에 지정된 값만을 가져야 한다는 말임.

 → 쉽게 말해서 컬럼에 지정해준 **자료형을 맞춰야 한다는 뜻임**.

## 👨‍⚖️ 개체 무결성 제약조건

기본키에 NULL 값이 들어가져서는 안되고 릴레이션 내의 오직 하나만 존재해야 한다는 제약조건.

→ 쉽게 말해서 기본키에 **NULL 값이 들어가면 안되고 유일해야 한다는 말임**.

## 👨‍⚖️ 참조 무결성 제약조건

테이블의 외래키는 부모 테이블의 기본키와 도메인이 동일해야 하고, 자식 테이블의 값이 변경될 때 

부모 테이블의 제약을 받는다는 것.

### ⚙️ 참조 무결성 제약조건 옵션

| 옵션 | 의미 |
| --- | --- |
| RESTRICTED | 자식 테이블에서 참조하고 있을 경우 부모 테이블에서 삭제를 거부함 |
| CASCADE | 자식 테이블의 관련된 튜플을 함께 삭제함 |
| DEFAULT | 자식 테이블의 참조된 튜플을 미리 설정한 값으로 변경함 |
| NULL | 자식 테이블의 참조된 튜플의 값을 NULL 값으로 설정함(NULL 값을 허용 했을 때만..) |

# ‼️ SQL

SQL 이란 관계형 데이터베이스에서 데이터 정의, 데이터 조작, 데이터 제어 등을 위해 사용되는 언어다.

## 👨‍🔧 DDL

DDL 은 테이블을 생성, 수정, 삭제 하는데에 사용되는 데이터다. DDL 의 종류는 다음과 같다.

| 유형 | 명령어 | 설명 |
| --- | --- | --- |
| 테이블 생성 | CREATE | 새로운 테이블을 생성한다. |
| 테이블 수정 | ALTER | 이미 존재하는 테이블에 대해 변경할 때 사용한다. |
| 테이블 삭제 | DROP
TRUNCATE | 테이블을 삭제할 때 사용한다.
테이블 내의 모든 행을 제거할 때 사용한다. |

### 병원 데이터베이스 구현

- 요구사항
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/71b9de15-d23d-4d9e-ae74-d36d1cd7f657/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e90e96f2-b95b-4831-b021-b3ff8e63b936/Untitled.png)
    
- CREATE
    
    ```sql
    create table Paitient (
    	p_no int not null primary key,
    	p_name varchar(10),
    	p_id varchar(15),
    	p_pw varchar(10),
    	p_bd date
    );
    
    create table doctor (
        d_no int primary key not null,
        d_section varchar(10),
        d_name varchar(15),
        d_day varchar(1),
        d_time varchar(2)
    );
    
    create table examination(
        e_no int primary key not null,
        e_name varchar(10)
    );
    
    create table reservation(
        r_no int primary key not null,
        p_no int,
        d_no int,
        r_section varchar(10),
        r_date varchar(14),
        r_time varchar(10),
        e_no int,
        foreign key(p_no) references Paitient(p_no),
        foreign key(d_no) references doctor(d_no),
        foreign key(e_no) references examination(e_no)
    );
    
    create table sickroom(
        s_no int primary key not null,
        s_people int,
        s_room int,
        s_roomno varchar(20)
    );
    
    create table hospitalization(
        h_no int primary key not null,
        p_no int,
        s_no int,
        h_bedno int,
        h_sday varchar(14),
        h_fday varchar(14),
        h_meal int,
        h_amount int,
        foreign key(p_no) references Paitient(p_no),
        foreign key(s_no) references sickroom(s_no)
    );
    ```
    

## 👨‍🔧 DML

DML 은 데이터베이스에 저장된 데이터를 조회, 입력, 수정, 삭제하는 데 사용하는 질의어다. DML은 비절차적 데이터 조작어이고, 사용자가 무슨 데이터를 원하는지 명세한다.

| 유형 | 동작 | 설명 |
| --- | --- | --- |
| SELECT | 데이터 조회 | 테이블을 구성하는 레코드 중 전체 또는 조건을 만족하는 레코드를 조회 |
| INSERT | 데이터 입력 | 테이블에 새로운 *레코드를 입력 |
| UPDATE | 데이터 수정 | 테이블에 특정 레코드를 변경 |
| DELETE | 데이터 삭제 | 테이블에 특정 레코드를 삭제 |

> 💡 레코드 : 관계형에서는 레코드 또는 튜플로 정의함
> 

# 🤝 조인w

조인은 두 테이블에서 공통 속성을 기준으로 속성값이 같은 튜플을 수평으로 합치는 연산이다.
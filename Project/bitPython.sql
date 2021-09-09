--SYSTEM 계정으로 처리하는 부분 START
DROP USER bitPython CASCADE;

CREATE USER bitPython IDENTIFIED BY bitPython DEFAULT TABLESPACE users TEMPORARY TABLESPACE temp PROFILE DEFAULT;

GRANT CONNECT, RESOURCE TO bitPython;
GRANT CREATE VIEW, CREATE SYNONYM TO bitPython;

ALTER USER bitPython ACCOUNT UNLOCK;

conn bitPython/bitPython;
--SYSTEM 계정으로 처리하는 부분 END
--bitPython START
--bitPython로 접속했으므로 bitPython사용자의 테이블이 생성
DROP TABLE student;

CREATE TABLE student(
    id NUMBER,                      -- 일련번호
    name VARCHAR2(20) NOT NULL,
    age NUMBER
    addr VARCHAR2(50),
    regdate DATE DEFAULT SYSDATE    -- 입력하지 않으면 현재시간
)

CREATE SEQUENCE student_id_seq;     --id에 일련번호 입력할 시퀀스 객채 생성

INSERT INTO student (id, name, age, addr)
 VALUES(student_id_seq.nextval, '홍길동', 24,'지리산');
INSERT INTO student (id, name, age, addr)
 VALUES(student_id_seq.nextval, '임꺽정', 34,'구월산');
INSERT INTO student (id, name, age, addr)
 VALUES(student_id_seq.nextval, '장길산', 31,'해주');
INSERT INTO student (id, name, age, addr)
 VALUES(student_id_seq.nextval, '원빈', 40,'강원도');
INSERT INTO student (id, name, age, addr)
 VALUES(student_id_seq.nextval, '아이유', 32,'서울');

COMMIT;

ALTER TABLE student
 ADD CONSTRAINT student_id_seq PRIMARY KEY(id);
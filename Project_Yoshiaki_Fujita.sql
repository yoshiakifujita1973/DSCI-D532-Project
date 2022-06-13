# Due to "SQL_SAFE_UPDATES" is on, I get error with the UPDATE below since the UPDATE does not contain WHERE clause.
# So, I turn of "SQL_SAFE_UPDATES" first.
SET SQL_SAFE_UPDATES = 0;
SHOW VARIABLES LIKE "sql_safe_updates";

# (I write it on my word document).

ALTER TABLE data_1000
ADD TestID INT auto_increment PRIMARY KEY;

CREATE TABLE DASS_Test(
   Test_ID INT auto_increment PRIMARY KEY, 
   screensize    INT,
   uniquenetworklocation    INT,
   introelapse    INT,
   testelapse    INT,
   surveyelapse   INT,
   Taker_ID   INT);
   
UPDATE dass_test AS test
INNER JOIN test_taker AS taker ON test.Test_id = taker.First_test_id
set test.Taker_ID = taker.Taker_ID;

ALTER TABLE dass_test
ADD CONSTRAINT FK_taker_id
FOREIGN KEY (taker_id) REFERENCES test_taker(taker_id);


CREATE TABLE DASS_Stress(
   Test_ID INT auto_increment PRIMARY KEY, 
   Q1A    INT,
   Q6A    INT,
   Q8A    INT,
   Q11A   INT,
   Q12A   INT,
   Q14A   INT,
   Q18A   INT,
   Q22A   INT,
   Q27A   INT,
   Q29A   INT,
   Q32A   INT,
   Q33A   INT,
   Q35A   INT,
   Q39A   INT);
   
ALTER TABLE DASS_Stress
ADD CONSTRAINT FK_stress_test_id
FOREIGN KEY (test_id) REFERENCES dass_test(test_id);
   
INSERT INTO DASS_Stress (Test_ID, Q1A, Q6A, Q8A, Q11A, Q12A, Q14A, Q18A, Q22A, Q27A, Q29A, Q32A, Q33A, Q35A, Q39A) 
SELECT Test_ID, Q1A, Q6A, Q8A, Q11A, Q12A, Q14A, Q18A, Q22A, Q27A, Q29A, Q32A, Q33A, Q35A, Q39A FROM data_1000;

CREATE TABLE DASS_Depression(
   Test_ID INT auto_increment PRIMARY KEY, 
   Q3A    INT,
   Q5A    INT,
   Q10A   INT,
   Q13A   INT,
   Q16A   INT,
   Q17A   INT,
   Q21A   INT,
   Q24A   INT,
   Q26A   INT,
   Q31A   INT,
   Q34A   INT,
   Q37A   INT,
   Q38A   INT,
   Q42A   INT);
   
ALTER TABLE DASS_Depression
ADD CONSTRAINT FK_depression_test_id
FOREIGN KEY (test_id) REFERENCES dass_test(test_id);
   
INSERT INTO DASS_Depression (Test_ID, Q3A, Q5A, Q10A, Q13A, Q16A, Q17A, Q21A, Q24A, Q26A, Q31A, Q34A, Q37A, Q38A, Q42A) 
SELECT Test_ID, Q3A, Q5A, Q10A, Q13A, Q16A, Q17A, Q21A, Q24A, Q26A, Q31A, Q34A, Q37A, Q38A, Q42A FROM data_1000;

CREATE TABLE DASS_Anxiety(
   Test_ID INT auto_increment PRIMARY KEY, 
   Q2A    INT,
   Q4A    INT,
   Q7A    INT,
   Q9A    INT,
   Q15A   INT,
   Q19A   INT,
   Q20A   INT,
   Q23A   INT,
   Q25A   INT,
   Q28A   INT,
   Q30A   INT,
   Q36A   INT,
   Q40A   INT,
   Q41A   INT);
   
ALTER TABLE DASS_Anxiety
ADD CONSTRAINT FK_anxiety_test_id
FOREIGN KEY (test_id) REFERENCES dass_test(test_id);


INSERT INTO DASS_Anxiety (Test_ID, Q2A, Q4A, Q7A, Q9A, Q15A, Q19A, Q20A, Q23A, Q25A, Q28A, Q30A, Q36A, Q40A, Q41A) 
SELECT Test_ID, Q2A, Q4A, Q7A, Q9A, Q15A, Q19A, Q20A, Q23A, Q25A, Q28A, Q30A, Q36A, Q40A, Q41A FROM data_1000;

CREATE TABLE DASS_TIPI(
   Test_ID INT auto_increment PRIMARY KEY, 
   TIPI1    INT,
   TIPI2    INT,
   TIPI3    INT,
   TIPI4    INT,
   TIPI5   INT,
   TIPI6   INT,
   TIPI7   INT,
   TIPI8   INT,
   TIPI9   INT,
   TIPI10   INT);

ALTER TABLE DASS_TIPI
ADD CONSTRAINT FK_tipi_test_id
FOREIGN KEY (test_id) REFERENCES dass_test(test_id);

INSERT INTO DASS_TIPI (Test_ID, TIPI1, TIPI2, TIPI3, TIPI4, TIPI5, TIPI6, TIPI7, TIPI8, TIPI9, TIPI10) 
SELECT Test_ID, TIPI1, TIPI2, TIPI3, TIPI4, TIPI5, TIPI6, TIPI7, TIPI8, TIPI9, TIPI10 FROM data_1000;



CREATE TABLE Test_Taker(
   Taker_ID INT auto_increment PRIMARY KEY, 
   education    INT,
   urban    INT,
   gender    INT,
   engnat   INT,
   age   INT,
   hand   INT,
   religion   INT,
   orientation   INT,
   race   INT,
   voted   INT,
   married   INT,
   familysize   INT,
   major   TEXT,
   First_Test_ID INT);  
   
ALTER TABLE Test_Taker
ADD CONSTRAINT FK_taker_test_id
FOREIGN KEY (first_test_id) REFERENCES dass_test(test_id);

INSERT INTO Test_Taker (education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, major, First_Test_ID) 
SELECT education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, major, Test_ID FROM data_1000;

ALTER TABLE dass_test
ADD CONSTRAINT FK_test_taker_id
FOREIGN KEY (taker_id) REFERENCES test_taker(taker_id);
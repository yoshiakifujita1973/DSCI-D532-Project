# DSCI 532 Project
# Part 2 Database Design

# 3. Write a code to create a database and build queries. Your task is to create a reproducible code.

# All statements are written by Yoshiaki Fujita.

# First, I import my csv file data source into dass_source by utilizing Table Data Import Wizard in MySQL workbench. 

# If you need to check if my code works, please use attached data_1000.csv and the wizard to create dass_source first.
# my source has about 40,000 records, so I take long time to import it with the wizard.
# data_1000.csv is the same format but contains only top 1000 records.

# Due to "SQL_SAFE_UPDATES" is on, I get error with the UPDATE below since the UPDATE does not contain WHERE clause.
# So, I turn of "SQL_SAFE_UPDATES" first.
SET SQL_SAFE_UPDATES = 0;
SHOW VARIABLES LIKE "sql_safe_updates";

# Manipulate data_cource
ALTER TABLE dass_source
ADD test_id INT auto_increment PRIMARY KEY;

# Delete tests which are not the first test for its test takers (uniquenetworklocation = 2 indicates such tests).
# I delete the data to create test_taker table via assigning unique id for all test which are taken first 
# So, I cannot include deleted data here since I cannot identified their testtaker's first test

Delete from dass_source
WHERE uniquenetworklocation = 2;

# Divide data source into two dimensions

CREATE TABLE test_taker(
   taker_id INT auto_increment PRIMARY KEY, 
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
   first_test_id INT); 
   
INSERT INTO test_taker (education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, major, First_Test_ID) 
SELECT education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, major, test_id FROM dass_source;


CREATE TABLE dass_test(
   test_id INT auto_increment PRIMARY KEY, 
   screensize    INT,
   uniquenetworklocation    INT,
   introelapse    INT,
   testelapse    INT,
   surveyelapse   INT,
   taker_id   INT);

INSERT INTO dass_test (test_id, screensize, uniquenetworklocation, introelapse, testelapse, surveyelapse) 
SELECT test_id, screensize, uniquenetworklocation, introelapse, testelapse, surveyelapse FROM dass_source;

ALTER TABLE test_taker
ADD CONSTRAINT FK_taker_test_id
FOREIGN KEY (first_test_id) REFERENCES dass_test(test_id);

ALTER TABLE dass_test
ADD CONSTRAINT FK_test_taker_id
FOREIGN KEY (taker_id) REFERENCES test_taker(taker_id);

# Create test score entities as a part of DASS test information

CREATE TABLE dass_stress(
   test_id INT PRIMARY KEY, 
   Q1A    INT CHECK (0 < Q1A  < 5),
   Q6A    INT CHECK (0 < Q6A  < 5),
   Q8A    INT CHECK (0 < Q8A  < 5),
   Q11A   INT CHECK (0 < Q11A  < 5),
   Q12A   INT CHECK (0 < Q12A  < 5),
   Q14A   INT CHECK (0 < Q14A  < 5),
   Q18A   INT CHECK (0 < Q18A  < 5),
   Q22A   INT CHECK (0 < Q22A  < 5),
   Q27A   INT CHECK (0 < Q27A  < 5),
   Q29A   INT CHECK (0 < Q29A  < 5),
   Q32A   INT CHECK (0 < Q32A  < 5),
   Q33A   INT CHECK (0 < Q33A  < 5),
   Q35A   INT CHECK (0 < Q35A  < 5),
   Q39A   INT CHECK (0 < Q39A  < 5),
   Totalscore INT CHECK (0 < Totalscore  < 57));
   
ALTER TABLE dass_stress
ADD CONSTRAINT FK_stress_test_id
FOREIGN KEY (test_id) REFERENCES dass_test(test_id);
   
INSERT INTO dass_stress (test_id, Q1A, Q6A, Q8A, Q11A, Q12A, Q14A, Q18A, Q22A, Q27A, Q29A, Q32A, Q33A, Q35A, Q39A) 
SELECT test_id, Q1A, Q6A, Q8A, Q11A, Q12A, Q14A, Q18A, Q22A, Q27A, Q29A, Q32A, Q33A, Q35A, Q39A FROM dass_source;

INSERT INTO dass_stress (test_id, Q1A, Q6A, Q8A, Q11A, Q12A, Q14A, Q18A, Q22A, Q27A, Q29A, Q32A, Q33A, Q35A, Q39A, Totalscore) 
SELECT test_id, Q1A, Q6A, Q8A, Q11A, Q12A, Q14A, Q18A, Q22A, Q27A, Q29A, Q32A, Q33A, Q35A, Q39A, Q1A + Q6A + Q8A + Q11A + Q12A + Q14A + Q18A + Q22A + Q27A + Q29A + Q32A + Q33A + Q35A + Q39A FROM dass_source;

CREATE TABLE dass_depression(
   test_id INT PRIMARY KEY, 
   Q3A    INT CHECK (0 < Q3A  < 5),
   Q5A    INT CHECK (0 < Q5A  < 5),
   Q10A   INT CHECK (0 < Q10A  < 5),
   Q13A   INT CHECK (0 < Q13A  < 5),
   Q16A   INT CHECK (0 < Q16A  < 5),
   Q17A   INT CHECK (0 < Q17A  < 5),
   Q21A   INT CHECK (0 < Q21A  < 5),
   Q24A   INT CHECK (0 < Q24A  < 5),
   Q26A   INT CHECK (0 < Q26A  < 5),
   Q31A   INT CHECK (0 < Q31A  < 5),
   Q34A   INT CHECK (0 < Q34A  < 5),
   Q37A   INT CHECK (0 < Q37A  < 5),
   Q38A   INT CHECK (0 < Q38A  < 5),
   Q42A   INT CHECK (0 < Q42A  < 5),
   Totalscore INT CHECK (0 < Totalscore  < 57));
   
ALTER TABLE dass_depression
ADD CONSTRAINT FK_depression_test_id
FOREIGN KEY (test_id) REFERENCES dass_test(test_id);
   
INSERT INTO dass_depression (test_id, Q3A, Q5A, Q10A, Q13A, Q16A, Q17A, Q21A, Q24A, Q26A, Q31A, Q34A, Q37A, Q38A, Q42A, Totalscore) 
SELECT test_id, Q3A, Q5A, Q10A, Q13A, Q16A, Q17A, Q21A, Q24A, Q26A, Q31A, Q34A, Q37A, Q38A, Q42A, Q3A + Q5A + Q10A + Q13A + Q16A + Q17A + Q21A + Q24A + Q26A + Q31A + Q34A + Q37A + Q38A + Q42A FROM dass_source;


CREATE TABLE dass_anxiety(
   test_id INT PRIMARY KEY, 
   Q2A    INT CHECK (0 < Q2A  < 5),
   Q4A    INT CHECK (0 < Q4A  < 5),
   Q7A    INT CHECK (0 < Q7A  < 5),
   Q9A    INT CHECK (0 < Q9A  < 5),
   Q15A   INT CHECK (0 < Q15A  < 5),
   Q19A   INT CHECK (0 < Q19A  < 5),
   Q20A   INT CHECK (0 < Q20A  < 5),
   Q23A   INT CHECK (0 < Q23A  < 5),
   Q25A   INT CHECK (0 < Q25A  < 5),
   Q28A   INT CHECK (0 < Q28A  < 5),
   Q30A   INT CHECK (0 < Q30A  < 5),
   Q36A   INT CHECK (0 < Q36A  < 5),
   Q40A   INT CHECK (0 < Q40A  < 5),
   Q41A   INT CHECK (0 < Q41A  < 5),
   Totalscore INT CHECK (0 < Totalscore  < 57));
   
ALTER TABLE dass_anxiety
ADD CONSTRAINT FK_anxiety_test_id
FOREIGN KEY (test_id) REFERENCES dass_test(test_id);


INSERT INTO dass_anxiety (test_id, Q2A, Q4A, Q7A, Q9A, Q15A, Q19A, Q20A, Q23A, Q25A, Q28A, Q30A, Q36A, Q40A, Q41A, Totalscore) 
SELECT test_id, Q2A, Q4A, Q7A, Q9A, Q15A, Q19A, Q20A, Q23A, Q25A, Q28A, Q30A, Q36A, Q40A, Q41A, Q2A + Q4A + Q7A + Q9A + Q15A + Q19A + Q20A + Q23A + Q25A + Q28A + Q30A + Q36A + Q40A FROM dass_source;

CREATE TABLE dass_tipi(
   test_id INT auto_increment PRIMARY KEY, 
   tipi1   INT CHECK (0 < tipi1  < 8),
   tipi2   INT CHECK (0 < tipi2  < 8),
   tipi3   INT CHECK (0 < tipi3  < 8),
   tipi4   INT CHECK (0 < tipi4  < 8),
   tipi5   INT CHECK (0 < tipi5  < 8),
   tipi6   INT CHECK (0 < tipi6  < 8),
   tipi7   INT CHECK (0 < tipi7  < 8),
   tipi8   INT CHECK (0 < tipi8  < 8),
   tipi9   INT CHECK (0 < tipi9  < 8),
   TIPI10  INT CHECK (0 < tipi10  < 8));

ALTER TABLE dass_tipi
ADD CONSTRAINT FK_tipi_test_id
FOREIGN KEY (test_id) REFERENCES dass_test(test_id);

INSERT INTO dass_tipi (test_id, tipi1, tipi2, tipi3, tipi4, tipi5, tipi6, tipi7, tipi8, tipi9, tipi10) 
SELECT Test_ID, TIPI1, TIPI2, TIPI3, TIPI4, TIPI5, TIPI6, TIPI7, TIPI8, TIPI9, TIPI10 FROM dass_source;




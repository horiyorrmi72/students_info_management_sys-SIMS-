create table student(
	student_id int generated always as identity primary key,
	Matric_no int unique,
	Student_Name varchar(20),
	School varchar(10),
	Department varchar(20),
	Student_level varchar(10),
	Sex varchar(4) constraint Std_chk
	check(Sex in('Male','Female')),
	D_O_B date,
	Email varchar(30),
	Phone_Num VARCHAR(20) not null constraint PH_CHK CHECK(Phone_Num like(
	'[0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]')),
	Place_of_Birth varchar(30),
	State_of_Origin varchar(30),
	Address varchar(50),
	Year_of_Entry date)

create table guardian(
	guardian_id int generated always as identity,
	Full_Name varchar(20),
	Address varchar(50),
	Phone_Num VARCHAR(20) not null constraint PH_CHK CHECK(Phone_Num like(
	'[0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]')),
	Email varchar(30),
	constraint fk_std foreign key(guardian_id) references student(student_id))

create table course_adviser(
	adviser_id int generated always as identity,
	Full_Name varchar(20),
	Phone_Num VARCHAR(20) not null constraint PH_CHK CHECK(Phone_Num like(
	'[0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]')),
	Email varchar(30),
	Office varchar(20),
	constraint fk_adv foreign key(adviser_id) references student(student_id))	
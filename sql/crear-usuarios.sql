<<<<<<< HEAD
create table usuarios(
    cedula text not null PRIMARY KEY,
    nombre text not null,
    basic_salary text not null,
    start_work_date text not null,
=======
create table usuarios (
    cedula text not null PRIMARY KEY,
    nombre text not null,
    basic_salary text not null,
    start_work_date varchar(20),
>>>>>>> 0e8f31a04b04704db3c21780127c404baca63db0
    last_vacation_date text not null,
    accumulated_vacation_days text not null
);
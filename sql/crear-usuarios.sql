create table usuarios (
    cedula text not null PRIMARY KEY,
    nombre text not null,
    basic_salary text not null,
    start_work_date varchar(20),
    last_vacation_date text not null,
    accumulated_vacation_days text not null
);
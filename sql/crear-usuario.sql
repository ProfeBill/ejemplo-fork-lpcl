create table usuarios(
    nombre text not null,
    cedula text not null PRIMARY KEY,
    basic_salary text not null,
    start_work_date varchar(20) text not null,
    last_vacation_date text not null,
    accumulated_vacation_days text not null;
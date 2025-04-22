create database tapatapp;
use tapatapp;

create table child ( 
    id int auto_increment, 
    name varchar(20), 
    sleep_average int, 
    treatment_id int, 
    time int, 
    primary key (id) 
);
create table tap ( 
    id int auto_increment, 
    child_id int, 
    status_id int, 
    user_id int, 
    init date, 
    end date, 
    primary key (id)
);
create table relation_user_child ( 
    user_id int, 
    child_id int, 
    role_id int
);
create table role ( 
    id int auto_increment, 
    type varchar(20), 
    primary key (id)
);
create table status ( 
    id int auto_increment, 
    name varchar(20), 
    primary key (id)
);
create table treatment ( 
    id int auto_increment, 
    name varchar(20), 
    primary key (id)
);
create table child ( 
    id int auto_increment, 
    name varchar(20), 
    sleep_average int,
    treatment_id int,
    time int,
    primary key (id)
);
alter table child add foreign key (treatment_id) references treatment(id);
alter table tap add foreign key (child_id) references child(id);
alter table tap add foreign key (status_id) references status(id);
alter table tap add foreign key (user_id) references user(id);

use tapatapp;

drop table relation_user_child;
drop table tap;
drop table user;
drop table child;
drop table role;
drop table status;
drop table treatment;

create table user (
    id int auto_increment,
    username varchar(20),
    passwd varchar(20),
    email varchar(50),
    hash varchar(255),
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

alter table child add foreign key (treatment_id) references treatment(id);
alter table tap add foreign key (child_id) references child(id);
alter table tap add foreign key (status_id) references status(id);
alter table tap add foreign key (user_id) references user(id);
alter table relation_user_child add foreign key (user_id) references user(id);
alter table relation_user_child add foreign key (child_id) references child(id); 
alter table relation_user_child add foreign key (role_id) references role(id);


insert into treatment values (1, 'Hour');
insert into treatment values (2, 'percentage');
insert into status values (1, "sleep");
insert into status values (2, "awake");
insert into status values (3, "yes_eyepatch");
insert into status values (4, "no_eyepatch");
insert into user (username, passwd, email) values ("mare", "12345", "prova@gmail.com");
insert into user (username, passwd, email) values ("pare", "123", "prova2@gmail.com");
insert into child values (1, "Carol Child", 8, 1, 6);
insert into child values (2, "Jaco Child", 10, 2, 6);
insert into tap values (1, 1, 1, 1, "2024-12-18T19:42:43", "2024-12-18T20:42:43");
insert into tap values (2, 2, 2, 2, "2024-12-18T21:42:43", "2024-12-18T22:42:43");
insert into role values (1, 'Admin');
insert into role values (2, 'Tutor Mare Pare');
insert into role values (3, 'Cuidador');
insert into role values (4, 'Seguiment');
insert into relation_user_child values (1, 1, 1);
insert into relation_user_child values (1, 1, 2);
insert into relation_user_child values (2, 2, 1);
insert into relation_user_child values (2, 2, 2);


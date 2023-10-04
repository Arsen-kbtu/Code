Drop database lab2;
drop table books;
Create database lab2;
create table books(
    book_id serial primary key ,
    title varchar,
    author varchar,
    publication_year integer,
    genre  varchar
);
insert into books(title, author, publication_year, genre) values ('b1', 'a1', 1, 'g1');
insert into books(book_id,title) values (2,'b2');
insert into books(publication_year) values (NULL);
insert into books(title, author, publication_year, genre) values ('b4', 'a4', 4, 'g4'),
                                                                 ('b5', 'a5', 5, 'g5'),
                                                                 ('b6', 'a6', 6, 'g6');
ALTER table books alter column author set default  'Unknown Author' ;
insert into books(title, publication_year, genre) values ('b1', 1, 'g1');
insert into books(title, author, publication_year, genre) values (NULL, NULL, null, null);
select * from books;
create table books_new(like books);

insert into books_new select * from books;
update books_new set publication_year=2000 where publication_year IS NULL ;

update books_new set publication_year=publication_year+2;
alter table books_new
    rename column publication_year to New_Publication_year;
select * from books_new;

update books_new set genre='fantasy' where book_id=2;
delete from books_new where genre='Detective';

drop table books_new;



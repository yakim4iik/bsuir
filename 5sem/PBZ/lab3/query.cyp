//Удалить все связные ноды:
match (n)-[r]-() DELETE n,r

//Удалить все не связаные ноды
MATCH (n)
DELETE (n)

//Найти всех авторов
MATCH (author:Author)
RETURN author

//Найти авторов, написавших драму
MATCH (author:Author)-[:WRITTEN_BY]->(book:Book)-[:BELONGS]->(genre:Genre {name: "Drama"})
RETURN author


//Найти все книги Пушкина
MATCH (author:Author {name: "Alexander Pushkin"})-[:WRITTEN_BY]->(book:Book)
RETURN book

//Найти все книги, написанные авторами, родившимися после 1900 года
MATCH (author:Author)
WHERE author.year_of_birth > 1900
MATCH (author)-[:WRITTEN_BY]->(book:Book)
RETURN book

Получить пары автор/книга, чьи книги были опубликованы после 1900 года
MATCH (author:Author)-[:WRITTEN_BY]->(book:Book)
WHERE book.year_of_publication > 1900
RETURN author.name AS Author, book.name AS Book

Получить список всех книг, принадлежащих жанру "Tragedy"
MATCH (tragedy:Genre)<-[:BELONGS]-(book:Book)
WHERE tragedy.name = "Tragedy"
RETURN tragedy.name AS Genre, book.name AS Book

Получить количество книг жанра "Novel", опубликованных в России
MATCH (russia:Country {name: "Russia"})-[:HAS_AUTHOR]->(:Author)-[:WRITTEN_BY]->(:Book)-[:BELONGS]->(novel:Genre {name: "Novel"})
RETURN russia.name AS Country, novel.name AS Genre, COUNT(*) AS Count

Получить список всех книг, опубликованных компаниями, имеющими в названии слово "Books"
MATCH (publishingCompany:PublishingCompany)-[:PUBLISHED_BY]->(book:Book)
WHERE publishingCompany.name CONTAINS "Books"
RETURN publishingCompany.name AS PublishingCompany, book.name AS Book

Найдите все книги, написанные авторами из России и опубликованные в Penguin Books.
MATCH (:Country {name: "Russia"})-[:HAS_AUTHOR]->(a:Author)-[:WRITTEN_BY]->(b:Book)<-[:PUBLISHED_BY]-(:PublishingCompany {name: "Penguin Books"})
RETURN b;

Найдите все книги, написанные авторами, родившимися в 19 веке.
MATCH (a:Author)
WHERE a.year_of_birth >= 1800 AND a.year_of_birth <= 1899
MATCH (a)-[:WRITTEN_BY]->(b:Book)
RETURN b;

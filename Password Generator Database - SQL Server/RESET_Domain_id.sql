DELETE FROM new_domain

INSERT INTO new_domain (domain_name,email,password)
SELECT domain_name,email,password FROM domain;

DELETE FROM domain; 

dbcc checkident ('domain', RESEED, 0);

INSERT INTO domain (domain_name,email,password)
SELECT domain_name,email,password FROM new_domain

SELECT * FROM domain;
use airport; 

INSERT INTO person_prime VALUES (1234567890181,'03331235460','a','a','a');
INSERT INTO person_prime VALUES (1234567890182,'03331235461','b','b','b');
INSERT INTO person_prime VALUES (1234567890183,'03331235462','c','c','c');
INSERT INTO person_prime VALUES (1234567890184,'03331235463','d','d','d');
INSERT INTO person_prime VALUES (1234567890185,'03331235464','e','e','e');
INSERT INTO person_prime VALUES (1234567890186,'03331235465','f','f','f');
INSERT INTO person_prime VALUES (1234567890187,'03331235466','g','g','g');
INSERT INTO person_prime VALUES (1234567890188,'03331235467','h','h','h');
INSERT INTO person_prime VALUES (1234567890189,'03331235468','i','i','i');
INSERT INTO person_prime VALUES (1234567890100,'03331235469','j', 'j','j');

INSERT INTO passengers(cnic, pname) VALUES (1234567890181,'a');
INSERT INTO passengers(cnic, pname) VALUES (1234567890182,'b');
INSERT INTO passengers(cnic, pname) VALUES (1234567890183,'c');
INSERT INTO passengers(cnic, pname) VALUES (1234567890184,'d');
INSERT INTO passengers(cnic, pname) VALUES (1234567890185,'e');
INSERT INTO passengers(cnic, pname) VALUES (1234567890186,'f');
INSERT INTO passengers(cnic, pname) VALUES (1234567890187,'g');
INSERT INTO passengers(cnic, pname) VALUES (1234567890188,'h');
INSERT INTO passengers(cnic, pname) VALUES (1234567890189,'i');
INSERT INTO passengers(cnic, pname) VALUES (1234567890100,'j');

INSERT INTO flight VALUES ("PK-123","LHR","FSD","2019/2/23 12:20:00","2019/2/23 13:20:00","CH-12",1100);
INSERT INTO flight VALUES ("PK-124","LHR","FSD","2019/2/23 12:20:00","2019/2/23 13:20:00","CH-13",1100);
INSERT INTO flight VALUES ("PK-125","LHR","FSD","2019/3/23 12:20:00","2019/2/23 13:30:00","CH-13",1100);
INSERT INTO flight VALUES ("PK-129","LHR","FSD","2019/3/23 12:20:00","2019/2/23 13:30:00","CH-13",1300);
INSERT INTO flight VALUES ("PK-122","LHR","FSD","2019/3/23 12:20:00","2019/2/23 13:40:00","CH-13",1300);
INSERT INTO flight VALUES ("PK-126","KHI","FSD","2019/3/23 12:20:00","2019/2/23 13:40:00","CA-13",1300);
INSERT INTO flight VALUES ("PK-127","LHR","FSD","2019/2/23 12:20:00","2019/2/23 13:40:00","CA-12",100);
INSERT INTO flight VALUES ("PK-128","LHR","FSD","2019/2/23 12:20:00","2019/2/23 13:40:00","CA-12",1200);
INSERT INTO flight VALUES ("PK-120","LHR","FSD","2019/2/23 12:20:00","2019/2/23 13:40:00","CH-12",100);
INSERT INTO flight VALUES ("PK-121","FSD","KHI","2019/2/23 13:20:00","2019/2/23 15:20:00","CH-12",2000);

INSERT INTO prime(flight_id,passenger_id) VALUES("PK-123",10);
INSERT INTO prime(flight_id,passenger_id) VALUES("PK-123",1);
INSERT INTO prime(flight_id,passenger_id) VALUES("PK-123",2);
INSERT INTO prime(flight_id,passenger_id) VALUES("PK-123",3);
INSERT INTO prime(flight_id,passenger_id) VALUES("PK-123",4);
INSERT INTO prime(flight_id,passenger_id) VALUES("PK-123",5);
INSERT INTO prime(flight_id,passenger_id) VALUES("PK-125",6);
INSERT INTO prime(flight_id,passenger_id) VALUES("PK-125",7);
INSERT INTO prime(flight_id,passenger_id) VALUES("PK-125",8);
INSERT INTO prime(flight_id,passenger_id) VALUES("PK-125",9);

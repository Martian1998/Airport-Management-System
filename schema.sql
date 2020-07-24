CREATE DATABASE airport;
use airport;

CREATE TABLE flight(
    flight_id VARCHAR(50) NOT NULL UNIQUE,
    departure_airport VARCHAR(50) NOT NULL,
    arrival_airport VARCHAR(50) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    airplane VARCHAR(50) NOT NULL,
    fair INT NOT NULL,
    PRIMARY KEY(flight_id)
);


CREATE TABLE person_prime(
    cnic BIGINT(13) NOT NULL,
    phone VARCHAR(12),
    pnationality VARCHAR(50),
    pname VARCHAR(50),
    paddress VARCHAR(100),
    PRIMARY KEY(cnic,pname)
);

CREATE TABLE passengers(
    passenger_id INT NOT NULL UNIQUE AUTO_INCREMENT,
    cnic BIGINT(13) NOT NULL,
    pname VARCHAR(50) NOT NULL,
    PRIMARY KEY(passenger_id),
    FOREIGN KEY (cnic,pname) REFERENCES person_prime(cnic,pname) ON UPDATE CASCADE ON DELETE CASCADE
    
);

create TABLE prime(
    flight_id VARCHAR(50) NOT NULL,
    passenger_id INT NOT NULL,
    ticket_id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (ticket_id),
    FOREIGN KEY (flight_id) REFERENCES flight(flight_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id) ON UPDATE CASCADE ON DELETE CASCADE
);
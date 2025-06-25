CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO users (username, password) VALUES
('admin', 'admin123'),
('user', 'user123'),
('guest', 'guest123');

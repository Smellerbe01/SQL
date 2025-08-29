DELETE FROM productos;
DELETE FROM sqlite_sequence WHERE name='productos';
DELETE FROM clientes;
DELETE FROM sqlite_sequence WHERE name='clientes';

INSERT INTO clientes (nombre, email, password) VALUES
('Ana Pérez', 'ana@example.com', 'hash_demo_1'),
('Luis Gómez', 'luis@example.com', 'hash_demo_2');

INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Camiseta Blanca', 'Algodón 100%', 39.9, 20),
('Jeans Slim', 'Azul oscuro', 119.5, 15),
('Zapatillas Runner', 'Deportivas', 199.0, 10),
('Gorra Negra', 'Talla única', 29.0, 25),
('Chaqueta de Cuero', 'Negra, talla M', 249.9, 5),
('Reloj Digital', 'Resistente al agua', 89.9, 30),
('Mochila Urbana', 'Negra, 20L', 59.9, 12),
('Auriculares Bluetooth', 'Inalámbricos', 79.9, 18),
('Smartphone X100', 'Tecnología avanzada', 999.0, 3),
('Tablet Pro', 'Pantalla 10 pulgadas', 499.0, 7);


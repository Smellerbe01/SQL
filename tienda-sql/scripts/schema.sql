PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS clientes (
  cliente_id   INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre       TEXT    NOT NULL,
  email        TEXT    NOT NULL UNIQUE,
  password     TEXT    NOT NULL,
  creado_en    DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS productos (
  producto_id  INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre       TEXT    NOT NULL,
  descripcion  TEXT,
  precio       REAL    NOT NULL CHECK(precio >= 0),
  stock        INTEGER NOT NULL CHECK(stock >= 0),
  creado_en    DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pedidos (
  pedido_id    INTEGER PRIMARY KEY AUTOINCREMENT,
  cliente_id   INTEGER NOT NULL,
  fecha        DATETIME DEFAULT CURRENT_TIMESTAMP,
  total        REAL    NOT NULL CHECK(total >= 0),
  FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

CREATE TABLE IF NOT EXISTS pedido_detalles (
  detalle_id   INTEGER PRIMARY KEY AUTOINCREMENT,
  pedido_id    INTEGER NOT NULL,
  producto_id  INTEGER NOT NULL,
  cantidad     INTEGER NOT NULL CHECK(cantidad > 0),
  subtotal     REAL    NOT NULL CHECK(subtotal >= 0),
  FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
  FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

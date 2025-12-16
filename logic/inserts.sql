# ---------------------------------------------------------------------- #
# INSERTS DE PRUEBA - RESTAURANTE
# ---------------------------------------------------------------------- #

# -----------------------------
# ROLES
# -----------------------------
INSERT INTO roles (nombre) VALUES
('ADMIN'),
('MESERO'),
('COCINA');

# -----------------------------
# SEDES
# -----------------------------
INSERT INTO sedes (direccion) VALUES
('Calle 10 #20-30'),
('Avenida Principal #45-90');

# -----------------------------
# USUARIOS
# id_rol:
# 1 = ADMIN
# 2 = MESERO
# 3 = COCINA
# -----------------------------
INSERT INTO usuarios (
    cedula, nombre_completo, activo, telefono, id_rol, password
) VALUES
('1001001001', 'Carlos Pérez', 1, '3001234567', 1, 'admin123'),
('1001001002', 'Laura Gómez', 1, '3007654321', 2, 'mesero123'),
('1001001003', 'Juan Martínez', 1, '3011112233', 3, 'cocina123');

# -----------------------------
# SEDES_USUARIOS
# -----------------------------
INSERT INTO sedes_usuarios (id_sede, id_usuario) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 2);

# -----------------------------
# SESION
# -----------------------------
INSERT INTO sesion (fecha, id_sede) VALUES
('2025-12-15', 1),
('2025-12-16', 1),
('2025-12-16', 2);

# -----------------------------
# PLATOS
# -----------------------------
INSERT INTO platos (
    nombre, descripcion, image_url, precio
) VALUES
('Hamburguesa Clásica', 'Hamburguesa con carne, queso y lechuga', 'https://img.com/hamburguesa.jpg', 18000),
('Pizza Pepperoni', 'Pizza personal con pepperoni', 'https://img.com/pizza.jpg', 22000),
('Ensalada César', 'Ensalada fresca con pollo', 'https://img.com/ensalada.jpg', 15000);

# -----------------------------
# SESION_PLATOS
# -----------------------------
INSERT INTO sesion_platos (id_sesion, id_plato, disponible) VALUES
(1, 1, 1),
(1, 2, 1),
(1, 3, 0),
(2, 1, 1),
(2, 3, 1),
(3, 2, 1);

# -----------------------------
# ORDENES
# -----------------------------
INSERT INTO ordenes (id_sesion, pagado, preparado) VALUES
(1, 1, 1),
(1, 0, 0),
(2, 1, 0);

# -----------------------------
# ORDENES_PLATOS
# -----------------------------
INSERT INTO ordenes_platos (id_orden, id_plato, cantidad) VALUES
(1, 1, 2),
(1, 3, 1),
(2, 2, 1),
(3, 1, 1),
(3, 2, 2);

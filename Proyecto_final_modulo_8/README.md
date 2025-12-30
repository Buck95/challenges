Mini Sistema de Notas Personales

Aplicación web desarrollada con **React + Vite + Tailwind CSS** y una **API REST en Node.js**, que permite a los usuarios gestionar notas personales con autenticación mediante **JWT**.

## 🚀 Funcionalidades principales

### 🔐 Autenticación
- Registro de usuarios
- Inicio de sesión
- Autenticación mediante JSON Web Tokens (JWT)
- Rutas protegidas
- Cierre de sesión (Logout)

### 🗂️ Gestión de Notas (CRUD)
- Crear notas personales
- Listar notas del usuario autenticado
- Eliminar notas
- Cada nota contiene:
  - Título
  - Contenido
  - Categoría
  - Fecha de creación

### 🏷️ Categorías
- Personal
- Trabajo
- Ideas
- Recordatorios
- Filtrado dinámico por categoría

### 🎨 Interfaz de Usuario
- Diseño responsivo con Tailwind CSS
- Tarjetas de notas con colores según categoría
- Formularios con validaciones básicas

## 🛠️ Tecnologías utilizadas

### Frontend
- React
- Vite
- React Router DOM
- Axios
- Tailwind CSS

### Backend
- Node.js
- Express
- JSON Web Token (JWT)
- bcryptjs
- CORS

## Cómo ejecutar el proyecto

Backend --> npm run server

La API se ejecuta en:

http://localhost:3000

Frontend --> npm run dev

La aplicación se ejecuta en:

http://localhost:5173


# 🤖 DOCUMENTACIÓN DEL USO DE IA

## Uso de Inteligencia Artificial en el desarrollo del proyecto

Durante el desarrollo del proyecto se utilizó Inteligencia Artificial como apoyo para optimizar y mejorar el proceso de implementación, sin sustituir la comprensión del código

### 🔹 Componentes creados o refactorizados con IA
- Componente `NoteCard.jsx` para la visualización de notas.
- Componente `FilterBar.jsx` para el filtrado por categorías.
- Middleware de rutas protegidas (`ProtectedRoute.jsx`).

### 🔹 Validaciones y lógica mejoradas con IA
- Validaciones básicas en formularios de Login y Registro.
- Lógica de filtrado dinámico de notas por categoría.
- Estructuración del CRUD en el backend.

### 🔹 Sugerencias aceptadas
- Uso de JWT para autenticación.
- Separación del cliente Axios para manejo del token.
- Diseño modular por componentes en React.

### 🔹 Sugerencias rechazadas
- Persistencia en base de datos externa, debido a que el reto solicita una solución simple.

### 🎯 Conclusión
La IA fue utilizada como herramienta de apoyo para:
- Acelerar la generación de código
- Mejorar la calidad y organización del proyecto
- Reducir errores comunes

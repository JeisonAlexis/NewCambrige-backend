# 🏫 Sistema de Paz y Salvo — NCS
# Backend · API REST

Backend del sistema de gestión de **Paz y Salvo** para el colegio *New Cambridge School*.  
Permite administrar el estado académico y administrativo de estudiantes y docentes de forma digital mediante una API REST.

---

## 🛠️ Stack Tecnológico

- Lenguaje: Python 3.12
- Framework: FastAPI 0.136.1
- Base de datos: postgreSQL 16
- ORM: SQLAlchemy 2.0.40
- Migraciones: Alembic 1.15.2
- Autenticación: python-jose + passlib
- Validación: Pydantic 2.11.1
- Generación de PDF: WeasyPrint 68.1

---

## ✅ Requisitos

python --version
git --version

---

## 🚀 Instalación y ejecución

# 1. Clonar repositorio
```bash
git clone https://github.com/Software262/NewCambrige-backend.git
cd paz-salvo-backend
```

# 2. Crear entorno virtual
```bash
py -3.12 -m venv venv        # Windows
python3.12 -m venv venv      # Linux/Mac
```

# 3. Activar entorno virtual

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

# 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

# 5. Configurar variables de entorno
```bash
cp .env.example .env
```
# 6. Ejecutar migraciones
```bash
alembic upgrade head
```
# 7. Iniciar servidor
```bash
uvicorn app.main:app --reload --port 8000

# API disponible en:
http://localhost:8000

# Documentación automática:
http://localhost:8000/docs
```
---

## 📁 Estructura del Proyecto
```bash
paz-salvo-backend/
├── app/
│   ├── main.py              # Punto de entrada de la API
│   ├── models.py            # Modelos ORM
│   ├── core/                # Configuración central (seguridad, DB, etc.)
│   ├── modules/
│   │   ├── auth/            # Autenticación y autorización
│   │   ├── usuarios/        # Gestión de usuarios
│   │   ├── estudiantes/     # Gestión de estudiantes
│   │   ├── parametrizacion/ # Configuración del sistema
│   │   ├── salon/           # Módulo salón
│   │   ├── banda/           # Módulo banda
│   │   ├── uniformes/       # Gestión de uniformes
│   │   ├── tesoreria/       # Pagos y finanzas
│   │   ├── secretaria/      # Papeleria y gestion a bajo nivel
│   │   ├── rectoria/        # Panel administrativo
│   │   └── paz_y_salvo/     # Lógica principal del sistema
│   └── shared/              # Utilidades y componentes compartidos
├── alembic/                 # Migraciones de base de datos
├── tests/                   # Pruebas
├── .env.example             # Variables de entorno de ejemplo
├── requirements.txt         # Dependencias
└── README.md
```
---

## ⚙️ Comandos útiles
```bash
# Ejecutar servidor
uvicorn app.main:app --reload --port 8000

# Crear nueva migración
alembic revision --autogenerate -m "descripcion_del_cambio"

# Aplicar migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1

# Ver historial de migraciones
alembic history
```
---

## 🔐 Autenticación

- Basada en JWT
- Manejo de contraseñas con hash seguro (passlib)
- Protección de endpoints mediante dependencias de FastAPI

---

## 📌 Buenas prácticas

- Arquitectura modular escalable
- Separación por dominios
- Uso de variables de entorno
- Migraciones versionadas con Alembic

---

## ⚠️ Flujo de trabajo

- No trabajar directamente sobre la rama `main`
- Crear ramas por feature o fix:
  - feature/nombre-funcionalidad
  - fix/nombre-error
- Usar pull requests para integración

---

## 🚧 Mejoras futuras

- Integración con PostgreSQL
- Implementación de tests automatizados
- Dockerización del proyecto
- CI/CD
- Roles y permisos más granulares

---


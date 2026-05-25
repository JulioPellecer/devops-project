from flask import Flask, jsonify, render_template_string
import os
import psycopg2
from datetime import datetime

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>DevOps Project</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
        h1 { color: #2c3e50; }
        .status { background: #2ecc71; color: white; padding: 10px 20px; border-radius: 5px; display: inline-block; }
        .info { background: #ecf0f1; padding: 15px; border-radius: 5px; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>🚀 DevOps Project - Funcionando!</h1>
    <span class="status">✅ App en línea</span>
    <div class="info">
        <p><strong>Hora del servidor:</strong> {{ hora }}</p>
        <p><strong>Versión:</strong> 1.0.0</p>
        <p><strong>Entorno:</strong> {{ entorno }}</p>
    </div>
    <h2>Endpoints disponibles</h2>
    <ul>
        <li><a href="/health">/health</a> - Estado de la aplicación</li>
        <li><a href="/api/tareas">/api/tareas</a> - Lista de tareas</li>
        <li><a href="/api/info">/api/info</a> - Información del sistema</li>
    </ul>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE,
        hora=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        entorno=os.getenv("ENVIRONMENT", "desarrollo")
    )

@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }), 200

@app.route('/api/tareas')
def tareas():
    tareas_lista = [
        {"id": 1, "nombre": "Configurar Docker", "completada": True},
        {"id": 2, "nombre": "Crear pipeline CI/CD", "completada": True},
        {"id": 3, "nombre": "Desplegar en AWS", "completada": False},
    ]
    return jsonify({"tareas": tareas_lista, "total": len(tareas_lista)})

@app.route('/api/info')
def info():
    return jsonify({
        "app": "DevOps Project",
        "version": "1.0.0",
        "ambiente": os.getenv("ENVIRONMENT", "desarrollo"),
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

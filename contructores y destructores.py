"""
Sistema de Gestión de Archivos y Recursos
Demostración de Constructores y Destructores en Python

Este programa demuestra el uso de constructores (__init__) y destructores (__del__)
a través de un sistema que gestiona archivos, conexiones y recursos.

Autor: Edwin Armijos
"""

import os
import time
from datetime import datetime


class GestorArchivos:
    """
    Clase que demuestra el uso de constructores y destructores
    para la gestión de archivos y recursos.
    """

    # Variable de clase para contar instancias
    contador_instancias = 0

    def __init__(self, nombre_archivo, modo='w'):
        """
        CONSTRUCTOR (__init__): Se ejecuta automáticamente cuando se crea una instancia

        Args:
            nombre_archivo (str): Nombre del archivo a gestionar
            modo (str): Modo de apertura del archivo ('w', 'r', 'a')
        """
        print(f"🚀 CONSTRUCTOR: Creando instancia de GestorArchivos")

        # Incrementar contador de instancias
        GestorArchivos.contador_instancias += 1
        self.id_instancia = GestorArchivos.contador_instancias

        # Inicializar atributos del objeto
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.fecha_creacion = datetime.now()
        self.archivo_abierto = False
        self.contenido_escrito = []

        # Intentar abrir el archivo
        try:
            self.archivo = open(self.nombre_archivo, self.modo)
            self.archivo_abierto = True
            print(f"   ✅ Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'")
            print(f"   📊 ID de instancia: {self.id_instancia}")
            print(f"   🕐 Creado el: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")

            # Escribir encabezado si es modo escritura
            if self.modo in ['w', 'a']:
                encabezado = f"=== Archivo creado el {self.fecha_creacion} ===\n"
                self.archivo.write(encabezado)
                self.contenido_escrito.append(encabezado)

        except Exception as e:
            print(f"   ❌ Error al abrir archivo: {e}")
            self.archivo_abierto = False

    def escribir_linea(self, texto):
        """
        Método para escribir una línea en el archivo
        """
        if self.archivo_abierto and self.modo in ['w', 'a']:
            linea = f"{datetime.now().strftime('%H:%M:%S')} - {texto}\n"
            self.archivo.write(linea)
            self.contenido_escrito.append(linea)
            print(f"   ✏️  Escrito: {texto}")
        else:
            print("   ⚠️  No se puede escribir: archivo no disponible")

    def leer_contenido(self):
        """
        Método para leer el contenido del archivo
        """
        if self.archivo_abierto and self.modo == 'r':
            self.archivo.seek(0)  # Volver al inicio
            contenido = self.archivo.read()
            print(f"   📖 Contenido del archivo:\n{contenido}")
            return contenido
        else:
            print("   ⚠️  No se puede leer: archivo no disponible para lectura")
            return None

    def obtener_info(self):
        """
        Método para obtener información de la instancia
        """
        print(f"\n📋 Información de la instancia {self.id_instancia}:")
        print(f"   📁 Archivo: {self.nombre_archivo}")
        print(f"   🔧 Modo: {self.modo}")
        print(f"   📅 Creado: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   💾 Estado: {'Abierto' if self.archivo_abierto else 'Cerrado'}")
        print(f"   📝 Líneas escritas: {len(self.contenido_escrito)}")

    def __del__(self):
        """
        DESTRUCTOR (__del__): Se ejecuta automáticamente cuando el objeto va a ser destruido

        Este método se encarga de:
        1. Cerrar el archivo si está abierto
        2. Liberar recursos
        3. Mostrar información de limpieza
        4. Decrementar el contador de instancias
        """
        print(f"\n🗑️  DESTRUCTOR: Eliminando instancia {self.id_instancia}")

        # Cerrar archivo si está abierto
        if hasattr(self, 'archivo_abierto') and self.archivo_abierto:
            try:
                # Escribir línea de cierre si es modo escritura
                if hasattr(self, 'modo') and self.modo in ['w', 'a']:
                    linea_cierre = f"=== Archivo cerrado el {datetime.now()} ===\n"
                    self.archivo.write(linea_cierre)

                self.archivo.close()
                print(f"   ✅ Archivo '{self.nombre_archivo}' cerrado correctamente")

            except Exception as e:
                print(f"   ❌ Error al cerrar archivo: {e}")

        # Mostrar estadísticas de la instancia
        if hasattr(self, 'contenido_escrito'):
            print(f"   📊 Líneas escritas en total: {len(self.contenido_escrito)}")

        # Decrementar contador
        GestorArchivos.contador_instancias -= 1
        print(f"   🔢 Instancias activas restantes: {GestorArchivos.contador_instancias}")
        print(f"   🧹 Recursos liberados para instancia {self.id_instancia}")


class ConexionBaseDatos:
    """
    Clase adicional que simula una conexión a base de datos
    para demostrar más casos de uso de constructores y destructores
    """

    def __init__(self, host="localhost", puerto=5432, usuario="admin"):
        """
        CONSTRUCTOR: Simula la conexión a una base de datos
        """
        print(f"\n🔌 CONSTRUCTOR: Estableciendo conexión a BD")

        self.host = host
        self.puerto = puerto
        self.usuario = usuario
        self.conectado = False
        self.consultas_realizadas = 0

        # Simular proceso de conexión
        print(f"   🔄 Conectando a {host}:{puerto} como {usuario}...")
        time.sleep(0.5)  # Simular tiempo de conexión

        self.conectado = True
        self.tiempo_conexion = datetime.now()
        print(f"   ✅ Conexión establecida exitosamente")
        print(f"   🕐 Conectado el: {self.tiempo_conexion.strftime('%Y-%m-%d %H:%M:%S')}")

    def ejecutar_consulta(self, consulta):
        """
        Simula la ejecución de una consulta
        """
        if self.conectado:
            self.consultas_realizadas += 1
            print(f"   🔍 Ejecutando consulta {self.consultas_realizadas}: {consulta}")
            time.sleep(0.1)  # Simular tiempo de ejecución
            print(f"   ✅ Consulta completada")
        else:
            print(f"   ❌ Error: No hay conexión a la base de datos")

    def __del__(self):
        """
        DESTRUCTOR: Cierra la conexión a la base de datos
        """
        print(f"\n🔌 DESTRUCTOR: Cerrando conexión a BD")

        if hasattr(self, 'conectado') and self.conectado:
            print(f"   🔄 Cerrando conexión a {self.host}:{self.puerto}")
            print(f"   📊 Consultas realizadas: {self.consultas_realizadas}")

            # Calcular tiempo de conexión
            if hasattr(self, 'tiempo_conexion'):
                tiempo_activo = datetime.now() - self.tiempo_conexion
                print(f"   ⏱️  Tiempo activo: {tiempo_activo.total_seconds():.2f} segundos")

            self.conectado = False
            print(f"   ✅ Conexión cerrada correctamente")

        print(f"   🧹 Recursos de BD liberados")


def demostrar_constructores_destructores():
    """
    Función principal que demuestra el uso de constructores y destructores
    """
    print("=" * 60)
    print("🎯 DEMOSTRACIÓN DE CONSTRUCTORES Y DESTRUCTORES")
    print("=" * 60)

    # 1. Crear instancias y mostrar cómo se ejecutan los constructores
    print("\n1️⃣ CREANDO INSTANCIAS (Constructores en acción)")
    print("-" * 50)

    # Crear gestor de archivos para escritura
    print("\n📝 Creando gestor de archivos para escritura:")
    gestor_escritura = GestorArchivos("datos_ejemplo.txt", "w")

    # Crear gestor de archivos para append
    print("\n📝 Creando gestor de archivos para append:")
    gestor_append = GestorArchivos("log_sistema.txt", "a")

    # Crear conexión a base de datos
    print("\n💾 Creando conexión a base de datos:")
    conexion_bd = ConexionBaseDatos("servidor.empresa.com", 3306, "desarrollo")

    # 2. Usar los objetos creados
    print("\n\n2️⃣ USANDO LOS OBJETOS CREADOS")
    print("-" * 50)

    # Escribir en archivos
    gestor_escritura.escribir_linea("Primera línea de datos")
    gestor_escritura.escribir_linea("Segunda línea de datos")
    gestor_escritura.escribir_linea("Datos procesados correctamente")

    gestor_append.escribir_linea("Sistema iniciado")
    gestor_append.escribir_linea("Usuario conectado")
    gestor_append.escribir_linea("Procesando solicitudes")

    # Ejecutar consultas en BD
    conexion_bd.ejecutar_consulta("SELECT * FROM usuarios")
    conexion_bd.ejecutar_consulta("SELECT * FROM productos WHERE activo = 1")
    conexion_bd.ejecutar_consulta("UPDATE estadisticas SET visitas = visitas + 1")

    # 3. Mostrar información de las instancias
    print("\n\n3️⃣ INFORMACIÓN DE LAS INSTANCIAS")
    print("-" * 50)

    gestor_escritura.obtener_info()
    gestor_append.obtener_info()

    print(f"\n💾 Información de conexión BD:")
    print(f"   🌐 Host: {conexion_bd.host}:{conexion_bd.puerto}")
    print(f"   👤 Usuario: {conexion_bd.usuario}")
    print(f"   🔍 Consultas realizadas: {conexion_bd.consultas_realizadas}")

    # 4. Crear un scope local para demostrar destrucción automática
    print("\n\n4️⃣ DEMOSTRACIÓN DE DESTRUCCIÓN AUTOMÁTICA")
    print("-" * 50)

    def crear_archivo_temporal():
        """
        Función que crea un archivo temporal para demostrar
        cómo se ejecuta el destructor al salir del scope
        """
        print("\n🔄 Entrando en función crear_archivo_temporal()")
        archivo_temp = GestorArchivos("archivo_temporal.txt", "w")
        archivo_temp.escribir_linea("Este archivo será destruido automáticamente")
        archivo_temp.escribir_linea("cuando salga del scope de la función")
        archivo_temp.obtener_info()
        print("🔄 Saliendo de función crear_archivo_temporal()")
        # El destructor se ejecutará automáticamente aquí

    crear_archivo_temporal()

    # 5. Esperar un momento para mostrar el estado actual
    print(f"\n\n5️⃣ ESTADO ACTUAL DEL SISTEMA")
    print("-" * 50)
    print(f"📊 Instancias activas de GestorArchivos: {GestorArchivos.contador_instancias}")

    # 6. Demostrar destrucción manual
    print("\n\n6️⃣ DESTRUCCIÓN MANUAL DE OBJETOS")
    print("-" * 50)

    print("\n🗑️  Eliminando gestor_escritura manualmente:")
    del gestor_escritura

    print("\n🗑️  Eliminando conexion_bd manualmente:")
    del conexion_bd

    print(f"\n📊 Instancias restantes: {GestorArchivos.contador_instancias}")

    # 7. El último objeto se destruirá automáticamente al final del programa
    print("\n\n7️⃣ FINALIZACIÓN DEL PROGRAMA")
    print("-" * 50)
    print("El objeto 'gestor_append' se destruirá automáticamente")
    print("cuando el programa termine (destructor automático)")

    return gestor_append  # Retornamos para que se destruya al final


# Punto de entrada principal
if __name__ == "__main__":
    print("🐍 PROGRAMA DE DEMOSTRACIÓN - CONSTRUCTORES Y DESTRUCTORES")
    print("Este programa demuestra cómo funcionan los métodos __init__ y __del__")
    print("en Python a través de ejemplos prácticos de gestión de recursos.")

    # Ejecutar demostración
    ultimo_objeto = demostrar_constructores_destructores()

    print("\n" + "=" * 60)
    print("🎉 FIN DE LA DEMOSTRACIÓN")
    print("=" * 60)
    print("\n📝 RESUMEN CONCEPTUAL:")
    print("• CONSTRUCTOR (__init__): Se ejecuta al crear una instancia")
    print("• DESTRUCTOR (__del__): Se ejecuta al destruir una instancia")
    print("• Los destructores son útiles para liberar recursos")
    print("• Python gestiona automáticamente la destrucción de objetos")
    print("• Es importante cerrar archivos y conexiones en el destructor")

    print("\n🔚 Los destructores se ejecutarán automáticamente al terminar el programa...")

    # ultimo_objeto se destruirá automáticamente aquí
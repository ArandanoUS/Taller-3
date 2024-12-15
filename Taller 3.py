import pymongo
from bson.objectid import ObjectId

# Configuración de la conexión con MongoDB
client = pymongo.MongoClient("mongodb://localhost:37021/")
db = client["recetasdb"]
collection = db["recetas"]

print(f"Database '{"recetasdb"}' and collection '{"recetas"}' have been set up.")

# Funciones de CRUD
def agregar_receta():
    """Agregar una nueva receta."""
    try:
        nombre = input("Nombre de la receta: ")
        ingredientes = input("Ingredientes (separados por comas): ")
        pasos = input("Pasos de la receta: ")

        receta = {
            "nombre": nombre,
            "ingredientes": ingredientes,
            "pasos": pasos
        }

        collection.insert_one(receta)
        print("✅ Receta agregada exitosamente.")
    except Exception as e:
        print(f"❌ Error: {e}")

def actualizar_receta():
    """Actualizar una receta existente."""
    try:
        nombre = input("Nombre de la receta a actualizar: ")
        receta = collection.find_one({"nombre": nombre})

        if receta:
            print(f"Receta encontrada:\nIngredientes: {receta['ingredientes']}\nPasos: {receta['pasos']}")
            nuevo_ingredientes = input("Nuevos ingredientes (dejar en blanco para no cambiar): ")
            nuevo_pasos = input("Nuevos pasos (dejar en blanco para no cambiar): ")

            nuevos_datos = {}
            if nuevo_ingredientes:
                nuevos_datos["ingredientes"] = nuevo_ingredientes
            if nuevo_pasos:
                nuevos_datos["pasos"] = nuevo_pasos

            if nuevos_datos:
                collection.update_one({"_id": receta["_id"]}, {"$set": nuevos_datos})
                print("✅ Receta actualizada exitosamente.")
            else:
                print("⚠️ No se realizaron cambios.")
        else:
            print("❌ No se encontró la receta especificada.")
    except Exception as e:
        print(f"❌ Error: {e}")

def eliminar_receta():
    """Eliminar una receta existente."""
    try:
        nombre = input("Nombre de la receta a eliminar: ")
        receta = collection.find_one({"nombre": nombre})

        if receta:
            collection.delete_one({"_id": receta["_id"]})
            print("✅ Receta eliminada exitosamente.")
        else:
            print("❌ No se encontró la receta especificada.")
    except Exception as e:
        print(f"❌ Error: {e}")

def ver_listado_recetas():
    """Mostrar el listado de todas las recetas."""
    try:
        recetas = list(collection.find())
        if recetas:
            print("📜 Listado de recetas:")
            for i, receta in enumerate(recetas, start=1):
                print(f"{i}. {receta['nombre']}")
        else:
            print("❌ No hay recetas disponibles.")
    except Exception as e:
        print(f"❌ Error: {e}")

def buscar_receta():
    """Buscar los detalles de una receta específica."""
    try:
        nombre = input("Nombre de la receta a buscar: ")
        receta = collection.find_one({"nombre": nombre})

        if receta:
            print(f"📖 Receta: {receta['nombre']}")
            print(f"Ingredientes: {receta['ingredientes']}")
            print(f"Pasos: {receta['pasos']}")
        else:
            print("❌ No se encontró la receta especificada.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Menú principal
def menu():
    """Mostrar el menú principal y gestionar las opciones del usuario."""
    while True:
        print("\n=== Libro de Recetas ===")
        print("1. Agregar nueva receta")
        print("2. Actualizar receta existente")
        print("3. Eliminar receta existente")
        print("4. Ver listado de recetas")
        print("5. Buscar ingredientes y pasos de receta")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_receta()
        elif opcion == "2":
            actualizar_receta()
        elif opcion == "3":
            eliminar_receta()
        elif opcion == "4":
            ver_listado_recetas()
        elif opcion == "5":
            buscar_receta()
        elif opcion == "6":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()

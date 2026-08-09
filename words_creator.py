
import json
import process_msg

def Main():
    print("""
¡Hola Este es un creador de JSON para el juego BombGame, selecciona y se tomara el txt de la carpeta!
1-Crear JSON
2-Arreglar JSON (remover palabras)
0-Exit
    """)
    menu = int(input("Selecciona una opcion: \n"))
    
    if menu == 1:
        txt = str(input("Escribe que TxT se seleccionara de la carpeta (revisa cual quieres antes): \n"))
        
        process_msg.start()
        Crear_JSON(txt)
        
        process_msg.finalizar.set()
        Main()
    elif menu == 2:
        select_json = str(input("Escribe que TxT se seleccionara de la carpeta (revisa cual quieres antes): \n"))
        
        process_msg.start()
        Arreglar_JSON(select_json)
        
        process_msg.finalizar.set()
        Main()
    

def Crear_JSON(select_txt):
    words = {}
    
    with open(f"./txt/{select_txt}.txt", "r", encoding="utf-8") as txt:
        print("\narchivo encontrado")
        for linea in txt:
            linea = linea.strip()
            for i in range(len(linea) - 1):
                pares = linea[i:i+2]
                
                if pares in words:
                    if linea not in words[pares]:
                        words[pares].add(linea)
                else:
                    words[pares] = {linea}
                
                if i < len(linea) - 2:
                    trio = linea[i:i+3]
                    if trio in words:
                        if linea not in words[trio]:
                            words[trio].add(linea)
                    else:
                        words[trio] = {linea}
    
    for key,value in words.items():
        words[key] = list(value)
    Guardar_JSON(words, select_txt)

def Guardar_JSON(JSON, select_txt):
    with open(f"./json/{select_txt}.json", "w", encoding="utf-8") as safe_json:
        json.dump(JSON, safe_json, ensure_ascii=False, indent=4)

def Arreglar_JSON(select_JSON):
    new_json = {}
    
    with open(f"./json/{select_JSON}.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        
        for key,value in datos.items():
            if len(value) > 500:
                new_json[key] = value
    
    Guardar_JSON(new_json, select_JSON)
    print(f"\n El JSON tiene un total de {len(new_json)} letras")

if __name__ == "__main__":
    Main()
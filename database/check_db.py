import sqlite3
import os

DB_PATH = "plates.db"

def check_database():
    if not os.path.exists(DB_PATH):
        print("❌ Banco de dados 'plates.db' não existe.")
        return

    print("✅ Banco de dados encontrado.")

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Verificar se a tabela existe
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='authorized_plates'
        """)
        result = cursor.fetchone()

        if result:
            print("✅ Tabela 'authorized_plates' encontrada.")
            cursor.execute("SELECT * FROM authorized_plates")
            rows = cursor.fetchall()

            if rows:
                print(f"📋 Placas cadastradas ({len(rows)}):")
                for row in rows:
                    print(f"  ID: {row[0]} | PLACA: {row[1]}")
            else:
                print("⚠️ Nenhuma placa cadastrada ainda.")
        else:
            print("❌ Tabela 'authorized_plates' não encontrada.")
            create = input("Deseja criá-la agora? (s/n): ")
            if create.lower() == "s":
                cursor.execute("""
                    CREATE TABLE authorized_plates (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        plate TEXT UNIQUE NOT NULL
                    )
                """)
                conn.commit()
                print("✅ Tabela criada com sucesso.")
        
        conn.close()

    except Exception as e:
        print(f"⚠️ Erro ao acessar o banco: {e}")

if __name__ == "__main__":
    check_database()

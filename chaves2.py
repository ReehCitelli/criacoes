import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Text, Scrollbar, VERTICAL, END
import sqlite3
from datetime import datetime


# Configuração do banco de dados
def setup_database():
    conn = sqlite3.connect('chaves.db')
    cursor = conn.cursor()

    # Criando tabela de chaves se não existir
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS chaves ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            chave TEXT NOT NULL, 
            cor TEXT NOT NULL, 
            retirado_por TEXT, 
            data_retirada TEXT, 
            data_devolucao TEXT, 
            UNIQUE(chave, cor) 
        ) 
    ''')

    # Criando tabela de histórico de eventos
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS historico ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            chave TEXT NOT NULL, 
            cor TEXT NOT NULL, 
            evento TEXT NOT NULL, 
            pessoa TEXT, 
            data_evento TEXT NOT NULL 
        ) 
    ''')

    # Criando 15 chaves para cada cor
    for cor in ["green", "blue", "orange"]:
        for chave_num in range(1, 16):
            chave_nome = f"Chave {chave_num:02d}"
            cursor.execute(''' 
                INSERT OR IGNORE INTO chaves (chave, cor) 
                VALUES (?, ?) 
            ''', (chave_nome, cor))

    conn.commit()
    conn.close()


# Função para resetar o estado das chaves
def resetar_estado_chaves():
    conn = sqlite3.connect('chaves.db')
    cursor = conn.cursor()
    cursor.execute(''' 
        UPDATE chaves 
        SET retirado_por = NULL, data_retirada = NULL, data_devolucao = NULL 
    ''')
    # Limpa o histórico de eventos
    cursor.execute('DELETE FROM historico')
    conn.commit()
    conn.close()
    messagebox.showinfo("Resetar Estado", "Todas as chaves foram resetadas para disponíveis.")

    # Atualiza a cor dos botões para indicar que as chaves estão disponíveis
    for botao in botoes:
        botao.config(bg=botao.original_color, fg='white')

    # Atualiza o relatório de chaves em uso
    atualizar_relatorio_em_uso()


# Funções principais da interface gráfica
def registrar_evento(chave_id, chave_nome, cor):
    conn = sqlite3.connect('chaves.db')
    cursor = conn.cursor()

    # Seleciona a chave específica com base no nome e na cor
    cursor.execute('SELECT retirado_por FROM chaves WHERE chave = ? AND cor = ?', (chave_nome, cor))
    result = cursor.fetchone()

    if result and result[0]:  # Se a chave já foi retirada
        cursor.execute(''' 
            UPDATE chaves 
            SET retirado_por = NULL, data_retirada = NULL, data_devolucao = ? 
            WHERE chave = ? AND cor = ?
        ''', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), chave_nome, cor))
        cursor.execute(''' 
            INSERT INTO historico (chave, cor, evento, data_evento) 
            VALUES (?, ?, 'Devolução', ?) 
        ''', (chave_nome, cor, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        messagebox.showinfo("Devolução", f"Chave {chave_nome} devolvida com sucesso.")
        botoes[chave_id].config(bg=botoes[chave_id].original_color, fg='white')
    else:  # Se a chave está disponível para retirada
        nome = simpledialog.askstring("Retirada de Chave", f"Quem está retirando a chave {chave_nome}?")
        if nome:
            cursor.execute(''' 
                UPDATE chaves 
                SET retirado_por = ?, data_retirada = ?, data_devolucao = NULL 
                WHERE chave = ? AND cor = ?
            ''', (nome, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), chave_nome, cor))
            cursor.execute(''' 
                INSERT INTO historico (chave, cor, evento, pessoa, data_evento) 
                VALUES (?, ?, 'Retirada', ?, ?) 
            ''', (chave_nome, cor, nome, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            messagebox.showinfo("Retirada", f"Chave {chave_nome} retirada por {nome}.")
            botoes[chave_id].config(bg='white', fg='black')

    conn.commit()
    conn.close()

    # Atualiza o relatório de chaves em uso
    atualizar_relatorio_em_uso()


def create_buttons(root, color, start_row, botoes):
    frame = tk.Frame(root)
    frame.grid(row=start_row, column=0, columnspan=5, padx=50)  # Adiciona margem à esquerda

    for chave_num in range(1, 16):
        chave_nome = f"Chave {chave_num:02d}"
        button_index = len(botoes)
        button = tk.Button(frame, text=chave_nome, bg=color, fg='white', width=10,
                           command=lambda i=button_index, chave_nome=chave_nome: registrar_evento(i, chave_nome, color),
                           highlightbackground='black', highlightthickness=2)
        button.original_color = color
        button.grid(row=(chave_num - 1) // 5, column=(chave_num - 1) % 5, padx=2, pady=2)
        botoes.append(button)



def atualizar_relatorio_em_uso():
    conn = sqlite3.connect('chaves.db')
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT chave, cor, retirado_por, data_retirada FROM chaves 
        WHERE retirado_por IS NOT NULL 
    ''')
    rows = cursor.fetchall()
    conn.close()

    relatorio_em_uso.delete(1.0, END)
    if not rows:
        relatorio_em_uso.insert(END, "Nenhuma chave está em uso no momento.")
    else:
        for row in rows:
            chave, cor, retirado_por, data_retirada = row
            relatorio_em_uso.insert(END, f"{chave} (Cor: {cor}) retirada por {retirado_por} em {data_retirada}\n")


def gerar_relatorio():
    conn = sqlite3.connect('chaves.db')
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT chave, cor, evento, pessoa, data_evento FROM historico 
        ORDER BY chave, data_evento 
    ''')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        messagebox.showinfo("Relatório de Chaves Retiradas", "Nenhuma chave foi retirada ou devolvida.")
        return

    relatorio_window = Toplevel()
    relatorio_window.title("Relatório de Chaves Retiradas e Devolvidas")
    relatorio_window.geometry("500x400")  # Define o tamanho da janela do relatório

    text_area = Text(relatorio_window, wrap='word', width=80, height=20)
    scroll_bar = Scrollbar(relatorio_window, orient=VERTICAL, command=text_area.yview)
    text_area.configure(yscrollcommand=scroll_bar.set)

    text_area.pack(side='left', fill='both', expand=True)
    scroll_bar.pack(side='right', fill='y')

    relatorio = "Relatório de Chaves Retiradas e Devolvidas:\n\n"
    chave_atual = None
    for row in rows:
        chave, cor, evento, pessoa, data_evento = row
        if chave != chave_atual:
            if chave_atual is not None:
                relatorio += "\n"
            relatorio += f"Chave {chave} (Cor: {cor}):\n"
            chave_atual = chave
        pessoa_info = f" por {pessoa}" if pessoa else ""
        relatorio += f"  - {evento}{pessoa_info} em {data_evento}\n"

    text_area.insert(END, relatorio)
    text_area.configure(state='disabled')


# Função principal
def main():
    setup_database()

    root = tk.Tk()
    root.title("Quadro de Chaves")

    # Ajusta o tamanho da janela principal para acomodar os botões sem sobreposição
    root.geometry("600x500")

    # Configura a grid para permitir redimensionamento
    for i in range(5):
        root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(8, weight=1)

    global botoes
    botoes = []

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    menu_bar.add_command(label="Gerar Relatório de Chaves Retiradas e Devolvidas", command=gerar_relatorio)
    menu_bar.add_command(label="Resetar Estado das Chaves", command=resetar_estado_chaves)

    create_buttons(root, "green", 0, botoes)
    create_buttons(root, "blue", 3, botoes)
    create_buttons(root, "orange", 6, botoes)

    # Adiciona a área de texto para o relatório de chaves em uso
    global relatorio_em_uso
    relatorio_em_uso = Text(root, height=5, wrap='word')
    relatorio_em_uso.grid(row=8, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

    # Adiciona um rótulo para direitos autorais
    label_direitos = tk.Label(root, text="Desenvolvido por @ReehCitelli com IA Monica", anchor='center')
    label_direitos.grid(row=9, column=0, columnspan=5, sticky='s', padx=5, pady=5)

    atualizar_relatorio_em_uso()
    root.mainloop()


if __name__ == "__main__":
    main()

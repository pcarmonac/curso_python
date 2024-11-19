import random
import os
from time import sleep

class Ship:
    def __init__(self, name, size):
        """
        Inicializa un barco con su nombre y tamaño
        Args:
            name (str): Nombre del barco
            size (int): Tamaño del barco en casillas
        """
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, start_row, start_col, direction, board):
        """
        Intenta colocar el barco en el tablero
        Args:
            start_row (int): Fila inicial
            start_col (int): Columna inicial
            direction (str): Dirección ('H' horizontal o 'V' vertical)
            board (list): Tablero de juego
        Returns:
            bool: True si el barco se colocó exitosamente, False en caso contrario
        """
        positions = []
        if direction == 'H':
            if start_col + self.size > len(board[0]):
                return False
            for i in range(self.size):
                if board[start_row][start_col + i] != '~':
                    return False
                positions.append((start_row, start_col + i))
        elif direction == 'V':
            if start_row + self.size > len(board):
                return False
            for i in range(self.size):
                if board[start_row + i][start_col] != '~':
                    return False
                positions.append((start_row + i, start_col))
        else:
            return False
        
        for pos in positions:
            board[pos[0]][pos[1]] = self.name[0]
        self.positions = positions
        return True

    def hit(self):
        """Registra un impacto al barco y verifica si fue hundido"""
        self.hits += 1
        return self.hits == self.size

class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destructor', 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarino', 3)

class Battleship(Ship):
    def __init__(self):
        super().__init__('Acorazado', 4)

class Player:
    def __init__(self, name=""):
        self.name = name or self.get_player_name()
        self.board = [['~' for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.hits = [['~' for _ in range(10)] for _ in range(10)]
        self.score = 0
        self.hits_count = 0
        self.ships_sunk = 0

    def get_player_name(self):
        """Solicita y valida el nombre del jugador"""
        while True:
            name = input("\n👤 Ingresa tu nombre (mínimo 3 caracteres): ").strip()
            if len(name) >= 3:
                return name
            print("❌ El nombre debe tener al menos 3 caracteres.")
            sleep(1)

    def clear_screen(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_board(self, board):
        """
        Muestra el tablero con formato mejorado y distinción de barcos
        Args:
            board (list): Tablero a mostrar
        """
        print("\n    0 1 2 3 4 5 6 7 8 9")
        print("   " + "─" * 21)
        
        for i, row in enumerate(board):
            formatted_row = []
            for cell in row:
                if cell == '~':  # Agua
                    formatted_row.append('🌊')
                elif cell == 'X':  # Disparo fallido
                    formatted_row.append('❌')
                elif cell == 'T':  # Impacto
                    formatted_row.append('💥')
                elif cell == 'D':  # Destructor
                    formatted_row.append('⛴️')
                elif cell == 'S':  # Submarino
                    formatted_row.append('🚤')
                elif cell == 'A':  # Acorazado
                    formatted_row.append('🚢')
                else:
                    formatted_row.append(cell)
            print(f"{i:2d} │ {' '.join(formatted_row)}")
        print()

    def print_score(self):
        """Muestra la información de puntuación"""
        print("\n┌────────── Puntuación ───────────┐")
        print(f"│ Puntos totales: {self.score:>14} │")
        print(f"│ Impactos:  {self.hits_count:>19} │")
        print(f"│ Barcos hundidos: {self.ships_sunk:>13} │")
        print("└────────────────────────────────┘")

    def print_game_boards(self, opponent):
        """
        Muestra los tableros del jugador y sus ataques lado a lado con puntuación
        Args:
            opponent (Player): Jugador oponente
        """
        self.clear_screen()
        print(f"\n{self.name} - Tablero de Barcos")
        print("\nLeyenda de barcos:")
        print("⛴️ - Destructor (2 casillas)")
        print("🚤 - Submarino (3 casillas)")
        print("🚢 - Acorazado (4 casillas)")
        self.print_board(self.board)
        self.print_score()
        print(f"\n{self.name} - Tablero de Ataques")
        self.print_board(self.hits)

    def place_ships(self):
        """Permite al jugador colocar sus barcos en el tablero"""
        ships = [Destroyer(), Submarine(), Battleship()]
        for ship in ships:
            while True:
                self.print_game_boards(None)
                print(f"\n{self.name}, coloca tu {ship.name} (tamaño: {ship.size})")
                print("Formato: fila columna dirección")
                print("Ejemplo: 3 4 H (para horizontal) o 3 4 V (para vertical)")
                
                try:
                    row, col, direction = input("Ingresa la posición (fila columna dirección): ").split()
                    row, col = int(row), int(col)
                    direction = direction.upper()
                    
                    if 0 <= row < 10 and 0 <= col < 10 and direction in ['H', 'V']:
                        if ship.place_ship(row, col, direction, self.board):
                            self.ships.append(ship)
                            break
                        else:
                            print("\n❌ No se puede colocar el barco en esa posición.")
                            sleep(2)
                    else:
                        print("\n❌ Posición no válida. Debe estar entre 0 y 9.")
                        sleep(2)
                except ValueError:
                    print("\n❌ Entrada inválida. Usa el formato: fila columna dirección")
                    sleep(2)

    def attack(self, opponent):
        """
        Realiza un ataque al oponente y actualiza la puntuación
        Args:
            opponent (Player): Jugador oponente
        """
        while True:
            self.print_game_boards(opponent)
            print(f"\n{self.name}, elige una posición para atacar.")
            try:
                row, col = map(int, input("Ingresa la posición (fila columna): ").split())
                if 0 <= row < 10 and 0 <= col < 10:
                    if opponent.board[row][col] == '~':
                        print("\n💦 ¡Agua!")
                        self.hits[row][col] = 'X'
                        opponent.board[row][col] = 'X'
                        sleep(1)
                        break
                    elif opponent.board[row][col] != 'X' and opponent.board[row][col] != 'T':
                        print("\n💥 ¡Impacto!")
                        self.hits[row][col] = 'T'
                        self.hits_count += 1
                        self.score += 1  # Punto por impacto
                        for ship in opponent.ships:
                            if (row, col) in ship.positions:
                                if ship.hit():
                                    print(f"🎯 ¡Hundido! Has hundido el {ship.name}!")
                                    self.ships_sunk += 1
                                    self.score += 2  # Puntos extra por hundimiento
                                break
                        opponent.board[row][col] = 'T'
                        sleep(1)
                        break
                    else:
                        print("\n❌ Ya has atacado esta posición. Intenta de nuevo.")
                        sleep(1)
                else:
                    print("\n❌ Posición no válida. Debe estar entre 0 y 9.")
                    sleep(1)
            except ValueError:
                print("\n❌ Entrada inválida. Usa el formato: fila columna")
                sleep(1)

    def all_ships_sunk(self):
        """Verifica si todos los barcos del jugador han sido hundidos"""
        return all(ship.hits == ship.size for ship in self.ships)
class Computer(Player):
    def __init__(self):
        super().__init__("Computadora")
        self.last_hit = None
        self.potential_targets = []
        self.hunt_mode = False
        self.successful_hits = []
        self.last_hit_direction = None

    def get_adjacent_cells(self, row, col):
        """Obtiene las celdas adyacentes válidas"""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if self.last_hit_direction:
            directions = [self.last_hit_direction,
                        (-self.last_hit_direction[0], -self.last_hit_direction[1])] + \
                       [d for d in directions if d != self.last_hit_direction]

        return [(row + dr, col + dc) for dr, dc in directions 
                if 0 <= row + dr < 10 and 0 <= col + dc < 10]

    def get_smart_target(self, opponent_board):
        """Determina el siguiente objetivo usando estrategia"""
        if self.successful_hits:
            last_hit = self.successful_hits[-1]
            if len(self.successful_hits) >= 2:
                prev_hit = self.successful_hits[-2]
                if last_hit[0] == prev_hit[0]:
                    self.last_hit_direction = (0, 1 if last_hit[1] > prev_hit[1] else -1)
                elif last_hit[1] == prev_hit[1]:
                    self.last_hit_direction = (1 if last_hit[0] > prev_hit[0] else -1, 0)

            adjacent = self.get_adjacent_cells(*last_hit)
            valid_targets = [(r, c) for r, c in adjacent 
                           if opponent_board[r][c] == '~']
            if valid_targets:
                return valid_targets[0]

        # Modo búsqueda con patrón de tablero de ajedrez
        empty_cells = [(r, c) for r in range(10) for c in range(10)
                      if opponent_board[r][c] == '~' and (r + c) % 2 == 0]
        if empty_cells:
            return random.choice(empty_cells)

        # Cualquier celda vacía
        empty_cells = [(r, c) for r in range(10) for c in range(10)
                      if opponent_board[r][c] == '~']
        return random.choice(empty_cells) if empty_cells else None

    def place_ships(self):
        """Coloca los barcos de manera estratégica"""
        ships = [Battleship(), Submarine(), Destroyer()]
        for ship in ships:
            while True:
                if ship.size > 2:
                    start_row = random.choice([0, 1, 8, 9] if random.random() < 0.7 else range(10))
                    start_col = random.choice([0, 1, 8, 9] if random.random() < 0.7 else range(10))
                else:
                    start_row = random.randint(0, 9)
                    start_col = random.randint(0, 9)
                
                direction = random.choice(['H', 'V'])
                if ship.place_ship(start_row, start_col, direction, self.board):
                    self.ships.append(ship)
                    break

    def attack(self, opponent):
        """Realiza un ataque inteligente"""
        self.print_game_boards(opponent)
        print("\n🤖 Turno de la Computadora...")
        sleep(1)

        target = self.get_smart_target(opponent.board)
        if not target:
            return

        row, col = target
        if opponent.board[row][col] == '~':
            print(f"\n💦 La computadora ataca ({row}, {col}) - ¡Agua!")
            self.hits[row][col] = 'X'
            opponent.board[row][col] = 'X'
            self.hunt_mode = False
            sleep(1)
        else:
            print(f"\n💥 La computadora ataca ({row}, {col}) - ¡Impacto!")
            self.hits[row][col] = 'T'
            opponent.board[row][col] = 'T'
            self.hits_count += 1
            self.score += 1
            self.successful_hits.append((row, col))
            self.hunt_mode = True
            
            for ship in opponent.ships:
                if (row, col) in ship.positions:
                    if ship.hit():
                        print(f"🎯 ¡La computadora ha hundido tu {ship.name}!")
                        self.ships_sunk += 1
                        self.score += 2
                        self.successful_hits = []
                        self.hunt_mode = False
                        self.last_hit_direction = None
                    break
            sleep(1)

class BattleshipGame:
    def __init__(self):
        self.player1 = None
        self.player2 = None

    def get_game_mode(self):
        """Permite elegir el modo de juego"""
        while True:
            print("\n🎮 Selecciona el modo de juego:")
            print("1. Jugador vs Computadora")
            print("2. Jugador vs Jugador")
            try:
                choice = int(input("\nElige una opción (1-2): "))
                if choice in [1, 2]:
                    return choice == 2
                print("❌ Opción no válida. Elige 1 o 2.")
            except ValueError:
                print("❌ Por favor, ingresa un número válido.")
            sleep(1)

    def show_welcome(self):
        """Muestra la pantalla de bienvenida"""
        if self.player1:
            self.player1.clear_screen()
        print("""
╔══════════════════════════════════════╗
║         BATALLA NAVAL v3.0           ║
╚══════════════════════════════════════╝
        
🚢 Instrucciones:
1. Coloca tus barcos en el tablero
2. Ataca por turnos las posiciones enemigas
3. Hunde todos los barcos enemigos para ganar

Puntuación:
- 1 punto por cada impacto
- 2 puntos extra por hundir un barco

Símbolos:
🌊 - Agua
⛴️ - Destructor
🚤 - Submarino
🚢 - Acorazado
❌ - Disparo fallido
💥 - Impacto

Presiona ENTER para comenzar...""")
        input()

    def show_final_score(self, winner, loser):
        """Muestra el resumen final de la partida"""
        print("\n╔═════════════════════════════════════╗")
        print("║           FIN DEL JUEGO            ║")
        print("╚═════════════════════════════════════╝")
        print(f"\n🏆 ¡{winner.name} ha ganado la partida!")
        print("\nEstadísticas finales:")
        print(f"\n{winner.name}:")
        print(f"• Puntuación total: {winner.score}")
        print(f"• Impactos: {winner.hits_count}")
        print(f"• Barcos hundidos: {winner.ships_sunk}")
        print(f"\n{loser.name}:")
        print(f"• Puntuación total: {loser.score}")
        print(f"• Impactos: {loser.hits_count}")
        print(f"• Barcos hundidos: {loser.ships_sunk}")
        
    def play(self):
        """Inicia y controla el flujo del juego"""
        try:
            self.show_welcome()
            
            is_pvp = self.get_game_mode()
            self.player1 = Player()
            self.player2 = Player() if is_pvp else Computer()
            
            print("\n🎮 Preparando el juego...")
            sleep(1)
            
            print(f"\n⚓ {self.player1.name}, coloca tus barcos.")
            self.player1.place_ships()
            
            if is_pvp:
                print(f"\n⚓ {self.player2.name}, coloca tus barcos.")
                self.player2.place_ships()
            else:
                print("\n⚙️ La computadora está colocando sus barcos...")
                self.player2.place_ships()
                sleep(1)

            current_player = self.player1
            opponent = self.player2

            while True:
                current_player.attack(opponent)
                if opponent.all_ships_sunk():
                    current_player.print_game_boards(opponent)
                    self.show_final_score(current_player, opponent)
                    break
                current_player, opponent = opponent, current_player

        except KeyboardInterrupt:
            print("\n\n👋 ¡Juego interrumpido! Gracias por jugar.")
        except Exception as e:
            print(f"\n❌ Ha ocurrido un error: {e}")
            print("Por favor, inténtalo de nuevo.")

if __name__ == "__main__":
    while True:
        try:
            game = BattleshipGame()
            game.play()
            
            while True:
                try:
                    play_again = input("\n¿Quieres jugar otra partida? (s/n): ").lower()
                    if play_again in ['s', 'n']:
                        break
                    print("❌ Por favor, responde 's' para sí o 'n' para no.")
                except KeyboardInterrupt:
                    play_again = 'n'
                    break
            
            if play_again == 'n':
                print("\n👋 ¡Gracias por jugar! ¡Hasta la próxima!")
                break

        except KeyboardInterrupt:
            print("\n\n👋 ¡Gracias por jugar! Hasta la próxima.")
            break
        except Exception as e:
            print(f"\n❌ Ha ocurrido un error: {e}")
            print("Por favor, inténtalo de nuevo.")
            sleep(2)
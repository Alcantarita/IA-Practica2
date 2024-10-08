#Aldo Alcantara Martinez  Boleta:2019630578
#Grupo: 6CV3

class Stack:
    """Implementación simple de una pila (stack)"""
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def is_empty(self):
        return len(self.stack) == 0


def get_neighbors(state, last_move=None):
    """Genera los estados vecinos para un estado 1x4 donde todos los números pueden moverse"""
    neighbors = []
    length = len(state)
    
    # Todos los números pueden moverse a la izquierda o a la derecha
    for i in range(length):
        # Evitar que se repita el último movimiento
        if last_move == (i, i-1) or last_move == (i, i+1):
            continue
        
        if i > 0:  # Mover el número a la izquierda
            new_state = list(state)
            new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
            neighbors.append((tuple(new_state), (i, i-1)))  # Guardar movimiento
        
        if i < length - 1:  # Mover el número a la derecha
            new_state = list(state)
            new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
            neighbors.append((tuple(new_state), (i, i+1)))  # Guardar movimiento
    
    return neighbors


def dfs_4_puzzle(start_state, goal_state):
    """Implementación de DFS para resolver el puzzle 1x4 sin espacios"""
    stack = Stack()
    stack.push((start_state, [], None))  # Estado inicial, camino y último movimiento
    visited = set()
    
    while not stack.is_empty():
        current_state, path, last_move = stack.pop()
        
        # Si ya hemos visitado este estado, lo saltamos
        if current_state in visited:
            continue
        
        # Marcar el estado como visitado
        visited.add(current_state)
        
        # Comprobar si hemos alcanzado el objetivo
        if current_state == goal_state:
            return path + [current_state]  # Devolver el camino completo
        
        # Obtener los estados vecinos y añadirlos a la pila, evitando movimientos redundantes
        for neighbor, move in get_neighbors(current_state, last_move):
            if neighbor not in visited:
                stack.push((neighbor, path + [current_state], move))
    
    return None  # Si no se encuentra solución


if __name__ == "__main__":
    # Estado inicial y objetivo del puzzle 1x4 sin espacio en blanco
    initial_state = (2, 4, 1, 3)  # Los números del 1 al 4
    goal_state = (1, 2, 3, 4)  # Estado final que queremos alcanzar
    
    solution = dfs_4_puzzle(initial_state, goal_state)
    
    if solution:
        print("Solución encontrada:")
        for step in solution:
            print(step)
    else:
        print("No se encontró solución.")

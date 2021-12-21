import rubik
import util
import sys

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    Assumes the rubik.quarter_twists move set.
    """
    print()
    print(f"shortest_path: start: {start}")
    print(f"shortest_path: end: {end}")    

    print()
    for movimiento in rubik.quarter_twists:
        estado = rubik.perm_apply(movimiento,  end)
        print(f"movimiento: {rubik.quarter_twists_names[movimiento]} estado: {estado}")

    path = []
    inicio = util.Node(start, None, None)
    print(f"inicio: {inicio.state}, {inicio.parent}, {inicio.action}")
    frontierFIFO = util.QueueFrontier()
    frontierFIFO.add(inicio)
    explorados = []

    print(f"frontierFIFO {frontierFIFO}")
    print(f"explorados {explorados}")
    print(f"path {path}")

    while frontierFIFO:
        nodo = frontierFIFO.remove()
        print(f"nodo {nodo.state}, {nodo.parent}, {nodo.action}")
        print(rubik.perm_to_string(end))
        if nodo.state == rubik.perm_to_string(end):
            print()
            print(f"Encontró la solución!!")
            print()
            actions = []
            cells = []
            while nodo.parent is not None:
                actions.append(nodo.action)
                cells.append(nodo.state)
                dupla = (nodo.action, nodo.state)
                path.append(dupla)
                nodo = nodo.parent
            actions.reverse()
            cells.reverse()
            path.reverse()
            return path

        try:
            explorados.append(nodo.state)
            print(f"explorados 2 {explorados}")
            for action, state in next_positions(nodo.state):
                print(f"action: {action}, state{state}")
                if not frontierFIFO.contains_state(state) and state not in explorados:
                    print(f"if not frontierFIFO.contains_state(state) and state not in explorados")
                    child = util.Node(state=state, parent=nodo, action=action)
                    frontierFIFO.add(child)
        except Exception as e:
            print(e.args)
        
    return None

# Saludos desde github, website

def next_positions(position):
    siguientes = set()
    for movimiento in rubik.quarter_twists:
        print(f"movimiento: {rubik.quarter_twists_names[movimiento]}  ")
        next = rubik.perm_apply(movimiento, position)
        sNext = rubik.perm_to_string(next)
        print(f"next: {next}")
        print(f"sNext: {sNext}")
        tupla =(rubik.quarter_twists_names[movimiento], sNext)
        try:
            siguientes.add(tupla)
        except Exception as e:
            print(e.args)
            pass
    print(f"siguientes: {siguientes}")
    return siguientes

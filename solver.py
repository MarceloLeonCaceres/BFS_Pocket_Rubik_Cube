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
                                                                                       
    path = []
    inicio = util.Node(start, None, None)
    print(f"Nodo inicio: {inicio.state}, {inicio.parent}, {inicio.action}")
    frontierFIFO = util.QueueFrontier()
    frontierFIFO.add(inicio)
    explorados = []

    print()
    print(f"frontierFIFO {frontierFIFO}")
    print(f"explorados {explorados}")
    print(f"path {path}")
    counter = 0
    SuperCounter = 0
    print()

    # path.append(rubik.Ui)
    # path.append(rubik.Fi)
    # return path

    while frontierFIFO:
        nodo = frontierFIFO.remove()
        
        SuperCounter += 1
        print()
        print(f"SuperCounter {SuperCounter}")
        print(f"nodo {nodo.state}, parent: {nodo.parent}, action: {nodo.action}")
        print(f"end: (string) {rubik.perm_to_string(end)}")
        if SuperCounter == 41:
            return None
        if nodo.state == end or tuple(nodo.state) == tuple(end):
            print()
            print(f"Encontro la solucion!!")            
            # print(f"nodo.state == end {nodo.state == end}")
            # print(f"tuple(nodo.state) == tuple(end) {tuple(nodo.state) == tuple(end)}")
            print()
            actions = []
            cells = []
            while nodo.parent is not None:
                actions.append(rubik.movimientos[nodo.action])
                cells.append(nodo.state)
                dupla = (nodo.action, nodo.state)
                path.append(dupla)
                nodo = nodo.parent
            actions.reverse()
            cells.reverse()
            path.reverse()
            return actions

        try:
            explorados.append(nodo.state)
            print(f"explora2 {explorados}")
            for action, state in next_positions(nodo.state):
                print()
                counter += 1
                print(f"counter {counter}: ")
                print(f"action: {action}, state{state}")
                if counter == 41:
                    return None
                if state in explorados:
                    print(f"Este ya esta explorado: {state}")
                elif frontierFIFO.contains_state(state): 
                    print(f"FrontierFIFO: {state}")
                if not frontierFIFO.contains_state(state) and state not in explorados:
                    print(f"if not frontierFIFO.contains_state(state) ... len = {frontierFIFO.len()}")
                    child = util.Node(state=state, parent=nodo, action=action)
                    print(f"child.state = {child.state} child.parent = {child.parent.state} child.action = {child.action}")
                    frontierFIFO.add(child)
                print()
        except Exception as e:
            print(e.args)
        
    return None

# Saludos desde github, website
# Ahora estos saludos (linea 67 y siguientes) vienen del branch pcOficina
# Los saludos de la línea 66 eran del branch master

def next_positions(position):
    siguientes = set()
    print()
    print("Next_positions: Inicio")
    print(f"position: {position}")
    for movimiento in rubik.quarter_twists:
        print(f"movimiento: {rubik.quarter_twists_names[movimiento]}  ")
        next = rubik.perm_apply(movimiento, position)
        sNext = rubik.perm_to_string(next)
        tupleNext = tuple(next)        
        print(f"tupleNext: {tupleNext}")        
        tupla = (rubik.quarter_twists_names[movimiento], tupleNext)        
        try:            
            siguientes.add(tupla)
        except Exception as e:
            print(e.args)
            pass
    print(f"siguientes: len()= {len(siguientes)} elements: {siguientes}")
    print("Next_positions: Fin")
    print()
    return siguientes

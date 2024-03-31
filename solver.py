import rubik
import util
import sys
from sortedcontainers import SortedList
import utilEstado

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    Assumes the rubik.quarter_twists move set.
    """
    print()
    print(f"shortest_path: sta: {start}")
    print(f"shortest_path: end: {end}")    
    print()                                                                                              
                                                                                       
    path = []
    inicio = util.Node(start, None, None)
    print(f"Nodo inicio: {inicio.state}, {inicio.parent}, {inicio.action}")
    frontierFIFO = util.QueueFrontier()
    frontierFIFO.add(inicio)
    explorados = SortedList()

    pathRegreso = []
    fin = util.Node(end, None, None)
    print(f"Nodo fin: {fin.state}, {fin.parent}, {fin.action}")
    frontierRegreso = util.QueueFrontier()
    frontierRegreso.add(fin)
    exploradosRegreso = SortedList()

    print()
    print(f"frontierFIFO {frontierFIFO}")
    print(f"explorados {explorados}")
    print(f"path {path}")
    counter = 0
    SuperCounter = 0
    print()

    while frontierFIFO:
        nodo = frontierFIFO.remove()        

        SuperCounter += 1
        print()
        print(f"SuperCounter {SuperCounter}")
        if SuperCounter == 6001:
            print(f"explorados: {explorados.len()}     frontier ida: {frontierFIFO.len()}")
            print(f"explorados Regreso: {exploradosRegreso.len()}     frontier regreso: {frontierRegreso.len()}")
            return None
        if frontierRegreso.contains_state(nodo.state):
            print()
            print(f"Encontro la solucion!!")            
            print(f"nodo.state: {nodo.state}")
            print(f"nodo.action: {nodo.action}")
            print()
            actions = []
            cells = []
            estadoComun = nodo.state
            while nodo.parent is not None:
                actions.append(rubik.movimientos[nodo.action])
                cells.append(nodo.state)
                dupla = (nodo.action, nodo.state)
                path.append(dupla)
                nodo = nodo.parent
            actions.reverse()
            cells.reverse()
            path.reverse()
            print(f"actions {actions}")
            nodoRegreso = frontierRegreso.retorna_nodo(estadoComun)
            while nodoRegreso.parent is not None:
                actions.append(rubik.movimientos[rubik.movimiento_inverso(nodoRegreso.action)])
                cells.append(nodoRegreso.parent.state)
                dupla = (rubik.movimiento_inverso(nodoRegreso.action), nodoRegreso.parent.state)
                path.append(dupla)
                nodoRegreso = nodoRegreso.parent   
            return actions

        try:
            explorados.add(utilEstado.Estado(nodo.state))
            for action, state in next_positions(nodo.state):
                print()
                counter += 1
                if counter == 16:
                    print()
                if counter == 20001:
                    return None
                if not frontierFIFO.contains_state(state) and utilEstado.Estado(state) not in explorados:
                    child = util.Node(state=state, parent=nodo, action=action)
                    frontierFIFO.add(child)
                print()
        except Exception as e:
            print(e.args)
        
        nodoRegreso = frontierRegreso.remove()
        if frontierFIFO.contains_state(nodoRegreso.state):
            print()
            print(f"Encontro la solucion al regreso!!")              
            actions = []
            cells = []
            estadoComun = nodoRegreso.state
            nodo = frontierFIFO.retorna_nodo(estadoComun)
            while nodo.parent is not None:
                actions.append(rubik.movimientos[nodo.action])
                cells.append(nodo.state)
                dupla = (nodo.action, nodo.state)
                path.append(dupla)
                nodo = nodo.parent
            actions.reverse()
            cells.reverse()
            path.reverse()
            nodoRegreso = frontierRegreso.retorna_nodo(estadoComun)
            if nodoRegreso is not None:
                while nodoRegreso.parent is not None:
                    actions.append(rubik.movimientos[rubik.movimiento_inverso(nodoRegreso.action)])
                    cells.append(nodoRegreso.parent.state)
                    dupla = (rubik.movimiento_inverso(nodoRegreso.action), nodoRegreso.parent.state)
                    path.append(dupla)
                    nodoRegreso = nodoRegreso.parent            
            return actions
        
        try:
            exploradosRegreso.add(utilEstado.Estado(nodoRegreso.state))
            for action, state in next_positions(nodoRegreso.state):
                print()
                counter += 1
                if counter == 16:
                    print()
                if not frontierRegreso.contains_state(state) and utilEstado.Estado(state) not in exploradosRegreso:
                    child = util.Node(state=state, parent=nodoRegreso, action=action)
                    frontierRegreso.add(child)
                print()
        except Exception as e:
            print(e.args)
    return None


def next_positions(position):
    siguientes = set()
    for movimiento in rubik.quarter_twists:
        next = rubik.perm_apply(movimiento, position)
        sNext = rubik.perm_to_string(next)
        tupleNext = tuple(next)        
        tupla = (rubik.quarter_twists_names[movimiento], tupleNext)        
        try:            
            siguientes.add(tupla)
        except Exception as e:
            print(e.args)
            pass

    return siguientes

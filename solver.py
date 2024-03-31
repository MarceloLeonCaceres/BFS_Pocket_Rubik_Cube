import rubik
import util
import sys
from sortedcontainers import SortedList
import utilEstado
import os
import time

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    Assumes the rubik.quarter_twists move set.
    """

    os.system('cls')
    tic = time.perf_counter()
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
    counter = 0
    SuperCounter = 0

    while frontierFIFO:        
        SuperCounter += 1
        # print(f"SuperCounter {SuperCounter}")
        nodo = frontierFIFO.remove()            
        # print(f"nodo.state: {nodo.state} \n")   

        if frontierRegreso.contains_state(nodo.state):            
            print(f"\nEncontro la solucion a la ida!!")            
            print(f"nodo.state: {nodo.state}")
            print(f"nodo.action: {nodo.action} \n")
            
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
            toc = time.perf_counter()
            print(f"Resuelto en {toc - tic:0.4f} segundos\n")   
            return actions

        try:
            explorados.add(utilEstado.Estado(nodo.state))
            # print(f"explorados.add: {nodo.state}")  
            for action, state in next_positions(nodo.state):
                counter += 1
                # if counter == 20001:
                #     return None
                if not frontierFIFO.contains_state(state) and utilEstado.Estado(state) not in explorados:
                    child = util.Node(state=state, parent=nodo, action=action)
                    frontierFIFO.add(child)
                    # print(f"frontierFIFO.add: {state}")  
            # print()
        except Exception as e:
            print(e.args)
        
        

        nodoRegreso = frontierRegreso.remove() 
        counter += 1
        # print(f"counter de regreso: {counter}")             
        # print(f"nodoRegreso.state: {nodoRegreso.state}")    
        if frontierFIFO.contains_state(nodoRegreso.state):
            print()
            print(f"Encontro la solucion al regreso!!")              
            actions = []
            cells = []
            estadoComun = nodoRegreso.state
            nodoComun = nodoRegreso
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
            # nodoRegreso = frontierRegreso.retorna_nodo(estadoComun)
            nodoRegreso = nodoComun
            if nodoRegreso is not None:
                while nodoRegreso.parent is not None:
                    actions.append(rubik.movimientos[rubik.movimiento_inverso(nodoRegreso.action)])
                    cells.append(nodoRegreso.parent.state)
                    dupla = (rubik.movimiento_inverso(nodoRegreso.action), nodoRegreso.parent.state)
                    path.append(dupla)
                    nodoRegreso = nodoRegreso.parent   
            toc = time.perf_counter()
            print(f"Resuelto en {toc - tic:0.4f} segundos\n")   
            return actions
        
        try:
            exploradosRegreso.add(utilEstado.Estado(nodoRegreso.state))          
            # print(f"exploradosRegreso.add: {nodoRegreso.state}")   
            for action, state in next_positions(nodoRegreso.state):
                if not frontierRegreso.contains_state(state) and utilEstado.Estado(state) not in exploradosRegreso:
                    child = util.Node(state=state, parent=nodoRegreso, action=action)
                    frontierRegreso.add(child)         
                    # print(f"frontierRegreso.add: {state}")    
            # print()
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

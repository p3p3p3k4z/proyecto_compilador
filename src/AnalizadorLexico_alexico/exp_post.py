import re
import sys
import os

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
thompson_path = os.path.join(base_path, 'AnalizadorLexico_thompson')
generales_path = os.path.join(base_path, 'AnalizadorLexico_generales')

sys.path.append(thompson_path)
sys.path.append(generales_path)

from thompson_alg import Thompson_
from lista_enlazada import LinkedList


#Funciones para ver el procesamiento que se le dará a la exp regular
def expresion_postfija(expresion):
    def precedencia(op):
        precedencias = {'|': 1, '.': 2, '*': 3, '+': 4, '?':5}
        return precedencias.get(op, 0)

    def a_postfija(expresion):
        pila_operadores = []
        salida = []
        i = 0

        while i < len(expresion):
            token = expresion[i]

            if token.isalnum():
                salida.append(token)
            elif token == '(':
                pila_operadores.append(token)
            elif token == ')':
                while pila_operadores and pila_operadores[-1] != '(':
                    salida.append(pila_operadores.pop())
                pila_operadores.pop()
            else:
                while pila_operadores and precedencia(token) <= precedencia(pila_operadores[-1]):
                    salida.append(pila_operadores.pop())
                pila_operadores.append(token)
            i += 1

        while pila_operadores:
            salida.append(pila_operadores.pop())

        return ''.join(salida)

    return a_postfija(expresion)


def evaluar_expresion_postfija(expresion_postfija):
    pila = []
    Automata = LinkedList()
    
    for token in expresion_postfija:
        if token.isalnum():
            pila.append(token)
            
        elif token == '?':
            operand1 = pila.pop()
            if type(operand1) != LinkedList:
                operand1 = SingleLetter(str(operand1))
                
            Automata = Cerradura_Opcional(operand1)
            pila.append(Automata)
            
        elif token == '*':
            operand1 = pila.pop()
            if type(operand1) != LinkedList:
                operand1 = SingleLetter(str(operand1))
                
            Automata = Cerradura_de_Kleene(operand1)
            pila.append(Automata)
            
        elif token == '+':
            operand1 = pila.pop()
            if type(operand1) != LinkedList:
                operand1 = SingleLetter(str(operand1))
                
            Automata = Cerradura_Positiva(operand1)
            pila.append(Automata)
            
        elif token == '.':
            operand2 = pila.pop()
            operand1 = pila.pop()
            if type(operand1) != LinkedList:
                operand1 = SingleLetter(str(operand1))
            if type(operand2) != LinkedList:
                operand2 = SingleLetter(str(operand2))
            Automata = Concatenation(operand1,operand2)
            pila.append(Automata)
            
        elif token == '|':
            operand2 = pila.pop()
            operand1 = pila.pop()
            if type(operand1) != LinkedList:
                operand1 = SingleLetter(str(operand1))
                
            if type(operand2) != LinkedList:
                operand2 = SingleLetter(str(operand2))
            
            Automata = Union(operand1,operand2)
            pila.append(Automata)
            
    # El resultado final debe estar en la cima de la pila
    return pila.pop()

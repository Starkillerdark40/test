import ply.lex as lex
import re
import codecs
import os
import sys

#Lista de tokens
tokens = ['ID', 'NUMNER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ODD', 'ASSING', 'NE', 'LT',
'LTE', 'GT', 'GTE', 'LPARENT', 'RPARENT', 'COMMA', 'SEMMICOLOM', 'DOT', 'UPDATE'];

#Diccionarios de palabras reservadas
reservadas = {
	'begin':'BEGIN',
	'end':'END',
	'if':'IF',
	'then':'THEN',
	'while':'WHILE',
	'do':'DO',
	'call':'CALL',
	'const':'CONST',
	'int':'INT',
	'procedure':'PROCEDURE',
	'out':'OUT',
	'in':'IN',
	'else':'ELSE'
};

tokens = tokens + list(reservadas.values());

#Definicion dentro de cada simblolo
t_ignore = '\t';
t_PLUS = r'\+';
t_MINUS = r'\-';
t_TIMES = r'\*';
t_DIVIDE = r'/';
t_ODD = r'ODD';
t_ASSING = r'=';
t_NE = r'<>';
t_LT = r'<';
t_LTE = r'<=';
t_GT = r'>';
t_GTE = r'>=';
t_LPARENT = r'\(';
t_RPARENT = r'\)';
t_COMMA = r',';
t_SEMMICOLOM = r';';
t_DOT = r'\.';
t_UPDATE = r':=';

#Funciones para los tokens faltates, ID, NUMERO, SALTO DE LINEA, COMENTARIOS, etc.
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*';
	if t.value.upper() in keywords:
		t_value = t.value.upper();
		t.type = t.value;
	return t;

def t_COMMENT(t):
	r'\#.*';
	pass

def t_NUMBER(t):
	r'\d+';
	t.value = int(t.value);
	return t;

def t_error(t):
	print "Caracter ilegal '%s'" % t.value[0];
	t.lexer.sikip(1);

directorio = 



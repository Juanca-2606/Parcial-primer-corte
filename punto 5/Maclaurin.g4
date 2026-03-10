grammar Maclaurin;

// Regla: evaluar x=[numero] n=[numero]
prog: (instruccion)+ ;
instruccion: 'evaluar' 'x=' NUM 'n=' NUM ;

NUM : [0-9]+('.'[0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
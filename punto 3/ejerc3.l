%{
#include "calc.tab.h"
#include <stdlib.h>
%}

%%
"sqrt"          { return SQRT; }
[0-9]+(\.[0-9]+)? { yylval.fval = atof(yytext); return NUM; }
"("             { return '('; }
")"             { return ')'; }
[ \t\n]         ; /* Ignorar espacios y saltos de linea */
.               { return yytext[0]; }
%%

int yywrap() { return 1; }
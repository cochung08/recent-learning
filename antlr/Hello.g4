// Define a grammar called Hello
//https://github.com/antlr/antlr4/blob/master/doc/getting-started.md
grammar Hello;
r  : 'hello' ID ;         // match keyword hello followed by an identifier
ID : [a-z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
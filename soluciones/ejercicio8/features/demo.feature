Feature: Feature Requests

 Scenario Outline: suma GET
   Given una URL
   When se hace una request GET con los parametros A = <a> y B = <b>
   Then el resultado es <c>

   Examples:
     | a    | b    | c    |
     | 1    | 2    | 3    |
     | 20   | 22   | 42   |

 Scenario: suma POST
   Given una URL
   When se hace una request POST con los parametros A = 1 y B = 2
   Then el resultado es 3
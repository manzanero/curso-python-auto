
Feature: AnimeFLV

 Scenario Outline: el último episodio es el 999
   Given <navegador> is up
   When the user gets <web> page
   And the user clicks one peace link
   Then the last episode is the <episode>th

   Examples:
     | navegador | web      | episode |
     | chrome    | animeflv | 999     |
     | chrome    | animeflv | 998     |

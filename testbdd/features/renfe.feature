@renfe
Feature: Renfe

 Scenario: inicio de sesión requerido al seleccionar un billete
   Given estoy en el portal de Renfe
   When selecciono origen Madrid
   And selecciono destino Barcelona
   Then llego a la lista de billetes
   When selecciono un billete
   Then el inicio de sesión es requerido
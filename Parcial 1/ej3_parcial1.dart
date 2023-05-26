import 'dart:math';
void main() {
 
  List<int> lista1 = generarListaAleatoria(10, 10, 20);
  print('Lista 1: $lista1');

  List<int> lista2 = generarListaAleatoria(10, 10, 20);
  print('Lista 2: $lista2');

  List<int> lista3 = ingresarListaPorTeclado(5);
  print('Lista 3: $lista3');

  double promedio = obtenerPromedio(listaConcatenada);
  print('Promedio: $promedio');

  listaConcatenada.sort();
  print('Lista ordenada: $listaConcatenada');
}





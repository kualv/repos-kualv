import 'dart:math';

void main() {
  Random random = Random();
  List<List<int>> listas = [];
  List<double> promedios = [];

  for (int i = 0; i < 3; i++) {
    List<int> lista = [];
    for (int j = 0; j < 7; j++) {
      int elemento = random.nextInt(71) + 30;
      lista.add(elemento);
    }
    listas.add(lista);
  }

  for (List<int> lista in listas) {
    double promedio = lista.reduce((a, b) => a + b) / lista.length;
    promedios.add(promedio);
  }

  print(promedios);
}



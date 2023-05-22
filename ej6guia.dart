import 'dart:math';
void main() {
  List<int> listaA = [4, 3, 2, 2, 1];
  List<int> listaB = [-3, 2, 8, 0, 1];

  List<int> listaC = [];
  for (int i = 0; i < listaA.length; i++) {
    listaC.add(listaA[i] * listaB[i]);
  }

  Random aleatorio = Random();
  for (int i = 0; i < 5; i++) {
    int aleatorioNumber = aleatorio.nextInt(5) + 1;
    listaC.add(-aleatorioNumber);
  }

  listaC.sort((a, b) => b.compareTo(a));

  print(listaC);
}
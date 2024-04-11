void addTwo(int num1, int num2) {
  int sum = num1 + num2;
  print(sum);
}

void subtractTwo(int num1, int num2) {
  int result = num1 - num2;
  print(result);
}

void multiplyTwo(int num1, int num2) {
  int result = num1 * num2;
  print(result);
}

void divideTwo(int num1, int num2) {
  double result = num1 / num2;
  print(result);
}

void stringLength(String inputString) {
  int length = inputString.length;
  print(length);
}

dynamic getFirtsElement(List<dynamic> list) {
  print(list.first);
}

void main() {
  addTwo(10, 5);
  subtractTwo(5, 9);
  multiplyTwo(20, 30);
  divideTwo(8, 4);
  stringLength("Hello world");
  getFirtsElement(["mango", "Griffin"]);
}

void checkNumber(int num) {
  if (num > 10) {
    print("Your number is greater than 10");
  } else if (num == 10) {
    print("Your number is equal to 10");
  } else {
    print("Your number is less than 10");
  }
}

void main() {
  checkNumber(9);
  checkNumber(20);
  checkNumber(10);
}

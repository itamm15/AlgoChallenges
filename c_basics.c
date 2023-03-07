#include <stdio.h>

// CONSTS
const int base_number = 10;

// STRUCTS

struct Plane{
  char name[30];
  int price;
  int max_speed;
};

// FUNCTIONS

void digitalizer() {
  int number, digiter = 1;
  printf("Provide the number!\n");
  scanf("%d", &number);
  while(number > base_number) {
    digiter += 1;
    number /= base_number;
  }
  printf("%d has %d digits.\n", number, digiter);
}

int calculate_sum(int numbers[]) {
  int size = sizeof(numbers) / sizeof(numbers[0]);
  int sum = 0;
  for (int iterator = 0; iterator < size; iterator++) {
    sum += numbers[iterator];
  }
  return sum;
}

void print_out_numbers(int numbers[]) {
  int size = sizeof(numbers) / sizeof(numbers[0]);
  for (int iterator = 0; iterator < size; iterator++ ){
    printf("The %d number is %d", iterator + 1, numbers[iterator]);
  }
}

void print_object_values(struct Plane plane) {
  printf("Plane's name: %s\n", plane.name);
  printf("Plane's price: %d\n", plane.price);
  printf("Plane's max speed: %d\n", plane.max_speed);
}

int main() {
  digitalizer();
  // arrays
  int numbers_container[10];

  // // Read values
  // for (int iterator = 0; iterator < base_number; iterator++) {
  //   scanf("%d", &numbers_container[iterator]);
  // }

  // // Print out values
  // print_out_numbers(numbers_container);
  // print("The sum is %d", calculate_sum(numbers_container));

  // Data structures!
  struct Plane F16 = {"F-16 Falcon", 12345, 1113};
  print_object_values(F16);

  // Pointer
  int age = 18;
  int *pAge = &age;
  printf("value of pAge %d\n", pAge);
  printf("pointer of pAge %d\n", &pAge);
  *pAge = 20;
  printf("value of pAge %d\n", pAge);
  printf("value of age %d\n", age);

  // Stacks and queues
}

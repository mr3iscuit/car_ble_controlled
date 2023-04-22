#include <SoftwareSerial.h>

#define right_1 5
#define right_2 4
#define left_1 3
#define left_2 2

SoftwareSerial controller(1, 2);

void setup() {
  pinMode(right_1, OUTPUT);
  pinMode(right_2, OUTPUT);
  pinMode(left_1, OUTPUT);
  pinMode(left_2, OUTPUT);
}

void loop() {
  if (controller.available()) {
    char c = controller.read();
    switch(c) {
    case '4':
      forward();
      break;
    case '2':
      backward();
      break;
    case '1':
      left();
      break;
    case '3':
      right();
      break;
    default:
      stop();
      break;
    }
  } else {
    stop();
  }

}

void forward() {
  digitalWrite(right_1, 1);
  digitalWrite(right_2, 0);
  digitalWrite(left_1, 1);
  digitalWrite(left_2, 0);
}

void backward() {
  digitalWrite(right_1, 0);
  digitalWrite(right_2, 1);
  digitalWrite(left_1, 0);
  digitalWrite(left_2, 1);
}

void stop() {
  digitalWrite(right_1, 0);
  digitalWrite(right_2, 0);
  digitalWrite(left_1, 0);
  digitalWrite(left_2, 0);
}

void left() {
  digitalWrite(right_1, 1);
  digitalWrite(right_2, 0);
  digitalWrite(left_1, 0);
  digitalWrite(left_2, 1);
}

void right() {
  digitalWrite(right_1, 0);
  digitalWrite(right_2, 1);
  digitalWrite(left_1, 1);
  digitalWrite(left_2, 0);
}

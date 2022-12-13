import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flame/flame.dart';

void main() {
  print("Game Started lessgo");
  runApp(GameWidget(game: MyGame()));
}

class MyGame extends FlameGame {}

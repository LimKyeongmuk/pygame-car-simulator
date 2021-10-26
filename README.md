# pygame_car-simulator
## Video
https://youtu.be/YI30ybn8uGY

## Goal
- 배경과 자동차의 충돌을 감지하는 시뮬레이터
- 자동차는 다른 파일에서 topic을 보내서 동작

## Environment
- Ubuntu 18.04
- ROS Melodic
- pytorch v1.2
- pyglet v1.4.11
- visdom v0.1.8.9
- pygame v1.9.6
- dill v0.3.3

~~~bash
$ pip install torch==1.2.0+cpu torchvision=0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
$ pip install visdom 
$ pip install pygame==1.9.2
$ pip install pyglet==1.4.11 --upgrade
~~~

## Structure
---
Project3
  └─ dummy_driver.python            # 자동차를 움직이는 ros topic 전송 파일
  └─ pygame_simulator_map.python    # 시뮬레이터
  └─ car.png                        # 자동차 이미지
  └─ map.png                        # map 이미지
  
## How to use
~~~bash
$ roscore
$ python dummy_driver.python
$ pygame_simulator_map.python
~~~

## What I've learned
- 시뮬레이터를 직접 제작해보면서 pygame 사용법 익힘
- 실제로 주행해보기 어려운 상황을 시뮬레이션에서 미리 주행이 가능해져서 다양한 시도 가능

import os
arr_1 = ['e','e','e']
arr_2 = ['e','e','e']
arr_3 = ['e','e','e']

arr_x = ['x','x','x']
arr_o = ['o','o','o']
arrays = ['arr_1','arr_2','arr_3']
while True:
 player_1 = input("player_1>").split()
 pl_1_arr = player_1[0]
 pl_1_ind = player_1[1]
 if globals()[pl_1_arr][int(pl_1_ind)] == 'o':
  print("Этот слот занят")
 else:
  globals()[pl_1_arr][int(pl_1_ind)] = 'x'
 if arr_1[0] and arr_1[1] and arr_1[2] == 'x':
  print('win!')
 if arr_2[0] and arr_2[1] and arr_2[2] == 'x':
  print('win!')
 if arr_3[0] and arr_3[1] and arr_3[2] == 'x':
  print('win!')
 if arr_1[0] and arr_2[0] and arr_3[0] == 'x':
  print('win!')
 if arr_1[1] and arr_2[1] and arr_3[1] == 'x':
  print('win!')
 if arr_1[2] and arr_2[2] and arr_3[2] == 'x':
  print('win!')
 if arr_1[0] and arr_2[1] and arr_3[2] == 'x':
  print('win!')
 if arr_1[2] and arr_2[1] and arr_3[0] == 'x':
  print('win!')
 for i in arrays:
  print(globals()[i])
  
 player_2 = input("player_2>").split()
 pl_2_arr = player_2[0]
 pl_2_ind = player_2[1]
 if globals()[pl_1_arr][int(pl_1_ind)] == 'x':
  print("Этот слот занят")
 else:
  globals()[pl_1_arr][int(pl_1_ind)] = 'o'
 if arr_1[0] and arr_1[1] and arr_1[2] == 'o':
  print('win!')
 if arr_2[0] and arr_2[1] and arr_2[2] == 'o':
  print('win!')
 if arr_3[0] and arr_3[1] and arr_3[2] == 'o':
  print('win!')
 if arr_1[0] and arr_2[0] and arr_3[0] == 'o':
  print('win!')
 if arr_1[1] and arr_2[1] and arr_3[1] == 'o':
  print('win!')
 if arr_1[2] and arr_2[2] and arr_3[2] == 'o':
  print('win!')
 if arr_1[0] and arr_2[1] and arr_3[2] == 'o':
  print('win!')
 if arr_1[2] and arr_2[1] and arr_3[0] == 'o':
  print('win!')
 for i in arrays:
  print(globals()[i])

 
 
 

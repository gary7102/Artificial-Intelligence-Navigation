def map_string_to_int(img):
    start_pos = []
    destination = []
    obstacle = []
    path_we_can_go = 0
    count = 0
    for i in range(len(img[0])):
      for j in range(len(img[0])):
        img[i][j] = int(img[i][j])
        dot = img[i][j]
        if dot == 0:
          path_we_can_go += 1
        elif dot == 1:
          obstacle.append(count)
        elif(dot == 2):
          start_pos.append(count)
          img[i][j] = 0
        elif dot == 3:
          destination.append(count)
          img[i][j] = 0
        count += 1
    print("node we can go = ", path_we_can_go)
    return start_pos[0], destination[0], obstacle

import csv
def small_easy():
  start = time.time()
  with open('./ai_map/s.csv', newline='') as csvfile:
        img = csv.reader(csvfile)
        img = list(img)

        start_pos, destination, obstacle = map_string_to_int(img)

        MultiRobotPathPlanner(500, 500, False, [start_pos, destination], [], obstacle, False)

        end = time.time()
        print("s map Time = ", round(end - start, 3), "seconds")
        print("job done, coverage = 100%")
        print()

        return end - start
def small_medium():
  start = time.time()
  with open('../ai_map/small-medium.csv', newline='') as csvfile:
        img = csv.reader(csvfile)
        img = list(img)

        start_pos, destination, obstacle = map_string_to_int(img)

        MultiRobotPathPlanner(500, 500, False, [start_pos, destination], [], obstacle, False)

        end = time.time()
        print("small_medium map Time = ", round(end - start, 3), "seconds")
        print("job done, coverage = 100%")

        print()
        return end - start
def small_hard():
  start = time.time()
  with open('../ai_map/small-hard.csv', newline='') as csvfile:
        img = csv.reader(csvfile)
        img = list(img)

        start_pos, destination, obstacle = map_string_to_int(img)

        MultiRobotPathPlanner(500, 500, False, [start_pos, destination], [], obstacle, False)

        end = time.time()
        print("small_hard map Time = ", round(end - start, 3), "seconds")
        print("job done, coverage = 100%")
        print()
        return end - start
def medium_easy():
  start = time.time()
  with open('../ai_map/m.csv', newline='') as csvfile:
      img = csv.reader(csvfile)
      img = list(img)

      start_pos, destination, obstacle = map_string_to_int(img)

      MultiRobotPathPlanner(1000, 1000, False, [start_pos, destination], [], obstacle, False)

      end = time.time()
      print("m map Time = ", round(end - start, 3), "seconds")
      print("job done, coverage = 100%")
      print()
      return end - start

def medium_medium():
  start = time.time()
  with open('../ai_map/medium-medium.csv', newline='') as csvfile:
        img = csv.reader(csvfile)
        img = list(img)

        start_pos, destination, obstacle = map_string_to_int(img)

        MultiRobotPathPlanner(1000, 1000, False, [start_pos, destination], [], obstacle, False)

        end = time.time()
        print("medium_medium map Time = ", round(end - start, 3), "seconds")
        print("job done, coverage = 100%")
        print()
        return end - start
def medium_hard():
  start = time.time()
  with open('../ai_map/medium-hard.csv', newline='') as csvfile:
        img = csv.reader(csvfile)
        img = list(img)

        start_pos, destination, obstacle = map_string_to_int(img)

        MultiRobotPathPlanner(1000, 1000, False, [start_pos, destination], [], obstacle, False)

        end = time.time()
        print("medium_hard map Time = ", round(end - start, 3), "seconds")
        print("job done, coverage = 100%")
        print()
        return end - start
def big_easy():
  start = time.time()
  with open('../ai_map/b.csv', newline='') as csvfile:
        img = csv.reader(csvfile)
        img = list(img)

        start_pos, destination, obstacle = map_string_to_int(img)

        MultiRobotPathPlanner(1500, 1500, False, [start_pos, destination], [], obstacle, False)

        end = time.time()
        # print("b map Time = ", round(end - stahttps://colab.research.google.com/drive/1rDnxsoPDQ2LwvzdRMgrrVrdBhlcPA
# Gic#scrollTo=NnPyhXsB1Bcyrt, 3), "seconds")
        print("job done, coverage = 100%")
        print()
        return end - start

def big_medium():
  start = time.time()
  with open('../ai_map/b.csv', newline='') as csvfile:
        img = csv.reader(csvfile)
        img = list(img)

        start_pos, destination, obstacle = map_string_to_int(img)

        MultiRobotPathPlanner(1500, 1500, False, [start_pos, destination], [], obstacle, False)

        end = time.time()
        print("b map Time = ", round(end - start, 3), "seconds")
        print("job done, coverage = 100%")
        print()
        return end - start

def big_hard():
  start = time.time()
  with open('../ai_map/big-hard.csv', newline='') as csvfile:
        img = csv.reader(csvfile)
        img = list(img)

        start_pos, destination, obstacle = map_string_to_int(img)

        MultiRobotPathPlanner(1500, 1500, False, [start_pos, destination], [], obstacle, False)

        end = time.time()
        print("big_hard map Time = ", round(end - start, 3), "seconds")
        print("job done, coverage = 100%")
        print()
        return end - start

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/

if __name__ == '__main__':
    '''
    Hello, this is the main funcion

    Notice that we can not execute the map that
    contain the area can't reach.

    For instance, the original small_hard map.
    '''
    total_time = 0
    total_time += small_easy()
    # total_time += small_medium()
    # total_time += small_hard()       ## original small_hard cannot success
    # total_time += medium_easy()
    # total_time += medium_medium()       ## original medium_medium cannot success
    # total_time += medium_hard()
    # total_time += big_easy()        ## runtime way too long
    # total_time += big_medium()       ## original big_medium cannot success
    # total_time += big_hard()        ## runtime way too long
    print("Total time = ", round(total_time, 3), "seconds")

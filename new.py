#queue manager
queue = [("Justin", "Sorry"), ("Charlie", "Attention")]
#the beginning queue that is shown by defualy

def show_queue(queue):
  print()
  if len(queue) == 0:
    print("Current queue: \n")
    print("The queue is empty!")
    print()
    print("Options:  add / remove / quit / next / move")
    print("-"*40)
    return
  else:
    print("Current queue: \n")
    for i,info in enumerate(queue):
        i+=1
        singer, song = info
        print(f"{i}.{singer} : {song}")
    print()
    print("Options:  add / remove / quit / next / move")
  print("-"*40)
#this function is to show queue if the length of the queue[] == 0 then it prints that the current queue is empty if not then it dispalys the queue

def prompt_for_singer():
  name = input("Enter the name of the artist : ").strip().title()
  song = input("Enter the song of the artist : ").strip().title()
  return name,song
#this takes input from the user to store the singers name and song in the respective variable .strip()strips the input out of every single random space

def add_singer(queue):
  print()
  name, song = prompt_for_singer()
#this saves the value of the function prompt_for_singer() into name and song
  if name == "" or song == "":
    print()
    print("Oops! Please enter a correct name or song")
    print("-"*40)
    return
  else:
    queue.append((name, song))
    print("=" *40)
    print(f"Added {name} - {song} ,to the queue")
    print("=" *40)
#if the name and song are empty the programm will throw and error if not then it will add and display the song and singer in the queue

def next_singer(queue):
  print()
  if len(queue) == 0:
    print("Oops! There's no one left to call up!")
    return
  name,song = queue.pop(0)
  print(f"Now playing! {name} : {song}")
  print("-" *40)
#this function calls the exact next singer up front

def move_to_top(queue):
  print()
  if len(queue) < 2:
    print("Not enough singers to move!")
    return
  try:
   position = int(input("Which position do you want to move to top! : "))
  except ValueError:
   print("Enter a valid number!")
#if the position is something else than an integer like a string that spells eight then the program will throw and error and return back
   return
  if position < 1 or position > len(queue):
    print()
    print("Enter a appropriate position!")
    print("-"*40)
    return
#if the position is something that dosent exist like if the queue has 4 singers and the position entered is 5 or something like -5 then the program will throw and error
  print()
  name ,song = queue.pop((position -1))
  queue.insert(0 ,(name,song))
  print()
  print(f"Sucessfully moved {name} to top of the queue!")
  print("-" *40)
#this function makes it so that any singer at any position can be thrown to the top of the queue

def remove_singer(queue):
   print()
   if len(queue)== 0:
     print("Oops! There's no one left to remove!")
     return
   else:
    name = input("Enter the name of the artist : ").strip().title()
    print()
    for singer_name in queue:
        if singer_name[0] == name:
          queue.remove(singer_name)
          singer , song = singer_name
          print(f"Removed {singer} : {song} from the queue")
          print("-"*40)
          return 
    print(f"{name} is not in the queue.")
    print("-"*40)
#this function allows the user to simply remove the singer from queue using simple function like queue.remove()

def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True 

    while is_running: 
      show_queue(queue)
      print()
      command = input("> ")
      
      if command == "add":
       add_singer(queue)

      elif command == "next":
        next_singer(queue)
      elif command == "move":
        move_to_top(queue)

      elif command == "remove":
       remove_singer(queue)
    
      elif command == "quit":
       is_running = False
      else:
        print("Please enter a correct options \nOptions: add / remove / quit / next / move")
#main function where the programm is running and doing all the task and calling every function
run_app(queue)
from os import name, system

welcome='''
     ____    __    ____  _______  __        ______   ______   .___  ___.  _______ 
     \   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
      \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__   
       \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|  
        \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
         \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|
     
'''
to = '''
                          .___________.  ______   
                          |           | /  __  \  
                          `---|  |----`|  |  |  | 
                              |  |     |  |  |  | 
                              |  |     |  `--'  | 
                              |__|      \______/  
                        
'''
racool= '''
        .______          ___       ______   ______     ______    __            
        |   _  \        /   \     /      | /  __  \   /  __  \  |  |           
        |  |_)  |      /  ^  \   |  ,----'|  |  |  | |  |  |  | |  |           
        |      /      /  /_\  \  |  |     |  |  |  | |  |  |  | |  |           
        |  |\  \----./  _____  \ |  `----.|  `--'  | |  `--'  | |  `----.      
        | _| `._____/__/     \__\ \______| \______/   \______/  |_______|      
                               .______    __       __  .__   __.  _______                 
                               |   _  \  |  |     |  | |  \ |  | |       \                
                               |  |_)  | |  |     |  | |   \|  | |  .--.  |               
                               |   _  <  |  |     |  | |  . `  | |  |  |  |               
                               |  |_)  | |  `----.|  | |  |\   | |  '--'  |               
                               |______/  |_______||__| |__| \__| |_______/                
             ___      __    __   ______ .___________.__   ______  .__   __. 
            /   \    |  |  |  | /      ||           |  | /  __  \ |  \ |  | 
           /  ^  \   |  |  |  ||  ,----'`---|  |----|  ||  |  |  ||   \|  | 
          /  /_\  \  |  |  |  ||  |         |  |    |  ||  |  |  ||  . `  | 
         /  _____  \ |  `--'  ||  `----.    |  |    |  ||  `--'  ||  |\   | 
        /__/     \__\ \______/  \______|    |__|    |__| \______/ |__| \__| 
                                                                       


'''
bid = '''
                               _______________
                               \             /
                                )___________(
                                |"""""""""""|_ .-._,.---------.,_.-._
                                |           | |     |               | |''-.
                                |           |_|     |              _| |_..-'
                                |___________| '-' `'----------'` '-'
                                )"""""""""""(
                               /_____________\.
                             `'---------------'==
                             .-------------------.
                            /Racool-Blind-Auction\.
                            ----------------------
'''
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
     _ = system('clear')

biders = {}
moreBiders = 'yes'
def add_biders(name,bidAmount):
    biders[name]=bidAmount
print(welcome)
print(to)
print(racool)    
print(bid)
while moreBiders == 'yes':    
    name = input('What is your Name ?\n:')
    bidAmount = int(input('What is your bid ?\n NO Commas or Dots\n: $'))
    add_biders(name,bidAmount)
    moreBiders = input('Are there more biders yes or no\n: ').lower()
    clear()
def checkTheHeighest(biders):
    heightest = 0
    keyh = ''
    for key in biders:
        if biders[key] > heightest:
            heightest = biders[key]
            keyh = key
    print(f'The Winner of The Bid is {keyh} with a bid of ${heightest}')        
checkTheHeighest(biders)

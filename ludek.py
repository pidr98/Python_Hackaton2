from termcolor import colored

def display_hangman(tries):
    stages = [colored(
                """
                       ┌--------┐
                       |        |
                       |        O
                       |       -┼-
                       |       ┌┴┐
                       |     You lost
                    ___|___ 
                """, 'red'),
                """
                       ┌--------┐
                       |        |
                       |        O
                       |       -┼-
                       |       
                       |     
                    ___|___ 
                """,
                """
                       ┌--------┐
                       |        |
                       |        O
                       |       
                       |       
                       |     
                    ___|___ 
                """,
                """
                       ┌--------┐
                       |        
                       |        
                       |       
                       |       
                       |     
                    ___|___ 
                """,
                """
                       
                       |        
                       |        
                       |       
                       |       
                       |     
                    ___|___ 
                """,
                """
                       
                             
                              
                             
                       |       
                       |     
                    ___|___ 
                """,
                """
                       
                             
                              
                             
                             
                            
                    ___|___ 
                """
    ]
    return stages[tries]

import pyautogui
import keyboard


def main():
    # Keys.
    STOP_PROGRAM = "End"
    TOGGLE_CLICK = "PgUp"
    TOGGLE_BUTTON = "PgDown"
    MOUSE_BUTTONS = [ "right", "left" ]
    
    print("Welcome to autoclicker by DOCtorActoAntohich!")
    print(f'To stop the script, press "{STOP_PROGRAM}"')
    print(f'To change the button to simulate clicks (default Left), press "{TOGGLE_BUTTON}"')
    print(f'To toggle clicking mode off and on (default off), press "{TOGGLE_CLICK}"')
    
    # Button states. True = Pressed
    current_click_state = False
    previous_click_state = current_click_state
    
    current_button_swapper_state = False
    previous_button_swapper_state = current_button_swapper_state
    
    
    # Flags of clicker.
    continue_clicking = False
    is_left_button = True
    
    
    while True:
        # Exit.
        if keyboard.is_pressed(STOP_PROGRAM):
            break
        
        # Get current states.
        current_click_state = keyboard.is_pressed(TOGGLE_CLICK)
        current_button_swapper_state = keyboard.is_pressed(TOGGLE_BUTTON)
        
        # Set flags.
        if current_click_state and not previous_click_state:
            continue_clicking = not continue_clicking
            print("Will program simulate clicks:", continue_clicking)
        if current_button_swapper_state and not previous_button_swapper_state:
            is_left_button = not is_left_button
            button_index = int(is_left_button)
            print(f'Now clicking with {MOUSE_BUTTONS[button_index]} button')
        
        # Save current values.
        previous_click_state = current_click_state
        previous_button_swapper_state = current_button_swapper_state
        
        # Handle events.
        if continue_clicking:
            button_index = int(is_left_button)
            pyautogui.click(button=MOUSE_BUTTONS[button_index])


if __name__ == "__main__":
    main()
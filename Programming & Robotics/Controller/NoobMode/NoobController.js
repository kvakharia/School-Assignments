// PASTE THIS INTO THE CONOLE
let gamepadConnected = false;
let GAMERMODE = false;
    let animationFrameId;
  
    function connectGamepad() {
      if (gamepadConnected) return "Gamepad Connected!";
  
      gamepadConnected = true;

      window.addEventListener("gamepadconnected", handleGamepadConnected);
    }
  
    function handleGamepadConnected(event) {
      const gamepad = event.gamepad;
      console.log("Gamepad connected:", gamepad);
  
      function updateGamepadState() {
        const gamepads = navigator.getGamepads();
        const gamepad = gamepads[0]; // Assuming only one gamepad is connected
  
        // Handle button states
        if (GAMERMODE) {
            window.RTurn = gamepad.buttons[5].value * gamepad.axes[1]
            window.LTurn = gamepad.buttons[4].value * gamepad.axes[1]
        } else {
            window.RTurn = gamepad.buttons[5].value
            window.LTurn = gamepad.buttons[4].value
        }
        window.Forward = gamepad.buttons[7].value
        window.Backward = gamepad.buttons[6].value
  
        // Handle axis values
        const axisThreshold = 0.1;
        
      }
  
      // Start updating the gamepad state
      const interval = setInterval(updateGamepadState, 16);
    }
    connectGamepad();
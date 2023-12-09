const Keyboard = window.SimpleKeyboard.default

const myKeyboard = new Keyboard({
  onChange: (input) => {
    document.querySelector('[name="q"]').value = input
    document.querySelector('[name="q"]').focus()
  },
  physicalKeyboardHighlight: true,
  layout: {
    default: [
      '1 2 3 4 5 6 7 8 9 0',
      'Q W E R T Y U I O P',
      'A S D F G H J K L Ç',
      'Z X C V B N M {bksp}',
      '{space}',
    ],
  },
  display: {
	  '{bksp}': '⇐ apagar',
	  '{space}': 'espaço',
	},
  preventMouseDownDefault: true,
  preventMouseUpDefault: true
})

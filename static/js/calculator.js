const $calculator = document.querySelector('.calculator-modal')
const $screen = document.querySelector('.calculator-screen')
const $keyboard = document.querySelector('.calculator-keyboard')

for (const key of $keyboard.children) {
  key.addEventListener('click', () => calcKeyPress(key.innerText))
}

function toggleCalculator() {
  $calculator.classList.toggle('show-calculator')
}

let num1 = '0'
let operation = ''
let num2 = '0'

loadCalc()

function calcKeyPress(key) {
  switch (key) {
    case 'C': clear(); break
    case '÷': runOperation(key); break
    case '×': runOperation(key); break
    case '-': runOperation(key); break
    case '+': runOperation(key); break
    case '%': percentage(); break
    case '+/-': invert(); break
    case ',': comma(); break
    case '=': result(); break
    default: insertAlg(key); break
  }

  renderScreen()
  saveCalc()
}

function loadCalc() {
  num1 = localStorage.getItem('calc.n1') ?? '0'
  operation = localStorage.getItem('calc.op') ?? ''
  num2 = localStorage.getItem('calc.n2') ?? '0'
  renderScreen()
}

function saveCalc() {
  localStorage.setItem('calc.n1', num1)
  localStorage.setItem('calc.op', operation)
  localStorage.setItem('calc.n2', num2)
}

// Limpa os cálculos
function clear() {
  if (!operation) {
    num1 = '0'
  } else if (Number(num2)) {
    num2 = '0'
  } else {
    operation = ''
  }
}

// Faz uma operação de soma/subtração/multiplicação/divisão
function runOperation(key) {
  if (operation && Number(num2)) {
    result()
  }
  operation = key
}

// Faz uma operação de porcentagem
function percentage() {
  if (!operation) {
    num1 = String(Number(num1) / 100)
  } else {
    const percentage = Number(num1) * (Number(num2) / 100)
    let result = 0
    switch (operation) {
      case '+': result = Number(num1) + percentage; break
      case '-': result = Number(num1) - percentage; break
      case '×': result = percentage; break
      case '÷': result = Number(num1) / (Number(num2) / 100); break
    }
    num1 = String(result)
    operation = ''
    num2 = '0'
  }
}

// Inverte o sinal do número
function invert() {
  if (!operation) {
    num1 = String(-num1)
  } else {
    num2 = String(-num2)
  }
}

// Adiciona vírgula
function comma() {
  if (!operation) {
    num1 = num1.replace('.', '') + '.'
  } else {
    num2 = num2.replace('.', '') + '.'
  }
}

// Aplica o resultado da operação
function result() {
  if (!operation) return
  let result = 0
  switch (operation) {
    case '+': result = Number(num1) + Number(num2); break
    case '-': result = Number(num1) - Number(num2); break
    case '×': result = Number(num1) * Number(num2); break
    case '÷': result = Number(num1) / Number(num2); break
  }
  num1 = String(result)
  operation = ''
  num2 = '0'
}

// Insere um algarismo
function insertAlg(key) {
  if (!operation) {
    if (num1 === '0') num1 = key
    else num1 += key
  } else {
    if (num2 === '0') num2 = key
    else num2 += key
  }
}

// Insere um número
function insertNum(num) {
  if (typeof num === 'string') {
    num = Number(num.replace(',', '.'))
  }

  if (!operation) {
    num1 = String(num)
  } else {
    num2 = String(num)
  }

  renderScreen()
  saveCalc()
  $calculator.classList.add('show-calculator')

  return false
}

// Mostra na tela
function renderScreen() {
  const op = operation
  
  let n1 = Number(Number(num1).toFixed(15)) // Corrige o erro de aproximação de ponto flutuante
  n1 = String(n1).replace('.', ',') // Transforma a vírgula
  n1 += num1.endsWith('.') ? ',' : '' // Renderiza a vírgula no final do número
  
  let n2 = Number(Number(num2).toFixed(15)) // Corrige o erro de aproximação de ponto flutuante
  n2 = operation ? String(n2).replace('.', ',') : '' // Só exibe se tiver uma operação / Transforma a vírgula
  n2 += num2.endsWith('.') ? ',' : '' // Renderiza a vírgula no final do número
  if (Number(num2 < 0)) n2 = `(${n2})` // Coloca parênteses se o número for negativo

  $screen.innerText = `${n1} ${operation} ${n2}`
}

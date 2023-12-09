const $progressBar = document.querySelector('.inactivity-progress')

function returnHome() {
	location.href = '/'
}

let timer = null
function resetProgress() {
	clearTimeout(timer)
	$progressBar.classList.remove('in-progress')
	setTimeout(() => $progressBar.classList.add('in-progress'), 1000)
	timer = setTimeout(returnHome, 31000)
}

resetProgress()

document.addEventListener('mousedown', resetProgress)
document.addEventListener('mouseup', resetProgress)
document.addEventListener('mousemove', resetProgress)
document.addEventListener('touchstart', resetProgress)
document.addEventListener('touchmove', resetProgress)
document.addEventListener('touchend', resetProgress)
document.addEventListener('keydown', resetProgress)
document.addEventListener('keyup', resetProgress)
document.addEventListener('visibilitychange', resetProgress)

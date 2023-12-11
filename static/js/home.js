localStorage.removeItem('calc.n1')
localStorage.removeItem('calc.op')
localStorage.removeItem('calc.n2')

new bootstrap.Carousel('.carousel', { pause: false })

let anuncios = null
async function fetchAnuncios() {
  // Carrega os anúncios
  const res = await fetch('/api/anuncios')
  
  // Se houver um erro não faz nada
  if (!res.ok) return false

  // Se é a primeira vez que carrega os anúncios, salva os anúncios
  if (anuncios === null) {
    anuncios = JSON.stringify(await res.json())
    return
  }

  novosAnuncios = JSON.stringify(await res.json())

  // Se os anúncios mudaram, atualiza a página
  if (novosAnuncios !== anuncios) {
    location.reload()
  }
}

setInterval(fetchAnuncios, 30000)
fetchAnuncios()

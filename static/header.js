async function mostrar_header()
{
    const resposta = await fetch("/api/header")
  
    if (!resposta.ok){
    }
    else{
        const categorias = await resposta.json()
        const categorias_lista = document.getElementById("lista-cat")
        categorias_lista.innerHTML = "";
      
        for (let categoria of categorias){
            let linha = `
                        <li><a href="${categoria.url_categoria}"></a>${categoria.nome_categoria}</li>
                        `
        categorias_lista.innerHTML += linha
        }
    }
}
mostrar_header()
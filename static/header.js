
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
                        <li><a href=${categoria.url_categoria}>${categoria.nome_categoria}</a></li>
                        `
        categorias_lista.innerHTML += linha
        }
    }
}
mostrar_header()

function pesquisar(){
    const busca = document.getElementById('form-input').value.toLowerCase().trim()
    // pega o input, o value oega oque esta escrito. O lower nao lia se é maiuscula ou minuscula, o trim ignora espaçoes vazios
    //verifica se o busca foi amigurumi, se foi, ele pega a seção pelo id dela, rola lento ate essa seção com o smooth
    
    if (busca === 'amigurumi' || busca === 'amigurumis') {
        const secaoAmigurumi = document.querySelector('.info-section-amigu');
        if(secaoAmigurumi) secaoAmigurumi.scrollIntoView({ behavior: 'smooth' });
        

    } else if (busca === 'linhas' || busca === 'fios') {
        const secaoLinhas = document.querySelector('.info-section-linha');
        if(secaoLinhas) secaoLinhas.scrollIntoView({ behavior: 'smooth' });
    }
    else if (busca === 'kit' || busca === 'kits') {
        const secaoKits = document.querySelector('.info-section-kit');
       if(secaoKits) secaoKits.scrollIntoView({ behavior: 'smooth' });
    } 

    else if (busca === 'acessorios' || busca === 'acessorio') {
        const secaoAcessorios = document.querySelector('.info-section-ace');
        if(secaoAcessorios) secaoAcessorios.scrollIntoView({ behavior: 'smooth' });
    }

   else {
        Swal.fire({
            icon: 'error',
            title: 'ERRO',
            text: 'Categoria não encontrada!',
            confirmButtonColor: '#702983'
        });
    }
};

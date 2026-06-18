async function mostrarCarrinho() {
    const resposta = await fetch("/api/get/carrinho")

    if (!resposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else{
        const dados = await resposta.json()
        const carrinho = document.querySelector(".cart__items")

        carrinho.innerHTML = "";
        let total = 0

        for (let dado of dados){
            //Converte os valores para números
            let precoUni = parseFloat(dado.preco_prod);
            let qtdItem = parent(dado.quantidade);

            // Soma o valor total de acordo com a quantidade de produtos
            total = total + (precoUni * qtdItem);

            let linha = `<div class="cart__item" style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px;">
                        
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <img src="${dado.img_1}" style="width: 60px; height: 60px; border-radius: 8px; object-fit: cover;">
                            
                            <div class="cart__item-info">
                                <p style="margin: 0; font-weight: bold;">${dado.nome_prod}</p>
                                <p style="margin: 0; color: #555;">${qtdItem}x R$ ${precoUnidade.toFixed(2)}</p>
                            </div>
                        </div>

                        <button onclick="deletarItemCarrinho(${dado.cod_prod})"
                            style="background:none; border:none; color: #7a3b00; cursor: pointer; font-size: 1.2rem; padding: 5px;"
                            title="Remover produto">
                          <i class="bi bi-trash"></i> 
                        <button>  

                        </div>`

            carrinho.innerHTML += linha
        }
        document.querySelector(".cart__total").innerHTML = "Total: R$ " + total.toFixed(2)
    };

};

mostrarCarrinho()


async function inserirItemCarrinho(cod_prod, quantidade=1){
    const resposta = await fetch("/api/post/item_carrinho", 
                                    {
                                        method:"POST",
                                        headers:{
                                            "Content-Type": "application/json"
                                        },
                                        body: JSON.stringify(
                                                {   "cod_prod":cod_prod,
                                                    "quantidade":quantidade}
                                            )
                                        
                                    }
                                )
    
    if (!resposta.ok)
        {
            alert("Erro ao inserir item!")
        }

        mostrarCarrinho();  

}


async function deletarItemCarrinho(cod_prod){
    const resposta = await fetch("/api/post/deletar_item_carrinho", 
                                    {
                                        method:"POST",
                                        headers:{
                                            "Content-Type": "application/json"
                                        },
                                        body: JSON.stringify(
                                                {   "cod_prod":cod_prod}
                                            )
                                        
                                    }
                                )
    
    if (!resposta.ok)
        {
            alert("Erro ao inserir item!")
        }

        mostrarCarrinho();  

}
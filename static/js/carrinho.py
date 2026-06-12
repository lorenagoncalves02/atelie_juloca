# async function mostrarCarrinho() {
#     const resposta = await fetch("/api/get/carrinho")

#     if (!resposta.ok) {
#         alert("ERRO AO CARREGAR CARRINHO!")
#     }
#     else{
#         const dados = await resposta.json()

#         const carrinho = document.querySelector(".cart__items")

#         carrinho.innerHTML = "";

#         let total = 0

#         for (let dado of dados){
            
#             total = total + parseFloat(dado.preco)

#             let linha = `<div class="cart__item" style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px;">
      
#                         <img src="${dado.url_imagem}" style="width: 60px; height: 60px; border-radius: 8px; object-fit: cover;">
                        
#                         <div class="cart__item-info">
#                             <p style="margin: 0; font-weight: bold;">🍔 ${dado.produtos}</p>
#                             <p style="margin: 0; color: #555;">R$ ${dado.preco}</p>
#                         </div>

#                         </div>`

#             carrinho.innerHTML += linha
#         }
#         document.querySelector(".cart__total").textContent = "Total: R$ " + total.toFixed(2)
#     };

# };

# mostrarCarrinho()


# async function inserirItemCarrinho(cod_produto, quantidade=1){
#     const resposta = await fetch("/api/post/item_carrinho", 
#                                     {
#                                         method:"POST",
#                                         headers:{
#                                             "Content-Type": "application/json"
#                                         },
#                                         body: JSON.stringify(
#                                                 {   "cod_produto":cod_produto,
#                                                     "quantidade":quantidade }
#                                             )
                                        
#                                     }
#                                 )
    
#     if (!resposta.ok)
#         {
#             alert("Erro ao inserir item!")
#         }

#         mostrarCarrinho();  

# }


# async function deletarItemCarrinho(cod_produto){
#     const resposta = await fetch("/api/post/deletar_item_carrinho", 
#                                     {
#                                         method:"POST",
#                                         headers:{
#                                             "Content-Type": "application/json"
#                                         },
#                                         body: JSON.stringify(
#                                                 {   "cod_produto":cod_produto}
#                                             )
                                        
#                                     }
#                                 )
    
#     if (!resposta.ok)
#         {
#             alert("Erro ao inserir item!")
#         }

#         mostrarCarrinho();  

# }
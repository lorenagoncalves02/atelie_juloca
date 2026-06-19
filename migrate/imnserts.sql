USE juloca;

insert into `juloca`.`categoria`
(
nome_categoria, 
url_categoria
)
VALUE
(
"Pagina Inicial",
"/"
),
(
"Amigurumis",
"#content-amigurumi"
),
(
"Kits",
"#content-kits"
),
(
"Linhas",
"#content-linha"
),
(
"Acessórios",
"#content-acessorio"
);
select * from categoria;
insert into `juloca`.`produto`
(
 nome_prod,
 descricao_prod,
 preco_prod,
 img_1,
 img_2,
 img_3,
 id_categoria
)
VALUES(
"Raposa",
"Feita com muito carinho por nossa equipe, com fios de algodão para uma experiencia confortável.",
"70.00",
"/static/img/6.png",
"/static/img/7.png",
"/static/img/8.png",
"2"
),

(
"Coelho",
"Feita com muito carinho por nossa equipe, com fios de algodão para uma experiencia confortável.",
"70.00",
"/static/img/9.png",
"/static/img/10.png",
"/static/img/11.png",
"2"
),

(
"Macaco",
"Feita com muito carinho por nossa equipe, com fios de algodão para uma experiencia confortável.",
"70.00",
"/static/img/12.png",
"/static/img/13.png",
"/static/img/14.png",
"2"
),
(
"Fada",
"Feita com muito carinho por nossa equipe, com fios de algodão para uma experiencia confortável.",
"70.00",
"/static/img/15.png",
"/static/img/16.png",
"/static/img/17.png",
"2"
),
(
"Girafa",
"Feita com muito carinho por nossa equipe, com fios de algodão para uma experiencia confortável.",
"70.00",
"/static/img/18.png",
"/static/img/19.png",
"/static/img/20.png",
"2"
),
(
"Capitão América",
"Feita com muito carinho por nossa equipe, com fios de algodão para uma experiencia confortável.",
"70.00",
"/static/img/21.png",
"/static/img/22.png",
"/static/img/23.png",
"2"
),
(
"Linha Amarela",
"Linha com cor forte, Fio Amigurumi, 500m.",
"25.00",
"/static/img/27.png",
"/static/img/27.png",
"/static/img/27.png",
"4"
),
(
"Linha Azul-Marinho",
"Linha com cor forte, Fio Amigurumi, 500m.",
"25.00",
"/static/img/28.png",
"/static/img/28.png",
"/static/img/28.png",
"4"
),
(
"Linha Rosa-Bebe",
"Linha com cor forte, Fio Amigurumi, 500m.",
"25.00",
"/static/img/29.png",
"/static/img/29.png",
"/static/img/29.png",
"4"
),
(
"Linha Vermelho-Vinho",
"Linha com cor forte, Fio Amigurumi, 500m.",
"25.00",
"/static/img/30.png",
"/static/img/30.png",
"/static/img/30.png",
"4"
),
(
"Linha Verde-Brasil",
"Linha com cor forte, Fio Amigurumi, 500m.",
"25.00",
"/static/img/31.png",
"/static/img/31.png",
"/static/img/31.png",
"4"
),
(
"Linha Marrom",
"Linha com cor forte, Fio Amigurumi, 500m.",
"25.00",
"/static/img/32.png",
"/static/img/32.png",
"/static/img/32.png",
"4"
),
(
"Kit Agulhas",
"8 Agulhas de tamanhos ideais para todos os projetos, com cabo de bambu. Pensado no conforto e estética, com um porta agulhas de pano, super visual.",
"40.00",
"/static/img/33.png",
"/static/img/33.png",
"/static/img/33.png",
"5"
),
(
"Marcadores coloridos",
"Marcadores de Platico, cores variadas, contém 100 Unidades",
"25.00",
"/static/img/34.png",
"/static/img/34.png",
"/static/img/34.png",
"5"
),
(
"Olhos para amigurumi",
"Olinhos com tamanhos variados, modelo pronto para encaixar.",
"15.00",
"/static/img/35.png",
"/static/img/35.png",
"/static/img/35.png",
"5"
),
(
"Tesoura Bambu",
"Tesoura com ponta, com cabo de bambu pensado no corforto e estética dos clientes.",
"25.00",
"/static/img/36.png",
"/static/img/36.png",
"/static/img/36.png",
"5"
),
(
"Fita Métrica",
"Fita métrica de 5M",
"15.00",
"/static/img/37.png",
"/static/img/37.png",
"/static/img/37.png",
"5"
),
(
"Kit Stitch",
"Kit completo com agulha, linhas, acessórios e receita.",
"60.00",
"/static/img/24.png",
"/static/img/25.png",
"/static/img/25.png",
"3"
), 
(
"Kit anjinho",
"Kit completo com agulha, linhas, acessórios e receita.",
"60.00",
"/static/img/26.png",
"/static/img/27_1.png",
"/static/img/27_1.png",
"3"
),
(
"Kit Capivara",
"Kit completo com agulha, linhas, acessórios e receita.",
"60.00",
"/static/img/29_1.png",
"/static/img/28_1.png",
"/static/img/28_1.png",
"3"
),
(
"Kit Patinho",
"Kit completo com agulha, linhas, acessórios e receita.",
"60.00",
"/static/img/31_1.png",
"/static/img/30_1.png",
"/static/img/30_1.png",
"3"
),
(
"Kit Leãozinho",
"Kit completo com agulha, linhas, acessórios e receita.",
"60.00",
"/static/img/35_1.png",
"/static/img/34_1.png",
"/static/img/34_1.png",
"3"
),
(
"Kit Homem-Aranha",
"Kit completo com agulha, linhas, acessórios e receita.",
"60.00",
"/static/img/33_1.png",
"/static/img/32_1.png",
"/static/img/32_1.png",
"3"
),
(
"Kit Elefantinho",
"Kit completo com agulha, linhas, acessórios e receita.",
"60.00",
"/static/img/37_1.png",
"/static/img/36_1.png",
"/static/img/36_1.png",
"3"
);

select * from produto;
select * from categoria;




 

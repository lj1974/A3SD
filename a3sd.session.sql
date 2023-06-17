SELECT sum(Vendas.valor)
    FROM Vendas
    JOIN Lojas ON Vendas.loja = Lojas.idloja
    JOIN Redes ON Lojas.redeloja = Redes.idrede
    WHERE Vendas.datavenda BETWEEN '2023-1-1' AND '2024-1-4' AND Redes.nomerede ='ATAKADAO'






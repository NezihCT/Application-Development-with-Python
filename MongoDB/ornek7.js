db.Categories.aggregate({ // ana tabloyu çağırıyoruz.

    $lookup: {
        from: "Products", // join yapılacak tablo
        localField: "CategoryID", // ana tablo içerisinde yer alan pk (primary key) birincil anahtar,
        foreignField: "CategoryID", // ForeignKey ikincil alan, ürünler tablosunda Kategoriyi temsil eden alan
        as: "Products" // sorgu sonucu kategorieye bağlı ürünler listelenirken, verilecek olan isim, (opsiyonel) dilediğiniz ismi verin elma armut vs..
    }
}).pretty()


db.Categories.aggregate({
    $lookup: {
        from: "Products",
        localField: "CategoryID",
        foreignField: "CategoryID",
        as: "Urunler"
    }
}).pretty()
// Equality ==

db.Products.find({ "ProductID": 77 }) //=> ürün id değeri 77 olan kaydı getirir.


// categoryıd si 8 olan ürünleri listeleyiniz.

db.Products.find({ "CategoryID": 8 }).pretty()

// less than
// Fiyatı 50$ dan az olan ürünlerin listelenmesi

db.Products.find({ "UnitPrice": { $lt: 50 } }).pretty()


// Ürünlerin sıralanması iki şekilde olur:
// 1) Ascending +1 A'dan Z'ye 0'dan 9'a şeklinde sıralama yapar (Fakirden Zengine)
// 2) Descending -1 Z'den A'ya 9'dan 0'a şeklinde sıralama yapar (Zenginden Fakire)

db.Products.find().pretty().sort({ "UnitPrice": 1 }) //ascending
db.Products.find().pretty().sort({ "UnitPrice": -1 }) //descending

// less then equal
// Fiyatı 50$ eşit veya küçük olan ürünlerin, küçükten büyüğe sıralanması
db.Products.find({ "UnitPrice": { $lte: 50 } }).pretty().sort({ "UnitPrice": 1 })

//greater than >
// fiyatı 100$ dan büyük olan ürünleri listeleyiniz
db.Products.find({ "UnitPrice": { $gt: 100 } }).pretty().sort({ "UnitPrice": 1 })

// greater than equals >=
db.Products.find({ "UnitPrice": { $gte: 100 } }).pretty().sort({ "UnitPrice": -1 })


// and ve or kullanımı

//  and kullanımı:
// fiyatı 30$ dan büyük ve stok adedi 100'den küçük olan ürünlerin listelenmesi
db.Products.find({ $and: [{ "UnitPrice": { $gte: 30 } }, { "UnitsInStock": { $lte: 100 } }] })

// fiyatı 30$ dan büyük ve stok adedi 100'den küçük olan ürünlerin sıralı ve düzgün şekilde listelenmesi
db.Products.find({ $and: [{ "UnitPrice": { $gte: 30 } }, { "UnitsInStock": { $lte: 100 } }] }).pretty().sort({ "UnitPrice": 1 })

// sırasıyla bu şekildedir
//  db.Products.find()
//  db.Products.find({})
//  db.Products.find({$and:})
//  db.Products.find({$and:[ ]})
//  db.Products.find({$and:[     {},{}   ]})

// select * from Products where UnitPrice >= 30 and UnitsInStock <= 100 order by UnitPrice desc
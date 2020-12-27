// var olan bir database'i silme
// use <database ismi>
// db.dropDatabase()

// db içerisinde yer alan kayıtları listelemek için, öncelikle database'in seçilmiş olması gerekir.

// 1) Kayıtların Listelenmesi
// 1.1) use Theaters

// 2)Koleksiyon içerisinde yer alan tüm kayıtların listelenmesi
// 2.1) db.Games.find()
// 2.2) db.Games.find().pretty()

// 3) Koleksiyon içerisinde yer alan kayıtların filtrelenerek listelenmesi
// 3.1) db.Games.find({"Key":"Value"})
// Ornek: db.Games.find({"Name":"FELATUN BEY İLE RAKIM EFENDİ"}).pretty() 
// ornek: db.Games.find({"Name":"FELATUN BEY İLE RAKIM EFENDİ"})

// 4) Update işlemi, bir kaydın belirli bir alanı veya tüm kayıtların belirli
// alanlarının değiştirilmesi işlemi
// 4.1) db.Games.update({"key":"value"},{$set:{"key":"value"}})
//      1. süslü parantez içeriği
//          {key => filtreleme yaparken, neye göre yapacaksınız propert adı : value => filtreleme yaparken verdiğiniz değer}
//      2. süslü parantez içeriği
//          {$set : => eşitle anlamına gelir {key =>hangi alan değişecek : value => o alanın yeni değeri nedir?}}
//      Ornek sorgu : db.Games.update({"Name":"FELATUN BEY İLE RAKIM EFENDİ"},{$set:{"ImageUrl":"bilgeadam"}})


// db.Games.update({"Id":1},{$set:{"ImageUrl":"bilgeadam"}})
// db.Games.update({"Id":4},{$set:{"ImageUrl":"bilgeadam"}})
// db.Games.update({"Id":180},{$set:{"ImageUrl":"bilgeadam"}})
// db.Games.update({"Id":183},{$set:{"ImageUrl":"bilgeadam"}})

// db.Games.find({"ImageUrl":"bilgeadam"}).pretty()

// Games içerisinde ImageUrl'i bilgeadam olan tüm kayıtların Url'si www.bilgeadam.com larak değiştirilmesi
// db.Games.update({"ImageUrl":"bilgeadam"},{$set:{"Url":"www.bilgeadam.com"}},{multi:true})

// veya

// db.Games.updateMany({"Url":"www.bilgeadam.com"},{$set:{"ImageUrl":"bilgeadam akademi"}})
// db.Games.find({"ImageUrl":"bilgeadam akademi"}).pretty()



// var.games = db.Games.find() =>oyun listesini değişkene atadık
// games.hasNext() => true dönüyorsa, içerde okunacak kayıt var anlamına gelir.
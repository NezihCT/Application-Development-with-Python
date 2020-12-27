/* 
1) show dbs : server icerisinde yer alan databaseleri goruntuler.
2) use <databse adı>  : calismak istediiginiz database in adını vermeniz yeterlidir. Not : kucuk buyuk harf duyarlılıgı vardir. 
3) show collections : database icerisinde yer alan koleksiyonlar(table) i gosterir.


*/


// use kisiler  => kisiler database ini secili hale getirdik. 

db.kisiler.insert()

// 1) use TelefonRehberi  => TelefonRehberi adında bir db olusturduk.
/* 2) 

        db.Kisiler.insert({
            "firstname":"omer",
            "lastname" : "kara",
            "mail" : "okara@etu.edu.tr",
            "phone" : "244242455646",
            "phones" : [
                {
                    "key" : "is",
                    "value" : "245893598538"
                },
                {
                    "key" : "okul",
                    "value" : "4387538593"

                }

            ]
        })

*/

// 3) db.Kisiler.find()
// 4) db.Kisiler.find().pretty()
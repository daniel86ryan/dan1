
let keyValueDuplicates = function(obj) {
    let arr = []
    let valArr = []
    for (let key in obj) {
        let values = obj[key]
        valArr.push(values)
    }

    for (let key in obj){
        for (let i = 0; i<valArr.length; i++){
            if (valArr[i] == key) {
                arr.push(key)
            }
        }
    }
    return arr  
}

obj1 = {orange: "juice", apple: "sauce", sauce: "pan" };
console.log(keyValueDuplicates(obj1)); // ["sauce"]

obj2 = {big: "foot", foot: "ball", ball: "boy", boy: "scout" };
console.log(keyValueDuplicates(obj2)); // ["sauce"]

obj3 = {pizza: "pie", apple: "pie", pumpkin: "pie" };
console.log(keyValueDuplicates(obj3)); // ["sauce"]



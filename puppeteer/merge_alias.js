const Papa = require('papaparse')

var fs = require('fs');
var datas_file = fs.readFileSync('companies_upload_with_alias_with_Tan_Update.csv', "utf8");
dataObjs = Papa.parse(datas_file,{header:true})

coms = dataObjs.data

valid_coms = []

unique = (arr) => {
    var hash = {}, result = [];
    for (var i = 0; i < arr.length; i++)
        if (!(arr[i] in hash)) { //it works with objects! in FF, at least
            hash[arr[i]] = true;
            result.push(arr[i]);
        }
    return result;
}


for (const com of coms) {
    let existed = false;

    for (const vcom of valid_coms) {
        if(com.name === vcom.name){
            existed = true
            vcom.alias += ` || `+com.alias;
            break;
        }
    }

    if(!existed){
        valid_coms.push(com);
    }
}

for (const vcoms of valid_coms) {
    alias = vcoms.alias.split('||').map(i=>i.trim())
    alias2 = unique(alias)
    if(alias2.length != alias.length){
        vcoms.alias = alias2.join(' || ')
    }
}

valid_coms_str = Papa.unparse(valid_coms,{header:true})
fs.writeFileSync('companies_20210609.csv',valid_coms_str ,"utf8");
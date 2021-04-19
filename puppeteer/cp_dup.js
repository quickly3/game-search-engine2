const Papa = require('papaparse')

var fs = require('fs');
var file = 'companies_linkedin.csv';
var file2 = 'companies_linkedin_merge.csv';


var input_file = fs.readFileSync(file, "utf8");
inputObjs = Papa.parse(input_file,{header:true})
names = []
output = []

for (const c1 of inputObjs.data){
    if(c1.success == 'true'){
        if(names.indexOf(c1.company) > -1){

        }else{
            names.push(c1.company)
            output.push(c1)
        }
    }
}


for (const c1 of inputObjs.data){
    if(c1.success == 'false'){
        if(names.indexOf(c1.company) > -1){

        }else{
            names.push(c1.company)
            output.push(c1)
        }
    }
}

outputstr = Papa.unparse(output,{header:true})
fs.writeFileSync(file2, outputstr ,"utf8");
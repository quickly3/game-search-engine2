const Papa = require('papaparse')

var fs = require('fs');
var file = 'linkedin_urls.csv';
var file2 = 'cleared_linkedin_urls.csv';


var input_file = fs.readFileSync(file, "utf8");
inputObjs = Papa.parse(input_file,{header:true})
names = []
output = []
count = 0
for (const c1 of inputObjs.data){
    if((c1.url.indexOf("/company/") == -1) && (c1.url.indexOf("/school/") == -1)){
        count++
        continue;
    }
    if(names.indexOf(c1.name) > -1){

    }else{
        names.push(c1.name)
        c1.url = c1.url+"/about/"
        
        output.push(c1)
    }
}
outputstr = Papa.unparse(output,{header:true})
fs.writeFileSync(file2, outputstr ,"utf8");
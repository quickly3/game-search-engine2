const Papa = require('papaparse')

var fs = require('fs');
var datas_file = fs.readFileSync('linkedin_companies.csv', "utf8");
var in_map = fs.readFileSync('in_map.csv', "utf8");

dataObjs = Papa.parse(datas_file,{header:true})
inMapObjs = Papa.parse(in_map,{header:true})

var inds = [{"id":1,"name":"All Industries","order":null,"parentId":null,"alias":"All","level":1},{"id":5020,"name":"Media & Entertainment","order":null,"parentId":50,"alias":"Media Ent","level":2},{"id":501010,"name":"Diversified Telecommunication Services","order":null,"parentId":5010,"alias":"Divers Telecom Srv","level":3},{"id":501020,"name":"Wireless Telecommunication Services","order":null,"parentId":5010,"alias":"Wireless Srv","level":3},{"id":5010,"name":"Telecommunication Services","order":null,"parentId":50,"alias":"Telecom","level":2},{"id":50,"name":"Communication Services","order":null,"parentId":null,"alias":"Comm Srv","level":1},{"id":251010,"name":"Auto Components","order":null,"parentId":2510,"alias":"Auto Comp","level":3},{"id":251020,"name":"Automobiles","order":null,"parentId":2510,"alias":"Auto","level":3},{"id":2510,"name":"Automobiles & Components","order":null,"parentId":25,"alias":"Auto Comp","level":2},{"id":252010,"name":"Household Durables","order":null,"parentId":2520,"alias":"House Durables","level":3},{"id":252020,"name":"Leisure Equipment & Products","order":null,"parentId":2520,"alias":"Leisure Prod","level":3},{"id":252030,"name":"Textiles, Apparel & Luxury Goods","order":null,"parentId":2520,"alias":"TALG","level":3},{"id":2520,"name":"Consumer Durables & Apparel","order":null,"parentId":25,"alias":"ConsR D&A","level":2},{"id":253020,"name":"Diversified Consumer Services","order":null,"parentId":2530,"alias":"DCS","level":3},{"id":253010,"name":"Hotels, Restaurants & Leisure","order":null,"parentId":2530,"alias":"HRL","level":3},{"id":2530,"name":"Consumer Services","order":null,"parentId":25,"alias":"ConsR Srv","level":2},{"id":255010,"name":"Distributors","order":null,"parentId":2550,"alias":"Distributors","level":3},{"id":255020,"name":"Internet & Catalog Retail","order":null,"parentId":2550,"alias":"ICR","level":3},{"id":255030,"name":"Multiline Retail","order":null,"parentId":2550,"alias":"MR","level":3},{"id":255040,"name":"Specialty Retail","order":null,"parentId":2550,"alias":"SR","level":3},{"id":2550,"name":"Retailing","order":null,"parentId":25,"alias":"Retailing","level":2},{"id":25,"name":"Consumer Discretionary","order":null,"parentId":null,"alias":"ConsR Disc","level":1},{"id":302010,"name":"Beverages","order":null,"parentId":3020,"alias":"Beverages","level":3},{"id":302020,"name":"Food Products","order":null,"parentId":3020,"alias":"Food Prod","level":3},{"id":302030,"name":"Tobacco","order":null,"parentId":3020,"alias":"Tabacco","level":3},{"id":3020,"name":"Food, Beverage & Tobacco","order":null,"parentId":30,"alias":"FBT","level":2},{"id":301010,"name":"Food & Staples Retailing","order":null,"parentId":3010,"alias":"FSR","level":3},{"id":3010,"name":"Food & Staples Retailing","order":null,"parentId":30,"alias":"FSR","level":2},{"id":303010,"name":"Household Products","order":null,"parentId":3030,"alias":"House Prod","level":3},{"id":303020,"name":"Personal Products","order":null,"parentId":3030,"alias":"Personal Prod","level":3},{"id":3030,"name":"Household & Personal Products","order":null,"parentId":30,"alias":"HPP","level":2},{"id":30,"name":"Consumer Staples","order":null,"parentId":null,"alias":"ConsR Stap","level":1},{"id":101010,"name":"Energy Equipment & Services","order":null,"parentId":1010,"alias":"EES","level":3},{"id":101020,"name":"Oil, Gas & Consumable Fuels","order":null,"parentId":1010,"alias":"OGCF","level":3},{"id":1010,"name":"Energy","order":null,"parentId":10,"alias":"Energy","level":2},{"id":10,"name":"Energy","order":null,"parentId":null,"alias":"Energy","level":1},{"id":401010,"name":"Commercial Banks","order":null,"parentId":4010,"alias":"Com Banks","level":3},{"id":401020,"name":"Thrifts & Mortgage Finance","order":null,"parentId":4010,"alias":"Thrifts","level":3},{"id":4010,"name":"Banks","order":null,"parentId":40,"alias":"Banks","level":2},{"id":402030,"name":"Capital Markets","order":null,"parentId":4020,"alias":"Cap Markets","level":3},{"id":402020,"name":"Consumer Finance","order":null,"parentId":4020,"alias":"ConsR Fin","level":3},{"id":402010,"name":"Diversified Financial Services","order":null,"parentId":4020,"alias":"Divers Fin Srv","level":3},{"id":4020,"name":"Diversified Financials","order":null,"parentId":40,"alias":"Div Fin","level":2},{"id":403010,"name":"Insurance","order":null,"parentId":4030,"alias":"Insurance","level":3},{"id":4030,"name":"Insurance","order":null,"parentId":40,"alias":"Insurance","level":2},{"id":40,"name":"Financials","order":null,"parentId":null,"alias":"Fin","level":1},{"id":351010,"name":"Health Care Equipment & Supplies","order":null,"parentId":3510,"alias":"Healthcare Equip","level":3},{"id":351020,"name":"Health Care Providers & Services","order":null,"parentId":3510,"alias":"Healthcare Srv","level":3},{"id":351030,"name":"Health Care Technology","order":null,"parentId":3510,"alias":"Healthcare Tech","level":3},{"id":3510,"name":"Health Care Equipment & Services","order":null,"parentId":35,"alias":"Healthcare Equip","level":2},{"id":352010,"name":"Biotechnology","order":null,"parentId":3520,"alias":"Biotech","level":3},{"id":352030,"name":"Life Sciences Tools & Services","order":null,"parentId":3520,"alias":"Life Science","level":3},{"id":352020,"name":"Pharmaceuticals","order":null,"parentId":3520,"alias":"Pharma","level":3},{"id":3520,"name":"Pharmaceuticals, Biotechnology & Life Sciences","order":null,"parentId":35,"alias":"Pharma","level":2},{"id":35,"name":"Health Care","order":null,"parentId":null,"alias":"HealthCare","level":1},{"id":201010,"name":"Aerospace & Defense","order":null,"parentId":2010,"alias":"Aerospace","level":3},{"id":201020,"name":"Building Products","order":null,"parentId":2010,"alias":"Bldg Prod","level":3},{"id":201030,"name":"Construction & Engineering","order":null,"parentId":2010,"alias":"Const Eng","level":3},{"id":201040,"name":"Electrical Equipment","order":null,"parentId":2010,"alias":"Electrical Equip","level":3},{"id":201050,"name":"Industrial Conglomerates","order":null,"parentId":2010,"alias":"Industrial Cong","level":3},{"id":201060,"name":"Machinery","order":null,"parentId":2010,"alias":"Machinery","level":3},{"id":201070,"name":"Trading Companies & Distributors","order":null,"parentId":2010,"alias":"Trading & Dist","level":3},{"id":2010,"name":"Capital Goods","order":null,"parentId":20,"alias":"Cap Goods","level":2},{"id":202010,"name":"Commercial Services & Supplies","order":null,"parentId":2020,"alias":"Com Srv","level":3},{"id":202030,"name":"Marketing Services","order":null,"parentId":2020,"alias":"Marketing Services","level":3},{"id":202020,"name":"Professional Services","order":null,"parentId":2020,"alias":"Prof Srv","level":3},{"id":202040,"name":"Staffing & Recruiting","order":null,"parentId":2020,"alias":"Staffing & Recruiting","level":3},{"id":2020,"name":"Commercial & Professional Services","order":null,"parentId":20,"alias":"Prof Srv","level":2},{"id":203010,"name":"Air Freight & Logistics","order":null,"parentId":2030,"alias":"Air Freight","level":3},{"id":203020,"name":"Airlines","order":null,"parentId":2030,"alias":"Airlines","level":3},{"id":203030,"name":"Marine","order":null,"parentId":2030,"alias":"Marine","level":3},{"id":203040,"name":"Road & Rail","order":null,"parentId":2030,"alias":"Road & Rail","level":3},{"id":203050,"name":"Transportation Infrastructure","order":null,"parentId":2030,"alias":"Trans Infra","level":3},{"id":2030,"name":"Transportation","order":null,"parentId":20,"alias":"Trans","level":2},{"id":20,"name":"Industrials","order":null,"parentId":null,"alias":"Industrials","level":1},{"id":453010,"name":"Semiconductors & Semiconductor Equipment","order":null,"parentId":4530,"alias":"Semiconductor Equip","level":3},{"id":4530,"name":"Semiconductors & Semiconductor Equipment","order":null,"parentId":45,"alias":"Semiconductors","level":2},{"id":451060,"name":"Cloud Computing, Data Center","order":null,"parentId":4510,"alias":"Cloud Computing, Data Center","level":3},{"id":451031,"name":"Computer Networking","order":null,"parentId":4510,"alias":"Computer Networking","level":3},{"id":451012,"name":"Custom Software Development","order":null,"parentId":4510,"alias":"Custom Software Development","level":3},{"id":451062,"name":"Digital Marketing Services","order":null,"parentId":4510,"alias":"Digital Marketing Services","level":3},{"id":451080,"name":"Education Software","order":null,"parentId":4510,"alias":"Education Software","level":3},{"id":451061,"name":"Engineering Software","order":null,"parentId":4510,"alias":"Engineering Software","level":3},{"id":451051,"name":"ERP Software","order":null,"parentId":4510,"alias":"ERP Software","level":3},{"id":451070,"name":"Financial Software","order":null,"parentId":4510,"alias":"Financial Software","level":3},{"id":451090,"name":"Health Care and Medical Software","order":null,"parentId":4510,"alias":"Health Care and Medical Software","level":3},{"id":451071,"name":"Hosting Services, ISPs","order":null,"parentId":4510,"alias":"Hosting Services, ISPs","level":3},{"id":451011,"name":"Human Resources Software","order":null,"parentId":4510,"alias":"Human Resources Software","level":3},{"id":451022,"name":"Information & Data Services","order":null,"parentId":4510,"alias":"Information & Data Services","level":3},{"id":451010,"name":"Internet Software & Services","order":null,"parentId":4510,"alias":"Internet","level":3},{"id":451052,"name":"IT Consulting & Professional Services","order":null,"parentId":4510,"alias":"IT Consulting & Professional Services","level":3},{"id":451040,"name":"IT Security","order":null,"parentId":4510,"alias":"IT Security","level":3},{"id":451020,"name":"IT Services","order":null,"parentId":4510,"alias":"IT Services","level":3},{"id":451032,"name":"IT Staffing & Recruiting","order":null,"parentId":4510,"alias":"IT Staffing & Recruiting","level":3},{"id":451050,"name":"IT Storage","order":null,"parentId":4510,"alias":"IT Storage","level":3},{"id":451021,"name":"Legal Software","order":null,"parentId":4510,"alias":"Legal Software","level":3},{"id":451072,"name":"Retail and eCommerce Software","order":null,"parentId":4510,"alias":"Retail and eCommerce Software","level":3},{"id":451030,"name":"Software","order":null,"parentId":4510,"alias":"Software","level":3},{"id":451042,"name":"Software As A Service","order":null,"parentId":4510,"alias":"SaaS","level":3},{"id":451041,"name":"Supply Chain & Logistics Software","order":null,"parentId":4510,"alias":"Supply Chain & Logistics Software","level":3},{"id":451091,"name":"Systems Integrators","order":null,"parentId":4510,"alias":"Systems Integrators","level":3},{"id":451081,"name":"Value Added Resellers","order":null,"parentId":4510,"alias":"VARs","level":3},{"id":4510,"name":"Software & Services","order":null,"parentId":45,"alias":"IT Software","level":2},{"id":452010,"name":"Communications Equipment","order":null,"parentId":4520,"alias":"Comm Equip","level":3},{"id":452020,"name":"Computers & Peripherals","order":null,"parentId":4520,"alias":"Computer Perip","level":3},{"id":452030,"name":"Electronic Equipment, Instruments & Components","order":null,"parentId":4520,"alias":"Electronics","level":3},{"id":452040,"name":"Office Electronics","order":null,"parentId":4520,"alias":"Office Electronic","level":3},{"id":452050,"name":"Semiconductor Equipment & Products -- Discontinued effective 04/30/2003.","order":null,"parentId":4520,"alias":"Semiconductor Equip","level":3},{"id":4520,"name":"Technology Hardware & Equipment","order":null,"parentId":45,"alias":"IT Hardware","level":2},{"id":45,"name":"Information Technology","order":null,"parentId":null,"alias":"IT","level":1},{"id":151010,"name":"Chemicals","order":null,"parentId":1510,"alias":"Chemicals","level":3},{"id":151020,"name":"Construction Materials","order":null,"parentId":1510,"alias":"Const Matl","level":3},{"id":151030,"name":"Containers & Packaging","order":null,"parentId":1510,"alias":"C&P","level":3},{"id":151040,"name":"Metals & Mining","order":null,"parentId":1510,"alias":"Metal & Mine","level":3},{"id":151050,"name":"Paper & Forest Products","order":null,"parentId":1510,"alias":"PFP","level":3},{"id":1510,"name":"Materials","order":null,"parentId":15,"alias":"Materials","level":2},{"id":15,"name":"Materials","order":null,"parentId":null,"alias":"Materials","level":1},{"id":6,"name":"Other","order":null,"parentId":null,"alias":"LastItem","level":1},{"id":6560,"name":"Colleges & Universities","order":null,"parentId":65,"alias":"Colleges & Universities","level":2},{"id":6530,"name":"Defense","order":null,"parentId":65,"alias":"Defense","level":2},{"id":6510,"name":"Federal Government","order":null,"parentId":65,"alias":"Fed Gov","level":2},{"id":6550,"name":"Non-Profit","order":null,"parentId":65,"alias":"Non-Profit","level":2},{"id":6540,"name":"Other Public Industries","order":null,"parentId":65,"alias":"Other Pub","level":2},{"id":6520,"name":"State and Local Government","order":null,"parentId":65,"alias":"State Gov","level":2},{"id":65,"name":"Public","order":null,"parentId":null,"alias":"Public","level":1},{"id":601010,"name":"Equity Real Estate Investment Trusts (REITs)","order":null,"parentId":6010,"alias":"REITs","level":3},{"id":601020,"name":"Real Estate Management & Development","order":null,"parentId":6010,"alias":"REMD","level":3},{"id":6010,"name":"Equity Real Estate Investment Trusts (REITs)","order":null,"parentId":60,"alias":"REITS","level":2},{"id":6020,"name":"Real Estate Management & Development","order":null,"parentId":60,"alias":"RSMD","level":2},{"id":60,"name":"Real Estate","order":null,"parentId":null,"alias":"Real Estate","level":1},{"id":551010,"name":"Electric Utilities","order":null,"parentId":5510,"alias":"Electric Util","level":3},{"id":551020,"name":"Gas Utilities","order":null,"parentId":5510,"alias":"Gas Util","level":3},{"id":551050,"name":"Independent Power Producers & Energy Traders","order":null,"parentId":5510,"alias":"IPPET","level":3},{"id":551030,"name":"Multi-Utilities","order":null,"parentId":5510,"alias":"Multi-Util","level":3},{"id":551040,"name":"Water Utilities","order":null,"parentId":5510,"alias":"Water Util","level":3},{"id":5510,"name":"Utilities","order":null,"parentId":55,"alias":"Utilities","level":2},{"id":55,"name":"Utilities","order":null,"parentId":null,"alias":"Utilities","level":1}]


parseData = (datasStr)=>{
    if('#LNF' === datasStr){ return false }
    if('' === datasStr.trim()){ return false }

    const obj = {}
    items = ["Industry","Website","Specialties","Company size"]
    for(item of items){
        var re = new RegExp(`${item}\n.*`);
        reg = re.exec(datasStr)
        if(reg){
            obj[item] = reg[0].replace(`${item}\n`,'')
        }
    }

    return obj;
}

unique = (arr) => {
    var hash = {}, result = [];
    for (var i = 0; i < arr.length; i++)
        if (!(arr[i] in hash)) { //it works with objects! in FF, at least
            hash[arr[i]] = true;
            result.push(arr[i]);
        }
    return result;
}

invalid_ind = []
uploadFileArr = []

names = []
nameIds = []

for (const company of dataObjs.data){
    if(company.name.trim() == ''){
        continue;
    }
    if(company.linkedin_url.trim() == ''){
        continue;
    }

    let inIds = false;
    for(const obj of nameIds){
        if(obj.name === company.name){
            obj.ids = obj.ids + ',' + company.expIds
            inIds = true;
            continue;
        }
    }

    if(!inIds){
        nameIds.push({
            name:company.name,
            ids:company.expIds
        })
    }
}



for (const company of dataObjs.data){

    if(names.indexOf(company.li_name)>-1){
        continue;
    }else{
        names.push(company.li_name)
    }

    if(!company.datas){
        continue;
    }

    if(company.linkedin_url.trim() == ''){
        continue;
    }else{
        datasObj = parseData(company.datas)
    }

    if(datasObj){
        if(company.li_name == '#LNF'){
            company.li_name = company.name
        }

        uploadObj = {
            name:company.li_name,
            alias:unique([company.li_name,company.name]).join(' || '),
            website:datasObj.Website || '',
            linkedInURL:company.linkedin_url?company.linkedin_url.replace(/\/about/g,''):'',
            industry:datasObj.Industry || '',
            products:datasObj.Specialties || '',
            companySize:datasObj["Company size"] || '',
            secondaryIndustries:''
        }

        if(uploadObj.industry != ''){
            for(const ind of inMapObjs.data){
                if(uploadObj.industry === ind['LI Industry']){
                    uploadObj.industry = ind['TH Industry 1']
                    if(ind['TH Industry 2']!=''){
                        uploadObj.secondaryIndustries = ind['TH Industry 2']
                    }
                }
            }
        }

        if(uploadObj.industry != ''){
            indExist = false;
            for(const ind of inds){
                if(ind.name.toLowerCase().indexOf(uploadObj.industry.toLowerCase()) > -1 ){
                    indExist = true;
                    break;
                }
            }
            if(!indExist){
                invalid_ind.push(uploadObj.industry);
            }
        }

        uploadFileArr.push(uploadObj)
    }
}

uploadFIleStr = Papa.unparse(uploadFileArr,{header:true})
fs.writeFileSync('companies_upload.csv',uploadFIleStr ,"utf8");


invalid_ind = [...new Set(invalid_ind)]
fs.writeFileSync('invalid_ind.csv',invalid_ind.join("\n") ,"utf8");


nameIdsStr = Papa.unparse(nameIds,{header:true})
fs.writeFileSync('nameIdsStr.csv',nameIdsStr ,"utf8");

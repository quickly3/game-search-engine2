
const PageParse = async(document)=>{
    company = {}
    nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
    company.name = document.querySelector(nameSelector).textContent


    tableDateKeySelector = '#main-content > section.core-rail > section.about-us.section-container > dl > div:nth-child(1) > dt'
    tableDateKeyNodes = document.querySelectorAll(tableDateKeySelector)

    tableDateKeys = tableDateKeyNodes.map(node=>{
        return node.textContent;
    })

    tableDateValueSelector = '#main-content > section.core-rail > section.about-us.section-container > dl > div:nth-child(1) > dd'
    tableDateValueNodes = document.querySelectorAll(tableDateValueSelector)
    tableDateValues = tableDateValueNodes.map(node=>{
        return node.textContent;
    })

    tableDateKeys.map((key,i)=>{
        company[key] = tableDateValues[i];
    })

    return company;
}

module.exports = PageParse;
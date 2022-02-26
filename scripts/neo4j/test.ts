var neo4j = require('neo4j-driver')

async function init(){
    const person = []
    var driver = neo4j.driver(
        'neo4j://localhost',
        neo4j.auth.basic('neo4j', '123456')
    )
    
    var session = driver.session({
        database:'neo4j'
    })
    
    const cql = 'Match(p:Person) return p'

    const resp = await session.run(cql)
    console.log(resp.records.map(r=>{
        person.push(r.get(0))
    }))    
    
    await session.close()
    await driver.close()
}

init();

